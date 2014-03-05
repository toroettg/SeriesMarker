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

import unittest

from seriesmarker.test.database.base.memory_db_test_case import MemoryDBTestCase
from seriesmarker.test.gui.base.main_window_test import MainWindowTest

class ContextMenuTest(MainWindowTest, MemoryDBTestCase):
    """Checks the functionality of the context menu in the main view.

    .. todo:
        Find a way to really open context menu and click menu entry (the regular
        right click via QTest does not emit the proper signal).
    """

    @classmethod
    def setUpClass(cls):
        MemoryDBTestCase.setUpClass()
        MainWindowTest.setUpClass()

    def setUp(self):
        MemoryDBTestCase.setUp(self)
        MainWindowTest.setUp(self)
        add_button = self.window.ui.toolBar.widgetForAction(
            self.window.ui.action_add)
        self.click(add_button)

        from seriesmarker.persistence.model.series import Series

        self.assertEqual(self.db_session.query(Series).count(), 1,
            "No Series to remove in database.")
        self.assertEqual(self.window.model.rowCount(), 1,
            "Model/View does not contain a Series.")

    def test_delete_by_series(self):
        """Tests the removal of a series via context menu, by clicking on itself."""
        self.click(*self.find_click_target())
        self.window.ui.action_remove.trigger()

        from seriesmarker.persistence.model.series import Series

        self.assertEqual(self.db_session.query(Series).count(), 0,
            "Series was not removed from DB")
        self.assertEqual(self.window.model.rowCount(), 0,
            "Model was not cleared")

    def test_delete_by_season(self):
        """Tests the removal of a series via context menu, by clicking on a season."""
        self.expand_series()
        self.click(*self.find_click_target(season_number=0))
        self.window.ui.action_remove.trigger()

        from seriesmarker.persistence.model.series import Series

        self.assertEqual(self.db_session.query(Series).count(), 0,
            "Series was not removed from DB")
        self.assertEqual(self.window.model.rowCount(), 0,
            "Model was not cleared")

    def test_mark_watched_by_series(self):
        def check_result(check_mark_unwatched=False):
            from seriesmarker.persistence.model.series import Series
            series = self.db_session.query(Series).one()

            episode_count = watched_count = 0

            for season in series.seasons:
                for episode in season.episodes:
                    if episode.extra.watched:
                        watched_count = watched_count + 1
                    episode_count = episode_count + 1

            target_count = 0 if check_mark_unwatched else watched_count

            self.assertEqual(target_count, watched_count,
                "Not every episode has been marked correctly.")

            self.assertEqual("  {} / {}  ".format(target_count, episode_count),
                self.window.ui.tree_view.model().data(
                    self.window.ui.tree_view.model().index(0, 1)),
                "Watched marking not displayed correctly")

        viewport, target = self.find_click_target()

        self.click(viewport, target)
        self.window.ui.action_mark_watched.trigger()
        check_result()

        self.click(viewport, target)
        self.window.ui.action_mark_unwatched.trigger()
        check_result(True)

    def test_mark_watched_by_season(self):
        self.fail()

    def test_mark_watched_when_partial_watched(self):
        self.fail()

if __name__ == '__main__':
    unittest.main()
