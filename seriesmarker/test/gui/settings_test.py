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
from unittest.mock import patch, MagicMock

from seriesmarker.test.database.base.persitent_db_test_case import \
    PersistentDBTestCase
from seriesmarker.test.gui.base.gui_test_case import GUITestCase

class SettingsTest(PersistentDBTestCase, GUITestCase):
    """Performs tests related to the handling of end-user settings.

    .. note::
        Cases in this test depend on a specific execution order.
        Therefore, case names are numbered.

    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

        from gui.main_window import MainWindow
        self.window = MainWindow()

        app_patcher = patch("seriesmarker.seriesmarker.QApplication",
                            return_value=self.app)
        window_patcher = patch("seriesmarker.seriesmarker.MainWindow",
                               return_value=self.window)
        exit_patcher = patch("seriesmarker.seriesmarker.sys.exit")

        for patcher in [app_patcher, window_patcher, exit_patcher]:
            mock = patcher.start()
            self.addCleanup(patcher.stop)

            if patcher is app_patcher:
                mock.return_value.exec_ = MagicMock()

    def test_01_initial_behavior(self):
        """Tests handling of non-existing settings file."""
        from seriesmarker.util import config
        from seriesmarker.util.settings import settings

        self.assertEqual(
            os.path.commonprefix(
                [
                    settings._CONFIG_FILE,
                    tempfile.gettempdir()
                ]
            ),
            tempfile.gettempdir(),
            "Settings file should reside in tmp directory for tests."

        )

        self.assertFalse(os.path.exists(config.dirs.user_config_dir),
                         "Settings directory should not exist.")

        self.assertFalse(os.path.exists(settings._CONFIG_FILE),
                         "Settings file should not exist.")

        from seriesmarker import seriesmarker
        seriesmarker.main()

        self.assertTrue(
            os.path.exists(config.dirs.user_config_dir),
            "Settings directory should be created at application start."
        )

        self.assertFalse(
            os.path.exists(settings._CONFIG_FILE),
            "Settings file should not be created at application start."
        )

    def tearDown(self):
        self.window.close()
        super().tearDown()


    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
