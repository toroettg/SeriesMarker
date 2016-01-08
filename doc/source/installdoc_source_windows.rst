Building on Microsoft Windows
=============================

.. _building_on_win_pre:

Prerequisites
-------------

Install `Python`_ on your system and let the installer add it to your `Path`
for convenience. You may have to reboot before those changes are applied.

Install SeriesMarker
--------------------

With the prerequisites fulfilled, SeriesMarker can now be built. Open the
`Command Prompt` (cmd.exe) and issue the following command:

.. code-block:: none

    pip install --only-binary PySide SeriesMarker

This will fetch, build, and install SeriesMarker together with its
remaining :ref:`dependencies <dependencies>`.

It will also try to install a binary package of `PySide`_ if it is not already
installed on your system. This is the recommended way, since `Building PySide on
Windows`_ is complex.

.. note::

    You may find additional binary packages of PySide at the `Qt`_ site.

    .. code-block:: none

     pip install --find-links https://download.qt.io/official_releases/pyside/ --only-binary PySide SeriesMarker


Afterwards, the SeriesMarker executable can be found within your Python's
`Scripts` directory. It is recommended to create a shortcut for it, having,
e.g.,

.. code-block:: none

    C:\Python34\python.exe C:\Python34\Scripts\seriesmarker

as the shortcut's `Target`. SeriesMarker can then be executed conveniently
via the shortcut.

You may now continue with the :ref:`User Guide` or explore the software
on your own.

.. include:: target_links.rst