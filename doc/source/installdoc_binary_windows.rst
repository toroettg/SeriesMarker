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
        to be able to complete the installation; click ``Yes`` to accept.

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

.. include:: target_links.rst