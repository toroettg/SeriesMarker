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

from PySide.QtCore import Qt
from PySide.QtGui import QTreeView
from PySide.QtTest import QTest
from pytvdbapi.api import Show
from seriesmarker.gui.search_dialog import SearchDialog
from seriesmarker.test.database.base.persitent_db_test_case import \
    PersistentDBTestCase
from seriesmarker.test.gui.base.gui_test_case import GUITestCase
from seriesmarker.test.util.example_data_factory import ExampleDataFactory
from unittest.mock import MagicMock
import random
import unittest

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


    def test_01_sort_on_add(self):
        tree_view = self.window.findChild(QTreeView, "tree_view")
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

        self.assertEqual(
            [tree_view.model().data(tree_view.model().index(index, 0)) for
                                    index in range(0, 7)
            ],
            [
                "Buffy the Vampire Slayer",
                "Defiance",
                "Doctor Who",
                "How I Met Your Mother",
                "Mad Love",
                "Rome: Power & Glory",
                "The Wonder Years"
            ],
            "Series not sorted correctly in view after adding"
        )

    def test_02_sort_on_load(self):
        tree_view = self.window.findChild(QTreeView, "tree_view")

        self.assertEqual(
            [tree_view.model().data(tree_view.model().index(index, 0)) for
                                    index in range(0, 7)],
            [
                "Buffy the Vampire Slayer",
                "Defiance",
                "Doctor Who",
                "How I Met Your Mother",
                "Mad Love",
                "Rome: Power & Glory",
                "The Wonder Years"
            ],
            "Series not sorted correctly in view after loading from data base"
        )

    def test_03_sort_by_name(self):
        tree_view = self.window.findChild(QTreeView, "tree_view")
        viewport = tree_view.viewport()

        result_list = [
            "Buffy the Vampire Slayer",
            "Defiance",
            "Doctor Who",
            "How I Met Your Mother",
            "Mad Love",
            "Rome: Power & Glory",
            "The Wonder Years"
        ]

        self.assertEqual(
            [tree_view.model().data(tree_view.model().index(index, 0)) for
                                    index in range(0, 7)],
            result_list,
            "Series not sorted correctly in view after loading from data base"
        )

        self.assertEqual(tree_view.header().isSortIndicatorShown(), True, "No column seems to be sorted.")
        self.assertEqual(tree_view.header().sortIndicatorOrder(), Qt.AscendingOrder)

        # Expand series
        series_node_index = tree_view.model().index(2, 0)
        item_rect = tree_view.visualRect(series_node_index)
        target = item_rect.center()
        self.click(viewport, target)
        self.click(viewport, target, double_click=True)

        target = self.header_center(tree_view.header(), 0)
        self.click(tree_view.header().viewport(), target)

        self.assertEqual(tree_view.header().sortIndicatorOrder(), Qt.DescendingOrder)
        self.assertEqual(
            [tree_view.model().data(tree_view.model().index(index, 0)) for
                                    index in range(0, 7)],
            list(reversed(result_list)),
            "Series not sorted correctly after descending sort"
        )


    def tearDown(self):
        QTest.mouseMove(self.window, delay=2000)  # Emulates waiting, can be removed
        self.window.close()
        super().tearDown()

def get_suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SortingTest))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(get_suit())
