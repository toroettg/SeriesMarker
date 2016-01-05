# ==============================================================================
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

from pytvdbapi.api import Season
from pytvdbapi.banner import Banner

from seriesmarker.test.util.examples.base_example import BaseExample


class HowIMetYourMotherExample(BaseExample):
    """Standard example for various test cases.

    .. seealso::
        :py:func:`.test_04_update`
    """

    @classmethod
    def series_attributes(cls):
        attributes = {
            'Actors': ['Josh Radnor', 'Cobie Smulders', 'Neil Patrick Harris',
                       'Jason Segel', 'Alyson Hannigan', 'Bob Saget'],
            'Airs_DayOfWeek': 'Monday',
            'Airs_Time': '8.00 PM',
            'ContentRating': 'TV-PG',
            'FirstAired': date(2005, 9, 19),
            'Genre': ['Comedy'],
            'IMDB_ID': 'tt0460649',
            'Language': 'en',
            'Network': 'CBS',
            'NetworkID': '',
            'Overview': "How I Met Your Mother is a comedy about Ted and how he fell in love. It all started when Ted's best friend, Marshall, dropped the bombshell that he was going to propose to his longtime girlfriend, Lily, a kindergarten teacher. At that moment, Ted realized that he had better get a move on if he, too, hopes to find true love. Helping him in his quest is his friend Barney, a confirmed bachelor with endless, sometimes outrageous opinions, a penchant for suits and a foolproof way to meet women. When Ted meets Robin, he's sure it's love at first sight, but destiny has something else in store.",
            'Rating': 9.2,
            'RatingCount': 393,
            'Runtime': 30,
            'SeriesID': 33700,
            'SeriesName': 'How I Met Your Mother',
            'Status': 'Continuing',
            'added': '',
            'addedBy': '',
            'banner': 'graphical/75760-g25.jpg',
            'fanart': 'fanart/original/75760-41.jpg',
            'id': 75760,
            'lastupdated': 1337529497,
            'poster': 'posters/75760-12.jpg',
            'zap2it_id': 'EP00753796'
        }

        return attributes

    @classmethod
    def seasons(cls, show):
        season0 = Season(0, show)
        season1 = Season(1, show)
        season2 = Season(2, show)

        attributes = {
            'Combined_episodenumber': 1,
            'Combined_season': 0,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': '',
            'EpImgFlag': 1,
            'EpisodeName': 'Robin Sparkles Music Video - Let\'s Go to the Mall',
            'EpisodeNumber': 1,
            'FirstAired': date(2006, 11, 20),
            'GuestStars': '',
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': 'Dummy Overview, ToolTip test',
            'ProductionCode': '',
            'Rating': 4.0,
            'RatingCount': 1,
            'SeasonNumber': 0,
            'Writer': '',
            'absolute_number': '',
            'airsafter_season': '',
            'airsbefore_episode': 10,
            'airsbefore_season': 2,
            'filename': 'episodes/75760/1159571.jpg',
            'id': 1159571,
            'lastupdated': 1275339740,
            'seasonid': 23219,
            'seriesid': 75760,
        }

        episode01 = cls.create_episode(attributes, season0)

        attributes = {
            'Combined_episodenumber': 2,
            'Combined_season': 0,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': '',
            'EpImgFlag': 1,
            'EpisodeName': 'Robin Sparkles Music Video - Sandcastles In the Sand',
            'EpisodeNumber': 2,
            'FirstAired': date(2008, 4, 21),
            'GuestStars': '',
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': 'Music video to go with Episode 03x16 - Sandcastles In the Sand. Full video was originally posted on YouTube: http://www.youtube.com/watch?v=bgBMFwVeIGI',
            'ProductionCode': '',
            'Rating': '',
            'RatingCount': 0,
            'SeasonNumber': 0,
            'Writer': '',
            'absolute_number': '',
            'airsafter_season': '',
            'airsbefore_episode': 17,
            'airsbefore_season': 3,
            'filename': 'episodes/75760/414248.jpg',
            'id': 414248,
            'lastupdated': 1258155936,
            'seasonid': 23219,
            'seriesid': 75760
        }

        episode02 = cls.create_episode(attributes, season0)

        attributes = {
            'Combined_episodenumber': 1.0,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': 1.0,
            'DVD_season': 1,
            'Director': 'Pamela Fryman',
            'EpImgFlag': 2,
            'EpisodeName': 'Pilot',
            'EpisodeNumber': 1,
            'FirstAired': date(2005, 9, 19),
            'GuestStars': ['Jack Shearer', 'Gary Riotto', 'Monique Edwards',
                           'Saba Homayoon', 'Sarah Loew', 'Marshall Manesh',
                           'Tony Rossi'],
            'IMDB_ID': 'tt0606110',
            'Language': 'en',
            'Overview': "When Ted's best friend Marshall proposes to his girlfriend, Lily, Ted realizes he'd better get a move on if he hopes to find true love. Ted soon meets Robin in a neighborhood bar, immediately becomes smitten and scores a first date. But when Ted can hardly wait to see her again, his eagerness threatens to scare her away.",
            'ProductionCode': '1ALH79',
            'Rating': 7.7,
            'RatingCount': 189,
            'SeasonNumber': 1,
            'Writer': ['Carter Bays', 'Craig Thomas'],
            'absolute_number': 1,
            'filename': 'episodes/75760/177831.jpg',
            'id': 177831,
            'lastupdated': 1313341093,
            'seasonid': 9285,
            'seriesid': 75760
        }

        episode11 = cls.create_episode(attributes, season1)

        attributes = {
            'Combined_episodenumber': 2.0,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': 2.0,
            'DVD_season': 1,
            'Director': 'Pamela Fryman',
            'EpImgFlag': 2,
            'EpisodeName': 'Purple Giraffe',
            'EpisodeNumber': 2,
            'FirstAired': date(2005, 9, 26),
            'GuestStars': ['Anna Zielinski', 'Pedro Miguel Arce', 'Jae Head',
                           'Jon Bernthal', 'Beth Riesgraf',
                           'Lindsay Schoneweis', 'Jay Head', 'Sean Lucore',
                           'Alyshia Ochse'],
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': b"In a desperate attempt for a second date, Ted invites Robin to a party he is throwing. However, she doesn't show up and he keeps throwing parties in the hopes she will finally arrive.",
            'ProductionCode': '1ALH01',
            'Rating': 7.3,
            'RatingCount': 162,
            'SeasonNumber': 1,
            'Writer': ['Craig Thomas', 'Carter Bays'],
            'absolute_number': 2,
            'filename': 'episodes/75760/300336.jpg',
            'id': 300336,
            'lastupdated': 1313341211,
            'seasonid': 9285,
            'seriesid': 75760,
        }

        episode12 = cls.create_episode(attributes, season1)

        attributes = {
            'Combined_episodenumber': 3.0,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': 3.0,
            'DVD_season': 1,
            'Director': 'Pamela Fryman',
            'EpImgFlag': 7,
            'EpisodeName': 'Sweet Taste of Liberty',
            'EpisodeNumber': 3,
            'FirstAired': date(2005, 10, 3),
            'GuestStars': ['Anna Zielinski', 'Floyd Vanbuskirk',
                           'Pedro Miguel Arce', 'Carla Toutz', 'Robb Derringer',
                           'Mark Edward Smith', 'Earl Billings', 'Gita Isak',
                           'Sean Lucore', 'Dustin Lancaster', 'Chuck Carter',
                           'Alyshia Ochse', 'Tiffany Brouwer'],
            'IMDB_ID': 'tt0606117',
            'Language': 'en',
            'Overview': 'Ted agrees to let Barney spice up his love life, and ends up on a crazy adventure of flying to Philadelphia, encountering the law and visiting the Liberty Bell.',
            'ProductionCode': '1ALH02',
            'Rating': 7.6,
            'RatingCount': 169,
            'SeasonNumber': 1,
            'Writer': ['Chris Miller', 'Phil Lord'],
            'absolute_number': 3,
            'filename': 'episodes/75760/300337.jpg',
            'id': 300337,
            'lastupdated': 1362319851,
            # 'season' : ignored
            'seasonid': 9285,
            'seriesid': 75760,
            'thumb_added': '',
            'thumb_height': '',
            'thumb_width': '',
            'tms_export': '',
        }

        episode13 = cls.create_episode(attributes, season1)

        attributes = {
            'Combined_episodenumber': 4.0,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': 4.0,
            'DVD_season': 1,
            'Director': 'Pamela Fryman',
            'EpImgFlag': 7,
            'EpisodeName': 'Return of the Shirt',
            'EpisodeNumber': 4,
            'FirstAired': date(2005, 10, 10),
            'GuestStars': ['John Henry Canavan', 'Choice Skinner',
                           'Charlene Amoia', 'Buck Kartalian', 'Katelin Chesna',
                           'Monique Edwards', 'Anne Dudek', 'Michael Kagan',
                           'Jackie Geary', 'Ange Billman'],
            'IMDB_ID': 'tt0606112',
            'Language': 'en',
            'Overview': "Ted's outlook on his continuing search for love is altered when he rediscovers a shirt that has not seen daylight in years. Meanwhile, Barney amuses himself by coaxing Robin into sacrificing her job by saying completely outlandish things on air live for a cash reward.",
            'ProductionCode': '1ALH03',
            'Rating': 7.5,
            'RatingCount': 170,
            'SeasonNumber': 1,
            'Writer': 'Kourtney Kang',
            'absolute_number': 4,
            'filename': 'episodes/75760/300338.jpg',
            'id': 300338,
            'lastupdated': 1362319935,
            # 'season' : ignored
            'seasonid': 9285,
            'seriesid': 75760,
            'thumb_added': '',
            'thumb_height': '',
            'thumb_width': '',
            'tms_export': '',
        }

        episode14 = cls.create_episode(attributes, season1)

        attributes = {
            'Combined_episodenumber': 1,
            'Combined_season': 3,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': 'Pamela Fryman',
            'EpImgFlag': '',
            'EpisodeName': 'Wait For It...',
            'EpisodeNumber': 1,
            'FirstAired': date(2007, 9, 24),
            'GuestStars': ['Enrique Iglesias', 'Mandy Moore', 'Amanda Loncar',
                           'Frank Alvarez'],
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': "Robin shows up with a date and this motivates Ted to 'get back out there'. We also learn something major about 'the Mother'.",
            'ProductionCode': '3ALH01',
            'Rating': 7.7,
            'RatingCount': 161,
            'SeasonNumber': 3,
            'Writer': ['Carter Bays', 'Craig Thomas'],
            'absolute_number': 45,
            'filename': 'episodes/75760/336246.jpg',
            'id': 336246,
            'lastupdated': 1318195975,
            # 'season' : ignored
            'seasonid': 28494,
            'seriesid': 75760,
            'thumb_added': '',
            'thumb_height': '',
            'thumb_width': '',
            'tms_export': '',
        }

        episode21 = cls.create_episode(attributes, season2)

        season0.episodes = {1: episode01, 2: episode02}
        season1.episodes = {1: episode11, 2: episode12, 3: episode13,
                            4: episode14}
        season2.episodes = {1: episode21}

        return {0: season0, 1: season1, 2: season2}

    @classmethod
    def seasons_update(cls, show):
        update_season = Season(1, show)
        seasons = HowIMetYourMotherExample.seasons(show)

        episode12 = seasons[1][2]
        episode12.season = update_season

        update_season.episodes = {2: episode12}

        return {1: update_season}

    @classmethod
    def banners(cls, show):
        mirror = "http://thetvdb.com"

        attributes = {
            'BannerPath': 'graphical/75760-g27.jpg',
            'BannerType': 'series',
            'BannerType2': 'graphical',
            'Language': 'en',
            'Rating': 10.0,
            'RatingCount': 2,
            'banner_url': 'http://thetvdb.com/banners/graphical/75760-g27.jpg',
            'id': 886577
        }

        banner1 = Banner(mirror=mirror, data=attributes, show=show)

        attributes = {
            'BannerPath': 'posters/75760-1.jpg',
            'BannerType': 'poster',
            'BannerType2': '680x1000',
            'Language': 'en',
            'Rating': 7.125,
            'RatingCount': 17,
            'banner_url': 'http://thetvdb.com/banners/posters/75760-1.jpg',
            'id': 25523
        }

        banner2 = Banner(mirror=mirror, data=attributes, show=show)

        attributes = {
            'BannerPath': 'seasons/75760-0-3.jpg',
            'BannerType': 'season',
            'BannerType2': 'season',
            'Language': 'de',
            'Rating': '',
            'RatingCount': 0,
            'Season': 0,
            'banner_url': 'http://thetvdb.com/banners/seasons/75760-0-3.jpg',
            'id': 875597
        }

        banner3 = Banner(mirror=mirror, data=attributes, show=show)

        attributes = {
            'BannerPath': 'seasonswide/75760-1-2.jpg',
            'BannerType': 'season',
            'BannerType2': 'seasonwide',
            'Language': 'es',
            'Rating': '',
            'RatingCount': 0,
            'Season': 1,
            'banner_url': 'http://thetvdb.com/banners/seasonswide/75760-1-2.jpg',
            'id': 934196,
        }

        banner4 = Banner(mirror=mirror, data=attributes, show=show)

        return [banner1, banner2, banner3, banner4]

    @classmethod
    def roles(cls, show):
        attributes = {
            'Image': 'actors/41068.jpg',
            'Name': 'Josh Radnor',
            'Role': 'Ted Mosby',
            'SortOrder': 0,
            'id': 41068,
            'image_url': 'http://thetvdb.com/banners/actors/41068.jpg'
        }

        actor1 = cls.create_actor(attributes, show)

        attributes = {
            'Image': 'actors/41067.jpg',
            'Name': 'Jason Segel',
            'Role': 'Marshall Eriksen',
            'SortOrder': 2,
            'id': 41067,
            'image_url': 'http://thetvdb.com/banners/actors/41067.jpg',
        }

        actor2 = cls.create_actor(attributes, show)

        return [actor1, actor2]
