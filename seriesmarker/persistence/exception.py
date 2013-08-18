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

class EntityExistsException(Exception):
    """Indicates the existence of an entity with same ID in the database."""
    def __init__(self, entity_id, table):
        self.entity_id = entity_id
        self.table = table

    def __str__(self):
        return repr("Entity already exists in database (ID '{id}', table '{table}')".format(id=self.entity_id, table=self.table))

class EntityNotFoundException(Exception):
    """Indicates the absence of an entity in the database."""
    def __init__(self, entity_id, table):
        self.entity_id = entity_id
        self.table = table

    def __str__(self):
        return repr("Entity does not exist in database (ID '{id}', table '{table}')".format(id=self.entity_id, table=self.table))
