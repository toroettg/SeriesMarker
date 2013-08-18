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

"""This module provides general information about SeriesMarker.

The information is used in the application itself at runtime,
as well as in the distribution process.

.. note::

    This configuration file is not meant to be edited by the end-user.

"""

import logging
from appdirs import AppDirs

application_name = "SeriesMarker"  #: The application's name.
application_author = "toroettg"  #: The application's author.
application_author_name = "Tobias Roettger"  #: The author's name.
application_author_email = "toroettg@gmail.com"  #: The author's contact information.

application_version = "0.0.3"  #: The current version of the application.

application_description = "A TV series browser and tracker application."  #: A short description of the application.

application_url = "http://toroettg.github.io/SeriesMarker"  #: The project-website of the application.

application_license = "GNU GPLv3"  #: The license, under which the application is distributed.

application_dependencies = ['pytvdbapi', 'PySide', 'appdirs', 'SQLAlchemy']  #: The required dependencies of the application.

dirs = AppDirs(application_name, application_author)  #: Defines platform-independent directories, used by the application.

loglevel = logging.INFO  #: The default log level (=INFO) of the application.

