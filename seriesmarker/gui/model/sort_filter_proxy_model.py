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

from PySide.QtCore import Qt
from PySide.QtGui import QSortFilterProxyModel
from seriesmarker.gui.model.tree_series_model import EpisodeNode

class SortFilterProxyModel(QSortFilterProxyModel):
    """Class to tweak the main view.
    
    This proxy model allows the sorting of series and visual tweaks, e.g.,
    text alignment.
    
    .. note::
        This class is intended to be used as a proxy between 
        :class:`.TreeSeriesModel` and the series view of :class:`.MainWindow`.
    
    """
    def __init__(self):
        """Initializes the proxy model."""
        super().__init__()

    def data(self, index, role=Qt.DisplayRole):
        """Relays the method call to the source model, but may alter the result.
        
        This method hides the decoration in the tree of the main view
        and aligns the names of series and seasons to the left.
        
        :param index: The item's position in the model to get data for.
        :type index: :class:`.PySide.QtCore.QModelIndex`
        :param role: Determines the kind of data to get from the model.
        :type role: integer
        
        :returns: None for :class:`PySide.QtCore.Qt.DecorationRole`
        :returns: :class:`.PySide.QtCore.Qt.AlignLeft` for
            :class:`.Qt.TextAlignmentRole`.
        :returns: The unaltered return value of the method call
            on the source model for other roles.
        
        """
        if role == Qt.DecorationRole:
            return None
        elif role == Qt.TextAlignmentRole and index.column() == 0:
            return Qt.AlignLeft
        else:
            return super().data(index, role)

    def filterAcceptsRow(self, source_row, source_parent):
        """Filters rows from the source mode to hide them in the proxy's views.
        
        This method hides episodes in the tree of the main view.
        
        :param source_row: The row-index to test for acceptance.
        :type source_row: integer
        :param source_parent: The parent of the row to test. 
        :type source_parent: :class:`.PySide.QtCore.QModelIndex`
        
        :returns: True if a described row should be displayed, otherwise False.
        
        """
        index = self.sourceModel().index(source_row, 0, source_parent)
        item = self.sourceModel().node_at(index)

        if isinstance(item, EpisodeNode):
            return False
        else:
            return True

    def pop_related_series(self, index):
        """Relays the method call to the source model.
        
        The relay is necessary, since the method is not part
        of a original Qt model. Does not alter the result.
        
        :param index: The proxy index to pass onto the source method.
        :type index: :class:`.PySide.QtCore.QModelIndex`
        
        :returns: The return value of the method call on the source model.
        
        """
        return super().pop_related_series(self.mapToSource(index))
