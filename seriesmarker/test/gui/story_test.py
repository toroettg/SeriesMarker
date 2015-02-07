# ==============================================================================
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 - 2015 Tobias Röttger <toroettg@gmail.com>
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
# ==============================================================================

from unittest.mock import MagicMock
import unittest

from PySide.QtCore import Qt, QPoint, QCoreApplication
from PySide.QtGui import QTreeView, QListView
from pytvdbapi.api import Show

from seriesmarker.persistence.database import db_get_series
from seriesmarker.net.tvdb import tvdb
from seriesmarker.test.database.base.persitent_db_test_case import \
    PersistentDBTestCase
from seriesmarker.test.gui.base.main_window_test import MainWindowTest
from seriesmarker.test.util.example_data_factory import ExampleDataFactory


class StoryTest(MainWindowTest, PersistentDBTestCase):
    """Performs tests of the application's main window.

    .. note::
        Cases in this test depend on a specific execution order.
        Therefore, case names are numbered.

    """

    @classmethod
    def setUpClass(cls):
        MainWindowTest.setUpClass()
        PersistentDBTestCase.setUpClass()

        from seriesmarker.persistence.database import db_init

        db_init()

    def setUp(self):
        super().setUp()

        for series in db_get_series():
            self.window.model.add_item(series)
        QCoreApplication.processEvents();

    def test_01_add(self):
        """Checks if a series can be added via the add-button."""
        self.check_count_series_equals(0)
        self.click_add_button()
        self.check_count_series_equals(1)

    def test_02_episode_toggle(self):
        """Checks if an episode can be marked as watched.

        Also checks if the progress information is updated accordingly.

        """
        self.expand_series()
        self.select(series_number=0, season_number=0)

        self.check_tree_view_displays("  0 / 7  ",
                                      self.get_index(series_number=0, column=1))
        self.check_tree_view_displays("0.0%",
                                      self.get_index(series_number=0, column=2))
        self.check_tree_view_displays(2, self.get_index(series_number=0,
                                                        season_number=0,
                                                        column=1))

        self.check_tree_view_displays("0.0%", self.get_index(series_number=0,
                                                             season_number=0,
                                                             column=2))

        self.mark_episode(series_number=0, season_number=0, episode_number=0)

        self.check_tree_view_displays("  1 / 7  ",
                                      self.get_index(series_number=0, column=1))
        self.check_tree_view_displays("14.3%",
                                      self.get_index(series_number=0, column=2))
        self.check_tree_view_displays(2, self.get_index(series_number=0,
                                                        season_number=0,
                                                        column=1))
        self.check_tree_view_displays("50.0%", self.get_index(series_number=0,
                                                              season_number=0,
                                                              column=2))

    def test_03_episode_tooltip(self):
        """Checks if a tooltip is displayed.

        A tooltip should be shown when hovering above an episode in the
        list view.

        """
        tree_view = self.window.findChild(QTreeView, "tree_view")
        viewport = tree_view.viewport()

        # Expand series
        item = tree_view.model().index(0, 0)
        itemRect = tree_view.visualRect(item)
        target = itemRect.center()

        self.click(viewport, target)
        self.click(viewport, target, double_click=True)

        # Expand season
        item = tree_view.model().index(0, 0, item)
        itemRect = tree_view.visualRect(item)
        target = itemRect.center()

        self.click(viewport, target)
        self.click(viewport, target, double_click=True)

        # Toggle episode
        list_view = self.window.findChild(QListView, "list_view")
        self.assertEqual(list_view.toolTip(), "",
                         "ToolTip is not empty at system start")

        viewport = list_view.viewport()
        self.move(viewport, QPoint(100, 10))
        self.move(viewport, QPoint(100,
                                   10))  # Needs to wait a little to let list_view recognize its new tooltip.
        self.assertEqual(list_view.toolTip(),
                         "<FONT COLOR=black>Dummy Overview, ToolTip test</FONT>",
                         "ToolTip not set after mouse over")

        self.move(viewport, QPoint(100, 20))
        self.move(viewport, QPoint(100,
                                   20))  # Needs to wait a little to let list_view recognize its new tooltip.
        self.assertEqual(list_view.toolTip(),
                         "<FONT COLOR=black>Music video to go with Episode 03x16 - Sandcastles In the Sand. Full video was originally posted on YouTube: http://www.youtube.com/watch?v=bgBMFwVeIGI</FONT>",
                         "ToolTip not changed when mouse over different series")

        self.move(viewport, QPoint(100, 300))
        self.move(viewport, QPoint(100,
                                   300))  # Needs to wait a little to let list_view recognize its new tooltip.
        self.assertEqual(list_view.toolTip(), "",
                         "ToolTip not cleared when leaving episode")

    def test_04_update(self):
        """Tests the GUI related part of the series update routine.

        On update, nodes of removed or added episodes and should be removed or
        added to or from the tree accordingly. While seasons and episodes
        are ordered correctly the next time they are loaded from the database
        after an update (at application start), their visual representation
        needs to be set in correct order immediately. This test case
        ensures the proper insertion into respectively removal from the GUI.

        This testcase also ensures the proper update of episode count and
        progress display in the GUI when removing or adding episodes/seasons.

        """
        tvdb.get_series = MagicMock(
            return_value=ExampleDataFactory.new_pytvdb_show("HIMYM-UPDATE"))
        Show.update = MagicMock()
        Show.load_banners = MagicMock()

        tree_view = self.window.findChild(QTreeView, "tree_view")
        viewport = tree_view.viewport()

        # Expand series
        series_node_index = tree_view.model().index(0, 0)
        item_rect = tree_view.visualRect(series_node_index)
        target = item_rect.center()
        self.click(viewport, target)
        self.click(viewport, target, double_click=True)

        # Expand season
        season2_index = tree_view.model().index(1, 0, series_node_index)
        season_rect = tree_view.visualRect(season2_index)
        target = season_rect.center()
        self.click(viewport, target)
        self.click(viewport, target, double_click=True)

        series_node = tree_view.model().data(series_node_index, Qt.UserRole)
        season2_node = tree_view.model().data(season2_index, Qt.UserRole)

        # Checking displayed series/episode information before update
        self.assertEqual(tree_view.model().data(tree_view.model().index(0, 1)),
                         "  1 / 7  ", "Initial series episode count not met.")
        self.assertEqual(tree_view.model().data(tree_view.model().index(0, 2)),
                         "14.3%", "Initial series progress not met.")
        self.assertEqual(tree_view.model().data(
            tree_view.model().index(0, 1, series_node_index)), 2,
                         "Initial season 0 episode count not met.")
        self.assertEqual(tree_view.model().data(
            tree_view.model().index(0, 2, series_node_index)), "50.0%",
                         "Initial season 0 progress not met.")
        self.assertEqual(tree_view.model().data(
            tree_view.model().index(1, 1, series_node_index)), 4,
                         "Initial season 1 episode count not met.")
        self.assertEqual(tree_view.model().data(
            tree_view.model().index(1, 2, series_node_index)), "0.0%",
                         "Initial season 1 progress not zero.")
        self.assertEqual(tree_view.model().data(
            tree_view.model().index(2, 1, series_node_index)), 1,
                         "Initial season 2 episode count not met.")
        self.assertEqual(tree_view.model().data(
            tree_view.model().index(2, 2, series_node_index)), "0.0%",
                         "Initial season 2 progress not met.")

        update_button = self.window.ui.toolBar.widgetForAction(
            self.window.ui.action_update)

        # Removing episodes and seasons
        self.assertEqual(len(series_node._children), 3,
                         "Initial season node count not met")
        self.assertEqual(len(season2_node._children), 4,
                         "Initial episode node count not met")
        self.click(update_button)
        self.assertEqual(len(series_node._children), 1,
                         "Season nodes not correctly removed from model")
        self.assertEqual(len(season2_node._children), 1,
                         "Episode nodes not correctly removed from model")
        self.assertEqual(series_node._children[0].data.season_number, 1,
                         "Wrong season node left after update")
        self.assertEqual(season2_node._children[0].data.id, 300336,
                         "Wrong episode node left after update")

        # Checking displayed series/episode information after first update
        self.assertEqual(tree_view.model().data(tree_view.model().index(0, 1)),
                         "  0 / 1  ",
                         "Series episode count display not corrected after first update.")
        self.assertEqual(tree_view.model().data(tree_view.model().index(0, 2)),
                         "0.0%",
                         "Series progress not corrected after first update.")
        self.assertEqual(tree_view.model().data(
            tree_view.model().index(0, 1, series_node_index)), 1,
                         "Season 2 episode count display not corrected after removing episodes.")
        self.assertEqual(tree_view.model().data(
            tree_view.model().index(0, 2, series_node_index)), "0.0%",
                         "Season 2 progress not corrected after removing episodes.")

        # Toggle episode, check display state to ensure it has updated
        list_view = self.window.findChild(QListView, "list_view")
        viewport = list_view.viewport()
        target = QPoint(10,
                        10)  # TODO find more generic way to click list_view item
        self.click(viewport, target)
        self.assertEqual(tree_view.model().data(tree_view.model().index(0, 1)),
                         "  1 / 1  ",
                         "Series episode count not correctly updated after toggle.")
        self.assertEqual(tree_view.model().data(
            tree_view.model().index(0, 1, series_node_index)), 1,
                         "Season 2 episode count should not be changed after toggle.")
        self.assertEqual(tree_view.model().data(tree_view.model().index(0, 2)),
                         "100.0%",
                         "Series progress not correctly updated after toggle.")
        self.assertEqual(tree_view.model().data(
            tree_view.model().index(0, 2, series_node_index)), "100.0%",
                         "Season 2 progress not correctly updated after toggle.")

        tvdb.get_series = MagicMock(
            return_value=ExampleDataFactory.new_pytvdb_show("HIMYM"))

        # Adding episodes and seasons
        self.click(update_button)
        self.assertEqual(len(series_node._children), 3,
                         "Season nodes not correctly added to model")
        self.assertEqual(len(season2_node._children), 4,
                         "Episode nodes not correctly added to model")
        self.assertEqual(
            [season.data.season_number for season in series_node._children],
            [0, 1, 2], "Season order not as expected after update")
        self.assertEqual(
            [episode.data.id for episode in season2_node._children],
            [177831, 300336, 300337, 300338],
            "Episode order not as expected after update")

        # Checking displayed series/episode information after second update
        self.assertEqual(tree_view.model().data(tree_view.model().index(0, 1)),
                         "  1 / 7  ",
                         "Series episode count display not corrected after second update.")
        self.assertEqual(tree_view.model().data(tree_view.model().index(0, 2)),
                         "14.3%",
                         "Series progress not corrected after second update.")
        self.assertEqual(tree_view.model().data(
            tree_view.model().index(0, 1, series_node_index)), 2,
                         "Season 0 episode count display not met after adding season.")
        self.assertEqual(tree_view.model().data(
            tree_view.model().index(0, 2, series_node_index)), "0.0%",
                         "Season 0 progress not met after adding season.")
        self.assertEqual(tree_view.model().data(
            tree_view.model().index(1, 1, series_node_index)), 4,
                         "Season 1 episode count display not met after adding episodes.")
        self.assertEqual(tree_view.model().data(
            tree_view.model().index(1, 2, series_node_index)), "25.0%",
                         "Season 1 progress not corrected after adding episodes.")
        self.assertEqual(tree_view.model().data(
            tree_view.model().index(2, 1, series_node_index)), 1,
                         "Season 2 episode count display not met after adding season.")
        self.assertEqual(tree_view.model().data(
            tree_view.model().index(2, 2, series_node_index)), "0.0%",
                         "Season 2 progress not met after adding season.")

    def test_05_remove(self):
        self.assertEqual(self.window.model.rowCount(), 1,
                         "Selected series was not added to model")

        # Select Series
        tree_view = self.window.findChild(QTreeView, "tree_view")
        viewport = tree_view.viewport()

        item = tree_view.model().index(0, 0)
        itemRect = tree_view.visualRect(item)
        target = itemRect.center()

        self.click(viewport, target)

        # Delete selected Series
        remove_button = self.window.ui.toolBar.widgetForAction(
            self.window.ui.action_remove)
        self.click(remove_button)

        self.assertEqual(self.window.model.rowCount(), 0,
                         "Model was not cleared")


def get_suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(StoryTest))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(get_suit())
