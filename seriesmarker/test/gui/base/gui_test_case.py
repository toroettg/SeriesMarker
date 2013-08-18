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

"""This file is part of SeriesMarker.

SeriesMarker is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 as
published by the Free Software Foundation.

SeriesMarker is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with SeriesMarker.  If not, see <http://www.gnu.org/licenses/>.

"""

from PySide.QtCore import Qt, QPoint
from PySide.QtGui import QApplication, QWidget, QCursor
from PySide.QtTest import QTest
import sys
import unittest


class GUITestCase(unittest.TestCase):

    DELAY = 750
    DELAY_TYPING = 50

    @classmethod
    def setUpClass(cls):
        if QApplication.instance() == None:
            cls.app = QApplication(sys.argv)


    def click(self, widget, target=QPoint(), double_click=False):
        self.move(widget, target)
        if double_click:
            QTest.mouseDClick(widget, Qt.MouseButton.LeftButton, pos=target, delay=self.DELAY)
        else:
            QTest.mouseClick(widget, Qt.MouseButton.LeftButton, pos=target, delay=self.DELAY)

    def move(self, widget, target=QPoint()):
        QTest.mouseMove(widget, pos=target, delay=self.DELAY)

    def wait(self):
        QTest.mouseMove(QWidget(), pos=QCursor.pos(), delay=self.DELAY * 10)

    def type(self, widget, text):
        QTest.keyClicks(widget, text, delay=self.DELAY_TYPING)

    def keyhit(self, widget, key):
        QTest.keyClick(self.dialog.ui.search_text_field, key, delay=self.DELAY_TYPING)
