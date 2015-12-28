Installer for Linux
===================


Arch Linux
----------

A `SeriesMarker Package`_ can be found in the `Arch User Repository (AUR)`_.
A simple way to install the package is by using the `AUR Helper`_ `Yaourt`_:

.. code-block:: bash

    $yaourt -S seriesmarker

The above mentioned command will resolve all necessary
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

.. include:: target_links.rst