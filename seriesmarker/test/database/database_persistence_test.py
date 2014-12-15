#==============================================================================
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 - 2014 Tobias Röttger <toroettg@gmail.com>
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

from seriesmarker.test.database.base.persitent_db_test_case import \
    PersistentDBTestCase
from seriesmarker.util import config
import os
import tempfile
import unittest

class DatabasePersistenceTest(PersistentDBTestCase):

    def test_directory_creation(self):
        from seriesmarker.persistence.database import db_init

        self.assertFalse(os.path.exists(os.path.join(tempfile.gettempdir(), config.application_name)), "DB directory should not exist")
        db_init()
        self.assertTrue(os.path.exists(os.path.join(tempfile.gettempdir(), config.application_name)), "DB directory was not created after data base init")
        db_init() #Check double invocation on same directory

        self.deleteDatabase()
        self.assertFalse(os.path.exists(os.path.join(tempfile.gettempdir(), config.application_name)), "DB directory should not exist")
        self.deleteDatabase() #Check double invocation on same directory

def get_suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DatabasePersistenceTest))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
