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

        self.window.move(50, 30)
        self.window.resize(800, 600)
        self.window.close()

        self._check_settings_file_contains(
            [
                "[MainWindow]",
                "state = 0",
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
                "state = 0",
                "position.x = 50",
                "position.y = 30",
                "size.width = 800",
                "size.length = 600"
            ]
        )

        self.run_main()

        self.assertEqual(
            self.window.windowState(),
            Qt.WindowNoState,
            "MainWindow should not be in a special state."
        )

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
                "state = 0",
            ]
        )

        self.run_main()

        self.assertFalse(
            self.window.isMaximized(),
            "MainWindow should not already be displayed maximized."
        )

        self.window.showMaximized()

        self.assertTrue(
            self.window.isMaximized(),
            "MainWindow should be displayed maximized."
        )

        self.window.close()

        self._check_settings_file_contains(
            [
                "[MainWindow]",
                "state = 2",
            ]
        )

    def test_05_restore_window_maximized(self):
        """Test if the application's main window is recreated maximized."""
        self._check_settings_file_contains(
            [
                "[MainWindow]",
                "state = 2",
            ]
        )

        self.run_main()

        self.assertTrue(
            self.window.isMaximized(),
            "MainWindow should be displayed maximized after application start."
        )

        self.reset_window_state()

    def test_06_store_window_minimized(self):
        """Test if the minimized window state is stored at application exit."""
        self._check_settings_file_contains(
            [
                "[MainWindow]",
                "state = 0",
            ]
        )

        self.run_main()

        self.assertFalse(
            self.window.isMinimized(),
            "MainWindow should not already be displayed minimized."
        )

        self.window.showMinimized()

        self.assertTrue(
            self.window.isMinimized(),
            "MainWindow should be displayed minimized."
        )

        self.window.close()

        self._check_settings_file_contains(
            [
                "[MainWindow]",
                "state = 1",
            ]
        )

    def test_07_restore_window_minimized(self):
        """
        Test if the application's main window is recreated minimized.

        The current wanted behavior for restoring a previously minimized
        application, is to restore it visible to the user.

        """
        self._check_settings_file_contains(
            [
                "[MainWindow]",
                "state = 1",
            ]
        )

        self.run_main()

        self.assertFalse(
            self.window.isMinimized(),
            "MainWindow should not be displayed minimized after application start."
        )

        self.reset_window_state()

    def test_08_store_window_fullscreen(self):
        """Test if the minimized window state is stored at application exit."""
        self._check_settings_file_contains(
            [
                "[MainWindow]",
                "state = 0",
            ]
        )

        self.run_main()

        self.assertFalse(
            self.window.isFullScreen(),
            "MainWindow should not already be displayed fullscreen."
        )

        self.window.showFullScreen()

        self.assertTrue(
            self.window.isFullScreen(),
            "MainWindow should be displayed fullscreen."
        )

        self.window.close()

        self._check_settings_file_contains(
            [
                "[MainWindow]",
                "state = 4",
            ]
        )

    def test_09_restore_window_fullscreen(self):
        """Test if the application's main window is recreated minimized."""
        self._check_settings_file_contains(
            [
                "[MainWindow]",
                "state = 4",
            ]
        )

        self.run_main()

        self.assertTrue(
            self.window.isFullScreen(),
            "MainWindow should be displayed fullscreen after application start."
        )

        self.reset_window_state()

    def test_10_store_window_maximized_minimized(self):
        """Test if the minimized window state is stored at application exit."""
        self._check_settings_file_contains(
            [
                "[MainWindow]",
                "state = 0",
            ]
        )

        self.run_main()

        self.assertFalse(
            self.window.isMinimized() or self.window.isMaximized(),
            "MainWindow should neither already be displayed maximized nor minimized."
        )

        self.window.showMaximized()
        self.window.showMinimized()

        self.assertTrue(
            self.window.isMinimized() and self.window.isMaximized(),
            "MainWindow should be displayed minimized after maximizing."
        )

        self.window.close()

        self._check_settings_file_contains(
            [
                "[MainWindow]",
                "state = 3",
            ]
        )

    def test_11_restore_window_maximized_minimized(self):
        """
        Test if the application's main window is recreated minimized.

        The current wanted behavior for restoring a previously minimized
        application, is to restore it visible to the user.

        """
        self._check_settings_file_contains(
            [
                "[MainWindow]",
                "state = 3",
            ]
        )

        self.run_main()

        self.assertFalse(
            self.window.isMinimized(),
            "MainWindow should not be displayed minimized after application start."
        )

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
        Ensure the main window is displayed after executing the application.

        :emphasis: `Extends` `.ApplicationTestCase.run_main`

        """
        super().run_main()
        self.waitForWindow()

    def reset_window_state(self):
        """Reset the settings' stored window state."""
        self.window.setWindowState(Qt.WindowNoState)


def get_suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SettingsTest))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(get_suit())
