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


class SettingsDecorator:
    """
    Class that allows access to a section of a specific `Settings` instance.

    .. note::

        Intended to be extended by subclasses.

    """

    def __init__(self, section):
        """
        Create a new decorator instance for the given settings section.

        Associate the instance with a `configparser.SectionProxy` for
        the given section.

        :param section: The section name to allow access to.
        :type section: str

        """
        super().__init__()
        self._section = settings.register_section(section)

    def store(self):
        """
        Delegate to the decorated method.

        .. seealso::

            `Settings.store`

        """
        self._section.parser.store()


class WindowSettings(SettingsDecorator):
    """Offers convenience methods to access window settings."""
    _MAXIMIZED = "maximized"
    _POSITION_X = "position.x"
    _POSITION_Y = "position.y"
    _SIZE_WIDTH = "size.width"
    _SIZE_LENGTH = "size.length"

    @property
    def maximized(self):
        """
        Property that indicates whether a window was set to maximize.

        When getting the property, retrieve the window's maximized state
        from the settings as boolean.

        When setting the property, convert the given value to a string
        and store it in the settings.

        :param value: The window's maximized state to store in the settings.
        :type value: bool
        :return: True if the window is set to maximize, False otherwise.
        :rtype: bool

        """
        return self._section.getboolean(self._MAXIMIZED, False)

    @maximized.setter
    def maximized(self, value):
        self._section[self._MAXIMIZED] = str(value)

    @property
    def position(self):
        """
        Property that indicates the position a window was set to.

        When getting the property, retrieve the window's x and y
        coordinates at the screen as a tuple of integers.

        When setting the property, convert the given values from a tuple
        of integers to string and store them in the settings.

        :param value: The window position to store in the settings.
        :type value: (int, int)
        :return: The position a window was set to.
        :rtype: (`int`, `int`)
        """
        x = self._section.getint(self._POSITION_X)
        y = self._section.getint(self._POSITION_Y)
        return x, y

    @position.setter
    def position(self, value):
        x, y = map(str, value)
        self._section[self._POSITION_X] = x
        self._section[self._POSITION_Y] = y

    @property
    def size(self):
        """
        Property that indicates the size a window was set to.

        When getting the property, retrieve the window's width and
        length from the settings as a tuple of integers.

        When setting the property, convert the given values from a tuple
        of integers to string and store them in the settings.

        :param value: The window size to store in the settings.
        :type value: (`int`, `int`)
        :return: The size a window was set to.
        :rtype: (`int`, `int`)

        """
        width = self._section.getint(self._SIZE_WIDTH)
        length = self._section.getint(self._SIZE_LENGTH)
        return width, length

    @size.setter
    def size(self, value):
        width, length = map(str, value)
        self._section[self._SIZE_WIDTH] = width
        self._section[self._SIZE_LENGTH] = length
