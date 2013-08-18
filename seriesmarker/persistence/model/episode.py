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

from seriesmarker.persistence.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Float, Date

class Episode(Base):
    """This class stores information about an episode."""

    __tablename__ = "episode"

    id = Column(Integer, primary_key=True)

    season_id = Column(Integer, ForeignKey('season.id'))


    episode_name = Column('EpisodeName', String)
    episode_number = Column('EpisodeNumber', Integer)

    # season_number = Column('SeasonNumber', Integer) shifted to Season
    # series_id = Column(Integer, ForeignKey('series.id')) shifted to Season

    combined_episode_number = Column('Combined_episodenumber', Float)
    combined_season = Column('Combined_season', Integer)

    language = Column('Language', String)

    overview = Column('Overview', String)

    imdb_id = Column('IMDB_ID', String)

    airs_before_season = Column('airsbefore_season', Integer)
    airs_before_episode = Column('airsbefore_episode', Integer)
    airs_after_season = Column('airsafter_season', Integer)

    DVD_season = Column('DVD_season', Integer)
    DVD_chapter = Column('DVD_chapter', Integer)
    DVD_episode_number = Column('DVD_episodenumber', Float)
    DVD_disc_id = Column('DVD_discid', Integer)

    ep_img_flag = Column('EpImgFlag', Integer)

    production_code = Column('ProductionCode', String)

    last_updated = Column('lastupdated', Integer)

    filename = Column('filename', String)

    first_aired = Column('FirstAired', Date)

    absolute_number = Column('absolute_number', Integer)

    rating = Column('Rating', Float)
    rating_count = Column('RatingCount', Integer)

    guests = relationship('Guest')
    writers = relationship('Writer')
    directors = relationship('Director')

    extra = relationship("EpisodeExtra", uselist=False)

    def __repr__(self):
        return "<Episode('%s','%s')>" % (self.id, self.episode_name)








