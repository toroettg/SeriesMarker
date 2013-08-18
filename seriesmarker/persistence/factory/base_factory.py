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

from seriesmarker.persistence.database import db_remove_item
import logging

logger = logging.getLogger(__name__)

class BaseFactory(object):
    """Base class of factories, offers common operations."""
    def __init__(self):
        super().__init__()
        self.reset()

    def reset(self):
        """Resets the factory log/history of performed updates."""
        self.added = []
        self.removed = []
        self.updated = []

    def _handle_list_attribute(self, items, pytvdb_values, cls):
        """Maps simple list attributes (containing strings) between pytvdbapi and seriesmarker.
        
        This method compares a list of strings, given by the pytvdbapi-object,
        with a given list of objects in the database. It creates and adds a
        new object, of the given class, to the database if the pytvdbapi-list
        contains an unknown string. It respectively removes objects from the
        database if a related string can not be found at the pytvdbapi-list.
        
        .. note::
        
            This method is intended to be used for simple data from TheTVDB, only.
            It applies to data, which has no relation to other objects and thus no
            dependencies, which need to be resolved on removal from the database.
        
        .. todo::
            
            Logging should be used to list differences on update of series/episodes.
        
        :param items: The list of objects from the database.
        :type items: list
        :param pytvdb_values: The list of strings from TheTVDB to compare with.
        :type pytvdb_values: list
        :param cls: The class which shall be used to create a new instance from.
    
        """
        if type(pytvdb_values) is str and pytvdb_values is not "":
            pytvdb_values = [pytvdb_values]
        else:
            pytvdb_values = set(pytvdb_values)  # Prevent possible duplicates

        for item in items:
            if item.name not in pytvdb_values:
                items.remove(item)
                db_remove_item(item)

        for value in pytvdb_values:
            if value not in [item.name for item in items]:
                item = cls(name=value)
                items.append(item)
