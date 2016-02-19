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

from PySide.QtCore import QSize, Qt, QPoint

from seriesmarker.test.core.base.application_test_case import \
    ApplicationTestCase
from seriesmarker.util import config
from seriesmarker.util.settings import settings


class SettingsTest(ApplicationTestCase):
    """Performs tests related to the handling of end-user settings.

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

    def test_02_store_window_position(self):
        """
        Test if the application's main window size and position are
        stored at application exit.

        """

        # Test for the defaults, given by the qt designer. Does not
        # check for position as it may vary because of window manager.
        self._check_settings_file_contains(
            [
                "size.width = 761",
                "size.length = 642"
            ]
        )

        self.run_main()

        # Prepare next test case
        self.window.move(50, 30)
        self.window.resize(800, 600)
        self.window.close()

        self._check_settings_file_contains(
            [
                "[MainWindow]",
                "maximized = False",
                "position.x = 50",
                "position.y = 30",
                "size.width = 800",
                "size.length = 600"
            ]
        )

    def test_03_restore_window_position(self):
        """
        Test if the application's main window is recreated with a
        previous size and position.

        """
        self._check_settings_file_contains(
            [
                "[MainWindow]",
                "maximized = False",
                "position.x = 50",
                "position.y = 30",
                "size.width = 800",
                "size.length = 600"
            ]
        )

        self.run_main()

        self.assertEqual(
            self.window.size(),
            QSize(800, 600),
            "MainWindow should be resized to the values from settings file."
        )

        self.assertEqual(
            self.window.pos(),
            QPoint(50, 30),
            "MainWindow should be positioned at the location from settings file."
        )

    def test_04_store_window_maximized(self):
        """Test if the maximized window state is stored at application exit."""

        self._check_settings_file_contains(
            [
                "[MainWindow]",
                "maximized = False",
            ]
        )

        self.run_main()

        self.assertFalse(
            self.window.isMaximized(),
            "MainWindow should not already be displayed maximized."
        )

        self.window.setWindowState(Qt.WindowMaximized)
        self.assertTrue(
            self.window.isMaximized(),
            "MainWindow should be displayed maximized."
        )

    def test_05_restore_window_maximized(self):
        """Test if the application's main window is recreated maximized."""
        self._check_settings_file_contains(
            [
                "[MainWindow]",
                "maximized = True",
            ]
        )

        self.run_main()

        self.assertTrue(
            self.window.isMaximized(),
            "MainWindow should be displayed maximized after application start."
        )

    def _check_settings_file_contains(self, lines):
        with open(settings._CONFIG_FILE) as file:
            content = file.read()
            self.assertIn(
                "\n".join(lines),
                content
            )

    def run_main(self):
        """
        Ensures the main window is displayed after executing the application.

        :emphasis: `Extends` `.ApplicationTestCase.run_main`
        """
        super().run_main()
        self.waitForWindow()


def get_suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SettingsTest))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(get_suit())
