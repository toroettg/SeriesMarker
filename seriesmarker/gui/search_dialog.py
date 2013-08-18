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

from PySide.QtCore import Slot, Qt
from PySide.QtGui import QDialog, QHeaderView
from seriesmarker.gui.model.search.search_model import SearchModel
from seriesmarker.gui.model.search.search_node import SearchNode
from seriesmarker.gui.resources.ui_search_dialog import Ui_Dialog
from seriesmarker.net.banner_loader import banner_loader
from seriesmarker.net.tvdb import tvdb
from PySide.QtCore import QCoreApplication

class SearchDialog(QDialog):
    """Displays a dialog to search for series."""

    def __init__(self, parent=None):
        """
        Creates a new dialog instance.
        
        :param parent: The parent widget of the dialog.
        :class parent: :class:`PySide.QtGui.QWidget`
        
        """
        super(SearchDialog, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.model = SearchModel()

        self.ui.result_view.setModel(self.model)
        self.ui.result_view.horizontalHeader().setResizeMode(1, QHeaderView.ResizeToContents)
        self.ui.result_view.horizontalHeader().setResizeMode(0, QHeaderView.Stretch)

        self._pytvdb_show = None

    @Slot()
    def on_search_button_clicked(self):
        """Performs the search for series.
                    
        Called whenever a search is triggered. Gets a search string from
        the dialog's text field and uses the :mod:`.tvdb` module to retrieve
        matching series. Results are being added to the dialog's model for
        displaying them.
        
        """
        search = tvdb.search(self.ui.search_text_field.text(), "en")

        self.model.clear()

        for show in search:
            show._load_banners()
            self.model.add_node(SearchNode(show))
            QCoreApplication.processEvents()

    @Slot()
    def accept(self):
        """Picks the result of the search.
        
        Called whenever the dialog should accept a result. The result is the
        latest selected series by the user. For that series, additional data
        is loaded from TheTVDB and stored for further usage.
        
        .. todo ::
        
            Accept button of SearchDialog should be disable while search is
            ongoing, or no valid result has been selected yet.
            
        """
        index = self.ui.result_view.currentIndex()

        # TODO disable OK button if no valid index is selected or show popup-information
        if index.isValid():
            self._pytvdb_show = self.model.data(index, role=Qt.UserRole)
            self._pytvdb_show.update()  # TODO load update in parallel
            super().accept()

    def result_value(self):
        """Passes the final result of the search.
        
        :returns: The :class:`.pytvdbapi.api.Show` that was selected.
        
        .. todo::
        
            Method may be omitted in favor of public attribute if
            :mod:`unittest.mock` offers a way to set it for testing. 
        
        """
        return self._pytvdb_show

