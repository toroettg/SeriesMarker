#==============================================================================
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
#==============================================================================

from datetime import date

from pytvdbapi.api import Season

from seriesmarker.test.util.examples.base_example import BaseExample


class BuffyExample(BaseExample):
    @classmethod
    def series_attributes(cls):
        attributes = {
            'Actors': ['Sarah Michelle Gellar', 'Alyson Hannigan',
                       'Emma Caulfield', 'Michelle Trachtenberg',
                       'Anthony Head', 'James Marsters'],
            'Airs_DayOfWeek': '',
            'Airs_Time': '',
            'ContentRating': 'TV-PG',
            'FirstAired': date(1997, 3, 10),
            'Genre': ['Action and Adventure', 'Comedy', 'Drama', 'Fantasy'],
            'IMDB_ID': 'tt0118276',
            'Language': 'en',
            'Network': 'The WB',
            'NetworkID': '',
            'Overview': "In every generation there is a Chosen One. She alone will stand against the vampires, the demons and the forces of darkness. She is the Slayer. Sarah Michelle Gellar stars as Buffy Summers, The Chosen One, the one girl in all the world with the strength and skill to fight the vampires. With the help of her close friends, Willow (Alyson Hannigan ), Xander (Nicholas Brendon), and her Watcher Giles (Anthony Stewart Head) she balances slaying, family, friendships, and relationships.",
            'Rating': 9.0,
            'RatingCount': 104,
            'Runtime': 60,
            'SeriesID': 10,
            'SeriesName': 'Buffy the Vampire Slayer',
            'Status': 'Ended',
            'added': '',
            'addedBy': '',
            'banner': 'graphical/70327-g23.jpg',
            'fanart': 'fanart/original/70327-3.jpg',
            'id': 70327,
            'lastupdated': 1338772285,
            'poster': 'posters/70327-10.jpg',
            # 'seasons': TODO
            'zap2it_id': 'EP00213110'
        }
        return attributes

    @classmethod
    def seasons(cls, show):
        season1 = Season(1, show)

        attributes = {
            'Combined_episodenumber': 1.0,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': 1.0,
            'DVD_season': 1,
            'Director': 'Charles Martin Smith',
            'EpImgFlag': '',
            'EpisodeName': 'Welcome to the Hellmouth (1)',
            'EpisodeNumber': 1,
            'FirstAired': date(1997, 3, 10),
            'GuestStars': ['Persia White', 'Tupelo Jereme', 'Natalie Strauss',
                           'Brian Thompson', 'Ken Lerner', 'J. Patrick Lawlor',
                           'Eric Balfour', 'Deborah Brown',
                           'Carmine Giovinazzo', 'Amy Faith Chance',
                           'Julie Benz', 'Marc Metcalf', 'Kristine Sutherland',
                           'David Boreanaz'],
            'IMDB_ID': 'tt0452716',
            'Language': 'en',
            'Overview': 'Determined to have a fresh start, Buffy Summers moves to Sunnydale only to find out that it\'s located on a Hellmouth and that her slaying duties have just begun.',
            'ProductionCode': '4V01',
            'Rating': 7.6,
            'RatingCount': 33,
            'SeasonNumber': 1,
            'Writer': 'Joss Whedon',
            'absolute_number': 1,
            'filename': 'episodes/70327/2.jpg',
            'id': 2,
            'lastupdated': 1364127226,
            #'season' : ignored
            'seasonid': 10,
            'seriesid': 70327,
        }
        episode11 = cls.create_episode(attributes, season1)

        season1.episodes = {1: episode11}

        return {1: season1}
