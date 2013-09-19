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

from datetime import date
from pytvdbapi.api import Season, Episode, Show

class BaseExample(object):
    """Testdata covers update where episode IDs are changed.
    
    Original season data is ordered as [A, B, C].
    Update inserts D, which causes a shift to [A, D, B', C']. 
    D = B but has a new id, B' has id of B but contains data of C (B' = C).
    Furthermore, C' is added and has id of C but contains a new episode
    
    """
    @classmethod
    def show(cls):
        show = Show(api=None, language=None, data=cls.series_attributes())
        show.seasons = cls.seasons(show)
        show.banner_objects = []
        show.actor_objects = cls.roles()
        return show

    @classmethod
    def show_update(cls):
        show = cls.show()
        show.seasons = cls.seasons_update(show)
        return show

    @classmethod
    def series_attributes(cls):
        return {}

    @classmethod
    def seasons(cls, show):
        return {}

    @classmethod
    def roles(cls):
        return []

    @classmethod
    def seasons_update(cls, show):
        return {}

