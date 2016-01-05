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

import unittest

from seriesmarker.test.gui import search_dialog_test, story_test, \
    sorting_test, context_menu_test


def get_suit():
    gui_suites = unittest.TestSuite()

    gui_suites.addTest(search_dialog_test.get_suit())
    gui_suites.addTest(story_test.get_suit())
    gui_suites.addTest(sorting_test.get_suit())
    gui_suites.addTest(context_menu_test.get_suit())

    return gui_suites


def load_tests(loader, tests, pattern):
    """Enables (graphical) unit testing in PyDev."""
    return get_suit()


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(get_suit())
