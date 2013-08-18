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

from seriesmarker.persistence.database import db_remove_banner
from seriesmarker.persistence.factory.base_factory import BaseFactory
from seriesmarker.persistence.model.banner import Banner
from seriesmarker.persistence.model.banner_extra import BannerExtra

class BannerFactory(BaseFactory):
    """Factory to create banner objects from TheTVDB data."""

    @staticmethod
    def new_banner(banner_type, banners, update=None, season=None):
        """Picks a banner from a list of pytvdbapi-banners and creates a persistable object of it.
    
        :param banner_type: The type of banner to pick, possible options are: 'series' (landscape), 'poster' and 'season'.
        :type banner_type: string
        :param banners: The banners related to a series or season, retrieved by pytvdbapi.
        :type banners: list
        :param update: The banner object to replace with a new banner.
        :type update: :class:`.Banner`
        :param season: Parameter can be omitted unless 'season' is given as banner type. Describes the number of the season to pick a banner for. 
        :type season: integer
        :returns: The picked :class:`.Banner`, or None if no one matched.
    
        .. todo::
            
            Convert banner_type to Enum, as soon as Python supports it (probably 3.4).
    
        """
        pytvdb_banners = [banner for banner in banners if banner.BannerType == banner_type]

        if banner_type == "season":
            pytvdb_banners = [banner for banner in pytvdb_banners if banner.Season == season]

        if len(pytvdb_banners) > 0:
            return BannerFactory._new_banner(pytvdb_banners[0], update)  # TODO intelligent banner choice


    @staticmethod
    def _new_banner(pytvdb_banner, update=None):
        """Creates a persistable banner object from TheTVDB data.
        
        :param pytvdb_banner: The data to create the banner from.
        :type pytvdb_banner: :class:`pytvdbapi.banner.Banner`
        :param update: The banner to replace with the created one.
        :type update: :class:`.Banner`
        :returns: The newly created :class:`.Banner` instance.
        
        """
        if update != None and update.id != pytvdb_banner.id:
            db_remove_banner(update)
            update = None

        if update == None:
            banner = Banner()
            banner.id = pytvdb_banner.id
        else:
            banner = update

        banner.banner_path = pytvdb_banner.BannerPath
        banner.banner_type = pytvdb_banner.BannerType
        banner.banner_type2 = pytvdb_banner.BannerType2
        banner.language = pytvdb_banner.Language
        banner.rating = -1 if pytvdb_banner.Rating is "" else pytvdb_banner.Rating
        banner.rating_count = pytvdb_banner.RatingCount

        if banner.extra == None:
            banner.extra = BannerExtra()

        banner.extra.banner_url = pytvdb_banner.banner_url

        return banner
