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

import seriesmarker.util.config as config

import os
import errno

class AppDirsMock(object):
    def __init__(self, user_data_dir, user_cache_dir):
        self.user_data_dir = user_data_dir
        self.user_cache_dir = user_cache_dir

class PersistentDBTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cwd = os.getcwd()

        testdir_path = ""
        while not os.path.basename(cwd) == "test":  # Climb path if executing sub-testrunner
            testdir_path += "../"
            cwd = os.path.dirname(cwd)
        testdir_path += "db_testdir"

        config.dirs = AppDirsMock(testdir_path, config.dirs.user_cache_dir)

        cls.db_path = '{db_path}/{db_name}.db'.format(db_path=config.dirs.user_data_dir, db_name=config.application_name)

        # logging.basicConfig(level=logging.INFO)

    @classmethod
    def deleteDatabase(cls):
        try:
            os.remove(cls.db_path)
        except OSError as error:
            if error.errno != errno.ENOENT:
                raise

        try:
            os.rmdir(config.dirs.user_data_dir)
        except OSError as error:
            if error.errno != errno.ENOENT:
                raise

        if os.path.exists(cls.db_path):
            raise IOError("DB was not deleted")

