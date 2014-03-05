from unittest.mock import MagicMock

from PySide.QtGui import QTreeView
from PySide.QtTest import QTest
from pytvdbapi.api import Show

from seriesmarker.gui.main_window import MainWindow
from seriesmarker.gui.search_dialog import SearchDialog
from seriesmarker.test.gui.base.gui_test_case import GUITestCase
from seriesmarker.test.util.example_data_factory import ExampleDataFactory

class MainWindowTest(GUITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        self.window = MainWindow()
        self.window.show()
        QTest.qWaitForWindowShown(self.window)

        SearchDialog.exec_ = MagicMock(return_value=SearchDialog.Accepted)
        SearchDialog.result_value = MagicMock(
            return_value=ExampleDataFactory.new_pytvdb_show("HIMYM"))
        Show.update = MagicMock()

        self.assertEqual(self.window.model.rowCount(), 0,
            "Default model is not empty")

    def click_add_button(self):
        add_button = self.window.ui.toolBar.widgetForAction(
            self.window.ui.action_add)
        self.click(add_button)
        SearchDialog.exec_.assert_called_once_with()

        self.assertEqual(self.window.model.rowCount(), 1,
            "Selected series was not added")

    def expand_series(self, series_number=0):
        """Expands the series with given index in the main window.

        :param series_number: The index of the series to expand, from top to
            bottom as displayed in the main window, starting at zero.
        :type series_number: integer

        """
        viewport, target = self.find_click_target(series_number)

        self.click(viewport, target)
        self.click(viewport, target, double_click=True)

    def find_click_target(self, series_number=0, season_number=None):
        """Finds the coordinates of an item in the tree view.

        :param series_number: The number of the series to find the coordinates for.
        :type series_number: integer
        The number of the series to find the coordinates for.
        :type season_number:

        :returns: The viewport of the tree view and the coordinates of the item's center.

        """
        tree_view = self.window.findChild(QTreeView, "tree_view")
        node_index = tree_view.model().index(series_number, 0)

        if season_number:
            node_index = tree_view.model().index(season_number, 0, node_index)

        return tree_view.viewport(), tree_view.visualRect(node_index).center()

    def tearDown(self):
        QTest.mouseMove(self.window,
            delay=2000)  # Emulates waiting, can be removed

        self.window.close()