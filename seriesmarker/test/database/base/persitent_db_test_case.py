# =============================================================================
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 - 2016 Tobias Röttger <toroettg@gmail.com>
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
# =============================================================================

import os
import shutil
import tempfile

import seriesmarker.util.config as config
from seriesmarker.test.database.base.db_test_case import DBTestCase


class PersistentDBTestCase(DBTestCase):
    """Prepares the execution of persistent test cases for deriving
    classes, i.e., data is stored at a temporary location on the hard
    disk and is available to multiple test cases."""

    @classmethod
    def setUpClass(cls):
        """
        Modifies SeriesMarker's database location to let it point at
        a temporary directory.

        :emphasis:`Overrides` :py:meth:`.unittest.TestCase.setUpClass`

        """
        super().setUpClass()

        data_dir_path = os.path.join(tempfile.gettempdir(),
                                     config.application_name)
        cache_dir_path = os.path.join(tempfile.gettempdir(),
                                      config.application_name, "cache")
        log_dir_path = os.path.join(tempfile.gettempdir(),
                                    config.application_name, "log")
        config_dir_path = os.path.join(tempfile.gettempdir(),
                                       config.application_name, "config")
        config.dirs = AppDirsMock(data_dir_path, cache_dir_path, log_dir_path,
                                  config_dir_path)

        cls.deleteDatabase()

    @classmethod
    def deleteDatabase(cls):
        """Removes the temporary directory, created by :py:meth:`.setUpClass`."""

        tmpdir = tempfile.gettempdir()
        # Prevent accidental deletion of real user data dir - should never happen
        if os.path.commonprefix([config.dirs.user_data_dir, tmpdir]) == tmpdir:
            try:
                shutil.rmtree(config.dirs.user_data_dir)
            except FileNotFoundError:
                pass

        if os.path.exists(config.dirs.user_data_dir):
            raise IOError("DB was not deleted")

    @classmethod
    def tearDownClass(cls):
        cls.deleteDatabase()
        super().tearDownClass()


class AppDirsMock(object):
    """Emulates the appdirs package with custom directories."""

    def __init__(self, user_data_dir, user_cache_dir, user_log_dir,
                 user_config_dir):
        """Sets the path to custom directories, which shall be returned
        by appdirs related method calls at runtime.

        :param user_data_dir: The path of the user data directory to return.
        :type user_data_dir: string
        :param user_cache_dir: The path of the user cache directory to return.
        :type user_cache_dir: string
        :param user_log_dir: The path of the user log directory to return.
        :type user_log_dir: string
        :param user_config_dir: The path of the user config directory to return.
        :type user_config_dir: string


        """
        self.user_data_dir = user_data_dir
        self.user_cache_dir = user_cache_dir
        self.user_log_dir = user_log_dir
        self.user_config_dir = user_config_dir
