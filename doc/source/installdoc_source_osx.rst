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
`Command Line Tools`. More information can be found at `Installing MacPorts`_.

.. note::
    It is not sufficient to install the `Command Line Tools` only,
    leaving out `Xcode`_.

.. _building_osx_install_deps:

Install Dependencies
--------------------

With `MacPorts`_ installed, open a shell and enter the following command
to update your ports database (see the `MacPorts Guide`_
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
    loaded where available, instead of building them from source.

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
    it from re-building SeriesMarker's :ref:`dependencies <dependencies>`,
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