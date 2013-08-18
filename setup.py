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

import sys
import os

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "py2app":
        _setup_mac()
        return

    if len(sys.argv) > 1 and sys.argv[1] == "bdist_msi":
        specific_arguments = _setup_win()
    else:
        specific_arguments = _setup_src()

    def read_description():
        readme = open('README').read()

        try:
            changelog = open('CHANGELOG').read()
        except FileNotFoundError:
            changelog = ""

        return readme + changelog

    common_arguments = {
        "name": application_name,  # @UndefinedVariable
        "version": application_version,  # @UndefinedVariable

        "author": application_author_name,  # @UndefinedVariable
        "author_email": application_author_email,  # @UndefinedVariable
        "url": application_url,  # @UndefinedVariable

        "description": application_description,  # @UndefinedVariable
        "long_description": read_description(),

        "license": application_license,  # @UndefinedVariable
        "install_requires": application_dependencies,  # @UndefinedVariable
        "platforms": ["any"],
        "classifiers": _classifier
    }

    arguments = dict(common_arguments)
    arguments.update(specific_arguments)

    setup(**arguments)

def _setup_win():
    try:
        global setup
        from cx_Freeze import setup, Executable
        import pytvdbapi, PySide, appdirs, sqlalchemy
        from PySide.QtCore import QLibraryInfo
    except ImportError as e:
        raise SystemExit("Missing module '{}'. Please install required modules"
            " before trying to build a binary distribution.".format(e.name))

    qt_plugins_path = os.path.relpath(os.path.join(os.path.dirname(PySide.__file__), "plugins"))
    pytvdb_path = os.path.relpath(os.path.join(os.path.dirname(pytvdbapi.__file__)))

    include_files = [
        (os.path.join(pytvdb_path, "data"), "data"),
        (os.path.join(qt_plugins_path, "imageformats"), os.path.join("plugins", "imageformats")),
        (os.path.join("resources", "qt.conf"), "qt.conf")
    ]

    exe = Executable(
        script=_scripts[0],
        base='Win32GUI'
    )

    # http://msdn.microsoft.com/en-us/library/windows/desktop/aa371847(v=vs.85).aspx
    shortcut_table = [
        (
            "ProgramMenuShortcut",  # Shortcut
            "ProgramMenuFolder",  # Directory_
            "SeriesMarker",  # Name
            "TARGETDIR",  # Component_
            "[TARGETDIR]seriesmarker.exe",  # Target
            None,  # Arguments
            application_description,  # Description @UndefinedVariable
            None,  # Hotkey
            None,  # Icon
            None,  # IconIndex
            None,  # ShowCmd
            'TARGETDIR'  # WkDir
        ),
        (
            "DesktopShortcut",  # Shortcut
            "DesktopFolder",  # Directory_
            "SeriesMarker",  # Name
            "TARGETDIR",  # Component_
            "[TARGETDIR]seriesmarker.exe",  # Target
            None,  # Arguments
            None,  # Description
            None,  # Hotkey
            None,  # Icon
            None,  # IconIndex
            None,  # ShowCmd
            'TARGETDIR'  # WkDir
        )
    ]

    msi_data = {
        "Shortcut": shortcut_table
    }

    bdist_msi = {
        "data": msi_data,
        "upgrade_code": "{9C7EE7FA-93F8-46C7-8CBF-0806E5556C9E}"
    }

    options = {
        "include_files": include_files,
        "packages": _packages,
    }

    specific_arguments = {
        "executables": [exe],
        "options": {'build_exe': options, 'bdist_msi': bdist_msi}
    }

    return specific_arguments

def _setup_mac():
    _import_setuptools()
    from subprocess import call, check_output

    APP = _scripts
    DATA_FILES = []
    OPTIONS = {
        'argv_emulation': True,
        'optimize': '01',
        'includes': _modules,
        'packages': ['sqlalchemy'],
        'qt_plugins': ['imageformats']
    }

    setup(
        app=APP,
        data_files=DATA_FILES,
        options={'py2app': OPTIONS},
        setup_requires=['py2app'],
    )

    def post_build():
        print("Created distribution, applying additional scripts...")

        in_file = "seriesmarker"
        out_file = application_name  # @UndefinedVariable
        print("Renaming distribution file '{}.app' to '{}.app'.".format(in_file, out_file))
        call(["mv", "dist/{}.app".format(in_file), "dist/{}.app".format(out_file)])

        print("Determining codename of the operating system.")
        def determine_codename():
            osx_version = str(check_output(["sw_vers", "-productVersion"]), encoding="UTF-8")
            osx_version = osx_version[:osx_version.rfind('.')]
            if osx_version == "10.9":
                return "Mavericks"
            elif osx_version == "10.8":
                return "MountainLion"
            elif osx_version == "10.7":
                return "Lion"
            elif osx_version == "10.6":
                return "SnowLeopard"
            else:
                return "osx{}".format(osx_version)
        codename = determine_codename()

        in_file = out_file
        out_file = "SeriesMarker-{}-{}".format(application_version, codename)  # @UndefinedVariable
        out_path = "dist/{}.dmg".format(out_file)
        print("Creating symbolic link to '/Applications'.")
        call(["ln", "-s", "/Applications", "dist/Applications"])
        try:
            with open(out_path) as file:
                print("Detected old disk image, removing '{}'.".format(out_path))
                os.remove(out_path)
        except IOError:
            pass
        print("Creating disk image.")
        call(["hdiutil", "create", out_path, "-srcfolder" , "dist", "-volname", out_file, "-format", "UDZO"])
        print("Cleaning up symbolic link.")
        call(["rm", "dist/Applications"])
        print("[finished]")
    post_build()

def _setup_src():
    _import_setuptools()

    specific_arguments = {
        "packages": _modules,
        "scripts": _scripts,
    }

    return specific_arguments

_scripts = [
    'bin/seriesmarker'
]

_modules = [
    'seriesmarker',

    'seriesmarker.gui',
    'seriesmarker.gui.model',
    'seriesmarker.gui.model.search',
    'seriesmarker.gui.resources',

    'seriesmarker.net',

    'seriesmarker.persistence',
    'seriesmarker.persistence.model',
    'seriesmarker.persistence.factory',

    'seriesmarker.util'
]

_packages = [
    "sqlalchemy.dialects.sqlite",
    "PySide.QtSvg",  # QtSvg and QtXml ensure that the frozen software
    "PySide.QtXml"  # is able to display svg-icons.
]

_classifier = [
    'Development Status :: 3 - Alpha',
    'Environment :: X11 Applications',
    'Environment :: X11 Applications :: Qt',
    'Environment :: Win32 (MS Windows)',
    'Environment :: MacOS X',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Operating System :: POSIX :: Linux',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: MacOS :: MacOS X',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Topic :: Multimedia',
    'Topic :: Utilities '
]

def _import_setuptools():
    """Imports distribute_setup from the tools directory without
    the need of converting it to a python package.
    
    """
    global setup
    import inspect

    cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(
        os.path.split(inspect.getfile(inspect.currentframe()))[0], "tools")))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)

    try:
        from setuptools import setup
    except ImportError:
        from distribute_setup import use_setuptools
        use_setuptools()
        from setuptools import setup  # @UnusedImport


# Sets variables starting with 'application'; avoids the import of
# config.py in case dependencies are not available on system.
with open("seriesmarker/util/config.py") as f:
    content = [line.strip() for line in f.readlines()
        if line.startswith("application")]
    for assignment in content:
        exec(assignment)

if __name__ == "__main__":
    main()
