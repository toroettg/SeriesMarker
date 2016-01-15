from unittest.mock import patch

from PySide.QtCore import Qt, QPoint
from PySide.QtGui import QTreeView, QListView
from PySide.QtTest import QTest

from seriesmarker.gui.main_window import MainWindow
from seriesmarker.gui.search_dialog import SearchDialog
from seriesmarker.test.gui.base.gui_test_case import GUITestCase
from seriesmarker.test.util.example_data_factory import ExampleDataFactory


class MainWindowTest(GUITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        super().setUp()

        self.window = MainWindow()

        self.window.show()
        QTest.qWaitForWindowShown(self.window)

        self.tree_view = self.window.findChild(QTreeView, "tree_view")
        self.list_view = self.window.findChild(QListView, "list_view")

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
        add_button = self.window.ui.toolBar.widgetForAction(
                self.window.ui.action_add)

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
                self.click(add_button)
        self.assertEqual(self.mock_dialog_exec.call_count, times,
                         "'Add' not called correctly")

    def expand_series(self, series_number=0):
        """Expands the series with given index in the main window.

        :param series_number: The index of the series to expand, from
            top to bottom as displayed in the main window, starting at zero.
        :type series_number: :class:`int`

        """
        viewport, target = self.find_click_target(series_number)

        self.click(viewport, target)
        self.click(viewport, target, double_click=True)

    def select(self, series_number, season_number=None):
        self.click(*self.find_click_target(series_number=series_number,
                                           season_number=season_number))

    def mark_episode(self, series_number, season_number, episode_number,
                     expected=Qt.Checked):
        self.click(*self.find_click_target(series_number=series_number,
                                           season_number=season_number,
                                           episode_number=episode_number,
                                           offset=(10, 10)))
        episode_index = self.get_index(series_number=series_number,
                                       season_number=season_number,
                                       episode_number=episode_number,
                                       model=self.list_view.model())
        episode_node = self.list_view.model().data(episode_index, Qt.UserRole)
        self.assertEqual(expected, self.list_view.model().data(episode_index,
                                                               Qt.CheckStateRole),
                         "Model did not return expected CheckState for episode")
        if expected == Qt.Checked:
            expected_boolean = True
        elif expected == Qt.Unchecked:
            expected_boolean = False
        else:
            expected_boolean = None
        self.assertEqual(expected_boolean, episode_node.checked(),
                         "Node did not return expected value from checked() method.")
        self.assertEqual(expected_boolean, episode_node.data.extra.watched,
                         "Episode was not toggled")

    def find_click_target(self, series_number=0, season_number=None,
                          episode_number=None, offset=None):
        """Finds the coordinates of an item in the tree view.

        :param series_number: The number of the series to find the
            coordinates for.
        :type series_number: :class:`int`
        :param season_number: The number of the season to find the
            coordinates for.
        :type season_number: :class:`int`
        :param episode_number: The number of the episode to find the
            coordinates for.
        :type episode_number: :class:`int`
        :param offset: The offset from the top left corner of the item
            to click at. Defaults to the center of the item if not set.
        :type offset: tuple(:class:`int`, :class:`int`)

        :returns: The viewport of the tree view and the coordinates of
            the item's center.

        """
        if episode_number is not None:
            model = self.list_view.model()
            view = self.list_view
        else:
            model = self.tree_view.model()
            view = self.tree_view

        index = self.get_index(series_number=series_number,
                               season_number=season_number,
                               episode_number=episode_number, model=model)
        if offset:
            target = view.visualRect(index).topLeft() + QPoint(*offset)
        else:
            target = view.visualRect(index).center()
        return view.viewport(), target

    def check_list_view_displays(self, expected, series_number, season_number,
                                 episode_number, column=1,
                                 role=Qt.DisplayRole):
        index = self.get_index(series_number=series_number,
                               season_number=season_number,
                               episode_number=episode_number, column=column,
                               model=self.list_view.model())
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
                    self.get_index(series_number=series_number,
                                   season_number=season_number,
                                   episode_number=i,
                                   model=self.list_view.model()),
                    Qt.CheckStateRole) == Qt.Checked:
                count_watched += 1
        self.assertEqual(expected, count_watched,
                         "Number of watched episodes did not match.")

    def get_index(self, series_number, season_number=None, episode_number=None,
                  column=0, model=None):
        def guard_index(index):
            if index.isValid():
                return index
            else:
                self.fail("Requested index is invalid.")

        if model is None:
            model = self.tree_view.model()

        node_index = guard_index(model.index(series_number, column))
        if season_number is not None:
            node_index = guard_index(
                    model.index(season_number, column, node_index))
            if episode_number is not None:
                node_index = guard_index(
                        model.index(episode_number, column, node_index))

        return node_index

    def check_count_series_equals(self, expected):
        self.assertEqual(self.window.model.rowCount(), expected,
                         "Model does not contain expected number of Series.")

    def tearDown(self):
        super().tearDown()

        QTest.mouseMove(self.window,
                        delay=2000)  # Emulates waiting, can be removed

        self.window.close()
