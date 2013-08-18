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
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Date, Float

class Series(Base):
    """This class stores information about a series."""

    __tablename__ = "series"

    id = Column(Integer, primary_key=True)  # private key of TheTVDB database, true series-id

    series_name = Column('SeriesName', String)
    overview = Column('Overview', String)
    status = Column('Status', String)
    last_updated = Column('lastupdated', Integer)
    rating = Column('Rating', Float)
    rating_count = Column('RatingCount', Integer)
    content_rating = Column('ContentRating', String)
    language = Column('Language', String)
    banner = Column('banner', String)
    fanart = Column('fanart', String)
    poster = Column('poster', String)
    first_aired = Column('FirstAired', Date)
    airs_day_of_week = Column('Airs_DayOfWeek', String)
    airs_time = Column('Airs_Time', String)
    runtime = Column('Runtime', Integer)
    added = Column('added', String)
    added_by = Column('added_by', Integer)
    network = Column('Network', String)
    network_id = Column('NetworkID', String)
    series_id = Column('SeriesID', Integer)
    imdb_id = Column('IMDB_ID', String)
    zap2it_id = Column('zap2it_id', String)

    actors = relationship('Actor')
    genre = relationship('Genre')

    seasons = relationship('Season', backref="series", order_by="Season.season_number")

    extra = relationship("SeriesExtra", uselist=False)

    def __repr__(self):
        return "<Series('%s','%s')>" % (self.id, self.series_name)


