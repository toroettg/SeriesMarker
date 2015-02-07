#==============================================================================
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 - 2015 Tobias Röttger <toroettg@gmail.com>
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

from seriesmarker.test.util.examples.buffy_example import BuffyExample
from seriesmarker.test.util.examples.defiance_example import DefianceExample
from seriesmarker.test.util.examples.dr_who_example import DrWhoExample
from seriesmarker.test.util.examples.how_i_met_your_mother_example import \
    HowIMetYourMotherExample
from seriesmarker.test.util.examples.mad_love_example import MadLoveExample
from seriesmarker.test.util.examples.wonder_years_example import \
    WonderYearsExample
from seriesmarker.test.util.examples.rome_pg_example import RomePGExample


class ExampleDataFactory(object):
    """Creates static data for testing, similar to data pytvdb would return."""
    @staticmethod
    def new_pytvdb_show(name):
        if name == "BUFFY":
            return BuffyExample.show()
        elif name == "HIMYM":
            return HowIMetYourMotherExample.show()
        elif name == "HIMYM-UPDATE":
            return HowIMetYourMotherExample.show_update()
        elif name == "ROMEPG":
            return RomePGExample.show()
        elif name == "MADLOVE":
            return MadLoveExample.show()
        elif name == "MADLOVE-UPDATE":
            return MadLoveExample.show_update()
        elif name == "DEFIANCE":
            return DefianceExample.show()
        elif name == "DEFIANCE-UPDATE":
            return DefianceExample.show_update()
        elif name == "WONDERYEARS":
            return WonderYearsExample.show()
        elif name == "DRWHO":
            return DrWhoExample.show()
        else:
            raise Exception("Key '{}' not found".format(name))
