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

from seriesmarker.persistence.factory.base_factory import BaseFactory
from seriesmarker.persistence.model.role import Role
from seriesmarker.persistence.model.role_extra import RoleExtra

class RoleFactory(BaseFactory):
    """Factory to create role objects from TheTVDB data."""

    @staticmethod
    def new_role(pytvdb_actor, update=None):
        """Creates a persistable role object from TheTVDB data.
        
        This method will create a new :class:`.Role` instance from a pytvdbapi
        actor object. If a role object is given, the existing one will be
        updated with the data instead.
        
        :param pytvdb_actor: The data to create the role from.
        :type pytvdb_actor: :class:`pytvdbapi.actor.Actor`
        :param update: A role to update with new data.
        :type update: :class:`.Role`
        :returns: The newly created or updated :class:`.Role` instance.
        
        """
        if update == None:
            role = Role()
            role.extra = RoleExtra()
        else:
            role = update

        if type(pytvdb_actor.Role) == list:
            role.role = ", ".join(pytvdb_actor.Role)
        else:
            role.role = pytvdb_actor.Role

        role.name = pytvdb_actor.Name
        role.sort_order = pytvdb_actor.SortOrder
        role.id = pytvdb_actor.id
        role.image = pytvdb_actor.Image

        role.extra.image_url = pytvdb_actor.image_url

        return role
