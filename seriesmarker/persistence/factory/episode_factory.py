#==============================================================================
# -*- coding: utf-8 -*-
# 
# Copyright (C) 2013 Tobias Röttger <toroettg@gmail.com>
# 
# This file is part of SeriesMarker.
# 
# SeriesMarker is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
# 
# SeriesMarker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with SeriesMarker.  If not, see <http://www.gnu.org/licenses/>.
#==============================================================================

from pytvdbapi.error import TVDBAttributeError
from seriesmarker.persistence.factory.base_factory import BaseFactory
from seriesmarker.persistence.model.director import Director
from seriesmarker.persistence.model.episode import Episode
from seriesmarker.persistence.model.episode_extra import EpisodeExtra
from seriesmarker.persistence.model.guest import Guest
from seriesmarker.persistence.model.writer import Writer
import logging

logger = logging.getLogger(__name__)

class EpisodeFactory(BaseFactory):
    """Factory to create episode objects from TheTVDB data."""

    def new_episode(self, pytvdb_episode, update=None):
        """Creates a persistable episode object from TheTVDB data.
        
        This method will create a new :class:`.Episode` instance from a
        pytvdbapi episode. If a episode object is given, the existing one
        will be updated with the data instead.
        
        :param pytvdb_episode: The data to create the episode from.
        :type pytvdb_episode: :class:`pytvdbapi.api.Episode`
        :param update: A episode to update with new data.
        :type update: :class:`.Episode`
        :returns: The newly created or updated :class:`.Episode` instance.
        
        .. todo::
        
            Episode specials have additional attributes where regular ones do
            not. The pytvdbapi logs an exception if it is tried to access them
            on a regular episode. Either check existence beforehand, or see if
            pytvdbapi changes output.
        
        """
        if update == None:
            episode = Episode()
            episode.id = pytvdb_episode.id
            episode.extra = EpisodeExtra(watched=False)
        else:
            episode = update

        episode.season_id = pytvdb_episode.seasonid
        episode.episode_name = pytvdb_episode.EpisodeName
        episode.episode_number = pytvdb_episode.EpisodeNumber
        episode.combined_episode_number = -1 if pytvdb_episode.Combined_episodenumber is "" else pytvdb_episode.Combined_episodenumber
        episode.combined_season = pytvdb_episode.Combined_season
        episode.language = pytvdb_episode.Language
        episode.overview = pytvdb_episode.Overview
        episode.imdb_id = pytvdb_episode.IMDB_ID
        episode.DVD_season = pytvdb_episode.DVD_season
        episode.DVD_chapter = pytvdb_episode.DVD_chapter
        episode.DVD_episode_number = -1 if pytvdb_episode.DVD_episodenumber is "" else pytvdb_episode.DVD_episodenumber
        episode.DVD_disc_id = pytvdb_episode.DVD_discid
        episode.ep_img_flag = pytvdb_episode.EpImgFlag
        episode.production_code = pytvdb_episode.ProductionCode
        episode.last_updated = pytvdb_episode.lastupdated
        episode.filename = pytvdb_episode.filename
        episode.first_aired = None if pytvdb_episode.FirstAired is "" else pytvdb_episode.FirstAired
        episode.absolute_number = pytvdb_episode.absolute_number
        episode.rating = -1 if pytvdb_episode.Rating is "" else pytvdb_episode.Rating
        episode.rating_count = pytvdb_episode.RatingCount

        # TODO beware of race-conditions - not threadsafe
        logging.getLogger("pytvdbapi.error").disabled = True
        logging.getLogger("pytvdbapi.api").disabled = True
        try:
            episode.airs_before_season = pytvdb_episode.airsbefore_season
            episode.airs_before_episode = pytvdb_episode.airsbefore_episode
            episode.airs_after_season = pytvdb_episode.airsafter_season
        except TVDBAttributeError:
            pass  # These values exist in series specials only
        logging.getLogger("pytvdbapi.error").disabled = False
        logging.getLogger("pytvdbapi.api").disabled = False

        self._handle_list_attribute(episode.directors, pytvdb_episode.Director, Director)
        self._handle_list_attribute(episode.writers, pytvdb_episode.Writer, Writer)
        self._handle_list_attribute(episode.guests, pytvdb_episode.GuestStars, Guest)

        return episode
