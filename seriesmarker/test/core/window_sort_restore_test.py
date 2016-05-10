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

from seriesmarker.test.core.base.settings_test_case import SettingsTestCase
from seriesmarker.util import config
from seriesmarker.util.settings import settings


class WindowSortRestoreTest(SettingsTestCase):
    def test_01_initial_behavior(self):
        """Tests handling of non-existing settings file."""
        self.assertEqual(
            tempfile.gettempdir(),
            os.path.commonprefix(
                [
                    settings._CONFIG_FILE,
                    tempfile.gettempdir()
                ]
            ),
            "Settings file should reside in tmp directory for tests."
        )

        self.assertFalse(os.path.exists(config.dirs.user_config_dir),
                         "Settings directory should not exist.")

        self.assertFalse(os.path.exists(settings._CONFIG_FILE),
                         "Settings file should not exist.")

        self.run_main()

        self.assertTrue(
            os.path.exists(config.dirs.user_config_dir),
            "Settings directory should be created at application start."
        )

        self.assertFalse(
            os.path.exists(settings._CONFIG_FILE),
            "Settings file should not be created at application start."
        )

        self.window.close()

        self.assertTrue(
            os.path.exists(settings._CONFIG_FILE),
            "Settings file should be created at application exit."
        )

        self.check_settings_file_contains(
            [
                "sort.column = 0",
                "sort.order = 1",
            ],
            section="MainWindow"
        )

def get_suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(WindowSortRestoreTest))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(get_suit())
