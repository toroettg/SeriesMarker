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

.. include:: target_links.rst