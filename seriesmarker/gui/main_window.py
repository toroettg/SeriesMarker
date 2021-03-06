# =============================================================================
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
# =============================================================================

import logging

from PySide.QtCore import Slot, QModelIndex, Qt, QCoreApplication
from PySide.QtGui import QMainWindow, QListView, QMessageBox, QIcon, \
    QHeaderView, QMenu

from seriesmarker.gui.about_dialog import AboutDialog
from seriesmarker.gui.model.episode_node import EpisodeNode
from seriesmarker.gui.model.season_node import SeasonNode
from seriesmarker.gui.model.series_node import SeriesNode
from seriesmarker.gui.model.sort_filter_proxy_model import SortFilterProxyModel
from seriesmarker.gui.model.tree_series_model import TreeSeriesModel
from seriesmarker.gui.resources.ui_main_window import Ui_MainWindow
from seriesmarker.gui.search_dialog import SearchDialog
from seriesmarker.net.tvdb import tvdb
from seriesmarker.persistence.database import db_get_series, db_add_series, \
    db_remove_series, db_commit
from seriesmarker.persistence.exception import EntityExistsException
from seriesmarker.persistence.factory.series_factory import SeriesFactory
from seriesmarker.util.settings import MainWindowSettings

log = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    """Displays the main application window."""

    def __init__(self, parent=None):
        """
        Create a new window instance.

        Initializes the different views and loads series information
        from the database into the view's models for displaying them.

        :param parent: The parent widget of the window.
        :type parent: :class:`PySide.QtGui.QWidget`

        :emphasis:`Extends` `.QMainWindow.__init__`

        """
        super().__init__(parent)

        self.settings = MainWindowSettings("MainWindow")

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action_about_qt.setIcon(
            QIcon(":/trolltech/qmessagebox/images/qtlogo-64.png")
        )
        self.ui.action_about.setMenu(self.ui.menuAbout)
        self.ui.menubar.setVisible(False)

        self.model = TreeSeriesModel()

        self.tree_proxy_model = SortFilterProxyModel()
        self.tree_proxy_model.setSourceModel(self.model)

        self.ui.tree_view.setModel(self.tree_proxy_model)
        self.ui.tree_view.sortByColumn(0, Qt.AscendingOrder)
        self.ui.tree_view.header().setResizeMode(QHeaderView.ResizeToContents)
        self.ui.tree_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tree_view.customContextMenuRequested.connect(
            self._handle_context_menu
        )

        self.ui.list_view.setModel(self.model)
        self.ui.list_view.setMouseTracking(True)

    @Slot()
    def on_action_add_triggered(self):
        """Displays a :class:`.SearchDialog` to add a new series to the database."""
        dialog = SearchDialog(self)

        if dialog.exec_() == SearchDialog.Accepted:
            pytvdb_show = dialog.result_value()

            series = SeriesFactory().new_series(pytvdb_show)

            try:
                db_add_series(series)
                self.model.add_item(series)
            except EntityExistsException:
                log.warning("Series '{name}' already exists, "
                            "ignoring add request".format(
                    name=series.series_name))

    @Slot()
    def on_action_remove_triggered(self):
        """Removes a series from the database and the views."""
        index = self.tree_proxy_model.mapToSource(
            self.ui.tree_view.currentIndex())

        series = self.model.pop_related_series(index)

        if series is not None:
            db_remove_series(series)

    @Slot()
    def on_action_update_triggered(self):
        """Sequentially updates all series in the database.

        .. todo::
            Update should also recognize/announce updated episodes.

        """
        series_factory = SeriesFactory()

        for series in db_get_series():
            log.info("Updating series '{}'".format(series.series_name))

            tvdb_show = tvdb.get_series(series.id, "en", cache=False)
            tvdb_show.update()
            tvdb_show.load_banners()
            series_factory.new_series(tvdb_show, update=series)
            db_commit()

            series_index = self.model.index_of(series)

            for removed_season in series_factory.removed:
                season_index = self.model.index_of(
                    removed_season,
                    series_index
                )
                season_row = self.model.node_at(season_index).child_index()
                self.model.removeRow(season_row, series_index)
                log.info("  Removed season {} from series '{}'".format(
                    removed_season.season_number, series.series_name))

            for added_season in series_factory.added:
                self.model.add_item(added_season, series_index)
                log.info(
                    "  Added season {}".format(added_season.season_number))

            for updated_season in series_factory.updated:
                season, added_episodes, removed_episodes = updated_season

                log.info(
                    "  Updated season {} (Episodes added: {}, removed: {})".format(
                        season.season_number, len(added_episodes),
                        len(removed_episodes)))

                season_index = self.model.index_of(season, series_index)

                for removed_episode in removed_episodes:
                    episode_index = self.model.index_of(removed_episode,
                                                        season_index)
                    episode_row = self.model.node_at(
                        episode_index).child_index()
                    self.model.removeRow(episode_row, season_index)
                for added_episode in added_episodes:
                    self.model.add_item(added_episode, season_index)

            series_factory.reset()
            QCoreApplication.processEvents()

    @Slot(QModelIndex)
    def on_tree_view_clicked(self, index):
        """Changes the style of the list view according to context.

        The list view shows icons in portrait mode if a series or season
        is selected in the tree view. It changes to list mode if an
        episode has been selected.

        .. todo::

            Should change view only if next style differs from current one -
            needs to compare with previous selection.

        """
        if index.column() is not 0:
            index = self.tree_proxy_model.index(index.row(), 0, index.parent())

        index = self.tree_proxy_model.mapToSource(index)

        node = self.model.node_at(index)

        self.ui.list_view.setRootIndex(index)

        if isinstance(node, SeriesNode):
            self._enable_icon_mode()
        elif isinstance(node, SeasonNode):
            self._enable_list_mode()

    def _enable_list_mode(self):
        """Changes the style of the list view to list mode."""
        self.ui.list_view.setFlow(QListView.TopToBottom)
        self.ui.list_view.setWrapping(False)
        self.ui.list_view.setWordWrap(False)
        self.ui.list_view.setViewMode(QListView.ListMode)

    def _enable_icon_mode(self):
        """Changes the style of the list view to icon mode."""
        self.ui.list_view.setFlow(QListView.LeftToRight)
        self.ui.list_view.setWrapping(True)
        self.ui.list_view.setWordWrap(True)
        self.ui.list_view.setViewMode(QListView.IconMode)

    def _handle_context_menu(self, pos):
        index = self.ui.tree_view.indexAt(pos)
        if index.isValid():
            pos = self.ui.tree_view.viewport().mapToGlobal(pos)
            menu = QMenu()
            menu.addAction(self.ui.action_mark_watched)
            menu.addAction(self.ui.action_mark_unwatched)
            menu.addSeparator()
            menu.addAction(self.ui.action_remove)
            menu.exec_(pos)

    @Slot()
    def on_action_mark_watched_triggered(self):
        """Marks all episodes of the currently selected series as watched."""
        self.tree_proxy_model.setData(self.ui.tree_view.currentIndex(),
                                      Qt.Checked, role=Qt.CheckStateRole)

    @Slot()
    def on_action_mark_unwatched_triggered(self):
        """Marks all episodes of the currently selected series as unwatched."""
        self.tree_proxy_model.setData(self.ui.tree_view.currentIndex(),
                                      Qt.Unchecked, role=Qt.CheckStateRole)

    @Slot(QModelIndex)
    def on_list_view_entered(self, index):
        """Sets the tooltip of the list view.

        A tooltip is set, when the mouse hovers above an episode in
        the list view.

        :param index: The index of the item whose view has been entered.
        :type index: :class:`~.PySide.QtCore.QModelIndex`
        """
        node = self.model.node_at(index)

        if isinstance(node, EpisodeNode):
            # HTML-style fonts makes tooltips 'rich text',
            # which enables automatic word wrapping for them.
            self.ui.list_view.setToolTip(
                "<FONT COLOR=black>{}</FONT>".format(node.data.overview))

    @Slot()
    def on_list_view_viewportEntered(self):
        """Removes the tooltip from the list view.

        A tooltip is removed, when the mouse leaves the area of an
        episode in the list view.

        """
        self.ui.list_view.setToolTip("")

    @Slot()
    def on_action_about_triggered(self):
        """Displays an :class:`.AboutDialog` for additional information."""
        AboutDialog(self).exec_()

    @Slot()
    def on_action_home_triggered(self):
        """Restores the initial perspective of the application."""
        self.ui.list_view.setRootIndex(QModelIndex())
        self._enable_icon_mode()

    @Slot()
    def on_action_about_qt_triggered(self):
        """Displays a dialog with information about Qt."""
        QMessageBox.aboutQt(self)

    def showEvent(self, event):
        """
        Handle a request to show the main window.

        At first restore the window properties from the user
        settings. Then handle the event as usual.

        :param event: The event to handle.
        :type event: `.QtGui.QShowEvent`

        :emphasis:`Overrides` `.QWidget.showEvent`

        """
        previous_state = self.settings.state

        if previous_state == Qt.WindowNoState:
            width, length = self.settings.size
            x, y = self.settings.position

            if width and length:
                self.resize(width, length)

            if x and y:
                self.move(x, y)
        elif previous_state:
            # PySide / Qt4.8 unable to restore minimized window on Windows-OS.
            self.setWindowState(previous_state & ~Qt.WindowMinimized)

        previous_sort = self.settings.sort

        if None not in previous_sort:
            column, order = previous_sort

            self.ui.tree_view.sortByColumn(
                column,
                Qt.SortOrder(order)
            )


        event.accept()

    def closeEvent(self, event):
        """
        Handle a request to close the main window.

        At first store the current window properties to the user
        settings. Then handle the event as usual.

        .. note::

            Closing the main window terminates the application normally.

        :param event: The event to handle.
        :type event: `.QtGui.QCloseEvent`

        :emphasis:`Overrides` `.QWidget.closeEvent`.

        """
        pos = self.pos()
        size = self.size()

        self.settings.state = int(self.windowState())
        self.settings.position = pos.x(), pos.y()
        self.settings.size = size.width(), size.height()

        self.settings.sort = (
            self.ui.tree_view.header().sortIndicatorSection(),
            int(self.ui.tree_view.header().sortIndicatorOrder())
        )

        self.settings.store()

        event.accept()

    @Slot()
    def on_action_exit_triggered(self):
        self.close()
