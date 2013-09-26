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

from pytvdbapi.api import Show


class BaseExample(object):
    """Base class of example files that contain series information for tests."""
    @classmethod
    def show(cls):
        show = Show(api=None, language=None, data=cls.series_attributes())
        show.seasons = cls.seasons(show)
        show.banner_objects = cls.banners(show)
        show.actor_objects = cls.roles(show)
        return show

    @classmethod
    def show_update(cls):
        show = cls.show()
        show.data = cls.attributes_update(show)
        show.seasons = cls.seasons_update(show)
        show.banner_objects = cls.banners_update(show)
        show.actor_objects = cls.roles_update(show)
        return show

    @classmethod
    def series_attributes(cls):
        return {}

    @classmethod
    def seasons(cls, show):
        return {}

    @classmethod
    def banners(cls, show):
        return []

    @classmethod
    def roles(cls, show):
        return []

    @classmethod
    def seasons_update(cls, show):
        return show.seasons
    @classmethod
    def attributes_update(cls, show):
        return show.attributes
    @classmethod
    def banners_update(cls, show):
        return show.banner_objects
    @classmethod
    def roles_update(cls, show):
        return show.actor_objects

