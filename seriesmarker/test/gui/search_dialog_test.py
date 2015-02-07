#==============================================================================
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 - 2015 Tobias Röttger <toroettg@gmail.com>
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

import unittest

from PySide.QtCore import Qt

from PySide.QtGui import QTableView
from PySide.QtTest import QTest

from seriesmarker.gui.search_dialog import SearchDialog

from seriesmarker.test.gui.base.gui_test_case import GUITestCase


class SearchDialogTest(GUITestCase):
    def setUp(self):
        self.dialog = SearchDialog()

        self.dialog.show()

        QTest.qWaitForWindowShown(self.dialog)

        self.assertEqual(self.dialog.ui.search_text_field.text(), "",
                         "Default Search Text is not empty")
        self.assertEqual(self.dialog.model.rowCount(), 0,
                         "Result model not cleared")

    def test_simple_search(self):
        self.type(self.dialog.ui.search_text_field, "how i")
        self.click(self.dialog.ui.search_button)

        self.assertEqual(self.dialog.model.rowCount(), 7,
                         "Search did not return expected results")
        self.assertEqual(self.dialog.model.data(self.dialog.model.index(0, 0)),
                         "How I Met Your Mother",
                         "First result not as expected")

    def test_search_by_keyhit(self):
        self.type(self.dialog.ui.search_text_field, "how i")
        self.keyhit(self.dialog.ui.search_text_field, Qt.Key_Enter);

        self.assertEqual(self.dialog.model.rowCount(), 7,
                         "Search did not return expected results")
        self.assertEqual(self.dialog.model.data(self.dialog.model.index(0, 0)),
                         "How I Met Your Mother",
                         "First result not as expected")

    def test_clear_on_new_search(self):
        self.type(self.dialog.ui.search_text_field, "how i")
        self.click(self.dialog.ui.search_button)

        self.assertEqual(self.dialog.model.rowCount(), 7,
                         "Search did not return expected results")

        self.click(self.dialog.ui.search_button)

        self.assertEqual(self.dialog.model.rowCount(), 7,
                         "Search did not clear model")

        self.click(self.dialog.ui.search_text_field)
        self.keyhit(self.dialog.ui.search_text_field, Qt.Key_End)
        for i in range(len(
                self.dialog.ui.search_text_field.text())):  # @UnusedVariable
            self.keyhit(self.dialog.ui.search_text_field, Qt.Key_Backspace)

        self.assertEqual(self.dialog.ui.search_text_field.text(), "",
                         "Emulated typing did not delete all characters")

        self.click(self.dialog.ui.search_button)

        self.assertEqual(self.dialog.model.rowCount(), 0,
                         "Search did not clear model")

    def test_reject(self):
        self.click(self.dialog.ui.cancel_button)

        self.assertEqual(self.dialog.result(), self.dialog.Rejected,
                         "Dialog did not reject")

    def test_accept(self):
        self.click(self.dialog.ui.ok_button)
        self.assertEqual(self.dialog.result(), self.dialog.Rejected,
                         "Dialog did accept without search or selection")
        self.assertEqual(self.dialog.result_value(), None,
                         "Accept without search changed result")

        self.type(self.dialog.ui.search_text_field, "how i met")
        self.click(self.dialog.ui.search_button)

        self.click(self.dialog.ui.ok_button)
        self.assertEqual(self.dialog.result(), self.dialog.Rejected,
                         "Dialog did accept without selection")
        self.assertEqual(self.dialog.result_value(), None,
                         "Accept without selection changed result")

        view = self.dialog.findChild(QTableView, "result_view")
        viewport = view.viewport()
        item = view.model().index(0, 1)
        itemRect = view.visualRect(item)
        self.click(viewport, itemRect.center())
        self.click(self.dialog.ui.ok_button)

        self.assertEqual(self.dialog.result(), self.dialog.Accepted,
                         "Dialog did not accept")
        self.assertEqual(self.dialog.result_value().SeriesName,
                         "How I Met Your Mother",
                         "Accept with selection did not return correct search result")

    def tearDown(self):
        QTest.mouseMove(self.dialog,
                        delay=2000)  # Emulates waiting, can be removed

        self.dialog.close()


def get_suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SearchDialogTest))
    return suite

if __name__ == "__main__":
    unittest.main()
