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

from PySide.QtCore import QSize
from seriesmarker.gui.model.decorated_node import DecoratedNode
from seriesmarker.persistence.factory.banner_factory import BannerFactory

SCALE_SIZE = QSize(379, 70)

class SearchNode(DecoratedNode):
    """Node used to display resulting series from a search in a :class:`.SearchDialog`."""

    def __init__(self, show):
        """Initializes the node.
        
        Also defines the result's banner size. Banners of search results
        will not be permanently cached on disk. However, a banner may
        be cached temporarily by pytvdbapi.
        
        :param show: The show the node will display.
        :type show: :class:`.pytvdbapi.api.Show`
        
        """
        super().__init__(scale=SCALE_SIZE, cache=False)
        self.show = show
        self._banner = BannerFactory.new_banner(banner_type="series", banners=show.banner_objects)

    def banner_url(self):
        """Describes the banner to load from net for display by :class:`.BannerLoader`.
        
        :returns: The URL of the banner related to the node's show.
        
        :emphasis:`Overrides` :meth:`.DecoratedNode.banner_url`
                
        """
        if self._banner:
            return self._banner.extra.banner_url
        else:
            return None

