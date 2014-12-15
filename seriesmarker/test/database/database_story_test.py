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

from seriesmarker.persistence.database import db_add_series, db_remove_series, \
    db_commit, db_get_series
from seriesmarker.persistence.exception import EntityExistsException, \
    EntityNotFoundException
from seriesmarker.persistence.factory.series_factory import SeriesFactory
from seriesmarker.persistence.model.actor import Actor
from seriesmarker.persistence.model.banner import Banner
from seriesmarker.persistence.model.banner_extra import BannerExtra
from seriesmarker.persistence.model.director import Director
from seriesmarker.persistence.model.episode import Episode
from seriesmarker.persistence.model.episode_extra import EpisodeExtra
from seriesmarker.persistence.model.genre import Genre
from seriesmarker.persistence.model.guest import Guest
from seriesmarker.persistence.model.role import Role
from seriesmarker.persistence.model.role_extra import RoleExtra
from seriesmarker.persistence.model.season import Season
from seriesmarker.persistence.model.series import Series
from seriesmarker.persistence.model.series_extra import SeriesExtra
from seriesmarker.persistence.model.writer import Writer
from seriesmarker.test.database.base.memory_db_test_case import \
    MemoryDBTestCase
from seriesmarker.test.util.example_data_factory import ExampleDataFactory
import random
import unittest

