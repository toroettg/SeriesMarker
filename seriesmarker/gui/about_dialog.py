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

from PySide.QtCore import Slot, QUrl
from PySide.QtGui import QDialog, QDesktopServices
from seriesmarker.gui.resources.ui_about_dialog import Ui_AboutDialog
from seriesmarker.util.config import application_version


class AboutDialog(QDialog):
    """Displays a dialog with additional information about the application."""
    def __init__(self, parent=None):
        """Creates a new dialog instance.

        Also sets the displayed application version information, according
        to the settings in the :mod:`.config` file.
        
        :param parent: The parent widget of the dialog.
        :class parent: :class:`PySide.QtGui.QWidget`
        
        """
        super(AboutDialog, self).__init__(parent)

        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)

        concat_version = "{} {}".format(self.ui.version.text(), application_version)

        self.ui.version.setText(concat_version)

    @Slot()
    def on_donate_button_clicked(self):
        """Opens the donation link in a browser of the operating system."""
        QDesktopServices.openUrl(QUrl("https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=TDQAJJ74TTYGJ", QUrl.StrictMode))
