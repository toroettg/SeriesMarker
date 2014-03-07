#######################
Installing SeriesMarker
#######################

The easiest way to install SeriesMarker is to use the binary distribution
that matches your operating system. If an installer is not available for your
operating system, see :ref:`Building from Source <building_from_source>` for
guidelines how to build SeriesMarker for your system.


****************
Binary Installer
****************

This section describes how SeriesMarker can be installed on various
operating systems by using an installer.


Installer for Linux
===================


Arch Linux
----------

A `SeriesMarker Package`_ can be found in the `Arch User Repository (AUR)`_.
A simple way to install the package is by using the `AUR Helper`_ `Yaourt`_:

.. code-block:: bash

	$yaourt -S seriesmarker

The abovementioned command will resolve all necessary
:ref:`dependencies <dependencies>` and install them with SeriesMarker for
you (`Yaourt`_ will guide you through the process). Afterwards, you can
execute the application from a shell:

.. code-block:: bash

	$seriesmarker

You may now continue with the :ref:`User Guide` or explore the
software on your own.

.. note::
	The described method to install SeriesMarker will not fetch a binary of
	SeriesMarker, but compile it from source, along with any dependency not
	in the official Arch Linux repository, which may take some time. However,
	this method is more comfortable	than the
	:ref:`manual build process <building_on_linux>` and comes with the
	advantage of using the distribution's package management. It is
	therefore the recommended way to install SeriesMarker on Arch Linux.


Installer for Microsoft Windows
===============================

Prerequisites
-------------

SeriesMarker, installed by binary, depends on the
`Microsoft Visual C++ Runtime Components`. Those may have already been
installed on your system and no further action is required. Otherwise, you
will encounter the error shown below, when trying to execute SeriesMarker
after its installation has been finished.

	.. image:: images/install_win/MSVCRError.png

To prevent this error, or to resolve it, the runtime components can be
obtained at the following locations:

* `Microsoft Visual C++ Redistributable Package (x86)`_
* `Microsoft Visual C++ Redistributable Package (x64)`_


Obtaining the Installer
-----------------------

The installer is available for download at the `SeriesMarker Download Site`_.
The name of the latest executable is SeriesMarker-|version|-win32.msi.

.. _install_procedure_win:

Install Procedure
-----------------

Once the download has been finished, double click the installer to begin
with the setup.

	.. figure:: images/install_win/TargetLocation.png
		:scale: 50 %

		The installer will ask you for the location, to which SeriesMarker
		shall be installed to. After selecting the desired target directory,
		click ``Next`` to proceed.

	.. figure:: images/install_win/UserAccountControl.png
		:scale: 50 %

		The installer might ask for your administration permissions
		in order to be able to complete the installation; click ``Yes``
		to accept.

	.. figure:: images/install_win/CopyingFiles.png
		:scale: 50 %

		The necessary files are then copied into the selected target directory.

	.. figure:: images/install_win/InstallComplete.png
		:scale: 50 %

		When the setup is finished, click ``Finish`` to exit the installer.

The installer creates a shortcut on your desktop as well as an entry
in your start menu during the process (there is currently no way to opt out
from this, sorry). Both of them allow you to start SeriesMarker.

You may now continue with the :ref:`User Guide` or explore the software
on your own.


Installer for OS X
==================


Obtaining the Installer
-----------------------

The installer are available for download at the `SeriesMarker Download Site`_.
The names of the latest disk images for supported OS X versions are listed
in the following:

``OS X Mountain Lion (10.8)``
	SeriesMarker-|version|-MountainLion.dmg
``OS X Lion (10.7)``
	SeriesMarker-|version|-Lion.dmg

.. warning::

	Trying to execute SeriesMarker, installed from a disk image that was
	intended for a different OS X version, will likely fail.

.. _install_procedure_mac:

Install Procedure
-----------------

