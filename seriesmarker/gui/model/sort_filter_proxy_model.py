#==============================================================================
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 - 2016 Tobias Röttger <toroettg@gmail.com>
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

from seriesmarker.gui.model.episode_node import EpisodeNode
from seriesmarker.gui.model.season_node import SeasonNode


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
        :type index: :class:`~.PySide.QtCore.QModelIndex`
        :param role: Determines the kind of data to get from the model.
        :type role: :class:`int`

        :returns: None for :class:`PySide.QtCore.Qt.DecorationRole`
        :returns: :class:`.PySide.QtCore.Qt.AlignLeft` for
            :class:`.Qt.TextAlignmentRole`.
        :returns: The unaltered return value of the method call
            on the source model for other roles.

        :emphasis:`Overrides` :py:meth:`.QAbstractItemModel.data`

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
        :type source_row: :class:`int`
        :param source_parent: The parent of the row to test.
        :type source_parent: :class:`~.PySide.QtCore.QModelIndex`

        :returns: True if a described row should be displayed, otherwise False.

        :emphasis:`Overrides` :py:meth:`.QSortFilterProxyModel.filterAcceptsRow`

        """
        index = self.sourceModel().index(source_row, 0, source_parent)
        item = self.sourceModel().node_at(index)

        return not isinstance(item, EpisodeNode)

    def lessThan(self, left, right):
        """Defines the sort order of elements, displayed in the proxy's view.

        This method sorts :class:`.SeasonNode` elements by their season
        number, instead of their :class:`.Qt.DisplayRole` (which would lead
        to the alphanumeric sort order of 'Season 10' < 'Season 2').

        This method also sorts the episodes column (column 1) by
        the number of total watched episodes rather than the displayed
        string of the column (so '1/7' may come before '1/2' if
        the related series name is also the lesser one).

        Series are sorted by numerical progress first, then by total
        number of watched episodes and finally by series name.
        Completed series (progress = 100.0%) are being ignored by progress
        sort and added at the end of the list in alphanumerical order.

        :param left: The index of the left item to be sorted.
        :type left: :class:`~.PySide.QtCore.QModelIndex`
        :param right: The index of the right item to be sorted.
        :type right: :class:`~.PySide.QtCore.QModelIndex`

        :returns: True if the value of the item referred to by the given
            index left is less than the value of the item referred to by
            the given index right , otherwise returns false.

        :emphasis:`Overrides` :py:meth:`.QSortFilterProxyModel.lessThan`

        """
        left_node = self.sourceModel().data(left, Qt.UserRole)
        right_node = self.sourceModel().data(right, Qt.UserRole)

        column = left.column()

        def _by_name(left_node, right_node):
            left_data = left_node.name()
            right_data = right_node.name()
            if self.sortOrder() == Qt.DescendingOrder:
                return right_data < left_data
            else:
                return left_data < right_data

        def _by_episodes(left_node, right_node):
            left_data = left_node.checked_count
            right_data = right_node.checked_count
            if left_data == right_data:
                return _by_name(left_node, right_node)
            else:
                return left_data < right_data

        if isinstance(left_node, SeasonNode):  #Always sort seasons by number
            left_data = left_node.data.season_number
            right_data = right_node.data.season_number
            if self.sortOrder() == Qt.DescendingOrder:
                return right_data < left_data
            else:
                return left_data < right_data
        elif column == 0:  #Sort by series name
            return super().lessThan(left, right)
        elif column == 1:  # Sort by episodes
            return _by_episodes(left_node, right_node)
        elif column == 2:  # Sort by progress
            left_data = round(
                left_node.checked_count / left_node.leaf_count, 3)
            right_data = round(
                right_node.checked_count / right_node.leaf_count, 3)
            if left_data == 1 and right_data == 1:
                return _by_name(left_node, right_node)
            elif left_data == 1:
                return True if self.sortOrder() == Qt.DescendingOrder else False
            elif right_data == 1:
                return False if self.sortOrder() == Qt.DescendingOrder else True
            elif left_data == right_data:
                return _by_episodes(left_node, right_node)
            else:
                return left_data < right_data

    def pop_related_series(self, index):
        """Relays the method call to the source model.

        The relay is necessary, since the method is not part
        of a original Qt model. Does not alter the result.

        :param index: The proxy index to pass onto the source method.
        :type index: :class:`~.PySide.QtCore.QModelIndex`

        :returns: The return value of the method call on the source model.

        """
        return self.sourceModel().pop_related_series(self.mapToSource(index))

    def node_at(self, index):
        """Relays the method call to the source model.

        The relay is necessary, since the method is not part
        of a original Qt model. Does not alter the result.

        :param index: The proxy index to pass onto the source method.
        :type index: :class:`~.PySide.QtCore.QModelIndex`

        :returns: The return value of the method call on the source model.

        """
        return self.sourceModel().node_at(self.mapToSource(index))
