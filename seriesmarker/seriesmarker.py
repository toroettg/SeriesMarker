# ==============================================================================
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
# ==============================================================================

from logging.handlers import RotatingFileHandler
import logging
import os
import sys

from PySide.QtGui import QApplication

from seriesmarker.gui.main_window import MainWindow
from seriesmarker.gui.splash_screen import SplashScreen
from seriesmarker.persistence.database import db_init, db_get_series
from seriesmarker.util import config


def main():
    """Main entry of program.

    Initializes logging, database access, the Qt framework,
    and displays the main window to the user.

    .. todo::
        Instead of adding each series sequentially, the model could be
        expanded with a method to add multiple series, which
        could speed up the application's start.

    """
    _init_logging()

    app = QApplication(sys.argv)

    splash_screen = SplashScreen()

    splash_screen.showMessage("Initializing database")
    db_init()

    splash_screen.showMessage("Loading Series")
    window = MainWindow()

    for series in db_get_series():
        splash_screen.showMessage("Loading {}".format(series.series_name))
        window.model.add_item(series)

    window.show()
    splash_screen.finish(window)

    sys.exit(app.exec_())


def _init_logging(loglevel=config.loglevel):
    """Initializes logging with the given log level, default as
    specified by the configuration file.

    .. seealso:: :mod:`.config`

    :param loglevel: The level of logging to use.

    """
    if not os.path.exists(config.dirs.user_log_dir):
        os.makedirs(config.dirs.user_log_dir)

    log_path = os.path.join(config.dirs.user_log_dir,
                            config.application_name + ".log")

    logging.basicConfig(level=loglevel,
                        format="[%(levelname)-8s] %(module)-15s - %(message)s")

    file_handler = RotatingFileHandler(log_path, maxBytes=5 * 1024 * 1024,
                                       backupCount=1)
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s [%(levelname)-8s] %(name)-40s - %(message)s"))
    file_handler.setLevel(loglevel)

    logging.getLogger("pytvdbapi").setLevel(logging.INFO)
    logging.getLogger().addHandler(file_handler)

    logging.getLogger("sqlalchemy").addHandler(file_handler)

    def log_uncaught_exception(*exception_info):
        logging.critical("Unhandled exception:\n\n", exc_info=exception_info)

    sys.excepthook = log_uncaught_exception