Once the download has been finished, double click the installer to begin
with the setup.

	.. figure:: images/install_osx/DiskImageOpen.png
	   :scale: 10 %

	   A new finder window will open and show you the contents of the
	   loaded disk image.

	.. figure:: images/install_osx/DiskImageDragnDrop.png
	   :scale: 50 %

	   To install `SeriesMarker`, click-and-hold on the application,
	   drag it above the shortcut to your `Applications` and release
	   the mouse button.

	.. figure:: images/install_osx/DiskImageCopy.png
	   :scale: 50 %

	   The application will now be copied to your applications directory,
	   from where you can start SeriesMarker afterwards.

You may now continue with the :ref:`User Guide` or explore the
software on your own.


.. _building_from_source:

********************
Building from Source
********************

This section describes how SeriesMarker can be installed on various operating
systems by building it from its source code.


Obtaining the Source
====================

Source files for SeriesMarker are available at the following locations:

* `SeriesMarker Project Site`_
* `SeriesMarker Package Site`_

.. note::

	It may not be necessary to download the source manually. Please refer to
	the section, matching your operating system, for instructions.


.. _dependencies:

Dependencies
============

The following lists the `Python`_ packages, SeriesMarker is depending on:

* `pytvdbapi`_
* `appdirs`_
* `SQLAlchemy`_
* `PySide`_

Before SeriesMarker can be built successfully, its dependencies must be
resolved first. While most of them are uncomplicated, `PySide`_ rather is a
heavyweight and may cause some inconvenience. Please refer to the section,
matching your operating system, for instructions how to resolve those
dependencies.


.. _building_on_linux:

Building on Linux
=================

Prerequisites
-------------

For `PySide`_ to be built successfully, additional dependencies must be
installed first: its make-dependencies. Those are not `Python`_ packages and,
thus, can not be installed by using `pip`_. PySide´s `Building on Linux`_ states
a complete list of needed make-dependencies; a successful build was
accomplished with the following software installed:

* `GNU Make`_
* `GNU Compiler Collection (GCC)`_
* `CMake`_
* `Qt`_

.. warning::

	*Qt5* is not yet compatible with `PySide`_; use *Qt4* instead
	(also check that your ``qmake`` binary is pointing to the *Qt4* version).


Install SeriesMarker
--------------------

With PySide's make-dependencies installed, SeriesMarker can now be built.
To fetch the source files, build, and install it on your machine,
the usage of `pip`_ is recommended:

.. code-block:: bash

	#pip install SeriesMarker

This will also fetch, build, and install SeriesMarker's
:ref:`dependencies <dependencies>` from source. Afterwards, SeriesMarker
can be executed from a shell:

.. code-block:: bash

	$seriesmarker

You may now continue with the :ref:`User Guide` or explore the software
on your own.


Building on Microsoft Windows
=============================

.. _building_on_win_pre:

Prerequisites
-------------