class DatabaseStoryTest(MemoryDBTestCase):

    def test_add_series(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")
        pytvdb_show.seasons = {}  # Ignoring Actors/Gueststars from Episodes
        series = SeriesFactory().new_series(pytvdb_show)

        db_add_series(series)

        added_series = self.db_session.query(Series).one()
        self.assertEqual(added_series.series_name, "How I Met Your Mother")

        db_actor_names = [actor.name for actor in self.db_session.query(Actor)]
        self.assertListEqual(sorted(db_actor_names), sorted(pytvdb_show.Actors), "Database doesn't contain correct actors")

        db_genre_names = [genre.name for genre in self.db_session.query(Genre)]
        self.assertListEqual(db_genre_names, pytvdb_show.Genre, "Database doesn't contain correct actors")

        self.assertRaises(EntityExistsException, db_add_series, series)

    def test_add_multiple_series(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")
        pytvdb_show.seasons = {}  # Ignoring Actors/Gueststars from Episodes
        series = SeriesFactory().new_series(pytvdb_show)

        db_add_series(series)

        pytvdb_show2 = ExampleDataFactory.new_pytvdb_show("BUFFY")
        series2 = SeriesFactory().new_series(pytvdb_show2)

        db_add_series(series2)

        self.assertEqual(self.db_session.query(Series).count(), 2, "Mismatched series count")
        self.assertEqual(self.db_session.query(Actor).count(), 12, "Mismatched actor count")  # one overlapping
        self.assertEqual(self.db_session.query(Genre).count(), 5, "Mismatched genre count")  # one overlapping


    def test_remove_series(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")
        pytvdb_show.seasons = {}  # Ignoring Actors/Gueststars from Episodes

        series = SeriesFactory().new_series(pytvdb_show)


        db_add_series(series)
        self.assertEqual(self.db_session.query(Series).one(), series, "Query result didn't return series")

        db_remove_series(series)
        self.assertFalse(self.db_session.query(Series).all(), "DB not empty")

        self.assertRaises(EntityNotFoundException, db_remove_series, series)  # check remove on empty DB

    def test_remove_series_cascading(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")
        pytvdb_show.seasons = {}  # Ignoring Actors/Gueststars from Episodes

        series = SeriesFactory().new_series(pytvdb_show)

        db_add_series(series)

        self.assertEqual(self.db_session.query(Actor).count(), 6, "Actors not propagated to DB")
        self.assertEqual(self.db_session.query(Genre).count(), 1, "Genre not propagated to DB")

        db_remove_series(series)

        self.assertEqual(self.db_session.query(Actor).count(), 0, "Actors weren't deleted from DB")
        self.assertEqual(self.db_session.query(Genre).count(), 0, "Genre weren't deleted from DB")

        self.db_session.query()

    def test_remove_multiple_series_cascading(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")
        pytvdb_show.seasons = {}  # Ignoring Actors/Gueststars from Episodes

        series = SeriesFactory().new_series(pytvdb_show)

        db_add_series(series)

        pytvdb_show2 = ExampleDataFactory.new_pytvdb_show("BUFFY")
        series2 = SeriesFactory().new_series(pytvdb_show2)

        db_add_series(series2)

        self.assertEqual(self.db_session.query(Series).count(), 2, "Mismatched series count")
        self.assertEqual(self.db_session.query(Actor).count(), 12, "Mismatched actor count")  # 11 unique
        self.assertEqual(self.db_session.query(Genre).count(), 5, "Mismatched genre count")  # 5 unique

        db_remove_series(series)

        self.assertEqual(self.db_session.query(Series).count(), 1, "Mismatched series count")
        self.assertEqual(self.db_session.query(Actor).count(), 6, "Mismatched actor count")
        self.assertEqual(self.db_session.query(Genre).count(), 4, "Mismatched actor count")

        db_remove_series(series2)

        self.assertEqual(self.db_session.query(Series).count(), 0, "Mismatched series count")
        self.assertEqual(self.db_session.query(Actor).count(), 0, "Mismatched actor count")
        self.assertEqual(self.db_session.query(Genre).count(), 0, "Mismatched actor count")



    def test_remove_season_with_series(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")
        series = SeriesFactory().new_series(pytvdb_show)

        db_add_series(series)

        self.assertEqual(self.db_session.query(Series).count(), 1, "Mismatched series count")
        self.assertEqual(self.db_session.query(Season).count(), 3, "Mismatched season count")

        db_remove_series(series)

        self.assertEqual(self.db_session.query(Series).count(), 0, "Series was not deleted")
        self.assertEqual(self.db_session.query(Season).count(), 0, "Seasons were not deleted")

    def test_remove_episodes_with_series(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")
        series = SeriesFactory().new_series(pytvdb_show)

        db_add_series(series)

        self.assertEqual(self.db_session.query(Series).count(), 1, "Mismatched series count")
        self.assertEqual(self.db_session.query(Episode).count(), 7, "Mismatched episode count")

        db_remove_series(series)

        self.assertEqual(self.db_session.query(Series).count(), 0, "Series was not deleted")
        self.assertEqual(self.db_session.query(Episode).count(), 0, "Episodes were not deleted")

    def test_remove_director_with_episodes(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")

        series = SeriesFactory().new_series(pytvdb_show)

        db_add_series(series)

        self.assertEqual(self.db_session.query(Episode).count(), 7, "Mismatched episode count")
        self.assertEqual(self.db_session.query(Director).count(), 5, "Mismatched director count")  # 1 unique

        db_remove_series(series)

        self.assertEqual(self.db_session.query(Director).count(), 0, "Director was not deleted")

    def test_remove_director_with_multiple_episodes(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")
        series = SeriesFactory().new_series(pytvdb_show)
        db_add_series(series)


        pytvdb_show2 = ExampleDataFactory.new_pytvdb_show("MADLOVE")
        series2 = SeriesFactory().new_series(pytvdb_show2)
        db_add_series(series2)

        self.assertEqual(self.db_session.query(Episode).count(), 9, "Mismatched episode count")
        self.assertEqual(self.db_session.query(Director).count(), 7, "Mismatched director count")  # 2 unique

        db_remove_series(series)

        self.assertEqual(self.db_session.query(Director).count(), 2, "Director count was incorrectly changed")

        db_remove_series(series2)

        self.assertEqual(self.db_session.query(Director).count(), 0, "Director was not deleted")

    def test_remove_writer_with_episodes(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")

        series = SeriesFactory().new_series(pytvdb_show)

        db_add_series(series)

        self.assertEqual(self.db_session.query(Episode).count(), 7, "Mismatched episode count")
        self.assertEqual(self.db_session.query(Writer).count(), 9, "Mismatched writer count")  # 2 unique

        db_remove_series(series)

        self.assertEqual(self.db_session.query(Writer).count(), 0, "Writer was not deleted")

    def test_remove_writer_with_multiple_episodes(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")
        series = SeriesFactory().new_series(pytvdb_show)
        db_add_series(series)


        pytvdb_show2 = ExampleDataFactory.new_pytvdb_show("MADLOVE")
        series2 = SeriesFactory().new_series(pytvdb_show2)
        db_add_series(series2)

        self.assertEqual(self.db_session.query(Episode).count(), 9, "Mismatched episode count")
        self.assertEqual(self.db_session.query(Writer).count(), 12, "Mismatched writer count")  # 5 unique

        db_remove_series(series)

        self.assertEqual(self.db_session.query(Writer).count(), 3, "Writer count was incorrectly changed")

        db_remove_series(series2)

        self.assertEqual(self.db_session.query(Writer).count(), 0, "Writer was not deleted")


    def test_remove_guest_stars_with_episodes(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")

        series = SeriesFactory().new_series(pytvdb_show)

        db_add_series(series)

        self.assertEqual(self.db_session.query(Episode).count(), 7, "Mismatched episode count")
        self.assertEqual(self.db_session.query(Guest).count(), 43, "Mismatched guest count")

        db_remove_series(series)

        self.assertEqual(self.db_session.query(Guest).count(), 0, "Guests were not deleted")

    def test_remove_guests_with_multiple_episodes(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")
        series = SeriesFactory().new_series(pytvdb_show)
        db_add_series(series)


        pytvdb_show2 = ExampleDataFactory.new_pytvdb_show("MADLOVE")
        series2 = SeriesFactory().new_series(pytvdb_show2)
        db_add_series(series2)

        self.assertEqual(self.db_session.query(Episode).count(), 9, "Mismatched episode count")
        self.assertEqual(self.db_session.query(Actor).count(), 11, "Mismatched Actor count")
        self.assertEqual(self.db_session.query(Guest).count(), 44, "Mismatched Guest count")

        db_remove_series(series)

        self.assertEqual(self.db_session.query(Episode).count(), 2, "Episode count was incorrectly changed")
        self.assertEqual(self.db_session.query(Actor).count(), 5, "Actor count was incorrectly changed")
        self.assertEqual(self.db_session.query(Guest).count(), 1, "Guest count was incorrectly changed")

        db_remove_series(series2)

        self.assertEqual(self.db_session.query(Episode).count(), 0, "Episode was not deleted")
        self.assertEqual(self.db_session.query(Actor).count(), 0, "Actor was not deleted")
        self.assertEqual(self.db_session.query(Guest).count(), 0, "Guest was not deleted")

    def test_remove_extra_information_with_episodes(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")

        series = SeriesFactory().new_series(pytvdb_show)

        db_add_series(series)

        self.assertEqual(self.db_session.query(Episode).count(), 7, "Mismatched episode count")
        self.assertEqual(self.db_session.query(EpisodeExtra).count(), 7, "ExtraInformation not correctly set up")

        db_remove_series(series)

        self.assertEqual(self.db_session.query(Episode).count(), 0, "Episode was not deleted")
        self.assertEqual(self.db_session.query(EpisodeExtra).count(), 0, "ExtraInformation were not deleted")

    def test_remove_extra_information_with_multiple_episodes(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")
        series = SeriesFactory().new_series(pytvdb_show)
        db_add_series(series)


        pytvdb_show2 = ExampleDataFactory.new_pytvdb_show("MADLOVE")
        series2 = SeriesFactory().new_series(pytvdb_show2)
        db_add_series(series2)

        self.assertEqual(self.db_session.query(Episode).count(), 9, "Mismatched episode count")
        self.assertEqual(self.db_session.query(EpisodeExtra).count(), 9, "ExtraInformation not correctly set up")
        db_remove_series(series)

        self.assertEqual(self.db_session.query(Episode).count(), 2, "Mismatched episode count")
        self.assertEqual(self.db_session.query(EpisodeExtra).count(), 2, "ExtraInformation were not deleted")
        db_remove_series(series2)

        self.assertEqual(self.db_session.query(Episode).count(), 0, "Episode was not deleted")
        self.assertEqual(self.db_session.query(EpisodeExtra).count(), 0, "ExtraInformation were not deleted")

    def test_remove_banner_with_series(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")
        pytvdb_show.seasons = {}  # ignore season banners

        series = SeriesFactory().new_series(pytvdb_show)

        db_add_series(series)

        self.assertEqual(self.db_session.query(Banner).count(), 1, "Mismatched banner count")
        self.assertEqual(self.db_session.query(BannerExtra).count(), 1, "Mismatched banner_extra count")

        db_remove_series(series)

        self.assertEqual(self.db_session.query(Banner).count(), 0, "Banner was not deleted")
        self.assertEqual(self.db_session.query(BannerExtra).count(), 0, "BannerExtra was not deleted")

    def test_remove_banner_with_seasons(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")

        series = SeriesFactory().new_series(pytvdb_show)

        db_add_series(series)

        self.assertEqual(self.db_session.query(Banner).count(), 3, "Mismatched banner count")
        self.assertEqual(self.db_session.query(BannerExtra).count(), 3, "Mismatched banner_extra count")

        db_remove_series(series)

        self.assertEqual(self.db_session.query(Banner).count(), 0, "Banner was not deleted")
        self.assertEqual(self.db_session.query(BannerExtra).count(), 0, "BannerExtra was not deleted")

    def test_remove_series_extra_with_series(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")

        series = SeriesFactory().new_series(pytvdb_show)

        db_add_series(series)

        self.assertEqual(self.db_session.query(Series).count(), 1, "Mismatched Series count")
        self.assertEqual(self.db_session.query(SeriesExtra).count(), 1, "Mismatched SeriesExtra count")

        db_remove_series(series)

        self.assertEqual(self.db_session.query(Series).count(), 0, "Series was not deleted")
        self.assertEqual(self.db_session.query(SeriesExtra).count(), 0, "SeriesExtra was not deleted")

    def test_remove_role_with_series(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("HIMYM")

        series = SeriesFactory().new_series(pytvdb_show)

        db_add_series(series)

        self.assertEqual(self.db_session.query(Role).count(), 2, "Mismatched Role count")
        self.assertEqual(self.db_session.query(RoleExtra).count(), 2, "Mismatched RoleExtra count")

        db_remove_series(series)

        self.assertEqual(self.db_session.query(Role).count(), 0, "Role was not deleted")
        self.assertEqual(self.db_session.query(RoleExtra).count(), 0, "RoleExtra was not deleted")

    def test_update_series(self):
        pytvdb_show = ExampleDataFactory.new_pytvdb_show("MADLOVE")
        pytvdb_show_updated = ExampleDataFactory.new_pytvdb_show("MADLOVE-UPDATE")

        series = SeriesFactory().new_series(pytvdb_show)

        series.seasons[0].episodes[0].extra.watched = True

        db_add_series(series)

        SeriesFactory().new_series(pytvdb_show_updated, series)

        db_commit()


        # ##Episode Test
        episode = self.db_session.query(Episode).filter_by(id=pytvdb_show[1][1].id).one()

        self.assertEqual(self.db_session.query(Episode).count(), 3, "Episode number does not match after update")

        self.assertEqual(episode.id, pytvdb_show[1][1].id, "Simple episode attribute (ID) should not have changed")
        self.assertEqual(episode.episode_name, pytvdb_show_updated[1][1].EpisodeName, "Simple episode attribute (EpisodeName) was not updated")


        self.assertEqual(sorted([director.name for director in episode.directors]), sorted(pytvdb_show_updated[1][1].Director), "List attribute (Actors) does not match after update")
        self.assertEqual(sorted([guest.name for guest in episode.guests]), sorted(pytvdb_show_updated[1][1].GuestStars), "List attribute (GuestStars) does not match after update")
        self.assertEqual(sorted([writer.name for writer in episode.writers]), sorted(pytvdb_show_updated[1][1].Writer), "List attribute (Writer) does not match after update")

        self.assertEqual(self.db_session.query(Director).count(), 4, "List attribute (Director) update did not change database correctly")
        self.assertEqual(self.db_session.query(Writer).count(), 4, "List attribute (Writer) update did not change database correctly")
        self.assertEqual(self.db_session.query(Guest).count(), 4, "List attribute (Guest) update did not change database correctly")
        # ##

        # ## EpisodeExtra Test
        self.assertTrue(episode.extra.watched, "Update did not recognize a former watched episode")
        # ##

        # ## Season Test
        db_seasons = self.db_session.query(Season).all()

        self.assertEqual(len(db_seasons), 2, "Update did not change seasons correctly")
        self.assertEqual(sorted([season.season_number for season in db_seasons]), sorted(pytvdb_show_updated.seasons.keys()), "Seasons do not match after update")
        # ##

        # ## SeasonBanner Test
        db_banners = self.db_session.query(Banner).all()

        self.assertEqual(len(db_banners), 3, "Update did not change season banner correctly")
        self.assertEqual(sorted([banner.id for banner in db_banners]), sorted([banner.id for banner in pytvdb_show_updated.banner_objects]), "Banners do not match after update")

        season1_banner = self.db_session.query(Banner).filter_by(id=796361).one()
        pytvdb_update_banner = [banner for banner in pytvdb_show_updated.banner_objects if banner.id == 796361][0]

        self.assertEqual(season1_banner.rating, pytvdb_update_banner.Rating, "Simple banner attribute (Rating) did not change")
        self.assertEqual(season1_banner.banner_path, pytvdb_update_banner.BannerPath, "Simple banner attribute (BannerPath) did not change")
        # ##

        # ##SeasonBannerExtra Test
        self.assertEqual(self.db_session.query(BannerExtra).count(), 3, "Update did not change season BannerExtra correctly")
        self.assertEqual(season1_banner.extra.banner_url, pytvdb_update_banner.banner_url, "Simple banner attribute (BannerURL) did not change")
        # ##

        # ##Series Test
        db_series = self.db_session.query(Series).one()

        self.assertEqual(db_series.id, pytvdb_show.id, "Simple series attribute (ID) should not have changed")
        self.assertEqual(db_series.airs_day_of_week, pytvdb_show_updated.Airs_DayOfWeek, "Simple attribute (AirsDayOfWeek) was not updated")

        self.assertEqual(self.db_session.query(Genre).count(), 2, "Genre count did not match")
        self.assertEqual(sorted([genre.name for genre in db_series.genre]), sorted(pytvdb_show_updated.Genre), "List attribute (Genre) update did not change database correctly");


        db_actor_names = sorted([actor.name for actor in self.db_session.query(Actor).all()])
        update_actor_names = sorted(pytvdb_show_updated.Actors)
        self.assertEqual(db_actor_names, update_actor_names, "Actors do not match")

        self.assertEqual(self.db_session.query(Actor).count(), 6, "List attribute (Actor) update did not change database correctly")
        # ##

        # ##SeriesExtra Test
        pytvdb_update_banner = [banner for banner in pytvdb_show_updated.banner_objects if banner.id == 78630101][0]

        self.assertEqual(db_series.extra.banner.id, pytvdb_update_banner.id, "Simple banner attribute (ID) did not change")
        self.assertEqual(db_series.extra.banner.extra.banner_url, pytvdb_update_banner.banner_url, "Simple banner attribute (BannerURL) did not change")
        # ##

        # ##Role Test
        db_roles = self.db_session.query(Role).all()

        self.assertEqual(len(db_roles), 3, "Update did not change series roles correctly")
        self.assertEqual(sorted([role.id for role in db_roles]), sorted([role.id for role in pytvdb_show_updated.actor_objects]), "Roles do not match after update")

        role = self.db_session.query(Role).filter_by(id=226641).one()
        pytvdb_update_role = [role for role in pytvdb_show_updated.actor_objects if role.id == 226641][0]

        self.assertEqual(role.role, pytvdb_update_role.Role, "Simple role attribute (Role) did not change")
        self.assertEqual(role.name, pytvdb_update_role.Name, "Simple role attribute (Name) did not change")
        self.assertEqual(role.sort_order, pytvdb_update_role.SortOrder, "Simple role attribute (SortOrder) did not change")
        self.assertEqual(role.image, pytvdb_update_role.Image, "Simple role attribute (Image) did not change")
        # ##

        # ##RoleExtra Test
        self.assertEqual(self.db_session.query(RoleExtra).count(), 3, "Update did not change season RoleExtra correctly")
        self.assertEqual(role.extra.image_url, pytvdb_update_role.image_url, "Simple banner attribute (RoleURL) did not change")
        # ##

    def test_sort_on_load(self):
        """Test ensures an alphanumeric order of series when loading
        from data base."""

        series = ["HIMYM", "DRWHO", "BUFFY", "MADLOVE", "ROMEPG",
                  "WONDERYEARS", "DEFIANCE"]
        random.shuffle(series)

        for series_name in series:
            db_add_series(SeriesFactory().new_series(
                ExampleDataFactory.new_pytvdb_show(series_name)))

        self.assertEqual(
            [series.series_name for series in db_get_series()],
            [
                "Buffy the Vampire Slayer",
                "Defiance",
                "Doctor Who",
                "How I Met Your Mother",
                "Mad Love",
                "Rome: Power & Glory",
                "The Wonder Years"
            ],
            "Series not sorted correctly after loading from data base"
        )

def get_suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DatabaseStoryTest))
    return suite

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
