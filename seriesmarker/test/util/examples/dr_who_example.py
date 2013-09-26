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

from pytvdbapi.api import Show, Season, Episode
from pytvdbapi.banner import Banner

from seriesmarker.test.util.examples.base_example import BaseExample


class DrWhoExample(BaseExample):
    """Standard example for various test cases.
    
    .. seealso:: 
        :py:func:`.test_04_update` 
    """
    @classmethod
    def series_attributes(cls):
        attributes = {
            'Actors': ['William Hartnell', 'Patrick Troughton', 'Jon Pertwee', 'Tom Baker', 'Sylvester McCoy', 'Peter Davison', 'Paul McGann', 'Richard Hurndall', 'Colin Baker', 'Sarah Sutton', 'Elizabeth Sladen', 'William Russell', 'Jacqueline Hill', 'Carole Ann Ford', "Maureen O'Brien", 'Mark Strickson', 'Bonnie Langford', 'Mary Tamm', 'Nicola Bryant', 'Caroline John', 'Louise Jameson', 'Katy Manning', 'Janet Fielding', 'Lalla Ward', 'Deborah Watling', 'Eric Roberts', 'Daphne Ashbrook', 'Sophie Aldred', 'Anthony Ainley', 'Geoffrey Beevers', 'Peter Pratt', 'Roger Delgado'],
            'Airs_DayOfWeek': 'Saturday',
            'Airs_Time': '5:15 PM',
            'ContentRating': 'TV-PG',
            'FirstAired': date(1963, 11, 23),
            'Genre': ['Action', 'Adventure', 'Science-Fiction'],
            'IMDB_ID': 'tt0056751',
            'Language': 'en',
            'Network': 'BBC One',
            'NetworkID': '',
            'Overview': 'Doctor Who is the longest-running science fiction TV series in history, airing initially from 1963 to 1989.  Doctor Who is about ideas.  It pioneered sophisticated mixed-level storytelling. Its format was the key to its longevity: the Doctor, a mysterious traveller in space and time, travels in his ship, the TARDIS.  The TARDIS can take him and his companions anywhere in time and space. Inevitably he finds evil at work wherever he goes...',
            'Rating': 9.2,
            'RatingCount': 95,
            'Runtime': 25,
            'SeriesID': 355,
            'SeriesName': 'Doctor Who',
            'Status': 'Ended',
           # 'actor_objects' : ignored
            'added': '',
            'addedBy': '',
            'banner': 'graphical/76107-g14.jpg',
            'fanart': 'fanart/original/76107-23.jpg',
            'id': 76107,
            'lastupdated': 1377922489,
            'poster': 'posters/76107-4.jpg',
           # 'seasons' : ignored
            'zap2it_id': 'SH001301',
        }

        return attributes

    @classmethod
    def seasons(cls, show):
        seasons = dict()

        attributes01 = {
            'Combined_episodenumber': 1,
            'Combined_season': 0,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': '',
            'EpImgFlag': 1,
            'EpisodeName': 'An Unearthly Child - Unaired Pilot',
            'EpisodeNumber': 1,
            'FirstAired': '',
            'GuestStars': '',
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': 'The first episode, "An Unearthly Child", was originally recorded a month before full recording on the series began. However, the initial recording was bedevilled with technical problems and errors made during the performance.  Two versions of the scene set in the TARDIS were recorded, along with an aborted first attempt to start the second version.',
            'ProductionCode': '',
            'Rating': 7.0,
            'RatingCount': 1,
            'SeasonNumber': 0,
            'Writer': '',
            'absolute_number': '',
            'airsafter_season': '',
            'airsbefore_episode': 1,
            'airsbefore_season': 1,
            'filename': 'episodes/76107/362678.jpg',
            'id': 362678,
            'lastupdated': 1285702634,
           # 'season' : ignored
            'seasonid': 23565,
            'seriesid': 76107,
            'thumb_added': '',
            'thumb_height': 300,
            'thumb_width': 400,
            'tms_export': 1374789754,
        }

        attributes11 = {
            'Combined_episodenumber': 1,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': 'Waris Hussein',
            'EpImgFlag': '',
            'EpisodeName': 'An Unearthly Child',
            'EpisodeNumber': 1,
            'FirstAired': date(1963, 11, 23),
            'GuestStars': ['Reg Cranfield'],
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': 'London, 1963. Schoolteachers Ian Chesterton and Barbara Wright are perplexed by the behaviour of one of their pupils, Susan Foreman. Her knowledge of science and history exceeds theirs, yet she seems totally ignorant of many common aspects of everyday life. They follow her to her home address, a junkyard with a police telephone box standing in it, and encounter her grandfather, the enigmatic Doctor. When they force their way past him into the police box, Susan\'s secret is revealed: she and the Doctor are aliens, and the police box is a time machine, the TARDIS, capable of visiting any point in the universe at any moment in time…',
            'ProductionCode': 'A',
            'Rating': 7.5,
            'RatingCount': 20,
            'SeasonNumber': 1,
            'Writer': 'Anthony Coburn',
            'absolute_number': '',
            'filename': 'episodes/76107/183204.jpg',
            'id': 183204,
            'lastupdated': 1200768302,
           # 'season' : ignored
            'seasonid': 9666,
            'seriesid': 76107,
            'thumb_added': '',
            'thumb_height': 300,
            'thumb_width': 400,
            'tms_export': 1374789754,
        }

        attributes12 = {
            'Combined_episodenumber': 2,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': 'Waris Hussein',
            'EpImgFlag': '',
            'EpisodeName': 'The Cave of Skulls',
            'EpisodeNumber': 2,
            'FirstAired': date(1963, 11, 30),
            'GuestStars': ['Jeremy Young', 'Howard Lang', 'Alethea Charlton', 'Eileen Way', 'Derek Newark'],
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': 'Earth, 100,000 B.C. The enigmatic Doctor, afraid that schoolteachers Ian Chesterton and Barbara Wright will reveal his secrets to the people of 20th century Earth, has taken them and his granddaughter Susan back to the dawn of human history. There, the four travellers are dragged into the savage politics of a tribe of cavemen who have lost the secret of making fire…',
            'ProductionCode': 'A',
            'Rating': 6.8,
            'RatingCount': 14,
            'SeasonNumber': 1,
            'Writer': 'Anthony Coburn',
            'absolute_number': '',
            'filename': 'episodes/76107/183206.jpg',
            'id': 183206,
            'lastupdated': 1200766733,
           # 'season' : ignored
            'seasonid': 9666,
            'seriesid': 76107,
        }

        attributes13 = {
            'Combined_episodenumber': 3,
            'Combined_season': 2,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': 'Mervyn Pinfield, Douglas Camfield',
            'EpImgFlag': 1,
            'EpisodeName': 'Crisis',
            'EpisodeNumber': 3,
            'FirstAired': date(1964, 11, 14),
            'GuestStars': ['Alan Tilvern', 'Reginald Barratt', 'Rosemary Johnson', 'Fred Ferris'],
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': 'Earth, 1964. An accident on landing vastly reduces the TARDIS and the travellers in size. They come across a scheme run by Forester, a ruthless businessman and his misguided scientist colleague Smithers to launch a new insecticide which is capable of destroying the local ecology. Forester is prepared to commit murder to secure the success of this project - can the inch-high travellers somehow foil him?',
            'ProductionCode': 'L',
            'Rating': 7.0,
            'RatingCount': 6,
            'SeasonNumber': 2,
            'Writer': 'Louis Marks',
            'absolute_number': '',
            'filename': 'episodes/76107/183214.jpg',
            'id': 183214,
            'lastupdated': 1234645307,
           # 'season' : ignored
            'seasonid': 9677,
            'seriesid': 76107,
        }

        attributes14 = {
            'Combined_episodenumber': 4,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': 'Waris Hussein',
            'EpImgFlag': '',
            'EpisodeName': 'The Firemaker',
            'EpisodeNumber': 4,
            'FirstAired': date(1963, 12, 14),
            'GuestStars': ['Jeremy Young', 'Howard Lang', 'Alethea Charlton', 'Eileen Way', 'Derek Newark'],
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': 'The TARDIS crew must make fire for the early humans to stay alive. But once they do, they may not be allowed to leave!',
            'ProductionCode': 'A',
            'Rating': 6.7,
            'RatingCount': 9,
            'SeasonNumber': 1,
            'Writer': 'Anthony Coburn',
            'absolute_number': '',
            'filename': 'episodes/76107/183208.jpg',
            'id': 183208,
            'lastupdated': 1200767219,
           # 'season' : ignored
            'seasonid': 9666,
            'seriesid': 76107,
        }

        attributes15 = {
            'Combined_episodenumber': 5,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': 'Christopher Barry',
            'EpImgFlag': '',
            'EpisodeName': 'The Dead Planet',
            'EpisodeNumber': 5,
            'FirstAired': date(1963, 12, 21),
            'GuestStars': '',
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': 'Time Unknown, Planet Unknown. The TARDIS lands in an eerie petrified forest overlooking a magnificent steel city.  The Doctor wants to explore the city – but what is waiting there?',
            'ProductionCode': 'B',
            'Rating': 7.1,
            'RatingCount': 12,
            'SeasonNumber': 1,
            'Writer': 'Terry Nation',
            'absolute_number': '',
            'filename': 'episodes/76107/183209.jpg',
            'id': 183209,
            'lastupdated': 1200767339,
           # 'season' : ignored
            'seasonid': 9666,
            'seriesid': 76107,
        }

        attributes16 = {
            'Combined_episodenumber': 6,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': 'Christopher Barry',
            'EpImgFlag': '',
            'EpisodeName': 'The Survivors',
            'EpisodeNumber': 6,
            'FirstAired': date(1963, 12, 28),
            'GuestStars': ['Michael  Summerton', 'Peter Hawkins', 'David Graham', 'Robert Jewell', 'Kevin Manser', 'Gerald Taylor'],
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': 'The dead planet is not uninhabited after all. The Doctor is about to meet what will become his greatest enemies. And he and his crew are dying of radiation sickness.',
            'ProductionCode': 'B',
            'Rating': 7.4,
            'RatingCount': 9,
            'SeasonNumber': 1,
            'Writer': 'Terry Nation',
            'absolute_number': '',
            'filename': 'episodes/76107/183210.jpg',
            'id': 183210,
            'lastupdated': 1200767442,
           # 'season' : ignored
            'seasonid': 9666,
            'seriesid': 76107,
        }

        attributes21 = {
            'Combined_episodenumber': 1,
            'Combined_season': 2,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': 'Mervyn Pinfield',
            'EpImgFlag': 1,
            'EpisodeName': 'Planet of Giants',
            'EpisodeNumber': 1,
            'FirstAired': date(1964, 10, 31),
            'GuestStars': ['Alan Tilvern', 'Frank Crawshaw'],
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': 'Earth, 1964. An accident on landing vastly reduces the TARDIS and the travellers in size. They come across a scheme run by Forester, a ruthless businessman and his misguided scientist colleague Smithers to launch a new insecticide which is capable of destroying the local ecology. Forester is prepared to commit murder to secure the success of this project - can the inch-high travellers somehow foil him?',
            'ProductionCode': 'J',
            'Rating': 7.1,
            'RatingCount': 8,
            'SeasonNumber': 2,
            'Writer': 'Louis Marks',
            'absolute_number': '',
            'filename': 'episodes/76107/183212.jpg',
            'id': 183212,
            'lastupdated': 1229961944,
           # 'season' : ignored
            'seasonid': 9677,
            'seriesid': 76107,
            'thumb_added': '',
            'thumb_height': 240,
            'thumb_width': 320,
            'tms_export': 1,
        }

        attributes101 = {
            'Combined_episodenumber': 1,
            'Combined_season': 10,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': 'Lennie Mayne',
            'EpImgFlag': 1,
            'EpisodeName': 'The Three Doctors (1)',
            'EpisodeNumber': 1,
            'FirstAired': date(1972, 12, 30),
            'GuestStars': ['Patricia Prior', 'Clyde Pollitt', 'Denys Palmer', 'Laurie Webb'],
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': 'England, the near future. A strange anti-matter creature arrives on Earth and attacks UNIT HQ. It seems to be specifically seeking the Doctor out - but why? With the Time Lords themselves unable to help, it seems the only person who can help the Doctor is himself - or selves...',
            'ProductionCode': 'RRR',
            'Rating': 7.7,
            'RatingCount': 3,
            'SeasonNumber': 10,
            'Writer': 'Bob Baker, Dave Martin',
            'absolute_number': '',
            'filename': 'episodes/76107/183268.jpg',
            'id': 183268,
            'lastupdated': 1249083224,
           # 'season' : ignored
            'seasonid': 9667,
            'seriesid': 76107,
            'thumb_added': '',
            'thumb_height': 300,
            'thumb_width': 400,
            'tms_export': 1374789754,
        }

        attributes111 = {
            'Combined_episodenumber': 1,
            'Combined_season': 11,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': 'Alan Bromley',
            'EpImgFlag': 1,
            'EpisodeName': 'The Time Warrior (1)',
            'EpisodeNumber': 1,
            'FirstAired': date(1973, 12, 15),
            'GuestStars': ['Donald Pelmear', 'John J Carney', 'Sheila Fay', 'June Brown', 'Gordon Pitt'],
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': 'England, the 12th century. Robber baron Irongron is recruited by Linx, a Sontaran warrior whose starship has been forced down on Earth. Linx is forced to use a time-travel device to steal resources and scientists from the future to repair his ship, but in doing so involves UNIT and the Doctor...',
            'ProductionCode': 'UUU',
            'Rating': 7.5,
            'RatingCount': 4,
            'SeasonNumber': 11,
            'Writer': 'Robert Holmes',
            'absolute_number': '',
            'filename': 'episodes/76107/183273.jpg',
            'id': 183273,
            'lastupdated': 1249087914,
           # 'season' : ignored
            'seasonid': 9668,
            'seriesid': 76107,
            'thumb_added': '',
            'thumb_height': 300,
            'thumb_width': 400,
            'tms_export': 1374789754,
        }

        attributes201 = {
            'Combined_episodenumber': 1,
            'Combined_season': 20,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': 'Ron Jones',
            'EpImgFlag': 1,
            'EpisodeName': 'Arc of Infinity (1)',
            'EpisodeNumber': 1,
            'FirstAired': date(1983, 1, 3),
            'GuestStars': ['Andrew  Boxer', 'Alastair  Cumming', 'Elspet Gray', 'Max Harvey', 'Neil Daglish', 'John D. Collins', 'Maya Woolfe', 'Malcolm  Harvey'],
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': 'The Time Lords of Gallifrey are disturbed by the possible return of an old enemy... and the only way to stop him is to execute the Doctor.',
            'ProductionCode': '6E',
            'Rating': 7.0,
            'RatingCount': 1,
            'SeasonNumber': 20,
            'Writer': 'Johnny Byrne',
            'absolute_number': '',
            'filename': 'episodes/76107/183327.jpg',
            'id': 183327,
            'lastupdated': 1227143789,
           # 'season' : ignored
            'seasonid': 9678,
            'seriesid': 76107,
            'thumb_added': '',
            'thumb_height': 300,
            'thumb_width': 400,
            'tms_export': 1374789754,
        }

        attributes211 = {
            'Combined_episodenumber': 1,
            'Combined_season': 21,
            'DVD_chapter': '',
            'DVD_discid': '',
            'DVD_episodenumber': '',
            'DVD_season': '',
            'Director': 'Pennant Roberts',
            'EpImgFlag': 1,
            'EpisodeName': 'Warriors of the Deep (1)',
            'EpisodeNumber': 1,
            'FirstAired': date(1984, 1, 5),
            'GuestStars': ['Tom Adams', 'Ian McCulloch', 'Nigel Humphreys', 'Martin Neil', 'Tara Ward', 'Norman Comer', 'Nitza Saul', 'Vincent Brimble', 'Christopher Farries', 'James Coombes'],
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': 'Earth\'s ocean floor, 2084. With two superpowers poised on the brink of a devastating photonic war, a missile base comes under attack from the reptilian Sea Devils and Silurians, intent on eradicating the upstart human race and reclaiming the planet…',
            'ProductionCode': '6L',
            'Rating': 8.0,
            'RatingCount': 1,
            'SeasonNumber': 21,
            'Writer': 'Johnny Byrne',
            'absolute_number': '',
            'filename': 'episodes/76107/183334.jpg',
            'id': 183334,
            'lastupdated': 1227222873,
           # 'season' : ignored
            'seasonid': 9679,
            'seriesid': 76107,
            'thumb_added': '',
            'thumb_height': 300,
            'thumb_width': 400,
            'tms_export': 1374789754,
        }

        lcl = locals()
        for season_number in [0, 1, 2, 10, 11, 20, 21]:
            season = Season(season_number, show)
            season.episodes = dict()

            if season_number == 1:
                range_limit = 7
            else:
                range_limit = 2
            for episode_number in range(1, range_limit):
                season.episodes[episode_number] = Episode(lcl["attributes{}{}".format(season_number, episode_number)], season)
            seasons[season_number] = season

        return seasons

    @classmethod
    def banners(cls, show):
        mirror = "http://thetvdb.com"

        attributes = {
            'BannerPath': 'graphical/76107-g14.jpg',
            'BannerType': 'series',
            'BannerType2': 'graphical',
            'Language': 'en',
            'Rating': 9.3333,
            'RatingCount': 6,
            'banner_url': 'http://thetvdb.com/banners/graphical/76107-g14.jpg',
            'id': 57581,
        }

        banner1 = Banner(mirror=mirror, data=attributes, show=show)

        attributes = {
            'BannerPath': 'posters/76107-4.jpg',
            'BannerType': 'poster',
            'BannerType2': '680x1000',
            'Language': 'en',
            'Rating': 9.0,
            'RatingCount': 3,
            'banner_url': 'http://thetvdb.com/banners/posters/76107-4.jpg',
            'id': 872858,
        }

        banner2 = Banner(mirror=mirror, data=attributes, show=show)

        attributes = {
            'BannerPath': 'seasons/76107-0.jpg',
            'BannerType': 'season',
            'BannerType2': 'season',
            'Language': 'en',
            'Rating': 9.0,
            'RatingCount': 1,
            'Season': 0,
            'banner_url': 'http://thetvdb.com/banners/seasons/76107-0.jpg',
            'id': 841011,
        }

        banner3 = Banner(mirror=mirror, data=attributes, show=show)

        attributes = {
            'BannerPath': 'seasons/76107-1.jpg',
            'BannerType': 'season',
            'BannerType2': 'season',
            'Language': 'en',
            'Rating': 7.0,
            'RatingCount': 3,
            'Season': 1,
            'banner_url': 'http://thetvdb.com/banners/seasons/76107-1.jpg',
            'id': 227201,
        }

        banner4 = Banner(mirror=mirror, data=attributes, show=show)

        attributes = {
            'BannerPath': 'seasons/76107-2.jpg',
            'BannerType': 'season',
            'BannerType2': 'season',
            'Language': 'en',
            'Rating': 7.0,
            'RatingCount': 3,
            'Season': 2,
            'banner_url': 'http://thetvdb.com/banners/seasons/76107-2.jpg',
            'id': 227221,
        }

        banner5 = Banner(mirror=mirror, data=attributes, show=show)

        attributes = {
            'BannerPath': 'seasons/76107-10.jpg',
            'BannerType': 'season',
            'BannerType2': 'season',
            'Language': 'en',
            'Rating': 10.0,
            'RatingCount': 1,
            'Season': 10,
            'banner_url': 'http://thetvdb.com/banners/seasons/76107-10.jpg',
            'id': 799081,
        }

        banner6 = Banner(mirror=mirror, data=attributes, show=show)

        attributes = {
            'BannerPath': 'seasons/76107-11.jpg',
            'BannerType': 'season',
            'BannerType2': 'season',
            'Language': 'en',
            'Rating': 10.0,
            'RatingCount': 1,
            'Season': 11,
            'banner_url': 'http://thetvdb.com/banners/seasons/76107-11.jpg',
            'id': 799091,
        }

        banner7 = Banner(mirror=mirror, data=attributes, show=show)

        attributes = {
            'BannerPath': 'seasons/76107-20-2.jpg',
            'BannerType': 'season',
            'BannerType2': 'season',
            'Language': 'en',
            'Rating': 5.5,
            'RatingCount': 2,
            'Season': 20,
            'banner_url': 'http://thetvdb.com/banners/seasons/76107-20-2.jpg',
            'id': 23950,
        }

        banner8 = Banner(mirror=mirror, data=attributes, show=show)

        attributes = {
            'BannerPath': 'seasons/76107-21.jpg',
            'BannerType': 'season',
            'BannerType2': 'season',
            'Language': 'en',
            'Rating': 10.0,
            'RatingCount': 1,
            'Season': 21,
            'banner_url': 'http://thetvdb.com/banners/seasons/76107-21.jpg',
            'id': 799191,
        }

        banner9 = Banner(mirror=mirror, data=attributes, show=show)

        lcl = locals()
        return [lcl["banner{}".format(number)] for number in range(1, 10)]
