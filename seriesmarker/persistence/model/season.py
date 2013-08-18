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
from sqlalchemy.types import Integer

class Season(Base):
    """This class stores information about a season of a series."""

    __tablename__ = "season"

    id = Column(Integer, primary_key=True)

    series_id = Column(Integer, ForeignKey('series.id'))

    season_number = Column('SeasonNumber', Integer)

    episodes = relationship('Episode', backref='season', order_by="Episode.episode_number")

    banner_id = Column(Integer, ForeignKey('banner.id'))
    banner = relationship("Banner", uselist=False)

    def __repr__(self):
        return "<Season('%s')>" % (self.id)








