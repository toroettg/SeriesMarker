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

from datetime import date

from pytvdbapi.actor import Actor
from pytvdbapi.api import Season, Episode

from seriesmarker.test.util.examples.base_example import BaseExample


class WonderYearsExample(BaseExample):
    """Testdata covers handling of roles where an actor has multiple roles.

    .. seealso:: :py:func:`.test_multiple_role_of_actor`
    """
    @classmethod
    def series_attributes(cls):
        attributes = {
            'Actors': ['Fred Savage', 'Danica McKellar', 'Josh Saviano', 'Dan Lauria', 'Jason Hervey', 'Alley Mills', "Olivia d'Abo", 'Daniel Stern'],
            'Airs_DayOfWeek': '',
            'Airs_Time': '',
            'ContentRating': 'TV-PG',
            'FirstAired': date(1988, 1, 31),
            'Genre': ['Comedy'],
            'IMDB_ID': 'tt0094582',
            'Language': 'en',
            'Network': 'ABC',
            'NetworkID': '',
            'Overview': b'The Wonder Years tells the story of Kevin Arnold (Fred Savage) facing the trials and tribulations of youth while growing up during the 1960s. Told through narration from an adult Kevin (Daniel Stern), Kevin faces the difficulties of mantaining relationships and friendships on his enthralling journey into adulthood.',
            'Rating': 8.4,
            'RatingCount': 12,
            'Runtime': 30,
            'SeriesID': 208,
            'SeriesName': 'The Wonder Years',
            'Status': 'Ended',
            'added': '',
            'addedBy': '',
            'banner': 'graphical/72888-g.jpg',
            'fanart': 'fanart/original/72888-3.jpg',
            'id': 72888,
            'lastupdated': 1372098651,
            'poster': 'posters/72888-1.jpg',
            'zap2it_id': 'SH019091',
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
            'Director': ['Steve Miner'],
            'EpImgFlag': 1,
            'EpisodeName': 'Pilot',
            'EpisodeNumber': 1,
            'FirstAired': date(1988, 1, 31),
            'GuestStars': ['Sean Faro', 'Bentley Mitchum', 'Don Jeffcoat', 'Jacqueline Square', 'Dah-ve Chodan'],
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': 'Kevin and Paul attend Robert F Kennedy Junior High for the first time. Winnie\'s brother is killed in Vietnam. Kevin and Winnie kiss for the first time.',
            'ProductionCode': 'B88003',
            'Rating': 8.6,
            'RatingCount': 7,
            'SeasonNumber': 1,
            'Writer': ['Neal Marlens', 'Carol Black'],
            'absolute_number': '',
            'filename': 'episodes/72888/102650.jpg',
            'id': 102650,
            'lastupdated': 1347794625,
           # 'season' : ignored
            'seasonid': 4959,
            'seriesid': 72888,
        }
        episode11 = cls.create_episode(attributes, season1)

        season1.episodes = {1: episode11}

        return {1: season1}

    @classmethod
    def roles(cls, show):
        attributes = {
            'Image': '',
            'Name': 'Daniel Stern',
            'Role': ['Narrator', 'Adult Kevin'],
            'SortOrder': 3,
            'id': 21028,
            'image_url': 'http://thetvdb.com/banners/',
        }

        actor1 = cls.create_actor(attributes, show)

        return [actor1]
