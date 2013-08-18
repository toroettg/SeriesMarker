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

from seriesmarker.persistence.database import db_remove_episode
from seriesmarker.persistence.factory.banner_factory import BannerFactory
from seriesmarker.persistence.factory.base_factory import BaseFactory
from seriesmarker.persistence.factory.episode_factory import EpisodeFactory
from seriesmarker.persistence.model.season import Season
import logging

logger = logging.getLogger(__name__)

class SeasonFactory(BaseFactory):
    """Factory to create season objects from TheTVDB data."""

    def __init__(self):
        """Creates a new factory instance."""
        super().__init__()
        self._episode_factory = EpisodeFactory()

    def new_season(self, series, pytvdb_season, update=None):
        """Creates a persistable season object from TheTVDB data.
        
        This method will create a new :class:`.Season` instance from pytvdbapi
        episode objects. If a season object is given, the existing one will be
        updated with the data instead. In both cases, it also traverses the 
        episodes of a season, using :class:`.EpisodeFactory`, to populate it
        with data.  
        
        :param series: The series, the season to create belongs to.
        :type series: :class:`.Series`
        :param pytvdb_season: The data to create the season instance from.
        :type pytvdb_season: :class:`.pytvdbapi.api.Season`
        :param update: A season to update with new data.
        :type update: :class:`.Season`
        :returns: The newly created or updated :class:`.Season` instance.
        
        """
        if update == None:
            season = Season()
        else:
            season = update

        original_episode_ids = [episode.id for episode in season.episodes]

        for episode in season.episodes:  # update, remove
            try:
                pytvdb_episode = next(pytvdb_episode for pytvdb_episode in pytvdb_season.episodes.values() if pytvdb_episode.id == episode.id)
                self._episode_factory.new_episode(pytvdb_episode, update=episode)
            except StopIteration:
                db_remove_episode(episode)
                self.removed.append(episode)
                logger.debug("Removed episode {}x{:02} of series '{}'".format(pytvdb_season.season_number, episode.episode_number, series.series_name))

        for pytvdb_episode in pytvdb_season.episodes.values():  # add
            if pytvdb_episode.id not in original_episode_ids:
                new_episode = self._episode_factory.new_episode(pytvdb_episode)
                season.episodes.insert(new_episode.episode_number - 1, new_episode)
                self.added.append(new_episode)
                logger.debug("Added episode {}x{:02} of series '{}'".format(pytvdb_season.season_number, new_episode.episode_number, series.series_name))

        season.id = season.episodes[0].season_id
        season.series_id = series.id
        season.season_number = pytvdb_season.season_number
        season.banner = BannerFactory.new_banner(banner_type="season", banners=pytvdb_season.show.banner_objects, update=season.banner, season=season.season_number)

        return season
