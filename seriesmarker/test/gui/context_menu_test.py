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

import unittest

from PySide.QtCore import Qt

from seriesmarker.test.core.base.application_test_case import ApplicationTestCase
from seriesmarker.test.database.base.memory_db_test_case import MemoryDBTestCase
from seriesmarker.test.gui.base.main_window_test_mixin import MainWindowMockedSearchMixin


class ContextMenuTest(MemoryDBTestCase, MainWindowMockedSearchMixin,
                      ApplicationTestCase):
    """Checks the functionality of the context menu in the main view.

    .. todo:
        Find a way to really open context menu and click menu entry (the regular
        right click via QTest does not emit the proper signal).
    """

    def setUp(self):
        super().setUp()

        self.run_main()
        self.waitForWindow()

        self.check_count_series_equals(0)
        self.click_add_button()
        self.check_count_series_equals(1)

        from seriesmarker.persistence.model.series import Series

        self.assertEqual(self.db_session.query(Series).count(), 1,
                         "No Series to remove in database.")

    def test_delete_by_series(self):
        """Tests the removal of a series via context menu, by clicking on itself."""
        self.select(series_number=0)
        self.window.ui.action_remove.trigger()

        from seriesmarker.persistence.model.series import Series

        self.assertEqual(self.db_session.query(Series).count(), 0,
                         "Series was not removed from DB")
        self.assertEqual(self.window.model.rowCount(), 0,
                         "Model was not cleared")

    def test_delete_by_season(self):
        """Tests the removal of a series via context menu, by clicking on a season."""
        self.expand(series_number=0)
        self.select(series_number=0, season_number=0)
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
                    episode_count += 1

            target_count = 0 if check_mark_unwatched else watched_count

            self.assertEqual(target_count, watched_count,
                             "Not every episode has been marked correctly.")
            self.check_tree_view_displays(
                "  {} / {}  ".format(target_count, episode_count),
                self.get_index(series_number=0, column=1))

        self.select(series_number=0)
        self.window.ui.action_mark_watched.trigger()
        check_result()

        self.select(series_number=0)
        self.window.ui.action_mark_unwatched.trigger()
        check_result(True)

    def test_mark_watched_by_season(self):
        def _check_result(check_state):
            from seriesmarker.persistence.model.episode import Episode

            series_index = self.get_index(series_number=0, column=1)
            episode_count = self.db_session.query(Episode).count()

            season_index = self.get_index(series_number=0, season_number=1)
            season_episode_count = self.tree_view.model().node_at(
                season_index).child_count()

            target_count = 0 if check_state == Qt.Unchecked else season_episode_count

            for i in range(season_episode_count):
                self.check_list_view_displays(check_state, series_number=0,
                                              season_number=1,
                                              episode_number=i,
                                              column=0, role=Qt.CheckStateRole)

                self.check_tree_view_displays(
                    "  {} / {}  ".format(target_count, episode_count),
                    series_index)

        self.expand(series_number=0)
        self.select(series_number=0, season_number=1)

        _check_result(Qt.Unchecked)

        self.window.ui.action_mark_watched.trigger()

        _check_result(Qt.Checked)

        self.select(series_number=0, season_number=1)
        self.window.ui.action_mark_unwatched.trigger()

        _check_result(Qt.Unchecked)

    def test_mark_watched_when_partial_watched(self):
        self.expand(series_number=0)
        self.select(series_number=0, season_number=1)

        self.mark_episode(series_number=0, season_number=1, episode_number=0)
        self.mark_episode(series_number=0, season_number=1, episode_number=2)

        self.check_count_marked_episodes_equals(season_number=1, expected=2)

        self.select(series_number=0, season_number=1)
        self.window.ui.action_mark_watched.trigger()
        self.check_count_marked_episodes_equals(season_number=1, expected=4)

        self.mark_episode(series_number=0, season_number=1, episode_number=1,
                          expected=Qt.Unchecked)
        self.mark_episode(series_number=0, season_number=1, episode_number=3,
                          expected=Qt.Unchecked)
        self.check_count_marked_episodes_equals(season_number=1, expected=2)

        self.select(series_number=0, season_number=1)
        self.window.ui.action_mark_unwatched.trigger()
        self.check_count_marked_episodes_equals(season_number=1, expected=0)


def get_suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ContextMenuTest))
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(get_suit())
