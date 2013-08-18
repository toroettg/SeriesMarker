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

from seriesmarker.gui.model.episode_node import EpisodeNode
from seriesmarker.gui.model.tree_node import TreeNode

class SeasonNode(TreeNode):
    """Provides data for display about a :class:`.Season`."""
    def __init__(self, season, parent=None):
        """Initializes the node.
        
        Each episode of the given season is wrapped in an
        :class:`.EpisodeNode` and added as child of
        the node to the tree.
        
        :param season: The season to be handled by the node.
        :type season: :class:`.Season`
        :param parent: The series node the season belongs to.
        :type parent: :class:`.SeriesNode`
        
        """
        super().__init__(season, parent)

        for episode in season.episodes:
            self.append(EpisodeNode(episode, self))

    def name(self):
        """Returns a string representation of the node's data.
        
        :returns: The number of the season related to the node.
        
        :emphasis:`Overrides` :py:meth:`.TreeNode.name`
        
        """
        return "Season {}".format(self.data.season_number)

    def banner_url(self):
        """Defines the decoration of the node.
        
        If a :class:`.Banner` is set for the season, its URL returned.
        
        :returns: The URL of the banner related to the node's season.
        
        :emphasis:`Overrides` :py:meth:`.DecoratedNode.banner_url`
        
        """
        if self.data.banner:
            return self.data.banner.extra.banner_url
