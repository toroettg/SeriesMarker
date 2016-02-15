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

from unittest.mock import patch

from seriesmarker.gui.search_dialog import SearchDialog
from seriesmarker.test.gui.base.main_window_test_case import MainWindowTestCase
from seriesmarker.test.util.example_data_factory import ExampleDataFactory


class MainWindowMockedSearchMixin(MainWindowTestCase):
    def setUp(self):
        super().setUp()

        self.mock_patcher_dialog_exec = patch(
            "seriesmarker.gui.main_window.SearchDialog.exec_",
            return_value=SearchDialog.Accepted
        )
        self.mock_dialog_exec = self.mock_patcher_dialog_exec.start()
        self.addCleanup(self.mock_patcher_dialog_exec.stop)

        self.mock_patcher_show_update = patch("pytvdbapi.api.Show.update")
        self.mock_patcher_show_update.start()
        self.addCleanup(self.mock_patcher_show_update.stop)

    def click_add_button(self, times=1, to_add=None):
        if to_add and isinstance(to_add, list):
            config = {"side_effect": to_add}
        else:
            config = {
                "return_value": to_add if to_add else ExampleDataFactory.new_pytvdb_show(
                    "HIMYM")
            }
        with patch("seriesmarker.gui.main_window.SearchDialog.result_value",
                   **config):
            for i in range(times):
                super().click_add_button()
        self.assertEqual(
            self.mock_dialog_exec.call_count,
            times,
            "'Add' not called correctly"
        )
