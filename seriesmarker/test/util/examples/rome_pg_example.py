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

from datetime import date

from pytvdbapi.api import Season, Episode

from seriesmarker.test.util.examples.base_example import BaseExample


class RomePGExample(BaseExample):
    """Used to check lacking information, e.g., Rating (empty-string vs. float)"""

    @classmethod
    def series_attributes(cls):
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
            'Combined_episodenumber': 2.0,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': 1,
            'DVD_episodenumber': 2.0,
            'DVD_season': '',
            'Director': 'Lynn Dougherty',
            'EpImgFlag': 1,
            'EpisodeName': 'Legions of Conquest',
            'EpisodeNumber': 2,
            'FirstAired': '',
            'GuestStars': '',
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': 'What began as an amateur citizens\' army becomes the formidable legions that conquered the Western world and beyond. These are the thrilling stories behind the campaigns that brought them greatness.',
            'ProductionCode': '',
            'Rating': 10.0,
            'RatingCount': 1,
            'SeasonNumber': 1,
            'Writer': 'Lynn Dougherty',
            'absolute_number': '',
            'filename': 'episodes/81623/358484.jpg',
            'id': 358484,
            'lastupdated': 1352487698,
           #'season' : ignored
            'seasonid': 31417,
            'seriesid': 81623,
        }

        episode12 = Episode(attributes, season1)

        attributes = {
            'Combined_episodenumber': 3.0,
            'Combined_season': 1,
            'DVD_chapter': '',
            'DVD_discid': 1,
            'DVD_episodenumber': 3.0,
            'DVD_season': '',
            'Director': 'Neil Barrett',
            'EpImgFlag': 1,
            'EpisodeName': 'Seduction of Power',
            'EpisodeNumber': 3,
            'FirstAired': '',
            'GuestStars': '',
            'IMDB_ID': '',
            'Language': 'en',
            'Overview': 'From Julius Caesar to Caligula, the story of Rome is populated by towering figures who were brilliant, powerful....and, sometimes, deranged!',
            'ProductionCode': '',
            'Rating': 10.0,
            'RatingCount': 1,
            'SeasonNumber': 1,
            'Writer': 'Neil Barrett',
            'absolute_number': '',
            'filename': 'episodes/81623/358485.jpg',
            'id': 358485,
            'lastupdated': 1352487703,
           #'season' : ignored
            'seasonid': 31417,
            'seriesid': 81623,
        }

        episode13 = Episode(attributes, season1)

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

        season1.episodes = {1: episode11, 2: episode12, 3: episode13, 8: episode18}

        return {1: season1}
