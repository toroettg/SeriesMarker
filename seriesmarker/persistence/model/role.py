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
from sqlalchemy.types import Integer, String

class Role(Base):
    """This class stores information about a role of an actor in a series."""

    __tablename__ = "role"

    id = Column(Integer, primary_key=True)

    series_extra_id = Column(Integer, ForeignKey('series_extra.id'))

    role = Column("Role", String)

    name = Column("Name", String)

    sort_order = Column("SortOrder", Integer)

    image = Column("Image", String)

    extra = relationship("RoleExtra", uselist=False)

    def __repr__(self):
        return "<Role('%s','%s')>" % (self.id, self.role)


