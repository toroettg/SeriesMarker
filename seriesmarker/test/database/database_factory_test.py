#==============================================================================
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
#==============================================================================

from seriesmarker.persistence.database import db_add_series, db_remove_series, \
    db_commit
from seriesmarker.persistence.factory.series_factory import SeriesFactory
from seriesmarker.persistence.model.actor import Actor
from seriesmarker.persistence.model.banner import Banner
from seriesmarker.persistence.model.banner_extra import BannerExtra
from seriesmarker.persistence.model.episode import Episode
from seriesmarker.persistence.model.episode_extra import EpisodeExtra
from seriesmarker.persistence.model.genre import Genre
from seriesmarker.persistence.model.guest import Guest
from seriesmarker.persistence.model.role import Role
from seriesmarker.persistence.model.role_extra import RoleExtra
from seriesmarker.persistence.model.season import Season
from seriesmarker.persistence.model.series import Series
from seriesmarker.test.database.base.memory_db_test_case import MemoryDBTestCase
from seriesmarker.test.util.example_data_factory import ExampleDataFactory
import unittest

class DatabaseFactoryTest(MemoryDBTestCase):

    def test_create_but_no_add_series(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")
        series = SeriesFactory().new_series(pytvdb_show)  # @UnusedVariable

        self.assertEqual(self.db_session.query(Series).count(), 0, "Mismatched series count")
        self.assertEqual(self.db_session.query(Season).count(), 0, "Mismatched season count")
        self.assertEqual(self.db_session.query(Episode).count(), 0, "Mismatched episode count")
        self.assertEqual(self.db_session.query(Actor).count(), 0, "Mismatched actor count")
        self.assertEqual(self.db_session.query(Genre).count(), 0, "Mismatched genre count")

    def test_create_episode_extra(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")
        series = SeriesFactory().new_series(pytvdb_show)

        db_add_series(series)

        self.assertNotEqual(self.db_session.query(Episode).count(), 0, "No Episodes were created")

        self.assertEqual(self.db_session.query(Episode).count(), self.db_session.query(EpisodeExtra).count(), "Did not create exactly one ExtraInformation for each episode")

        self.assertEqual(series.seasons[0].episodes[0].extra.watched, False, "Watched does not default to False")


    def test_defaulting_incomplete_series(self):
        """Adresses conversion bug

        Adresses a Bug from converting a missing attribute (empty string as Rating)
        to a real (float) database-value.
        """
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("ROMEPG")

        self.assertEqual(pytvdb_show.Rating, "", "Rating was initially empty string for this series")
        self.assertEqual(pytvdb_show.FirstAired, "", "FirstAired was initially empty string for this series")

        series = SeriesFactory().new_series(pytvdb_show)

        episode = series.seasons[0].episodes[0]

        self.assertEqual(series.rating, -1, "rating did not convert to default value")
        self.assertEqual(series.first_aired, None, "Series first_aired did not convert to default value")
        self.assertEqual(episode.first_aired, None, "Episode first_aired did not convert to default value")

        db_add_series(series)

        added_series = self.db_session.query(Series).one()
        added_episode = self.db_session.query(Episode).filter_by(episode_number=1).one()

        self.assertEqual(added_series.first_aired, None, "Series first_aired was not restored correctly")
        self.assertEqual(added_episode.first_aired, None, "Episode first_aired was not restored correctly")

    def test_add_season(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")

        series = SeriesFactory().new_series(pytvdb_show)

        self.assertEqual(self.db_session.query(Season).count(), 0, "Mismatched season count")

        db_add_series(series)

        self.assertEqual(self.db_session.query(Season).count(), 3, "Mismatched season count")

        result = self.db_session.query(Series).one()

        seasonOne, seasonTwo, seasonThree = sorted(result.seasons, key=lambda season: season.season_number)

        self.assertEqual(seasonOne.series_id, result.id, "Series IDs didn't match")
        self.assertEqual(seasonTwo.series_id, result.id, "Series IDs didn't match")
        self.assertEqual(seasonThree.series_id, result.id, "Series IDs didn't match")

        self.assertEqual(seasonOne.season_number, 0, "Season number didn't match")
        self.assertEqual(seasonTwo.season_number, 1, "Season number didn't match")
        self.assertEqual(seasonThree.season_number, 2, "Season number didn't match")

        self.assertEqual(seasonOne.id, 23219, "Season ID didn't match")
        self.assertEqual(seasonTwo.id, 9285, "Season ID didn't match")
        self.assertEqual(seasonThree.id, 28494, "Season ID didn't match")

    def test_add_episode(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")

        series = SeriesFactory().new_series(pytvdb_show)

        self.assertEqual(self.db_session.query(Episode).count(), 0, "Mismatched episode count")

        db_add_series(series)

        self.assertEqual(self.db_session.query(Episode).count(), 7, "Mismatched episode count")

        seasonOne, seasonTwo, seasonThree = self.db_session.query(Series).one().seasons

        episode01, episode02 = seasonOne.episodes

        episode11 = seasonTwo.episodes[0]

        episode21 = seasonThree.episodes[0]

        self.assertEqual(episode01.id, 1159571, "Mismatched episode ID")
        self.assertEqual(episode02.id, 414248, "Mismatched episode ID")
        self.assertEqual(episode11.id, 177831, "Mismatched episode ID")
        self.assertEqual(episode21.id, 336246, "Mismatched episode ID")

        self.assertEqual(episode11.directors[0].name, "Pamela Fryman", "Mismatched episode director")
        self.assertEqual(sorted([writer.name for writer in episode11.writers]), ['Carter Bays', 'Craig Thomas'], "Mismatched episode writer")
        self.assertEqual(len(episode11.guests), 7, "Mismatched episode guest stars")

    def test_add_series_banner(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")

        series = SeriesFactory().new_series(pytvdb_show)

        self.assertEqual(self.db_session.query(Banner).count(), 0, "Mismatched banner count")
        self.assertEqual(self.db_session.query(BannerExtra).count(), 0, "Mismatched banner count")

        db_add_series(series)

        self.assertEqual(self.db_session.query(Banner).count(), 3, "Mismatched banner count")
        self.assertEqual(self.db_session.query(BannerExtra).count(), 3, "Mismatched banner_extra count")

        self.assertEqual(None, self.db_session.query(Banner).get(886577), "Fanart was not ignored")

        banner = series.extra.banner

        self.assertEqual(banner.id, 25523, "Mismatched banner id")
        self.assertEqual(banner.banner_path, 'posters/75760-1.jpg', "Mismatched banner path")

        self.assertEqual(banner.rating, 7.125, "Mismatched banner rating")
        self.assertEqual(banner.rating_count, 17, "Mismatched banner rating count")

        self.assertEqual(banner.extra.banner_url, 'http://thetvdb.com/banners/posters/75760-1.jpg', "Mismatched banner URL")

    def test_add_role(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")

        series = SeriesFactory().new_series(pytvdb_show)

        self.assertEqual(self.db_session.query(Role).count(), 0, "Mismatched Role count")
        self.assertEqual(self.db_session.query(RoleExtra).count(), 0, "Mismatched RoleExtra count")

        db_add_series(series)

        self.assertEqual(self.db_session.query(Role).count(), 2, "Mismatched Role count")
        self.assertEqual(self.db_session.query(RoleExtra).count(), 2, "Mismatched RoleRextra count")

        role = self.db_session.query(Role).filter_by(id=41068).one()

        self.assertEqual(role.id, 41068, "Mismatched role id")
        self.assertEqual(role.image, "actors/41068.jpg", "Mismatched image path")

        self.assertEqual(role.name, "Josh Radnor", "Mismatched actor name")
        self.assertEqual(role.role, "Ted Mosby", "Mismatched role name")

        self.assertEqual(role.sort_order, 0, "Mismatched role sort order")

        self.assertEqual(role.extra.image_url, "http://thetvdb.com/banners/actors/41068.jpg", "Mismatched image URL")

    def test_handle_multiple_identical_attributes(self):
        """Adresses bug, caused by improper data from thetvdb, where one guest star was listed twice

        As a precaution, attributes where this may also happen have been protected, too.
        """
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("ROMEPG")

        pytvdb_show.Genre = ["DUMMY_GENRE", "DUMMY_GENRE", "ANOTHER_GENRE"]
        pytvdb_show.Actors = ["ANOTHER_ACTOR", "DUMMY_ACTOR", "DUMMY_ACTOR"]

        episode = pytvdb_show.seasons[1].episodes[1]

        episode.Director = ["DUMMY_DIRECTOR", "ANOTHER_DIRECTOR", "DUMMY_DIRECTOR"]
        episode.Writer = ["DUMMY_WRITER", "ANOTHER_WRITER", "DUMMY_WRITER"]


        series = SeriesFactory().new_series(pytvdb_show)

        db_add_series(series)


        duplicate_actor_id = self.db_session.query(Actor).filter_by(name="DUMMY_ACTOR").one().id
        duplicate_genre_id = self.db_session.query(Genre).filter_by(name="DUMMY_GENRE").one().id
        duplicate_guest_id = self.db_session.query(Guest).filter_by(name="Shaka Bunsie").one().id


        self.assertEqual(self.db_session.query(Actor).filter_by(id=duplicate_actor_id).count(), 1, "Multiple entries of same actor in database")
        self.assertEqual(self.db_session.query(Genre).filter_by(id=duplicate_genre_id).count(), 1, "Multiple entries of same genre in database")
        self.assertEqual(self.db_session.query(Guest).filter_by(id=duplicate_guest_id).count(), 1, "Multiple entries of same genre in database")


        db_remove_series(series)


        self.assertEqual(self.db_session.query(Actor).filter_by(id=duplicate_actor_id).count(), 0, "Actor was not deleted from database")
        self.assertEqual(self.db_session.query(Genre).filter_by(id=duplicate_genre_id).count(), 0, "Genre was not deleted from database")
        self.assertEqual(self.db_session.query(Guest).filter_by(id=duplicate_guest_id).count(), 0, "Guest was not deleted from database")

    def test_resorting_update(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("DEFIANCE")
        series = SeriesFactory().new_series(pytvdb_show)

        db_add_series(series)

        self.assertEqual(self.db_session.query(Episode).count(), 3, "Initial Episode count not met")

        pytvdb_update_show = ExampleDataFactory.new_pytvdb_show("DEFIANCE-UPDATE")
        SeriesFactory().new_series(pytvdb_update_show, update=series)

        db_commit()

        ordered_episode_ids_pytvdb = [episode[1].id for episode in sorted(pytvdb_update_show[1].episodes.items())]
        ordered_episode_ids_series = [episode.id for episode in series.seasons[0].episodes]

        self.assertEqual(self.db_session.query(Episode).count(), 4, "Target Episode count not met")
        self.assertEqual(ordered_episode_ids_series, ordered_episode_ids_pytvdb, "Update did not resolve ID shift correctly")
        for i in range(0, 3):
            self.assertEqual(series.seasons[0].episodes[i].episode_name, pytvdb_update_show[1][i + 1].EpisodeName, "Update did not resolve ID shift correctly")

    def test_multiple_role_of_actor(self):
        """Tests the :class:`.RoleFactory` for handling of roles where an actor has multiple roles.

        It is assumed that an actor usually plays a single role only. Therefore,
        in cases where multiple roles exist within an Role-object anyhow, they
        are joined to a single string in the database.

        .. note::

            This database schema differs from the approach of having a separate
            object for each information to be stored. As long as lists of
            strings need to be modeled via relations (sqlalchemy restriction),
            creating objects for role names is considered to be overkill.

        """
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("WONDERYEARS")
        series = SeriesFactory().new_series(pytvdb_show)

        db_add_series(series)

        self.assertEqual(self.db_session.query(Role).count(), 1, "Role was not added to database")

        role = self.db_session.query(Role).one()

        self.assertEqual(role.role, "Narrator, Adult Kevin", "Multi-Role was not joined to single string correctly")



def get_suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DatabaseFactoryTest))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
