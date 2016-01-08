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
from PySide.QtCore import Qt
from PySide.QtGui import QSplashScreen, QPixmap


class SplashScreen(QSplashScreen):
    """Creates a splash screen to display at application start."""

    def __init__(self):
        super().__init__(
            QPixmap(":/misc/icons/SplashScreen.png"),
            Qt.WindowStaysOnTopHint
        )

        self.setCursor(Qt.BusyCursor)
        self.show()

    def showMessage(self, message):
        """Displays a given message on the splash screen.

        :param message: The message to display on the splash screen.
        :type message: string

        """
        super().showMessage(message, Qt.AlignBottom | Qt.AlignRight)