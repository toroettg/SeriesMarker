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

from PySide.QtCore import Qt, QPoint
from PySide.QtGui import QTreeView, QListView
from PySide.QtTest import QTest

from seriesmarker.gui.main_window import MainWindow
from seriesmarker.test.gui.base.gui_test_case import GUITestCase


class MainWindowTestCase(GUITestCase):
    """Test base that adds main window controls."""

    def setUp(self):
        super().setUp()

        self.window = MainWindow()

        self.tree_view = self.window.findChild(QTreeView, "tree_view")
        self.list_view = self.window.findChild(QListView, "list_view")

    def expand(self, series_number, season_number=None):
        """Expands a series or a season in the main window.

        :param series_number: The index of the series to expand, from
            top to bottom as displayed in the main window, starting at zero.
        :type series_number: :class:`int`
        :param season_number: The index of the season to expand, from
            top to bottom as displayed in the main window, starting at zero.
        :type season_number: :class:`int`

        """
        viewport, target = self.find_click_target(series_number, season_number)

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

    def click_add_button(self):
        add_button = self.window.ui.toolBar.widgetForAction(
            self.window.ui.action_add
        )
        self.click(add_button)

    def click_remove_button(self):
        remove_button = self.window.ui.toolBar.widgetForAction(
            self.window.ui.action_remove)
        self.click(remove_button)

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
            self.get_index(series_number, season_number),
            Qt.UserRole
        )

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
                model.index(season_number, column, node_index)
            )
            if episode_number is not None:
                node_index = guard_index(
                    model.index(episode_number, column, node_index)
                )

        return node_index

    def check_count_series_equals(self, expected):
        self.assertEqual(self.window.model.rowCount(), expected,
                         "Model does not contain expected number of Series.")

    def waitForWindow(self):
        self.window.raise_()
        QTest.qWaitForWindowShown(self.window)

    def tearDown(self):
        self.wait(delay=2000)

        if self.window.isVisible():
            self.window.close()

        super().tearDown()
