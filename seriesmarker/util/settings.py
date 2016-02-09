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

    def __init__(self):
        super().__init__()

        self.read(self._CONFIG_FILE, encoding="UTF-8")
        try:
            self.add_section("MainWindow")
        except DuplicateSectionError:
            pass

    def store(self):
        with open(self._CONFIG_FILE, mode="w",
                  encoding="UTF-8") as config_file:
            self.write(config_file)
        log.info(
            "Stored settings in '{}'.".format(config.dirs.user_config_dir))


settings = Settings()
