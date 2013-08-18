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

import unittest

from seriesmarker.test.database import database_model_test, database_persistence_test, \
    database_story_test, database_factory_test

def get_suit():
    database_suites = unittest.TestSuite()

    database_suites.addTest(database_model_test.get_suit())
    database_suites.addTest(database_persistence_test.get_suit())
    database_suites.addTest(database_story_test.get_suit())
    database_suites.addTest(database_factory_test.get_suit())

    return database_suites

def load_tests(loader, tests, pattern):
    """Enables (graphical) unit testing in PyDev."""
    return get_suit()

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(get_suit())
