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

import logging as log
import os
from configparser import ConfigParser, DuplicateSectionError

from seriesmarker.util import config


class Settings(ConfigParser):
    """Class to manage settings that are configurable by the end-user."""

    _CONFIG_FILE = os.path.join(config.dirs.user_config_dir,
                                "settings.ini")

    def load(self):
        """Read the settings from a predefined location."""
        loaded = self.read(self._CONFIG_FILE, encoding="UTF-8")

        for file in loaded:
            log.info("Loaded settings from '{}'.".format(file))

        if not loaded:
            log.info("No settings stored at '{}', using defaults.".format(
                self._CONFIG_FILE))

    def store(self):
        """Write the settings to a predefined location."""
        with open(self._CONFIG_FILE, mode="w",
                  encoding="UTF-8") as config_file:
            self.write(config_file)
        log.info("Stored settings at '{}'.".format(self._CONFIG_FILE))

    def register_section(self, section):
        """
        Add the given section to the settings unless it already exists.

        :param section: The name of the section to add.
        :type section: str

        :return: The registered section.

        """
        try:
            self.add_section(section)
            log.debug("Registered section '{}'.".format(section))
        except DuplicateSectionError:
            pass

        return self[section]


settings = Settings()
