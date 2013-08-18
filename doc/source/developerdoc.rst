###############
Developer Guide
###############

This part of the documentation currently acts as a note pad. Information
contained may be incomplete and incoherent. It will be improved over time.

******************
Coding Conventions
******************

Adding a new Source Code File
=============================

1.
	Add the file to the packages section of setup.py.

2.
	Add the copyright note.
		
3.
	Document the file by using docstrings (sphinx).
	
4.
	Add the file to the documentation:
	
	1.
		Add the module to the proper .rst file. You may need to create
		a new one. In that case, ensure that the new .rst is also added
		to the proper file in the documentation tree.
	2.
		Create a new build of the documentation and check if your
		references are set correctly and see if new errors/warnings
		have occurred.
		
5.
	If the file contains new features, ensure you have written a test case.
	Add it to the test package. Repeat steps 2-4 for the test file.
		
*************************
Distributing SeriesMarker
*************************

This section describes how a binary of SeriesMarker can be built for
various operating systems.

Prepare Packages
================

.. note::

	This section applies to every platform on which a binary shall
	be created on. Perform the operations described after the related
	packages have been installed in the process. 
	

The `pytvdbapi`_ package currently relies on methods, which are not compatible
to be used in a binary [#f1]_. Microsoft Windows and OS X also have some
problems with the encoding of the shipped UTF-8 files. Thus, these glitches
need to be fixed before building a binary:

#.
	Open the `pytvdbapi`_ main file, located in your python package directory,
	e.g., ``/opt/local/Library/Frameworks/Python.framework/Version/3.3/lib/python/site-packages/pytvdbapi/api.py``.
#.
	In line 46, change the import of ``resource_filename`` to ``resource_string``
#.
	In line 557, change ``resource_filename`` to ``resource_string``
#.
	In line 567, change ``generate_tree(language_file)`` to
	``generate_tree(str(language_file, encoding="UTF-8"))``.

.. [#f1] http://mail.python.org/pipermail/distutils-sig/2005-October/005236.html

.. note::

	This section is referring to pytvdbapi's master branch, not the latest
	released version (0.3.0). A new release is assumed to be brought soon. 


Microsoft Windows
=================

On Microsoft Windows, `cx_Freeze`_ is the recommended tool to create a binary
of SeriesMarker.

Prerequisites
-------------
The prerequisites to build a binary on Microsoft Windows
are the same as for :ref:`building from source <building_on_win_pre>`.
Please fulfill those first before continuing.

Install Dependencies
--------------------

Install SeriesMarkers :ref:`dependencies <dependencies>` via pip. In addition,
`cx_Freeze`_ needs to be installed:

.. code-block:: none
	
	pip install cx_Freeze

Creating a Binary Distribution
------------------------------

This section describes, how to create a installer for SeriesMarker from source.

1.
	Check out SeriesMarker.
2. 
	Open the `Command Prompt` (cmd.exe) and change to the root directory
	of SeriesMarker.
3.
	Execute ``python setup.py bdist_msi`` to create a msi-installer, 
	which can be found at the *dist* directory.
	
The installer can then be used as described in the :ref:`install procedure
<install_procedure_win>` for Microsoft Windows.

OS X
====

On OS X, `py2app`_ is the recommended tool to create a binary of SeriesMarker.


Basic Prerequisites
-------------------
The basic prerequisites to build a binary for SeriesMarker on OS X are the
same as for :ref:`building from source <building_on_osx_pre>`.
Please fulfill those first before continuing.


.. _distribute_osx_pre_plus:

Additional Prerequisites
------------------------

To prevent a build error, described at the `py2app FAQ`_, while creating
a binary, the `MacPorts`_ configuration should be changed to always build
ports from source instead of fetching a binary.
The configuration file should be located at
``/opt/local/etc/macports/macports.conf`` if you have installed `MacPorts`_
with default settings. Find and change the line defining the build behavior:

+--------------------------------------+-------------------------------------+
| .. code-block:: none                 | .. code-block:: none                |
|                                      |                                     |
|     #buildfromsource        ifneeded |     buildfromsource        always   |
|                                      |                                     |
+--------------------------------------+-------------------------------------+
	
This will ensure the adherence of the mentioned linker flag
, ``-headerpad_max_install_names``, when building packages. To ensure that 
the flag is set, see ``/opt/local/share/macports/Tcl/port1.0/portconfigure.tcl``
and check if it has been added to the ``ldflags``, e.g., by setting the
relevant line to:

.. code-block:: none
	
	default configure.ldflags   {"-L${prefix}/lib -Wl,-headerpad_max_install_names"}

Install Dependencies
--------------------

Proceed as described in :ref:`building_osx_install_deps`. In addition,
`py2app`_ needs to be installed:

.. code-block:: bash
	
	$sudo port install py33-py2app
	

Prepare Packages
----------------

py2app
^^^^^^

There is an `py2app bug`_, which prevents `Qt`_ plugins from being
copied to the binary correctly. To resolve it, open the `PySide`_
recipe file of `py2app`_, probably located at 

.. code-block:: bash

	/opt/local/Library/Frameworks/Python.framework.Versions/3.3/lib/python3.3/site-packages/py2app/recipes/pyside.py
	
and change the indentation of the else-part of the for-loop to match the
if-statement as shown in the bug report. 

httplib2
^^^^^^^^

The `httplib2`_ library stores some certificates, which cannot be read
from `py2app`_ due to restricted permissions. To change those permissions,
issue the following command:

.. code-block:: bash

	sudo chmod o=r /opt/local/Library/Frameworks/Python.framework.Versions/3.3/lib/python3.3/site-packages/httplib2-0.8-py3.3.egg/httplib2/cacerts.txt


Creating a Binary distribution
------------------------------

When your system is prepared to build SeriesMarker as described in
the previous sections, you can now create a distributable binary with the
following steps:

#.
	Check out SeriesMarker.
#.
	Open the a shell (`Terminal`) and change to the root directory
	of SeriesMarker.
#.
	Execute ``python3.3 setup.py py2app`` to create an application and
	a disk image, containing a copy of the application. Both can be found
	at the *dist* directory.
	
The resulting .app can then be used as usual. The disk image is
the preferred way to distribute the application, providing a simple installer
as shown in the :ref:`install procedure <install_procedure_mac>` for OS X.


*****
Notes
*****

TheTVDB API
===========

Links to the TheTVDB API for checking raw data. 

Languages:
	http://thetvdb.com/api/APIKEY/languages.xml
Mirrors:
	http://thetvdb.com/api/APIKEY/mirrors.xml
Server Time:
	http://www.thetvdb.com/api/Updates.php?type=none
Search:
	http://www.thetvdb.com/api/GetSeries.php?seriesname=how%20i%20met%20your%20mother
Series (basic):
	http://thetvdb.com/api/APIKEY/series/75760/en.xml
Series (full):
	http://thetvdb.com/api/APIKEY/series/75760/all/en.xml
Banners:
	http://thetvdb.com/api/APIKEY/series/75760/banners.xml
Episode:
	http://thetvdb.com/api/APIKEY/episodes/1159571/en.xml
Updates:
	http://thetvdb.com/api/APIKEY/updates/updates_all.xml

*********
Todo List
*********

.. todolist::


.. _cx_Freeze: http://cx-freeze.sourceforge.net/
.. _httplib2: https://code.google.com/p/httplib2/
.. _MacPorts: https://www.macports.org/
.. _py2app: https://bitbucket.org/ronaldoussoren/py2app
.. _py2app FAQ: https://bitbucket.org/ronaldoussoren/py2app/src/3e50b18722c57735988e13cfaacd59b163fda654/doc/faq.rst?at=default
.. _py2app bug: https://bitbucket.org/ronaldoussoren/py2app/issue/97/copying-file-dbfseventsd-when-set
.. _pytvdbapi: https://github.com/fuzzycode/pytvdbapi/
.. _PySide: https://qt-project.org/wiki/PySide/
.. _Qt: https://qt-project.org/
