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

from PySide.QtCore import Qt

from seriesmarker.test.core.base.settings_test_case import SettingsTestCase
from seriesmarker.util import config
from seriesmarker.util.settings import settings


class WindowSortRestoreTest(SettingsTestCase):
    """Performs tests related to the main window end-user settings.

     .. note::
         Cases in this test depend on a specific execution order.
         Therefore, case names are numbered.

     """

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
                "sort.order = 0",
            ],
            section="MainWindow"
        )

    def test_02_sort_order_store(self):
        """Test whether sort by progress is stored in the settings file."""
        self.check_settings_file_contains(
            [
                "sort.column = 0",
                "sort.order = 0",
            ],
            section="MainWindow"
        )

        self.run_main()

        target = self.header_center(self.tree_view.header(), 2)
        self.click(self.tree_view.header().viewport(), target)
        self.click(self.tree_view.header().viewport(), target)

        self.window.close()

        self.check_settings_file_contains(
            [
                "sort.column = 2",
                "sort.order = 1",
            ],
            section="MainWindow"
        )

    def test_03_sort_order_restore(self):
        """Test whether sort by progress is restored from the settings file."""
        self.check_settings_file_contains(
            [
                "sort.column = 2",
                "sort.order = 1",
            ],
            section="MainWindow"
        )

        self.assertEqual(
            self.tree_view.header().sortIndicatorSection(),
            0,
            "Should be sorted by default column."
        )
        self.assertEqual(
            self.tree_view.header().sortIndicatorOrder(),
            Qt.AscendingOrder,
            "Should be sorted by default order."
        )

        self.run_main()

        self.assertEqual(
            self.tree_view.header().sortIndicatorSection(),
            2,
            "Should be sorted by progress column."
        )
        self.assertEqual(
            self.tree_view.header().sortIndicatorOrder(),
            Qt.DescendingOrder,
            "Should be sorted by descending order."
        )

        self.window.close()

def get_suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(WindowSortRestoreTest))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(get_suit())
