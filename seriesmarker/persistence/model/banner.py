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
from sqlalchemy.types import Integer, String, Float

class Banner(Base):
    """This class stores information about a banner of series and episodes."""

    __tablename__ = "banner"

    id = Column(Integer, primary_key=True)

    banner_path = Column("BannerPath", String)

    banner_type = Column("BannerType", String)

    banner_type2 = Column("BannerType2", String)

    language = Column("Language", String)

    rating = Column("Rating", Float)

    rating_count = Column("RatingCount", Integer)

    extra = relationship("BannerExtra", uselist=False)

    def __repr__(self):
        return "<Banner('%s','%s')>" % (self.id, self.banner_path)


