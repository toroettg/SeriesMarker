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
import tempfile
import unittest

import shutil

from seriesmarker.util import settings, config


class AppDirsMock(object):
    """Emulates the appdirs package with custom directories."""

    BASE_PATH = os.path.join(tempfile.gettempdir(), config.application_name)

    def __init__(self):
        """Sets the path to custom directories, which shall be returned
        by appdirs related method calls at runtime.

        """

        self.user_data_dir = os.path.join(self.BASE_PATH, "data")
        self.user_cache_dir = os.path.join(self.BASE_PATH, "cache")
        self.user_log_dir = os.path.join(self.BASE_PATH, "log")
        self.user_config_dir = os.path.join(self.BASE_PATH, "config")



class CoreTestCase(unittest.TestCase):
    """Modifies storage paths to point to temporary files.

    ..note::
        All test cases should inherit from this class, to ensure no real
        data is ever touched by tests.

    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        config.dirs = AppDirsMock()

        settings.Settings._CONFIG_FILE = os.path.join(
            config.dirs.user_config_dir, "settings.ini")

        cls.cleanupData()

    @classmethod
    def cleanupData(cls, path=AppDirsMock.BASE_PATH):
        """Removes a temporary directory, created by :py:meth:`.setUpClass`."""
        tmpdir = tempfile.gettempdir()
        # Prevent accidental deletion of real user data dir - should never happen
        if os.path.commonprefix([path, tmpdir]) == tmpdir:
            try:
                shutil.rmtree(path)
            except FileNotFoundError:
                pass

        if os.path.exists(path):
            raise IOError("Data in '{}' could not be deleted.".format(path))

    @classmethod
    def tearDownClass(cls):
        cls.cleanupData()
        super().tearDownClass()
