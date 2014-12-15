#==============================================================================
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 - 2014 Tobias Röttger <toroettg@gmail.com>
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

from seriesmarker.persistence.database import db_add_series

from seriesmarker.persistence.model.episode import Episode
from seriesmarker.persistence.model.genre import Genre  # @UnusedImport, Genre needed for DB import
from seriesmarker.persistence.model.season import Season
from seriesmarker.persistence.model.series import Series
from seriesmarker.test.database.base.memory_db_test_case import MemoryDBTestCase
import unittest

class DatabaseModelTest(MemoryDBTestCase):

    def test_simple_show(self):
        series = Series(series_name="TestSeries", id=12345)

        self.db_session.add(series)

        self.db_session.commit()

        result = self.db_session.query(Series).one()

        self.assertEqual(result.series_name, "TestSeries")

    def test_ordering_series(self):
        series = Series()

        j = 0

        for i in list(range(50, 100)) + list(range(0, 50)):
            season = Season()
            season.id = i
            season.season_number = j
            series.seasons.append(season)
            j = j + 1

        db_add_series(series)

        i = 50
        j = 0

        for season in self.db_session.query(Series).one().seasons:
            self.assertEqual(season.id, i, "Season ID was not expected, seasons in wrong order")
            self.assertEqual(season.season_number, j, "Season number was not expected, seasons in wrong order")
            i = i + 1 if i < 99 else 0
            j = j + 1

    def test_ordering_episodes(self):
        series = Series()

        season = Season()

        j = 0

        for i in list(range(50, 100)) + list(range(0, 50)):
            episode = Episode()
            episode.id = i
            episode.episode_number = j
            season.episodes.append(episode)
            j = j + 1

        series.seasons.append(season)

        db_add_series(series)

        i = 50
        j = 0

        for episode in self.db_session.query(Season).one().episodes:
            self.assertEqual(episode.id, i, "Episode ID was not expected, episodes in wrong order")
            self.assertEqual(episode.episode_number, j, "Episode number was not expected, episodes in wrong order")
            i = i + 1 if i < 99 else 0
            j = j + 1


def get_suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DatabaseModelTest))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
