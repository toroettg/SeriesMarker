.. _building_from_source:

********************
Building from Source
********************

This section describes how SeriesMarker can be installed on various operating
systems, by building it from its source code.


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
resolved first. Please refer to the section, matching your operating system,
for instructions how to resolve those dependencies.


.. _building_on_linux:

Building on Linux
=================

Prerequisites
-------------

For `PySide`_ to be built successfully, additional dependencies must be
installed first: its make-dependencies. Those are not `Python`_ packages and,
thus, can not be installed by using `pip`_. `Building PySide on Linux`_ states
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

Visit `PySide Binaries for Microsoft Windows`_,
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

The recommended way to build SeriesMarker is by using `MacPorts`_.

.. _building_on_osx_pre:

Prerequisites
-------------

To build SeriesMarker, and its :ref:`dependencies <dependencies>`,
`MacPorts`_ requires an installed copy of `Xcode`_, which can be found
in the `Mac App Store`_ on your system for free. It also requires the
`Command Line Tools`, which can be installed from within `Xcode`_:

#. Start Xcode and open the ``Preferences`` via the `Xcode` menu.
#. Click on the ``Downloads`` tab.
#. Click the ``Install`` button next to the `Command Line Tools` entry.

More information can be found at `Installing MacPorts`_.

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

    $sudo port install python34
    $sudo port install py34-pyside
    $sudo port install py34-sqlalchemy

.. note::
    In the default configuration of `MacPorts`_, pre-build packages are
    loaded, instead of building them from source.

The commands mentioned above will also install all necessary
make-dependencies, including `Qt`_.

By issuing the following command, the `MacPorts`_ version of `pip`_ can
be installed and, with it, the remaining :ref:`dependencies <dependencies>`
as well:

.. code-block:: bash

    $sudo port install py34-pip
    $sudo pip-3.4 install pytvdbapi
    $sudo pip-3.4 install appdirs


Install SeriesMarker
--------------------

The following command will fetch the latest source distribution from
the `SeriesMarker Package Site`_, build, and install the application.

.. code-block:: bash

    $sudo pip-3.4 install --no-deps SeriesMarker

.. note::
    Due to the mix of installation methods, some packages are not being
    recognized correctly by `pip`_. The parameter ``--no-deps`` prevents
    it from re-building SeriesMarkers' :ref:`dependencies <dependencies>`,
    which have been installed beforehand.

The location of the SeriesMarker executable is displayed at the end of the
install process by `pip`_, e.g.:

.. code-block:: none

    /opt/local/Library/Frameworks/Python.framework/Versions/3.4/bin/seriesmarker

SeriesMarker can now be started from within a shell at this path. You may
want to create a shortcut to the executable for your convenience, e.g., in
your applications directory:

.. code-block:: bash

    $ln -s /opt/local/Library/Frameworks/Python.framework/Versions/3.4/bin/seriesmarker /Applications/SeriesMarker

You may now continue with the :ref:`User Guide` or explore the software on your own.

.. include:: target_links.rst