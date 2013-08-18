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

class BannerExtra(Base):
    """This class stores extra information about a banner, e.g., its URL."""

    __tablename__ = "banner_extra"

    id = Column(Integer, primary_key=True)

    banner_id = Column(Integer, ForeignKey("banner.id"))

    banner_url = Column("BannerURL", String)

    def __repr__(self):
        return "<BannerExtra('%s','%s')>" % (self.id, self.banner_url)


