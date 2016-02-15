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

import os
import unittest

from seriesmarker.test.core.base.application_test_case import \
    ApplicationTestCase
from seriesmarker.test.core.base.core_test_case import AppDirsMock


class DirectoryTest(ApplicationTestCase):
    """Checks the creation of directories at application start."""

    def setUp(self):
        super().setUp()

        dirs = AppDirsMock()

        self.dirs = {
            "Database": dirs.user_data_dir,
            "Settings": dirs.user_config_dir,
            "Log":      dirs.user_log_dir,
            "Cache":    dirs.user_cache_dir
        }

    def _check_directories(self, expected, msg):
        for description, path in self.dirs.items():
            self.assertEqual(
                expected,
                os.path.exists(path),
                msg.format(description)
            )

    def test_01_directory_creation(self):
        """Tests creation of paths at application start up."""

        self._check_directories(
            False,
            "{} directory should not exist before application start."
        )

        self.run_main()

        self._check_directories(
            True,
            "{} directory should exist after application start."
        )

    def test_02_directory_recreation(self):
        """Tests if errors are raised if directories already exist."""
        self._check_directories(
            True,
            "{} directory should exist before second application start."
        )

        self.run_main()


def get_suit():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DirectoryTest))
    return suite


if __name__ == "__main__":
    unittest.main()
