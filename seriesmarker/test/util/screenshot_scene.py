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

import unittest

from PySide.QtGui import QTableView
from PySide.QtTest import QTest

from seriesmarker.gui.search_dialog import SearchDialog
from seriesmarker.test.database.base.persitent_db_test_case import \
    PersistentDBTestCase
from seriesmarker.test.gui.base.main_window_test import MainWindowTest
from seriesmarker.test.util.screenshot import _Screenshot


class ScreenshotScene(MainWindowTest, PersistentDBTestCase):
    """Pseudo test to create scenes to take screenshots from.

    .. note::

        Should not be run with regular test cases.

    """

    @classmethod
    def setUpClass(cls):
        MainWindowTest.setUpClass()
        PersistentDBTestCase.setUpClass()

        from seriesmarker.persistence.database import db_init

        db_init()

    def setUp(self):
        super().setUp()
        self.screenshot = _Screenshot(self.id(), self.window.frameGeometry())

    def _create_dialog(self, parent=None):
        """Creates an :class:`.SearchDialog` instance, independent from the
        :class:`.MainWindow`.

        :param parent: The parent widget of the dialog.
        :type parent: :class:`PySide.QtGui.QWidget`

        :return: The dialog instance.
        """
        dialog = SearchDialog(parent)
        dialog.show()
        QTest.qWaitForWindowShown(dialog)
        return dialog

    def _prefetch_series(self):
        results = []

        for search in ["House", "Game of Thrones", "Scrubs", "The X-Files",
            "How I met your mother"]:
            dialog = self._create_dialog()

            self.type(dialog.ui.search_text_field, search)
            self.click(dialog.ui.search_button)
            view = dialog.findChild(QTableView, "result_view")
            viewport = view.viewport()
            item = view.model().index(0, 1)
            item_rect = view.visualRect(item)
            self.click(viewport, item_rect.center())
            self.click(dialog.ui.ok_button)

            results.append(dialog.result_value())
        return results

    def test_01_introduction(self):
        """Takes the screenshots for the project website and readme file."""

        # Temporarily allow remote show updates.
        self.mock_patcher_show_update.stop()
        series = self._prefetch_series()
        self.mock_patcher_show_update.start()

        self.click_add_button(times=len(series), to_add=series)

        self.click(
                self.tree_view.header().viewport(),
                self.header_center(self.tree_view.header(), 0)
        )
        self.click(
                self.tree_view.header().viewport(),
                self.header_center(self.tree_view.header(), 0)
        )
        self.screenshot.take_screenshot(show_cursor=False)

        self.expand_series(2)
        self.select(2, 1)

        for episode in range(8):
            self.mark_episode(2, 1, episode)

        self.select(2, 1)

        target = self.find_click_target(2, 1, 11, offset=(30, 10))
        self.move(*target)
        self.move(*target)
        self.screenshot.take_screenshot()

        dialog = self._create_dialog(self.window)
        self.type(dialog.ui.search_text_field, "theory")
        self.click(dialog.ui.search_button)
        self.wait()
        view = dialog.findChild(QTableView, "result_view")
        viewport = view.viewport()
        item = view.model().index(0, 1)
        item_rect = view.visualRect(item)
        self.click(viewport, item_rect.center())
        self.move(dialog.ui.ok_button)
        self.screenshot.take_screenshot()
        self.click(dialog.ui.ok_button)

    def test_02_startup(self):
        """Takes a screenshot after the first application start."""
        self.screenshot.take_screenshot(show_cursor=False)


def get_suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ScreenshotScene))
    return suite


if __name__ == "__main__":
    unittest.main()
