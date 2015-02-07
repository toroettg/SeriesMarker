#!/usr/bin/python

#==============================================================================
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 - 2015 Tobias Röttger <toroettg@gmail.com>
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

from glob import glob
from os.path import basename, splitext
import os

RESOURCE_PATH = "../resources/"
OUTPUT_PATH = "../seriesmarker/gui/resources/"

def main():
    print("Processing ui-files:")
    for filepath in glob("%s%s" % (RESOURCE_PATH, "*.ui")):
        filename = splitext(basename(filepath))[0]
        output_filepath = "%s%s%s%s" % (OUTPUT_PATH, "ui_", filename, ".py")

        command = "pyside-uic --from-imports -o %s %s" % (output_filepath, filepath)

        os.system(command)

        print("    generated '%s'" % output_filepath)

    print("Processing rc-files:")
    for filepath in glob("%s%s" % (RESOURCE_PATH, "*.qrc")):
        filename = splitext(basename(filepath))[0]
        output_filepath = "%s%s%s" % (OUTPUT_PATH, filename, "_rc.py")

        command = "pyside-rcc -py3 -o %s %s" % (output_filepath, filepath)

        os.system(command)

        print("    generated '%s'" % output_filepath)

if __name__ == '__main__':
    main()
    print("done")
