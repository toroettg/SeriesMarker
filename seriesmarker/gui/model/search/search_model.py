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

from PySide.QtCore import QAbstractTableModel, QModelIndex, Qt
from seriesmarker.gui.model.search.search_node import SCALE_SIZE

import logging

logger = logging.getLogger(__name__)

class SearchModel(QAbstractTableModel):
    """This model is used to display search results in a :class:`.SearchDialog`."""
    def __init__(self, parent=None):
        """Initializes the model.
        
        :param parent: The parent of the model.
        :type parent: :class:`.PySide.QtCore.QObject`
        
        """
        super().__init__(parent)
        self._node_list = []

    def node_at(self, index):
        """Returns the node at the given index of the model.
        
        :param index: The index to get the associated node from.
        :type index: :class:`.PySide.QtCore.QModelIndex`
        
        .. todo::
            The banner_loader may cause an access to an invalid index
            if another search with less results was initiated before
            all banner were loaded. Prevent the beginning of a new search
            before the last has been finished, or clear the banner_loader
            at clearing this model. Afterwards remove the warning log.
            Also remove the None check at setData of this model then.
        
        :returns: The :class:`.TreeNode` if a node is associated with the
            given index, otherwise None.
        
        """
        if index.isValid():
            try:
                return self._node_list[index.row()]
            except IndexError:
                logger.warning("Invalid index, probably started a new "
                    "search before the last finished (banner loading).")


    def add_node(self, node):
        """Appends a node to the end of the model.
        
        :param node: The node to add to the model.
        :type node: :class:`.SearchNode`
        
        """
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._node_list.append(node)
        self.endInsertRows()

    def clear(self):
        """Removes all nodes from the model."""
        self.removeRows(0, self.rowCount())

    def removeRows(self, position, rows, parent=QModelIndex()):
        """Removes a number of nodes from a given parent, beginning at a given position.
        
        :param position: The index to start removing nodes from.
        :type position: integer
        :param rows: The number of nodes to remove from the parent.
        :type rows: integer
        :param parent: The parent to remove the nodes from.
        :type parent: :class:`.PySide.QtCore.QModelIndex`
        
        :returns: True if the nodes were successfully removed, otherwise False.
        
        :emphasis:`Overrides` :py:meth:`.QAbstractItemModel.removeRows`
        
        """
        self.beginRemoveRows(parent, position, position + rows - 1)
        del self._node_list[position : position + rows]
        self.endRemoveRows()
        return True

    def data(self, index, role=Qt.DisplayRole):
        """Returns the data under the given role from the model at a given index.
        
        :param index: The position of the model to get data from.
        :type index: :class:`.PySide.QtCore.QModelIndex`
        :param role: Determines the kind of data to get from the model.
        :type role: integer
        
        :returns: The series name, at the given index,
            for :class:`PySide.QtCore.Qt.DisplayRole`.
        :returns: The :class:`.pytvdbapi.api.Show`, hold by the node at
            the given index, for :class:`PySide.QtCore.Qt.UserRole`.
        :returns: The :meth:`~DecoratedNode.decoration` of the node, at the given index,
            for :class:`PySide.QtCore.Qt.DecorationRole`.
        :returns: The desired column dimension, at the given index,
            for :class:`PySide.QtCore.Qt.SizeHintRole`.
            
        :emphasis:`Overrides` :py:meth:`.QAbstractItemModel.data`
        
        """
        if index.isValid():
            column = index.column()
            search_node = self.node_at(index)

            if role == Qt.DisplayRole:
                if column == 0:
                    return search_node.show.SeriesName
            elif role == Qt.UserRole:
                    return search_node.show
            elif role == Qt.DecorationRole:
                if column == 1:
                    return search_node.decoration(index)
            elif role == Qt.SizeHintRole:
                if column == 1:
                    return SCALE_SIZE
        return None

    def setData(self, index, value, role=Qt.DecorationRole):
        """Sets the given value of the given role at the given index.
                
        This method is also whenever a banner was loaded to set
        the node's decoration to a :class:`.PySide.QtGui.Pixmap`
        and refresh the views afterwards.
        
        :param index: The position to set the value at.
        :type index: :class:`.PySide.QtCore.QModelIndex`
        :param value: Value to be set at given index.
        :type value: :class:`.PySide.QtGui.Pixmap`
        :param role: Determines the kind of data to set for the item.
        :type role: integer
        
        :returns: True if successful, otherwise False.
        
        :emphasis:`Overrides` :py:meth:`.QAbstractItemModel.setData`
        
        """
        node = self.node_at(index)

        if node is None or role != Qt.DecorationRole:
            return False

        node.banner_loaded(value)
        self.dataChanged.emit(index, index)
        return True

    def rowCount(self, parent=QModelIndex()):
        """Returns the number of rows (nodes), currently added to the model.
        
        :param parent: The parent to return the number of rows for.
        :type parent: :class:`.PySide.QtCore.QModelIndex`
        
        :returns: The number of :class:`.SearchNode` added to the model.
        
        :emphasis:`Overrides` :py:meth:`.QAbstractItemModel.rowCount`
        
        """
        if parent.isValid():
            return 0
        else:
            return len(self._node_list)

    def columnCount(self, parent=QModelIndex()):
        """Describes the number of columns the model is using.
        
        :param parent: The parent to return the number of columns for.
        :type parent: :class:`.PySide.QtCore.QModelIndex`
        
        :returns: The number of columns.
        
        :emphasis:`Overrides` :py:meth:`.QAbstractItemModel.columnCount`
        
        """
        if parent.isValid():
            return 0
        else:
            return 2
