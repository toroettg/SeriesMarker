from unittest.mock import MagicMock

from PySide.QtCore import Qt
from PySide.QtGui import QTreeView, QListView
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

        self.tree_view = self.window.findChild(QTreeView, "tree_view")
        self.list_view = self.window.findChild(QListView, "list_view")

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

    def find_click_target(self, series_number=0, season_number=None,
                          episode_number=None, offset=None):
        """Finds the coordinates of an item in the tree view.

        :param series_number: The number of the series to find the coordinates for.
        :type series_number: integer
        The number of the series to find the coordinates for.
        :type season_number:

        :returns: The viewport of the tree view and the coordinates of the item's center.

        """
        index = self.get_index(series_number, season_number, episode_number)
        view = self.list_view if episode_number is not None else self.tree_view
        if offset:
            target = view.visualRect(index).topLeft() + offset
        else:
            target = view.visualRect(index).center()
        return view.viewport(), target

    def check_list_view_displays(self, expected, episode_number, column=1,
                                 role=Qt.DisplayRole):
        index = self.get_index(episode_number=episode_number, column=column)
        data = self.list_view.model().data(index, role)
        self.assertEqual(expected, data,
                         "Displayed data for episode incorrect.")

    def check_tree_view_displays(self, expected, index):
        self.assertEqual(expected, self.tree_view.model().data(index),
                         "Displayed data for index incorrect.")

    def check_count_marked_episodes_equals(self, expected, series_number=0,
                                           season_number=0):

        season_node = self.tree_view.model().data(
            self.get_index(series_number, season_number), Qt.UserRole)

        count_watched = 0
        for i in range(season_node.child_count()):
            if self.list_view.model().data(
                    self.get_index(series_number, season_number, i),
                    Qt.CheckStateRole) == Qt.Checked:
                count_watched += 1
        self.assertEqual(expected, count_watched,
                         "Number of watched episodes did not match.")

    def get_index(self, series_number=0, season_number=None,
                  episode_number=None, column=0):
        if episode_number is not None:
            node_index = self.list_view.model().index(episode_number, column,
                                                      self.list_view.rootIndex())
        else:
            node_index = self.tree_view.model().index(series_number, column)
            if season_number is not None:
                node_index = self.tree_view.model().index(season_number, column,
                                                          node_index)
        if node_index.isValid():
            return node_index
        else:
            self.fail("Requested index is invalid.")

    def tearDown(self):
        QTest.mouseMove(self.window,
                        delay=2000)  # Emulates waiting, can be removed

        self.window.close()