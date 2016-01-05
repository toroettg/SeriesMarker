# ==============================================================================
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
# ==============================================================================

from bisect import bisect
import logging
from enum import IntEnum

from PySide.QtCore import QAbstractItemModel, QModelIndex, Qt

from PySide.QtGui import QFont

from seriesmarker.gui.model.episode_node import EpisodeNode
from seriesmarker.gui.model.season_node import SeasonNode
from seriesmarker.gui.model.series_node import SeriesNode
from seriesmarker.gui.model.tree_node import TreeNode
from seriesmarker.persistence.database import db_commit
from seriesmarker.persistence.model.episode import Episode
from seriesmarker.persistence.model.season import Season
from seriesmarker.persistence.model.series import Series

logger = logging.getLogger(__name__)


class Column(IntEnum):
    """Convenience enumeration of columns used by :class:`.TreeSeriesModel`"""
    SERIES = 0
    EPISODE = 1
    PROGRESS = 2


class TreeSeriesModel(QAbstractItemModel):
    """This model is used to display series data (including seasons and
    episodes) in a :class:`.MainWindow`.

    The model stores data in a tree structure, using :class:`.TreeNode`
    and derived classes as nodes in it. Those nodes contain items (series,
    seasons and episodes), which contain the actual data to display.

    """

    def __init__(self, parent=None):
        """Initializes the model with a given parent.

        :param parent: The parent of the model.
        :type parent: :class:`.PySide.QtCore.QObject`

        """
        super().__init__(parent)
        self.root = TreeNode("Series")

    def headerData(self, section, orientation, role):
        """Defines the header data displayed in the GUI.

        :param section: Describes the column to get the header data for.
        :type section: :class:`int`
        :param orientation: Determines for which orientation of the header
            data should be get.
        :type orientation: :class:`PySide.QtCore.Qt.Orientation`
        :param role: Determines the kind of data to get from the model.
        :type role: :class:`int`

        :returns: The header caption for the given section as string for
            :class:`.Qt.DisplayRole`.
        :returns: :class:`.PySide.QtCore.Qt.AlignCenter` for
            :class:`.Qt.TextAlignmentRole`.
        :returns: None for orientations other than :class:`.Qt.Horizontal`.

        :emphasis:`Overrides` :meth:`.QAbstractItemModel.headerData`

        """
        if orientation == Qt.Horizontal:
            if role == Qt.DisplayRole:
                if section == Column.SERIES:
                    return self.root.name()
                elif section == Column.EPISODE:
                    return "Episodes"
                elif section == Column.PROGRESS:
                    return "Progress"
            elif role == Qt.TextAlignmentRole:
                return Qt.AlignCenter

        return None

    def data(self, index, role=Qt.DisplayRole):
        """Returns the data stored under the given role at a given index.

        :param index: Describes the node of the model to get data from.
        :type index: :class:`~.PySide.QtCore.QModelIndex`
        :param role: Determines the kind of data to get from the node.
        :type role: :class:`int`

        :returns: The string representation of the :class:`.TreeNode`
            at the given index for :class:`.Qt.DisplayRole`.
        :returns: The node at the given index itself for :class:`.Qt.UserRole`.
        :returns: The :py:meth:`~.DecoratedNode.decoration` of the node
            at the given index for :class:`.Qt.DecorationRole`.
        :returns: The :class:`.Qt.CheckState` representing the
            :py:meth:`~.TreeNode.checked` state of the node at the given index
            for :class:`.Qt.CheckedStateRole`.
        :returns: The text alignment to use for the string representation of
            the node at the given index for :class:`.Qt.TextAlignmentRole`.
        :returns: A monospace-family :class:`.PySide.QtGui.QFont` for column 1
            and 2 for :class:`.Qt.FontRole`.
        :returns: None for an invalid index or other roles.

        :emphasis:`Overrides` :meth:`.QAbstractItemModel.data`

        """
        if index.isValid():
            node = self.node_at(index)
            column = index.column()

            if role == Qt.DisplayRole:
                episodes = node.leaf_count
                watched = node.checked_count

                if column == Column.SERIES:
                    return node.name()
                elif column == Column.EPISODE:
                    if isinstance(node, SeriesNode):
                        return "{:3} / {: <3}".format(watched, episodes)
                    else:
                        return episodes
                elif column == Column.PROGRESS:
                    return "{:.1%}".format(watched / episodes)
            elif role == Qt.UserRole:
                return node
            elif role == Qt.DecorationRole:
                return node.decoration(index)
            elif role == Qt.CheckStateRole:
                state = node.checked()
                if state == True:
                    return Qt.Checked
                elif state == False:
                    return Qt.Unchecked
                else:
                    return None
            elif role == Qt.FontRole:
                if column == Column.EPISODE:
                    return QFont("Monospace")
            elif role == Qt.TextAlignmentRole:
                if isinstance(node, EpisodeNode):
                    return Qt.AlignLeft
                else:
                    return Qt.AlignCenter
        return None

    def setData(self, index, value, role=Qt.EditRole):
        """Sets the given value of the given role at the given index.

        This method is called whenever an episode is marked
        as (un)watched in the GUI. It then toggles the watched state
        of the corresponding :class:`.Episode`.

        This method is also called whenever a banner was loaded to set
        a :class:`.PySide.QtGui.Pixmap` as the node's decoration and
        refresh the views afterwards.

        :param index: The position to set the value at.
        :type index: :class:`~.PySide.QtCore.QModelIndex`
        :param value: Value to be set at given index: :class:`Qt.CheckState`
            for :class:`Qt.CheckStateRole`, :class:`.PySide.QtGui.Pixmap`
            for :class:`Qt.DecorationRole`.
        :type value: :class:`object`
        :param role: Determines the kind of data to set for the item.
        :type role: :const:`.PySide.QtCore.Qt.ItemDataRole`

        :returns: True if successful, otherwise False.

        :emphasis:`Overrides` :py:meth:`.QAbstractItemModel.setData`

        .. todo::
            Update of CheckState / progress kinda ugly, may be done in
            check(value), but needs reference to index and model - add
            reference to each node? Example: ``for change in changes:
            self.dataChanged.emit(change.get_index())``

        .. todo::
            After upgrade to QT5, use SignalSpy in test case to check if only
            changes are emitted if there was really a change after checking.
        """
        node = self.node_at(index)
        if role == Qt.CheckStateRole:
            if value == Qt.Checked:
                value = True
            elif value == Qt.Unchecked:
                value = False
            else:
                value = None

            changes = node.check(value)

            try:
                next(item for item in changes if item)
            except StopIteration:
                # Filter seasons without changes ([] in changes) for early exit
                return False

            db_commit()

            def notify_change(index):
                node = index.internalPointer()
                episode_index = self.createIndex(index.row(), Column.EPISODE,
                                                 node)
                progress_index = self.createIndex(index.row(), Column.PROGRESS,
                                                  node)
                self.dataChanged.emit(episode_index, progress_index)

            def traverse_down(item, index):
                if isinstance(item, tuple) and item:
                    for pos, value in enumerate(item):
                        traverse_down(value, index.child(pos, 0))
                    notify_change(index)

            def traverse_up(node, index):
                if node is not self.root:
                    notify_change(index)
                    traverse_up(node.parent, index.parent())

            traverse_down(changes, index)
            traverse_up(node.parent, index.parent())
            return True

        elif role == Qt.DecorationRole:
            node.banner_loaded(value)
            self.dataChanged.emit(index, index)
            return True

        else:
            return False

    def index(self, row, column, parent=QModelIndex()):
        """Returns the index of the item at the given row
        and column of the given parent.

        :param row: The row of the item to get an index for.
        :type row: :class:`int`
        :param column: The column of the item to get an index for.
        :type column: :class:`int`
        :param parent: The parent index of the item to get an index for.
        :type parent: :class:`~.PySide.QtCore.QModelIndex`

        :returns: The :class:`~.PySide.QtCore.QModelIndex` of the item
            or an invalid index if no item exists at the given row or
            colum under the given parent.

        :emphasis:`Overrides` :meth:`.QAbstractItemModel.index`

        """
        parent_node = self.node_at(parent)

        try:
            child_node = parent_node.child(row)
        except IndexError:
            return QModelIndex()
        else:
            return self.createIndex(row, column, child_node)

    def index_of(self, item, parent=QModelIndex()):
        """Looks up the index of the item's node in the model.

        The method checks the children of the parent, referred by the given
        index, if any of them contains the given item as data. If the search
        is successful, an index referring to the containing node is returned.

        :param item: Data contained in a :class:`.TreeNode` to look for.
        :type item: :class:`object`
        :param parent: The index referring to the parent
            node of the given item's node.
        :type parent: :class:`~.PySide.QtCore.QModelIndex`

        :returns: A :class:`~.PySide.QtCore.QModelIndex`, referring to
            the node which contains the given item if the search was
            successful, otherwise an invalid index.

        """
        parent_node = self.node_at(parent)

        try:
            row = next(
                index for index, child_node in enumerate(parent_node.children)
                if child_node.data is item)
        except StopIteration:
            return QModelIndex()
        else:
            return self.index(row, Column.SERIES, parent)

    def parent(self, child_index):
        """Returns the index referring to the parent of the node referred by
        the given index.

        :param child_index: The index of the item to get the parent index for.
        :type child_index: :class:`~.PySide.QtCore.QModelIndex`

        :returns: The :class:`~.PySide.QtCore.QModelIndex`, referring to the
            parent of the given index, or an invalid index if no parent exists.

        :emphasis:`Overrides` :meth:`.QAbstractItemModel.parent`

        """
        parent_node = self.node_at(child_index).parent

        if parent_node is None or parent_node is self.root:
            return QModelIndex()
        else:
            return self.createIndex(parent_node.child_index(), Column.SERIES,
                                    parent_node)

    def node_at(self, index):
        """Returns the node at the given index of the model.

        :param index: The index to get the associated node from.
        :type index: :class:`~.PySide.QtCore.QModelIndex`

        :returns: The :class:`.TreeNode` if a node is associated with the
            given index, otherwise the model's root node.

        """
        if index.isValid():
            return index.internalPointer()
        return self.root

    def add_item(self, item, parent_index=QModelIndex()):
        """Adds a given item to the model under the given parent.

        The item is wrapped in a matching :class:`.TreeNode`, depending
        on the item's type, before it's being added to the model.
        :class:`.Series` are being appended to the model's root node,
        :class:`.Season` and :class:`.Episode` are inserted at the
        proper position in their parent's children, so the display shows
        them in correct order (sorted by season respectively episode number).

        :param item: The item to add to the model.
        :type item: :class:`object`
        :param parent_index: The index of the node to add the item to.
        :type parent_index: :class:`~.PySide.QtCore.QModelIndex`

        """
        parent_node = self.node_at(parent_index)

        if isinstance(item, Series):
            cls = SeriesNode
            position = bisect([node.name() for node in parent_node.children],
                              item.series_name)
        elif isinstance(item, Season):
            cls = SeasonNode
            position = bisect(
                [node.data.season_number for node in parent_node.children],
                item.season_number)
        elif isinstance(item, Episode):
            cls = EpisodeNode
            position = bisect(
                [node.data.episode_number for node in parent_node.children],
                item.episode_number)
        else:
            return

        self.beginInsertRows(parent_index, position, position)
        parent_node.insert(position, cls(item, parent_node))
        self.endInsertRows()

    def removeRows(self, position, rows, parent=QModelIndex()):
        """Removes a number of nodes from a given parent, beginning
        at a given position.

        :param position: The index to start removing nodes from.
        :type position: :class:`int`
        :param rows: The number of nodes to remove from the parent.
        :type rows: :class:`int`
        :param parent: The parent to remove the rows from.
        :type parent: :class:`~.PySide.QtCore.QModelIndex`

        :returns: True if the nodes were successfully removed,
            otherwise False.

        :emphasis:`Overrides` :py:meth:`.QAbstractItemModel.removeRows`

        """
        parent_node = self.node_at(parent)

        self.beginRemoveRows(parent, position, position + rows - 1)
        for index in range(position, position + rows):
            parent_node.remove(index)
        self.endRemoveRows()
        return True

    def pop_related_series(self, index):
        """Removes the series to which a given index is associated with
        from the model, regardless which part of the series the index
        describes (i.e. which part was selected in the GUI).

        :param index: The index which describes the series to remove.
        :type index: :class:`~.PySide.QtCore.QModelIndex`

        :returns: The removed :class:`.Series` if successful, otherwise None.

        """
        node = self.node_at(index)
        if node == self.root:
            return None
        while node.parent != self.root:
            node = node.parent
        self.removeRow(node.child_index())
        return node.data

    def flags(self, index):
        """Describes the item flags for a given index.

        Item flags determine the behavior of an item in the GUI. By
        (de)activating different flags, the 'look and feel' of an item
        can be changed.

        :param index: The index referring to the item to get flags for.
        :type index: :class:`~.PySide.QtCore.QModelIndex`

        :returns: The flags :class:`.Qt.ItemIsUserCheckable` and
            :class:`.Qt.ItemIsUserEnabled` for :class:`.TreeNode`
            types that implement :py:meth:`~.TreeNode.checked`.
        :returns: The flag :class:`.Qt.ItemIsEnabled` otherwise.

        :emphasis:`Overrides` :py:meth:`.QAbstractItemModel.flags`

        """
        item = self.node_at(index)

        if item.checked() is not None:
            return Qt.ItemIsUserCheckable | Qt.ItemIsEnabled
        else:
            return Qt.ItemIsEnabled

    def rowCount(self, parent=QModelIndex()):
        """Returns the number of rows (nodes) under the given parent.

        :param parent: The parent to return the number of rows for.
        :type parent: :class:`~.PySide.QtCore.QModelIndex`

        :returns: The number of :class:`.TreeNode` added to the model as
            children of the given parent.

        :emphasis:`Overrides` :py:meth:`.QAbstractItemModel.rowCount`

        """
        return self.node_at(parent).child_count()

    def columnCount(self, parent=QModelIndex()):
        """Describes the number of columns the model is using.

        :param parent: The parent to return the number of columns for.
        :type parent: :class:`~.PySide.QtCore.QModelIndex`

        :returns: The number of columns.

        :emphasis:`Overrides` :py:meth:`.QAbstractItemModel.columnCount`

        """
        return 3
