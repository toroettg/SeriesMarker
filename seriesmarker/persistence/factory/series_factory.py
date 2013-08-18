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

from seriesmarker.persistence.database import db_remove_season, db_remove_role
from seriesmarker.persistence.factory.banner_factory import BannerFactory
from seriesmarker.persistence.factory.base_factory import BaseFactory
from seriesmarker.persistence.factory.role_factory import RoleFactory
from seriesmarker.persistence.factory.season_factory import SeasonFactory
from seriesmarker.persistence.model.actor import Actor
from seriesmarker.persistence.model.genre import Genre
from seriesmarker.persistence.model.series import Series
from seriesmarker.persistence.model.series_extra import SeriesExtra
import logging

logger = logging.getLogger(__name__)

class SeriesFactory(BaseFactory):
    """Factory to create series objects from TheTVDB data."""

    def new_series(self, pytvdb_show, update=None):
        """Creates a persistable series object from TheTVDB data.
        
        This method will create a new :class:`.Series` instance from pytvdbapi
        data. If a series object is given, the existing one will be updated
        with the data instead. In both cases, it also traverses the seasons
        and episodes of a series, using :class:`.SeasonFactory`, to populate it
        with data.
        
        :param pytvdb_show: The data to create the series instance from.
        :type pytvdb_show: :class:`.pytvdbapi.api.Show`
        :param update: A series to update with new data.
        :type update: :class:`.Series`
        :returns: The newly created or updated :class:`.Series` instance.
        
        """
        if update == None:
            series = Series()
            series.id = pytvdb_show.id
            series.extra = SeriesExtra()
        else:
            series = update

        series.series_name = pytvdb_show.SeriesName
        series.overview = pytvdb_show.Overview
        series.status = pytvdb_show.Status
        series.last_updated = pytvdb_show.lastupdated
        series.rating = -1 if pytvdb_show.Rating is "" else pytvdb_show.Rating
        series.rating_count = pytvdb_show.RatingCount
        series.content_rating = pytvdb_show.ContentRating
        series.language = pytvdb_show.Language
        series.banner = pytvdb_show.banner
        series.fanart = pytvdb_show.fanart
        series.poster = pytvdb_show.poster
        series.first_aired = None if pytvdb_show.FirstAired is "" else pytvdb_show.FirstAired
        series.airs_day_of_week = pytvdb_show.Airs_DayOfWeek
        series.airs_time = pytvdb_show.Airs_Time
        series.runtime = pytvdb_show.Runtime
        series.added = pytvdb_show.added
        series.added_by = pytvdb_show.addedBy
        series.network = pytvdb_show.Network
        series.network_id = pytvdb_show.NetworkID
        series.series_id = pytvdb_show.SeriesID
        series.imdb_id = pytvdb_show.IMDB_ID
        series.zap2it_id = pytvdb_show.zap2it_id

        self._handle_list_attribute(series.genre, pytvdb_show.Genre, Genre)
        self._handle_list_attribute(series.actors, pytvdb_show.Actors, Actor)

        self._handle_seasons(series, pytvdb_show.seasons)

        self._handle_roles(series, pytvdb_show.actor_objects)

        series.extra.banner = BannerFactory.new_banner(banner_type="poster", banners=pytvdb_show.banner_objects, update=series.extra.banner)

        return series

    def _handle_roles(self, series, pytvdb_actors):
        """Updates or adds the roles of a series.
        
        By using the :class:`.RoleFactory`, each role of the series data
        is compared to existing roles in the database, to update the series.
        New roles are added, existing roles are updated and missing roles
        will be deleted. 
        
        :param series: The series to update role data for.
        :type series: :class:`.Series`
        :param pytvdb_actors: The new role data from TheTVDB. 
        :type pytvdb_actors: list
        
        """
        roles = series.extra.roles

        for role in roles:
            try:
                pytvdb_actor = next(actor for actor in pytvdb_actors if actor.id == role.id)
                RoleFactory.new_role(pytvdb_actor, update=role)
                logger.debug("Updated role {} from '{}'".format(role, series.series_name))
            except StopIteration:
                db_remove_role(role)
                logger.debug("Removed role {} from '{}'".format(role, series.series_name))

        for pytvdb_actor in pytvdb_actors:
            try:
                next(role for role in roles if role.id == pytvdb_actor.id)
            except StopIteration:
                new_role = RoleFactory.new_role(pytvdb_actor)
                roles.append(new_role)
                logger.debug("Added role {} from '{}'".format(new_role, series.series_name))

    def _handle_seasons(self, series, pytvdb_seasons):
        """Updates or adds the seasons of a series.
        
        By using the :class:`.SeasonFactory`, each season of the series data
        is compared to existing seasons in the database, to update the series.
        New seasons are added, existing seasons are updated and missing seasons
        will be deleted. 
        
        :param series: The series to update season data for.
        :type series: :class:`.Series`
        :param pytvdb_seasons: The new season data from TheTVDB. 
        :type pytvdb_seasons: list
        
        """
        season_factory = SeasonFactory()

        for season in series.seasons:
            if season.season_number in pytvdb_seasons:
                season_factory.new_season(series, pytvdb_seasons[season.season_number], update=season)
                if season_factory.added or season_factory.removed:
                    self.updated.append((season, season_factory.added, season_factory.removed))
                    season_factory.reset()
                    logger.debug("Updated season {} of '{}'".format(season.season_number, series.series_name))
            else:
                db_remove_season(season)
                self.removed.append(season)
                logger.debug("Removed season {} of '{}'".format(season.season_number, series.series_name))

        for pytvdb_season in pytvdb_seasons.values():
            try:
                next(season for season in series.seasons if season.id == next(iter(pytvdb_season)).seasonid)
            except StopIteration:
                new_season = season_factory.new_season(series, pytvdb_season, None)
                series.seasons.append(new_season)
                self.added.append(new_season)
                logger.debug("Added season {} of '{}'".format(new_season.season_number, series.series_name))


