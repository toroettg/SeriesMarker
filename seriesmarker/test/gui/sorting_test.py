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

from PySide.QtGui import QTreeView
from PySide.QtTest import QTest
from pytvdbapi.api import Show
from seriesmarker.gui.search_dialog import SearchDialog
from seriesmarker.test.database.base.memory_db_test_case import \
    MemoryDBTestCase
from seriesmarker.test.gui.base.gui_test_case import GUITestCase
from seriesmarker.test.util.example_data_factory import ExampleDataFactory
from unittest.mock import MagicMock
import unittest

class SortingTest(GUITestCase, MemoryDBTestCase):
    """Performs tests of the application's main window.
    
    .. note::
        Cases in this test depend on a specific execution order.
        Therefore, case names are numbered.
    
    """
    @classmethod
    def setUpClass(cls):
        GUITestCase.setUpClass()

    def setUp(self):
        super().setUp()

        from seriesmarker.gui.main_window import MainWindow
        self.window = MainWindow()
        self.window.show()
        QTest.qWaitForWindowShown(self.window)


    def test_sort_by_name(self):
        tree_view = self.window.findChild(QTreeView, "tree_view")
        viewport = tree_view.viewport()
        add_button = self.window.ui.toolBar.widgetForAction(self.window.ui.action_add)

        Show.update = MagicMock()
        series1 = ExampleDataFactory.new_pytvdb_show("HIMYM")
        series2 = ExampleDataFactory.new_pytvdb_show("DRWHO")
        SearchDialog.exec_ = MagicMock(return_value=SearchDialog.Accepted)
        SearchDialog.result_value = MagicMock(side_effect=[series1, series2])

        self.assertEqual(self.window.model.rowCount(), 0, "Default model is not empty")

        self.click(add_button)
        self.click(add_button)

        self.assertEqual(SearchDialog.exec_.call_count, 2, "'Add' not called correctly")
        self.assertEqual(self.window.model.rowCount(), 2, "Selected series were not added")

        # Expand series
        series_node_index = tree_view.model().index(1, 0)
        item_rect = tree_view.visualRect(series_node_index)
        target = item_rect.center()

        self.click(viewport, target)
        self.click(viewport, target, double_click=True)

        self.assertEqual([tree_view.model().data(
            tree_view.model().index(0, 0)),
            tree_view.model().data(series_node_index)],
            ["Doctor Who", "How I Met Your Mother"],
            "Series not sorted correctly after adding")





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
