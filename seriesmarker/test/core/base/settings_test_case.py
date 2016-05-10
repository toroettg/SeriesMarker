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
import re

from seriesmarker.test.core.base.application_test_case import \
    ApplicationTestCase
from seriesmarker.util.settings import settings


class SettingsTestCase(ApplicationTestCase):
    """Base class for tests related to the handling of end-user settings."""

    def check_settings_file_contains(self, lines, section=None):
        """Test if a list of lines is included in the settings file.

        If a section is given, the check is limited to that section name.

        :param lines: The lines to check for.
        :type lines: [str]
        :param section: The section name to inspect.
        :type section: str

        """
        with open(settings._CONFIG_FILE) as file:
            content = file.read()

            if section:
                start = content.find("[{}]".format(section))
                end = content.find("[", start+1)
                content = content[start:end]

        self.assertIn(
            "\n".join(lines),
            content
        )

    def run_main(self):
        """
        Ensure the main window is displayed after executing the application.

        :emphasis: `Extends` `.ApplicationTestCase.run_main`

        """
        super().run_main()
        self.waitForWindow()

    def reset_window_state(self):
        """Reset the settings' stored window state."""
        self.window.setWindowState(Qt.WindowNoState)
