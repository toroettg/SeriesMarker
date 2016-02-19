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

from unittest.mock import MagicMock, patch

from seriesmarker.test.gui.base.main_window_test_case import MainWindowTestCase


class ApplicationTestCase(MainWindowTestCase):
    """Test base that runs the whole application initialization."""

    def setUp(self):
        super().setUp()

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

    def run_main(self):
        from seriesmarker import seriesmarker
        seriesmarker.main()
