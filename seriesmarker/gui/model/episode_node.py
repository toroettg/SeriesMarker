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
from PySide.QtGui import QIcon

from seriesmarker.gui.model.tree_node import TreeNode


class EpisodeNode(TreeNode):
    """Provides data for display about an :class:`.Episode`."""

    def __init__(self, episode, parent=None):
        """Initializes the node.

        :param episode: The episode to be handled by the node.
        :type episode: :class:`.Episode`
        :param parent: The season node the episode belongs to.
        :type parent: :class:`.SeasonNode`

        """
        super().__init__(episode, parent)

    def name(self):
        """Returns a string representation of the node's data.

        :returns: The title of the episode related to the node.

        :emphasis:`Overrides` :py:meth:`.TreeNode.name`

        """
        return self.data.episode_name

    def check(self, state, origin=None):
        """Sets the checked state of the node.

        The checked state indicates whether or not an episode has been
        watched. When the state is set, the tree of the node is
        traversed upwards to its root, and the cached count of watched
        episodes in its branch is updated accordingly.

        :param state: The checked state to set.
        :type state: :class:`bool`
        :param origin: The node which initiated the check call. Used to
            determine when to traverse the tree upward.
        :type: :class:`.TreeNode`

        :returns: The node itself, wrapped in a tuple, if only an episode has
            been checked. If a series or season has been checked, a tuple of a number and
            a reference is returned. The number indicates whether the episode
            has been checked (=1), unchecked (-1), or hasn't been altered (0).
            The reference points either to the episode itself, or is None, to
            indicate that no change has happened.

        .. seealso::

            :py:meth:`.TreeNode.check`

        :emphasis:`Overrides` :py:meth:`.TreeNode.check`

        """
        changed = None
        total_changed = 0

        if state != self.data.extra.watched:
            self.data.extra.watched = state
            changed = self
            total_changed = 1 if state else -1

        if changed and origin is None:
            parent = self.parent
            while parent and parent._checked_cache is not None:
                parent._checked_cache += total_changed
                parent = parent.parent
            return (self,)
        elif changed and origin is not None:
            return total_changed, self
        else:
            return 0, None

    def checked(self):
        """Gets the checked state of the node.

        :returns: True if the episode is marked as watched,
            otherwise False.

        :emphasis:`Overrides` :py:meth:`.TreeNode.checked`

        """
        return self.data.extra.watched

    def decoration(self, index):
        """Retuns a snapshot image of the episode the node is related to.

        :param index: The index of the node, whose decoration was requested.
        :type index: :class:`~.PySide.QtCore.QModelIndex`

        .. todo::

            Should return a pixmap of an episode snapshot image instead of
            a default icon. By solving the todo, this method becomes
            obsolet and needs to be deleted - use/override
            :py:meth:`.DecoratedNode.banner_url` instead.

        :returns: The :class:`.PySide.QtGui.QPixmap` containing the episode snapshot.

        :emphasis:`Overrides` :py:meth:`.DecoratedNode.decoration`

        """
        return QIcon(
            ":/trolltech/styles/commonstyle/images/viewdetailed-128.png")
