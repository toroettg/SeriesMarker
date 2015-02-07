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

from datetime import date

from pytvdbapi.api import Season

from seriesmarker.test.util.examples.base_example import BaseExample


class DefianceExample(BaseExample):
    """Testdata covers update where episode IDs are changed.

    Original season data is ordered as [A, B, C].
    Update inserts D, which causes a shift to [A, D, B', C'].
    D = B but has a new id, B' has id of B but contains data of C (B' = C).
    Furthermore, C' is added and has id of C but contains a new episode

    """

    @classmethod
    def series_attributes(cls):
        attributes = {
            'Actors': ['Mia Kirshner', 'Stephanie Leonidas', 'Grant Bowler',
                       'Tony Curran', 'Jaime Murray', 'Graham Greene',
                       'Julie Benz'],
            'Airs_DayOfWeek': 'Monday',
            'Airs_Time': '9:00 PM',
            'ContentRating': 'TV-14',
            'FirstAired': date(2013, 4, 15),
            'Genre': ['Action', 'Drama', 'Science-Fiction'],
            'IMDB_ID': 'tt2189221',
            'Language': 'en',
            'Network': 'Syfy',
            'NetworkID': '',
            'Overview': b'Set on a future Earth, Defiance introduces players and viewers to a world where humans and aliens live together on a planet ravaged by decades of war and transformed by alien terra-forming machines. It centers on Jeb Nolan, the law-keeper in a bustling frontier boomtown that is one of the new world\\u2019s few oasis of civility and inclusion. Nolan is a former Marine who fought in the alien conflict and suffered the loss of his wife and child in the war. The trauma transformed him into a lone wanderer in the wilds of this new and dangerous world.',
            'Rating': 8.0,
            'RatingCount': 12,
            'Runtime': 60,
            'SeriesID': 173737,
            'SeriesName': 'Defiance',
            'Status': 'Continuing',
            'added': '2012-01-18 14:37:12',
            'addedBy': 357106,
            'banner': 'graphical/255326-g4.jpg',
            'fanart': 'fanart/original/255326-2.jpg',
            'id': 255326,
            'lastupdated': 1367074085,
            'poster': 'posters/255326-3.jpg',
            # 'seasons' : TODO
            'zap2it_id': 'EP01562200',
        }
        return attributes

    @classmethod
    def seasons(cls, show):
        season1 = Season(1, show)

        attributes = {
            'Combined_episodenumber': 1,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': 'Scott Stewart',
            'EpImgFlag': 2,
            'EpisodeName': 'Pilot',
            'EpisodeNumber': 1,
            'FirstAired': date(2013, 4, 15),
            'GuestStars': 'Robert Clarke',
            'IMDB_ID': 'tt2297333',
            'Language': 'en',
            'Overview': b'The arrival of the mysterious Nolan and his charge Irisa to the town of Defiance marks a threat to the fragile peace that exists between the residents in the premiere of this futuristic drama, which is set in the year 2046, more than 30 years following a war between humans and aliens that left Earth forever changed.',
            'ProductionCode': '',
            'Rating': 7.7,
            'RatingCount': 66,
            'SeasonNumber': 1,
            'Writer': ["Rockne S. O'Bannon", 'Kevin Murphy', 'Michael Taylor'],
            'absolute_number': '',
            'filename': 'episodes/255326/4325883.jpg',
            'id': 4325883,
            'lastupdated': 1366837702,
            'seasonid': 492238,
            'seriesid': 255326,
        }
        episode11 = cls.create_episode(attributes, season1)

        attributes = {
            'Combined_episodenumber': 2,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': 'Michael Nankin',
            'EpImgFlag': 2,
            'EpisodeName': 'Down in the Ground Where the Dead Men Go',
            'EpisodeNumber': 2,
            'FirstAired': date(2013, 4, 22),
            'GuestStars': ['Robert Clarke', 'Nicole Munoz', 'Justin Rain',
                           'Jesse Rath'],
            'IMDB_ID': 'tt2361364',
            'Language': 'en',
            'Overview': b'Nolan and Datak clash over an ancient ritual, while the hunt for a killer is on.',
            'ProductionCode': '',
            'Rating': 7.6,
            'RatingCount': 36,
            'SeasonNumber': 1,
            'Writer': ['Kevin Murphy', 'Anupam Nigam'],
            'absolute_number': '',
            'filename': 'episodes/255326/4548788.jpg',
            'id': 4448857,
            'lastupdated': 1365539059,
            'seasonid': 492238,
            'seriesid': 255326,
        }
        episode12 = cls.create_episode(attributes, season1)

        attributes = {
            'Combined_episodenumber': 3,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': '',
            'EpImgFlag': 2,
            'EpisodeName': 'A Well Respected Man',
            'EpisodeNumber': 3,
            'FirstAired': date(2013, 4, 29),
            'GuestStars': '',
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': b'',
            'ProductionCode': '',
            'Rating': '',
            'RatingCount': 0,
            'SeasonNumber': 1,
            'Writer': '',
            'absolute_number': '',
            'filename': 'episodes/255326/4448857.jpg',
            'id': 4448858,
            'lastupdated': 1365539070,
            'seasonid': 492238,
            'seriesid': 255326,
        }
        episode13 = cls.create_episode(attributes, season1)

        season1.episodes = {1: episode11, 2: episode12, 3: episode13}

        return {1: season1}

    @classmethod
    def seasons_update(cls, show):
        update_season = Season(1, show)

        seasons = DefianceExample.seasons(show)

        episode11 = seasons[1][1]
        episode11.season = update_season

        episode12 = seasons[1][2]
        episode12.season = update_season
        episode12.id = 4548788
        episode12.lastupdated = 1366868300

        episode13 = seasons[1][3]
        episode13.season = update_season
        episode13.id = 4448857
        episode13.lastupdated = 1366918097

        attributes = {
            'Combined_episodenumber': 4,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': '',
            'EpImgFlag': '',
            'EpisodeName': 'The Devil in the Dark',
            'EpisodeNumber': 4,
            'FirstAired': date(2013, 5, 6),
            'GuestStars': '',
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': b'',
            'ProductionCode': '',
            'Rating': '',
            'RatingCount': 0,
            'SeasonNumber': 1,
            'Writer': '',
            'absolute_number': '',
            'filename': '',
            'id': 4448858,
            'lastupdated': 1366800217,
            'seasonid': 492238,
            'seriesid': 255326,
        }
        episode14 = cls.create_episode(attributes, update_season)

        update_season.episodes = {1: episode11, 2: episode12, 3: episode13,
                                  4: episode14}

        return {1: update_season}

