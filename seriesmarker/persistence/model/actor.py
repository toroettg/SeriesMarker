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
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String


class Actor(Base):
    """This class stores the basic (string) information about an actor of a series."""

    __tablename__ = "actor"

    id = Column('id', Integer, primary_key=True)

    series_id = Column(Integer, ForeignKey('series.id'))

    name = Column('name', String)

    def __repr__(self):
        return "<Actor('%s', '%s')>" % (self.id, self.name)
