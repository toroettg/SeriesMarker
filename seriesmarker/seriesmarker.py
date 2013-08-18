#==============================================================================
# -*- coding: utf-8 -*-
# 
# Copyright (C) 2013 Tobias Röttger <toroettg@gmail.com>
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

from PySide.QtGui import QApplication
from logging.handlers import RotatingFileHandler
from seriesmarker.gui.main_window import MainWindow
from seriesmarker.persistence.database import db_init
from seriesmarker.util import config
import logging
import os
import sys

def main():
    """Main entry of program.
    
    Initializes logging, database access, the Qt framework,
    and displays the main window to the user.
    
    """
    _init_logging()

    db_init()

    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    sys.exit(app.exec_())

def _init_logging(loglevel=config.loglevel):
    """Initializes logging with the given log level, default as specified by the configuration file.

    .. seealso:: :mod:`.config`

    :param loglevel: The level of logging to use.
    
    """
    if not os.path.exists(config.dirs.user_log_dir):
        os.makedirs(config.dirs.user_log_dir)

    log_path = os.path.join(config.dirs.user_log_dir, config.application_name + ".log")

    logging.basicConfig(level=loglevel, format="[%(levelname)-8s] %(module)-15s - %(message)s")

    file_handler = RotatingFileHandler(log_path, maxBytes=5 * 1024 * 1024, backupCount=1)
    file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)-8s] %(name)-40s - %(message)s"))
    file_handler.setLevel(loglevel)

    logging.getLogger("pytvdbapi").setLevel(logging.INFO)
    logging.getLogger().addHandler(file_handler)

    logging.getLogger("sqlalchemy").addHandler(file_handler)

