.. _binary_installer:

================
Binary Installer
================

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
The names of the latest executables are listed in the following:

``64-bit Windows Operating System``
    SeriesMarker-|version|-amd64.msi
``32-bit Windows Operating System``
    SeriesMarker-|version|-win32.msi

.. note::
    If in doubt, use the 32-bit version.

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

``OS X Mountain Lion (10.10)``
    SeriesMarker-|version|-Yosemite.dmg
``OS X Lion (10.9)``
    SeriesMarker-|version|-Mavericks.dmg

.. warning::

    Trying to execute SeriesMarker, installed from a disk image that was
    intended for a different OS X version, will likely fail.

.. _install_procedure_mac:

Install Procedure
-----------------

Once the download has been finished, double click the installer to begin
with the setup.

    .. figure:: images/install_osx/DiskImageOpen.png
        :scale: 50 %

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
