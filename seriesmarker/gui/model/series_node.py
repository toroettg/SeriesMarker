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

from seriesmarker.gui.model.season_node import SeasonNode
from seriesmarker.gui.model.tree_node import TreeNode

class SeriesNode(TreeNode):
    """Provides data for display about a :class:`.Series`."""
    def __init__(self, series, parent=None):
        """Initializes the node.
        
        Each season of the given series is wrapped in an
        :class:`.SeasonNode` and added as child of
        the node to the tree.
        
        :param series: The series to be handled by the node.
        :type series: :class:`.Series`
        :param parent: The parent of this node (likely the root of the tree).
        :type parent: :class:`.TreeNode`
        
        """
        super().__init__(series, parent)

        for season in series.seasons:
            self.append(SeasonNode(season, self))

    def name(self):
        """Returns a string representation of the node's data.
        
        :returns: The title of the series related to the node.
        
        :emphasis:`Overrides` :py:meth:`.TreeNode.name`
        
        """
        return self.data.series_name

    def banner_url(self):
        """Defines the decoration of the node.
        
        If a :class:`.Banner` is set for the series, its URL returned.
        
        :returns: The URL of the banner related to the node's series.
        
        :emphasis:`Overrides` :py:meth:`.DecoratedNode.banner_url`
        
        """
        if self.data.extra.banner:
            return self.data.extra.banner.extra.banner_url
