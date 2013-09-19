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

import random
import unittest
from unittest.mock import MagicMock

from PySide.QtCore import Qt, QModelIndex
from PySide.QtGui import QTreeView
from PySide.QtTest import QTest
from pytvdbapi.api import Show
from seriesmarker.gui.search_dialog import SearchDialog

from seriesmarker.test.database.base.persitent_db_test_case import \
    PersistentDBTestCase
from seriesmarker.test.gui.base.gui_test_case import GUITestCase
from seriesmarker.test.util.example_data_factory import ExampleDataFactory


class SortingTest(GUITestCase, PersistentDBTestCase):
    """Performs tests of the application's main window's features
    related to sorting.

    .. note::
        Cases in this test depend on a specific execution order.
        Therefore, case names are numbered.

    """
    @classmethod
    def setUpClass(cls):
        GUITestCase.setUpClass()
        PersistentDBTestCase.setUpClass()

        from seriesmarker.persistence.database import db_init
        db_init()

    def setUp(self):
        from seriesmarker.gui.main_window import MainWindow
        self.window = MainWindow()
        self.window.show()
        QTest.qWaitForWindowShown(self.window)
        self.tree_view = self.window.findChild(QTreeView, "tree_view")


    def test_01_sort_on_add(self):
        add_button = self.window.ui.toolBar.widgetForAction(self.window.ui.action_add)

        Show.update = MagicMock()

        series = []
        series_names = ["HIMYM", "DRWHO", "BUFFY", "MADLOVE", "ROMEPG",
                        "WONDERYEARS", "DEFIANCE"]
        random.shuffle(series_names)

        for name in series_names:
            series.append(ExampleDataFactory.new_pytvdb_show(name))

        SearchDialog.exec_ = MagicMock(return_value=SearchDialog.Accepted)
        SearchDialog.result_value = MagicMock(side_effect=series)

        self.assertEqual(self.window.model.rowCount(), 0, "Default model is not empty")

        for x in range(len(series)):  # @UnusedVariable
            self.click(add_button)

        self.assertEqual(SearchDialog.exec_.call_count, 7, "'Add' not called correctly")
        self.assertEqual(self.window.model.rowCount(), 7, "Selected series were not added")

        # Create progress by marking specific episodes watched
        model = self.tree_view.model()
        for series_number in range(0, model.rowCount()):
            series_index = model.index(series_number, 0)
            series_node = model.node_at(series_index)

            name = series_node.name()
            if name == "How I Met Your Mother":
                select = 6
            else:
                select = 1
            episodes = []
            for season_node in series_node.children:
                for episode_node in season_node.children:
                    episodes.append(episode_node)
            for index in range(0, select):
                episodes[index].toggle_check()

        result = [
            ("Buffy the Vampire Slayer", "  1 / 1  ", "100.0%"),
            ("Defiance", "  1 / 3  ", "33.3%"),
            ("Doctor Who", "  1 / 7  ", "14.3%"),
            ("How I Met Your Mother", "  6 / 7  ", "85.7%"),
            ("Mad Love", "  1 / 2  ", "50.0%"),
            ("Rome: Power & Glory", "  1 / 2  ", "50.0%"),
            ("The Wonder Years", "  1 / 1  ", "100.0%")
        ]
        self._check_displayed_data(0, Qt.AscendingOrder, result, "Sort view after adding a series")

    def test_02_sort_on_load(self):
        result = [
            ("Buffy the Vampire Slayer", "  1 / 1  ", "100.0%"),
            ("Defiance", "  1 / 3  ", "33.3%"),
            ("Doctor Who", "  1 / 7  ", "14.3%"),
            ("How I Met Your Mother", "  6 / 7  ", "85.7%"),
            ("Mad Love", "  1 / 2  ", "50.0%"),
            ("Rome: Power & Glory", "  1 / 2  ", "50.0%"),
            ("The Wonder Years", "  1 / 1  ", "100.0%")
        ]
        self._check_displayed_data(0, Qt.AscendingOrder, result, "Sort view after loading from data base")

    def test_03_sort_series_by_name(self):
        target = self.header_center(self.tree_view.header(), 0)

        result = [
            ("Buffy the Vampire Slayer", "  1 / 1  ", "100.0%"),
            ("Defiance", "  1 / 3  ", "33.3%"),
            ("Doctor Who", "  1 / 7  ", "14.3%"),
            ("How I Met Your Mother", "  6 / 7  ", "85.7%"),
            ("Mad Love", "  1 / 2  ", "50.0%"),
            ("Rome: Power & Glory", "  1 / 2  ", "50.0%"),
            ("The Wonder Years", "  1 / 1  ", "100.0%")
        ]
        self._check_displayed_data(0, Qt.AscendingOrder, result, "Sort view after loading from data base")
        self.click(self.tree_view.header().viewport(), target)
        self._check_displayed_data(0, Qt.DescendingOrder, list(reversed(result)), "Sort view after descending sort by name")

    def test_04_sort_season_by_name(self):
        # Expand series
        viewport = self.tree_view.viewport()
        series_node_index = self.tree_view.model().index(2, 0)
        item_rect = self.tree_view.visualRect(series_node_index)
        target = item_rect.center()
        self.click(viewport, target)
        self.click(viewport, target, double_click=True)

        result = [
            ("Season 0", 1, "100.0%"),
            ("Season 1", 1, "0.0%"),
            ("Season 2", 1, "0.0%"),
            ("Season 10", 1, "0.0%"),
            ("Season 11", 1, "0.0%"),
            ("Season 20", 1, "0.0%"),
            ("Season 21", 1, "0.0%")
        ]

        self._check_displayed_data(0, Qt.AscendingOrder, result, "Sort season after loading from data base", parent=series_node_index)

        target = self.header_center(self.tree_view.header(), 0)
        self.click(self.tree_view.header().viewport(), target)
        series_node_index = self.tree_view.model().index(4, 0)  # change of order changed index too

        self._check_displayed_data(0, Qt.DescendingOrder, result, "Changing sort order should not alter season order", parent=series_node_index)

    def test_05_sort_series_by_episodes(self):
        target = self.header_center(self.tree_view.header(), 1)

        result_asc = [
            ("Buffy the Vampire Slayer", "  1 / 1  ", "100.0%"),
            ("Defiance", "  1 / 3  ", "33.3%"),
            ("Doctor Who", "  1 / 7  ", "14.3%"),
            ("Mad Love", "  1 / 2  ", "50.0%"),
            ("Rome: Power & Glory", "  1 / 2  ", "50.0%"),
            ("The Wonder Years", "  1 / 1  ", "100.0%"),
            ("How I Met Your Mother", "  6 / 7  ", "85.7%"),
        ]
        result_dsc = list(result_asc[-1:]) + result_asc[0:-1]

        self.click(self.tree_view.header().viewport(), target)
        self._check_displayed_data(1, Qt.AscendingOrder, result_asc, "Sort view after ascending sort by episodes")
        self.click(self.tree_view.header().viewport(), target)
        self._check_displayed_data(1, Qt.DescendingOrder, result_dsc, "Sort view after descending sort by episodes")

    def test_06_sort_series_by_progress(self):
        """Tests 'intelligent' sorting by progress.
        
        Series are sorted by numerical progress first, then by total
        number of watched episodes and finally by series name. 
        
        Completed series (progress = 100.0%) are being ignored by progress
        sort and added at the end of the list in alphanumerical order.
        
        """
        target = self.header_center(self.tree_view.header(), 2)

        result_asc = [
            ("Doctor Who", "  1 / 12 ", "8.3%"),
            ("Defiance", "  1 / 3  ", "33.3%"),
            ("Rome: Power & Glory", "  1 / 2  ", "50.0%"),
            ("Mad Love", "  2 / 4  ", "50.0%"),
            ("How I Met Your Mother", "  6 / 7  ", "85.7%"),
            ("Buffy the Vampire Slayer", "  1 / 1  ", "100.0%"),
            ("The Wonder Years", "  1 / 1  ", "100.0%")
        ]

        result_dsc = list(reversed(result_asc[0:5])) + result_asc[5:]

        self.click(self.tree_view.header().viewport(), target)
        self._check_displayed_data(2, Qt.AscendingOrder, result_asc, "Sort view after ascending sort by progress")
        self.click(self.tree_view.header().viewport(), target)
        self._check_displayed_data(2, Qt.DescendingOrder, result_dsc, "Sort view after descending sort by progress")

    def tearDown(self):
        QTest.mouseMove(self.window, delay=2000)  # Emulates waiting, can be removed
        self.window.close()
        super().tearDown()

    def _check_displayed_data(self, expected_section, expected_order, expected_result, msg, parent=QModelIndex()):
        header = self.tree_view.header()
        self.assertEqual(header.isSortIndicatorShown(), True, "No column seems to be sorted.")
        self.assertEqual(header.sortIndicatorSection(), expected_section, "Not sorted by correct column.")
        self.assertEqual(header.sortIndicatorOrder(), expected_order, "Not sorted by correct order.")

        model = self.tree_view.model()
        for column in range(0, 3):
            self.assertEqual(
                [model.data(model.index(index, column, parent)) for index in range(0, 7)],
                [elem[column] for elem in expected_result],
                "Column '{}' not sorted correctly in case: {}.".format(
                    self.tree_view.model().headerData(column, Qt.Horizontal, Qt.DisplayRole),
                    msg
                )
            )

def get_suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SortingTest))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(get_suit())
