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

from datetime import date
from pytvdbapi.actor import Actor
from pytvdbapi.api import Show, Season, Episode
from pytvdbapi.banner import Banner
from seriesmarker.test.util.examples.defiance_example import DefianceExample
from seriesmarker.test.util.examples.wonder_years_example import \
    WonderYearsExample
from seriesmarker.test.util.examples.how_i_met_your_mother_example import HowIMetYourMotherExample

class ExampleDataFactory(object):
    """Creates static data for testing, similar to data pytvdb would return."""
    @staticmethod
    def new_pytvdb_show(name):
        if name == "BUFFY":
            attributes = ExampleDataFactory.buffy_attributes()
            seasons = {}
            banners = []
            roles = []
        elif name == "HIMYM":
            return HowIMetYourMotherExample.show()
        elif name == "HIMYM-UPDATE":
            return HowIMetYourMotherExample.show_update()
        elif name == "ROMEPG":
            attributes = ExampleDataFactory.rome_power_and_glory_attributes()
            seasons = ExampleDataFactory.rome_power_and_glory_seasons()
            banners = []
            roles = []
        elif name == "MADLOVE":
            attributes = ExampleDataFactory.mad_love_attributes()
            seasons = ExampleDataFactory.mad_love_seasons()
            banners = ExampleDataFactory.mad_love_banner()
            roles = ExampleDataFactory.mad_love_roles()
        elif name == "MADLOVE-UPDATE":
            attributes = ExampleDataFactory.mad_love_update_attributes()
            seasons = ExampleDataFactory.mad_love_update_seasons()
            banners = ExampleDataFactory.mad_love_update_banner()
            roles = ExampleDataFactory.mad_love_update_roles()
        elif name == "DEFIANCE":
            return DefianceExample.show()
        elif name == "DEFIANCE-UPDATE":
            return DefianceExample.show_update()
        elif name == "WONDERYEARS":
            return WonderYearsExample.show()

        show = Show(api=None, language=None, data=attributes)
        show.seasons = seasons
        show.banner_objects = banners
        show.actor_objects = roles

        for season in show.seasons.values():
            season.show = show

        return show

    @staticmethod
    def buffy_attributes():
        attributes = {
                    'Actors': ['Sarah Michelle Gellar', 'Alyson Hannigan', 'Emma Caulfield', 'Michelle Trachtenberg', 'Anthony Head', 'James Marsters'],
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


    @staticmethod
    def rome_power_and_glory_attributes():
        """Used to check lacking information, e.g., Rating (empty-string vs. float)"""
        attributes = {
                      'Actors': [''],
                      'Airs_DayOfWeek': '',
                      'Airs_Time': '',
                      'ContentRating': '',
                      'FirstAired': '',
                      'Genre': ['Documentary'],
                      'IMDB_ID': 'tt0237666',
                      'Language': 'en',
                      'Network': '',
                      'NetworkID': '',
                      'Overview': b"Travel back in time to one of the most glorious empires in history. For over 1,000 years, Rome was the center of the known world, bringing to her subjects a common language, shared culture and wealth beyond imagination. But war, barbarian attacks and moral decay eventually took their toll, and the empire slowly began to crumble. Experience ancient history come to life, from Rome's primitive beginnings to the height of its glory \\u2013 and its eventual downfall.Filmed in 10 countries, this documentary combines location footage of ancient monuments, detailed reenactments, period art and writings, and fascinating insights from scholars and public figures. Witness the ancient world come to life \\u2013 and see history in all its drama.",
                      'Rating': '',
                      'RatingCount': 0,
                      'Runtime': 45,
                      'SeriesID': '',
                      'SeriesName': 'Rome: Power & Glory',
                      'Status': 'Ended',
                      'actor_objects': [],
                      'added': '',
                      'addedBy': '',
                      'banner': 'graphical/81623-g.jpg',
                      'fanart': 'fanart/original/81623-1.jpg',
                      'id': 81623,
                      'lastupdated': 1321055910,
                      'poster': '',
                     # 'seasons' : TODO
                     'zap2it_id': '',
        }

        return attributes;

    @staticmethod
    def rome_power_and_glory_seasons():
        season1 = Season(1, None)

        attributes = {
            'Combined_episodenumber': 1,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': '',
            'EpImgFlag': '',
            'EpisodeName': 'The Rise of the Roman Empire',
            'EpisodeNumber': 1,
            'FirstAired': '',
            'GuestStars': '',
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': b'',
            'ProductionCode': '',
            'Rating': 10.0,
            'RatingCount': 1,
            'SeasonNumber': 1,
            'Writer': '',
            'absolute_number': '',
            'filename': '',
            'id': 358483,
            'lastupdated': 1206676730,
           # 'seasons': TODO
            'seasonid': 31417,
            'seriesid': 81623,
        }

        episode11 = Episode(attributes, season1)

        attributes = {
            'Combined_episodenumber': 8,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': 3,
            'DVD_episodenumber': '',
            'DVD_season': 1,
            'Director': 'Steve Shill',
            'EpImgFlag': 2,
            'EpisodeName': 'Caesarion',
            'EpisodeNumber': 8,
            'FirstAired': date(2005, 10, 16),
            'GuestStars': ['Axel  Shumacher', 'Shaka Bunsie', 'Lyndsey Marshal', 'David de Keyser', 'Kathryn Hunter', 'David Kennedy', 'Tony Guilfoyle', 'Enoch Frost', 'Shaka Bunsie', 'Grant Masters'],
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': b"Having pursued Pompey into Egypt, Caesar arrives in Alexandria and meets the boy king Ptolemy XIII, who offers the general a surprise gift. Vorenus and Pullo play liberators again, freeing Ptolemy's incarcerated sister, Cleopatra. Caesar seeks payment from Egypt for past debts, and ends up forging a strategic union to ensure his legacy.",
            'ProductionCode': '',
            'Rating': 8.1,
            'RatingCount': 32,
            'SeasonNumber': 1,
            'Writer': 'William J. MacDonald',
            'absolute_number': '',
            'filename': 'episodes/73508/302630.jpg',
            'id': 302630,
            'lastupdated': 1250447392,
            # 'season': < Season 001 > ,
            'seasonid': 5899,
            'seriesid': 73508,
        }

        episode18 = Episode(attributes, season1)



        season1.episodes = {1: episode11, 8: episode18}

        return {1: season1}

    @staticmethod
    def mad_love_attributes():
        """Used to check correct handling of multiple occurrence of director (Pamela Fryman, HIMYM + ML)"""
        attributes = {
            'Actors': ['Jason Biggs', 'Sarah Chalke', 'Tyler Labine', 'Judy Greer', 'Sarah Wright'],
            'Airs_DayOfWeek': 'Monday',
            'Airs_Time': '8:30PM',
            'ContentRating': 'TV-14',
            'FirstAired': date(2011, 2, 14),
            'Genre': ['Comedy', 'DUMMYGENRE'],
            'IMDB_ID': 'tt1684910',
            'Language': 'en',
            'Network': 'CBS',
            'NetworkID': '',
            'Overview': b"MAD LOVE is a comedy about a quartet of New Yorkers - two who are falling in love and two who despise each other... at least for now. Ben, a lawyer, is a hopeless romantic trying to build a relationship with Kate, a beautiful, smart girl whom Ben thinks is the woman of his dreams. Larry, Ben's unrefined best friend and co-worker, is a guy who doesn't believe in love and has a long track record as the third wheel. Connie, Kate's roommate, works as a nanny and finds Larry aggravating... or does she? Larry and Connie have a lot in common, but refuse to let their guard down long enough to see it.",
            'Rating': 7.6,
            'RatingCount': 14,
            'Runtime': 30,
            'SeriesID': 78742,
            'SeriesName': 'Mad Love',
            'Status': 'Ended',
            'actor_objects': [],
            'added': '2010-09-02 12:03:09',
            'addedBy': 39111,
            'banner': 'graphical/186551-g2.jpg',
            'fanart': 'fanart/original/186551-1.jpg',
            'id': 186551,
            'lastupdated': 1343400449,
            'poster': 'posters/186551-1.jpg',
           # 'seasons' : TODO
            'zap2it_id': '',
        }

        return attributes;

    @staticmethod
    def mad_love_seasons():
        """
        Director: Pamela Fryman, DUMMYDIRECTOR
        Actor: Rachel Boston, DUMMYGUEST
        Writer: Adrian Wenner, DUMMYWRITER1, DUMMYWRITER2
        """
        season1 = Season(1, None)

        attributes = {
            'Combined_episodenumber': 1,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': ['Pamela Fryman', 'DUMMYDIRECTOR'],
            'EpImgFlag': 2,
            'EpisodeName': 'Fireworks',
            'EpisodeNumber': 1,
            'FirstAired': date(2011, 2, 14),
            'GuestStars': ['Rac2'],
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': b'When Ben Parr and Kate Swanson accidentally meet at the top of the Empire State Building, they make a date for later that evening and each bring along their best friends, Larry and Connie, who instantly despise each other.',
            'ProductionCode': '',
            'Rating': 7.6,
            'RatingCount': 27,
            'SeasonNumber': 1,
            'Writer': ['DUMMYWRITER1', 'DUMMYWRITER2'],
            'absolute_number': '',
            'filename': 'episodes/186551/3351461.jpg',
            'id': 3351461,
            'lastupdated': 1339322155,
            'seasonid': 379611,
            'seriesid': 186551,
        }

        episode11 = Episode(attributes, season1)

        season1.episodes = {1: episode11}

        season2 = Season(2, None)

        attributes = {
            'Combined_episodenumber': 3,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': '',
            'EpImgFlag': 2,
            'EpisodeName': 'The Kate Gatsby',
            'EpisodeNumber': 3,
            'FirstAired': date(2011, 2, 28),
            'GuestStars': '',
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': b"Ben gives bad advice to Kate not realizing that the advice could ruin a friendship that Kate and Connie have as well as the party being planned for Kate's birthday.",
            'ProductionCode': '',
            'Rating': 7.6,
            'RatingCount': 19,
            'SeasonNumber': 1,
            'Writer': 'Adrian Wenner',
            'absolute_number': '',
            'filename': 'episodes/186551/3486231.jpg',
            'id': 3486231,
            'lastupdated': 1339322255,
            'seasonid': 379612,
            'seriesid': 186551,
        }

        episode21 = Episode(attributes, season2)

        season2.episodes = {1: episode21}

        return {1: season1, 2: season2}

    @staticmethod
    def mad_love_banner():
        mirror = "http://thetvdb.com"

        attributes = {
                      'BannerPath': 'posters/186551-1.jpg',
                      'BannerType': 'poster',
                      'BannerType2': '680x1000',
                      'Language': 'en',
                      'Rating': 8.5,
                      'RatingCount': 2,
                      'banner_url': 'http://thetvdb.com/banners/posters/186551-1.jpg',
                      'id': 786301,
        }

        banner1 = Banner(mirror=mirror, data=attributes, show=None)

        attributes = {
                      'BannerPath': 'seasons/186551-1-2.jpg',
                      'BannerType': 'season',
                      'BannerType2': 'season',
                      'Language': 'en',
                      'Rating': 6.0,
                      'RatingCount': 1,
                      'Season': 1,
                      'banner_url': 'http://thetvdb.com/banners/seasons/186551-1-2.jpg',
                      'id': 796361,
        }

        banner2 = Banner(mirror=mirror, data=attributes, show=None)

        attributes = {
                      'BannerPath': 'seasons/186551-1-2.jpg',
                      'BannerType': 'season',
                      'BannerType2': 'season',
                      'Language': 'en',
                      'Rating': 6.0,
                      'RatingCount': 1,
                      'Season': 2,
                      'banner_url': 'http://thetvdb.com/banners/seasons/186551-1-2.jpg',
                      'id': 7963611,
        }

        banner3 = Banner(mirror=mirror, data=attributes, show=None)

        return [banner1, banner2, banner3]

    @staticmethod
    def mad_love_roles():
        mirror = "http://thetvdb.com"

        attributes = {
                      'Image': 'actors/226641.jpg',
                      'Name': 'Jason Biggs',
                      'Role': '',
                      'SortOrder': 0,
                      'id': 226641,
                      'image_url': 'http://thetvdb.com/banners/actors/226641.jpg',
        }

        role1 = Actor(mirror=mirror, data=attributes, show=None)

        attributes = {
                      'Image': 'actors/226661.jpg',
                      'Name': 'Sarah Chalke',
                      'Role': '',
                      'SortOrder': 1,
                      'id': 226661,
                      'image_url': 'http://thetvdb.com/banners/actors/226661.jpg',
        }

        role2 = Actor(mirror=mirror, data=attributes, show=None)

        attributes = {
                      'Image': 'actors/226651.jpg',
                      'Name': 'Judy Greer',
                      'Role': '',
                      'SortOrder': 2,
                      'id': 226651,
                      'image_url': 'http://thetvdb.com/banners/actors/226651.jpg',
        }

        role4 = Actor(mirror=mirror, data=attributes, show=None)

        attributes = {
                      'Image': 'actors/226681.jpg',
                      'Name': 'Sarah Wright',
                      'Role': '',
                      'SortOrder': 3,
                      'id': 226681,
                      'image_url': 'http://thetvdb.com/banners/actors/226681.jpg',
        }

        role5 = Actor(mirror=mirror, data=attributes, show=None)

        return [role1, role2, role4, role5]

    @staticmethod
    def mad_love_update_attributes():
        """Used to check correct handling of update behavior
            
        Genre: add Action; remove DUMMYGENRE; keep Comedy
        
        Actor: add DUMMY ACTOR2; remove Jason Biggs; keep Sarah Chalke, Tyler Labine, Judy Greer, Sarah Wright
            
           Changed attributes are: Actors, Rating, Status
        
        """
        attributes = {
            'Actors': ['Sarah Chalke', 'Tyler Labine', 'DUMMY ACTOR 1', 'Judy Greer', 'Sarah Wright', 'DUMMY ACTOR 2'],
            'Airs_DayOfWeek': 'Tuesday',
            'Airs_Time': '8:45PM',
            'ContentRating': 'TV-16',
            'FirstAired': date(2011, 2, 15),
            'Genre': ['Action', 'Comedy'],
            'IMDB_ID': 'tt1684911',
            'Language': 'de',
            'Network': '',
            'NetworkID': 'dummy_id',
            'Overview': b"Mad Love is a comedy about a quartet of New Yorkers - two who are falling in love and two who despise each other... at least for now. Ben, a lawyer, is a hopeless romantic trying to build a relationship with Kate, a beautiful, smart girl whom Ben thinks is the woman of his dreams. Larry, Ben's unrefined best friend and co-worker, is a guy who doesn't believe in love and has a long track record as the third wheel. Connie, Kate's roommate, works as a nanny and finds Larry aggravating... or does she? Larry and Connie have a lot in common, but refuse to let their guard down long enough to see it.",
            'Rating': 7.8,
            'RatingCount': 15,
            'Runtime': 35,
            'SeriesID': 78743,
            'SeriesName': 'Mad LOVE',
            'Status': 'Finished',
            'actor_objects': [],
            'added': '2010-09-02 12:04:09',
            'addedBy': 39112,
            'banner': 'graphical/186551-g3.jpg',
            'fanart': 'fanart/original/186551-2.jpg',
            'id': 186551,
            'lastupdated': 1343400450,
            'poster': 'posters/186551-2.jpg',
           # 'seasons' : TODO
            'zap2it_id': 'dummy_id',
        }

        return attributes;

    @staticmethod
    def mad_love_update_seasons():
        """
        Season: Adds 0, Updates Season 1, Removes Season 2
        
        Episode: Adds 0.1, Updates Episode 1.1, Adds Episode 1.2, Removes Episode 2.1
        
        Episode0.1:
          Guest: Add Brittany Snow
          Writer: Add Corey Nickerson
          Director: Add Beth McCarthy-Miller
        
        Episode1.1:
          Guest: Keep Rachel Boston, Remove DUMMYGUEST, Add GUESTDUMMY
          Writer: Keep DUMMYWRITER2, Remove DUMMYWRITER1, Add WRITERDUMMY
          Director: Keep Pamela Fryman, Remove DUMMYDIRECTOR, Add DIRECTORDUMMY
          
        Episode1.2:
          Guest: Add Martin Starr
          Writer: Add Rob DesHotel
          Director: Add Scott Ellis
          
        Episode2.1:
          Writer: Remove Adrian Wenner

        """
        season0 = Season(0, None)

        attributes = {
            'Combined_episodenumber': 4,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': 'Beth McCarthy-Miller',
            'EpImgFlag': 2,
            'EpisodeName': 'Little Sister, Big City',
            'EpisodeNumber': 4,
            'FirstAired': date(2011, 3, 7),
            'GuestStars': 'Brittany Snow',
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': b"Kate welcomes her younger sister Julia for a visit and doesn't realize that her sister is all grown up. Larry and Connie decide to support each other at the bar.",
            'ProductionCode': '',
            'Rating': 7.9,
            'RatingCount': 19,
            'SeasonNumber': 1,
            'Writer': 'Corey Nickerson',
            'absolute_number': '',
            'filename': 'episodes/186551/3486241.jpg',
            'id': 3486241,
            'lastupdated': 1339322312,
            'seasonid': 379610,
            'seriesid': 186551,
        }

        episode01 = Episode(attributes, season0)

        season0.episodes = {1: episode01}

        season1 = Season(1, None)

        attributes = {
            'Combined_episodenumber': 11,
            'Combined_season': 11,
            'DVD_chapter': '11',
            'DVD_discid': '11',
            'DVD_episodenumber': '11',
            'DVD_season': '11',
            'Director': ['Pamela Fryman', 'DIRECTORDUMMY'],
            'EpImgFlag': 22,
            'EpisodeName': 'New Fireworks',
            'EpisodeNumber': 11,
            'FirstAired': date(2011, 2, 15),
            'GuestStars': ['GUESTDUMMY', 'Rachel Boston'],
            'IMDB_ID': '1234',
            'Language': 'de',
            'Overview': b'CHANGED When Ben Parr and Kate Swanson accidentally meet at the top of the Empire State Building, they make a date for later that evening and each bring along their best friends, Larry and Connie, who instantly despise each other.',
            'ProductionCode': '1234',
            'Rating': 7.7,
            'RatingCount': 28,
            'SeasonNumber': 1,
            'Writer': ['DUMMYWRITER2', 'WRITERDUMMY'],
            'absolute_number': '1122',
            'filename': 'episodes/186551/3351462.jpg',
            'id': 3351461,
            'lastupdated': 1339322156,
            'seasonid': 379611,
            'seriesid': 186551,
        }

        episode11 = Episode(attributes, season1)

        attributes = {
            'Combined_episodenumber': 2,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': 'Scott Ellis',
            'EpImgFlag': 2,
            'EpisodeName': 'Friends and Other Obstacles',
            'EpisodeNumber': 2,
            'FirstAired': date(2011, 2, 21),
            'GuestStars': 'Martin Starr',
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': b"Ben and Kate aren't able to go on their first date because Larry and Connie are keeping them from it.",
            'ProductionCode': '',
            'Rating': 7.5,
            'RatingCount': 21,
            'SeasonNumber': 1,
            'Writer': 'Rob DesHotel',
            'absolute_number': '',
            'filename': 'episodes/186551/3486221.jpg',
            'id': 3486221,
            'lastupdated': 1339322208,
            'seasonid': 379611,
            'seriesid': 186551,
        }

        episode12 = Episode(attributes, season1)

        season1.episodes = {1: episode11, 2: episode12}

        return {0: season0, 1: season1}

    @staticmethod
    def mad_love_update_banner():
        """
        Remove
            Season2 banner
        Update
            Season1 and Series banner
        Add
            Season0 banner
        
        """

        mirror = "http://thetvdb.com"

        attributes = {
                      'BannerPath': 'fanart/original/186551-3.jpg',
                      'BannerType': 'poster',
                      'BannerType2': '680x1000',
                      'Language': 'en',
                      'Rating': 8.5,
                      'RatingCount': 2,
                      'banner_url': 'http://thetvdb.com/banners/fanart/original/186551-3.jpg',
                      'id': 78630101,
        }

        banner1 = Banner(mirror=mirror, data=attributes, show=None)

        attributes = {
                      'BannerPath': 'fanart/original/186551-3.jpg',
                      'BannerType': 'season',
                      'BannerType2': 'season',
                      'Language': 'en',
                      'Rating': 8.0,
                      'RatingCount': 1,
                      'Season': 1,
                      'banner_url': 'http://thetvdb.com/banners/fanart/original/186551-3.jpg',
                      'id': 796361,
        }

        banner2 = Banner(mirror=mirror, data=attributes, show=None)

        attributes = {
                      'BannerPath': 'seasons/186551-1-2.jpg',
                      'BannerType': 'season',
                      'BannerType2': 'season',
                      'Language': 'en',
                      'Rating': 6.0,
                      'RatingCount': 1,
                      'Season': 0,
                      'banner_url': 'http://thetvdb.com/banners/seasons/186551-1-2.jpg',
                      'id': 7963610,
        }

        banner3 = Banner(mirror=mirror, data=attributes, show=None)

        return [banner1, banner2, banner3]

    @staticmethod
    def mad_love_update_roles():
        mirror = "http://thetvdb.com"

        attributes = {
                      'Image': 'actors/22664101.jpg',
                      'Name': 'Jason Bigs',
                      'Role': 'DUMMYROLE',
                      'SortOrder': 2,
                      'id': 226641,
                      'image_url': 'http://thetvdb.com/banners/actors/22664101.jpg',
        }

        role1 = Actor(mirror=mirror, data=attributes, show=None)

        attributes = {
                      'Image': 'actors/226661.jpg',
                      'Name': 'Sarah Chalke',
                      'Role': '',
                      'SortOrder': 1,
                      'id': 226661,
                      'image_url': 'http://thetvdb.com/banners/actors/226661.jpg',
        }

        role2 = Actor(mirror=mirror, data=attributes, show=None)

        attributes = {
                      'Image': 'actors/226671.jpg',
                      'Name': 'Tyler Labine',
                      'Role': '',
                      'SortOrder': 2,
                      'id': 226671,
                      'image_url': 'http://thetvdb.com/banners/actors/226671.jpg',
        }

        role3 = Actor(mirror=mirror, data=attributes, show=None)

        return [role1, role2, role3]