Install `Python`_ on your system and let the installer add it to your `Path`
for convenience. Also visit `setuptools`_ and `pip`_ and install
them as well. It is also recommended to add your Python`s `Scripts` directory
to your `Path` afterwards.

PySide
^^^^^^

There are two possible options to install `PySide`_ on your system: installing
it from a binary, or completely building it from source.

Binary Install
""""""""""""""

Visit `PySide Binaries for Microsoft Windows <PySide_Binaries_Windows>`_,
download, and execute the matching installer for your system.

Building from Source
""""""""""""""""""""

For `PySide`_ to be built successfully, additional dependencies must be
installed first: its make-dependencies. Those are not `Python`_ packages and,
thus, can not be installed by using `pip`_. PySide´s
`Building on Windows <PySide_Building_on_Windows>`_ states a complete list of
needed make-dependencies; a successful build was accomplished with the
following software installed:

* `Microsoft Visual Studio`_
* `CMake`_
* `Qt`_

.. warning::

	*Qt5* is not yet compatible with `PySide`_; use *Qt4* instead.

.. note::

	While PySide´s `Building on Windows <PySide_Building_on_Windows>`_ lists
	the	`Microsoft Windows SDK`_ as an prerequisite only, skipping the
	installation of	`Microsoft Visual Studio`_ causes an error while
	building `PySide`_ due to the missing tool `nmake`. It is therefore
	necessary to install `Microsoft Visual Studio` instead (it includes the SDK).
	Also make sure to install the version on which your `Qt`_ libraries
	depend on, which currently is edition 2010,
	called `Visual 2010 C++ Express` on the site.

It is also necessary to add `CMake`_ and `qmake`_ to your `Path`:

*
	`CMake`_ will ask you if it shall be added to your path while installing,
 	otherwise it can be found in its install directory, e.g.,
 	``C:\Program Files\CMake 2.8\bin``.
*
	`qmake`_ was installed along with `Qt`_ and can be found in its install
	directory, e.g., ``C:\Qt\4.8.5\bin``.


Install SeriesMarker
--------------------

With the prerequisites fulfilled, SeriesMarker can now be built. Open the
`Command Prompt` (cmd.exe) and issue the following command:

.. code-block:: none

	pip install SeriesMarker

This will fetch, build, and install SeriesMarker together with its
:ref:`dependencies <dependencies>` from source.

Afterwards, the SeriesMarker executable can be found within your Python's
`Scripts` directory. It is recommended to create a shortcut for it, having,
e.g.,

.. code-block:: none

	C:\Python33\python.exe C:\Python33\Scripts\seriesmarker

as the shortcut's `Target`. SeriesMarker can then be executed conveniently
via the shortcut.

You may now continue with the :ref:`User Guide` or explore the software
on your own.



.. _building_on_osx:

Building on OS X
================


.. _building_on_osx_pre:

Prerequisites
-------------

Due to a `PySide bug`_, it is currently not possible to build SeriesMarker's
:ref:`dependencies <dependencies>` by using `pip`_ from the official `Python`_
release on OS X. The recommended way to build SeriesMarker is by using
`MacPorts`_.

To build SeriesMarker and its :ref:`dependencies <dependencies>`,
`MacPorts`_ requires an installed copy of `Xcode`_, which can be found
in the `Mac App Store`_ on your system for free. It also requires the
`Command Line Tools`, which can be installed from within `Xcode`_:

#. Start Xcode and open the ``Preferences`` via the `Xcode` menu.
#. Click on the ``Downloads`` tab.
#. Click the ``Install`` button next to the `Command Line Tools` entry.

More information can be found at `Installing MacPorts <MacPorts_Install>`_.

.. note::
	It is not sufficient to install the `Command Line Tools` only,
	leaving out `Xcode`_.

.. note::
	If you intend to create a distributable binary for OS X as well,
	you should also fulfill the :ref:`distribute_osx_pre_plus` before
	continuing.


.. _building_osx_install_deps:

Install Dependencies
--------------------

With `MacPorts`_ installed, open a shell and enter the following command
to update your ports database (see the `MacPorts Guide <MacPorts_Guide>`_
for more information):

.. code-block:: bash

	$sudo port selfupdate

The following commands will install those of SeriesMarker's
:ref:`dependencies <dependencies>`, which are available as ports:

.. code-block:: bash

	$sudo port install python33
	$sudo port install py33-pyside
	$sudo port install py33-sqlalchemy

.. note::
	In the default configuration of `MacPorts`_, pre-build packages are
	loaded instead of building them from source.

The commands mentioned above will also install all necessary
make-dependencies, including `Qt`_.

By issuing the following command, the `MacPorts`_ version of `pip`_ can
be installed and, with it, the remaining :ref:`dependencies <dependencies>`
as well:

.. code-block:: bash

	$sudo port install py33-pip
	$sudo pip-3.3 install pytvdbapi
	$sudo pip-3.3 install appdirs


Install SeriesMarker
--------------------

The following command will fetch the latest source distribution from
the `SeriesMarker Package Site`_, build, and install the application.

.. code-block:: bash

	$sudo pip-3.3 install --no-deps SeriesMarker

.. note::
	Due to the mix of installation methods, some packages are not being
	recognized correctly by `pip`_. The parameter ``--no-deps`` prevents
	it from re-building SeriesMarkers' :ref:`dependencies <dependencies>`,
	which have been installed beforehand.

The location of the SeriesMarker executable is displayed at the end of the
install process by `pip`_, e.g.:

.. code-block:: none

	/opt/local/Library/Frameworks/Python.framework/Versions/3.3/bin/seriesmarker

SeriesMarker can now be started from within a shell at this path. You may
want to create a shortcut to the executable for your convenience, e.g., in
your applications directory:

.. code-block:: bash

	$ln -s /opt/local/Library/Frameworks/Python.framework/Versions/3.3/bin/seriesmarker /Applications/SeriesMarker

You may now continue with the :ref:`User Guide` or explore the software on your own.


.. _appdirs: https://github.com/ActiveState/appdirs/
.. _Arch User Repository (AUR): https://wiki.archlinux.org/index.php/AUR_User_Guidelines
.. _AUR Helper: https://wiki.archlinux.org/index.php/AUR_helper
.. _CMake: http://www.cmake.org/
.. _GNU Make: https://www.gnu.org/software/make/
.. _GNU Compiler Collection (GCC): http://gcc.gnu.org
.. _MacPorts: https://www.macports.org/
.. _MacPorts_Install: https://www.macports.org/install.php
.. _MacPorts_Guide: https://www.macports.org/guide/#using
.. _Mac App Store: https://www.apple.com/de/osx/apps/app-store.html
.. _Microsoft .NET Framework: https://www.microsoft.com/en-us/download/details.aspx?id=17718
.. _Microsoft Visual C++ Redistributable Package (x86): https://www.microsoft.com/en-us/download/details.aspx?id=8328
.. _Microsoft Visual C++ Redistributable Package (x64): https://www.microsoft.com/en-us/download/details.aspx?id=13523
.. _Microsoft Visual Studio: https://www.microsoft.com/visualstudio/
.. _Microsoft Windows SDK: https://www.microsoft.com/en-us/download/details.aspx?id=8279
.. _NMAKE: https://msdn.microsoft.com/en-us/library/dd9y37ha.aspx
.. _pip: https://www.pip-installer.org
.. _pytvdbapi: https://github.com/fuzzycode/pytvdbapi/
.. _PySide: https://qt-project.org/wiki/PySide/
.. _PySide_Binaries_Linux: https://qt-project.org/wiki/PySide_Binaries_Linux
	.. _Binaries
.. _PySide_Binaries_Windows: http://qt-project.org/wiki/PySide_Binaries_Windows
.. _PySide_Building_on_Linux: https://qt-project.org/wiki/Building_PySide_on_Linux/
	.. _Building on Linux: PySide_Building_on_Linux_
.. _PySide_Building_on_Windows: http://qt-project.org/wiki/Building_PySide_on_Windows/
.. _PySide bug: https://bugreports.qt-project.org/browse/PYSIDE-178
.. _Python: http://www.python.org
.. _Qt: https://qt-project.org/
.. _qmake: https://en.wikipedia.org/wiki/Qmake
.. _setuptools: https://pypi.python.org/pypi/setuptools/
.. _SeriesMarker Download Site: https://sourceforge.net/projects/seriesmarker/files/
.. _SeriesMarker Project Site: https://toroettg.github.io/SeriesMarker/
.. _SeriesMarker Package: https://aur.archlinux.org/packages/seriesmarker/
.. _SeriesMarker Package Site: https://pypi.python.org/pypi/SeriesMarker/
.. _SQLAlchemy: http://www.sqlalchemy.org/
.. _Xcode: https://developer.apple.com/xcode/
.. _Yaourt: https://wiki.archlinux.org/index.php/Yaourt

