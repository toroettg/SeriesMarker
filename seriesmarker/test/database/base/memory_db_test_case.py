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

from seriesmarker.persistence import database
from seriesmarker.persistence.database import Base
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker
import unittest




class MemoryDBTestCase(unittest.TestCase):
    """Base class for non-persistent database testing in memory.
    
    .. note::
    
        Make sure to import the models used in the derived test, so the database tables can be created by Base.metadata.
        
    """
    def setUp(self):
        self.db_engine = create_engine('sqlite:///:memory:', echo=True)

        self.db_connection = self.db_engine.connect()

        self.db_session = scoped_session(sessionmaker(bind=self.db_engine, autoflush=False, autocommit=False))

        Base.metadata.create_all(bind=self.db_engine)

        database.db_session = self.db_session

    def tearDown(self):
        self.db_session.close()

        database.db_session = scoped_session(sessionmaker())  # restore original db_session for following test cases

        Base.metadata.drop_all(bind=self.db_engine)
