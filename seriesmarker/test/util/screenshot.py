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
import subprocess
import tempfile


class _Screenshot:
    """Utility class to take screenshots.

    .. note::

        Intended for internal usage only. Class is currently not portable.

    """
    COUNTER = 1

    def __init__(self, id, area):
        self.screenshot_dir_path = os.path.join(tempfile.gettempdir(),
                                                "screenshots",
                                                id)

        self.area = area

        if not os.path.exists(self.screenshot_dir_path):
            os.makedirs(self.screenshot_dir_path)

    def take_screenshot(self, show_cursor=True):
        screenshot_path = os.path.join(self.screenshot_dir_path,
                                       "{}.png".format(self.COUNTER))

        subprocess.call(
                [
                    "maim",
                    "--showcursor" if show_cursor else "",
                    "-g {}x{}+{}+{}".format(
                            self.area.width(),
                            self.area.height(),
                            self.area.x(),
                            self.area.y()
                    ),
                    screenshot_path
                ]
        )

        self.COUNTER += 1
