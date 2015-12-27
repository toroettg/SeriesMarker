.. _User Guide:

##########
User Guide
##########

This user guide will show you the most important features of SeriesMarker and
explains how to use them. After starting the application, you will be greeted
with the main window, from which you can begin your exciting journey.

.. note::

    Depending on the size of your series collection, starting SeriesMarker may
    take a while. A splash screen displays the loading progress during the
    start-up. Please be patient.

.. figure:: images/application/MainWindowEmpty.png
    :scale: 50 %

    SeriesMarker's main window, first application start.

***************
Adding a Series
***************

To add one of your favorite TV series to your SeriesMarker collection, click
on the *Add* button in the toolbar. You can also use the shortcut ``CTRL + A``.

A new dialog will be presented to you. Enter the (partial) name of the series
you would like to add into the text field, click on the *Search* button,
and wait for the results of your search to be displayed.

Select the desired Series by clicking on it. Confirm your selection by clicking
on the *OK* button. The data, related to your selection, will be downloaded, and
the series is added to your SeriesMarker collection.

The search dialog will close, and you can then see your recently added series in
the main window of the application (among previously added series).

*****************
Removing a Series
*****************

If you would like to remove a series from your collection, either click on the
series itself in the main window, or click on one of its seasons to select it.
Then, click the *Remove* button in the toolbar or use the shortcut ``CTRL + R``.
The selected series will then be removed from your system with all its data.

You can also right-click on a series or season to open up a context menu,
which allows you to remove the selected series.

.. note::

    Removing a series is permanent. All information related to it, e.g., which
    episode was marked as watched, will be lost. However, you can re-add a
    removed series at any time by following `Adding a Series`_.

.. warning::

    There is currently no confirmation dialog to prevent the unintended removal
    of a series from the collection, be careful.

**************
Sorting Series
**************

The main window of SeriesMarker allows you to sort your collection of series
by several ways, as described in the following.

Sort by Name
************

Click on the first column of the table, labeled 'Series', to sort your series by
their names, in either ascending or descending order. This is the default at
application start.

Sort by Episode
***************

Click on the second column of the table, labeled 'Episodes', to sort your series
by their number of episodes that you have already watched in total, in either ascending or
descending order.

Sort by Progress
****************

Click on the third column of the table, labeled 'Progress', to sort your series
by their relative progress in being watched, in either ascending or descending
order. Series, which have been completely watched, are being listed at the end
of the table.

**************
Marking Series
**************

In the main window of SeriesMarker, select the season you would like to
mark progress for. The detail window to your right will now list all episodes
of that selected season. Click on the field next to each episode, that you
would like to mark, to change its watched state.

You can also right-click on a series or season to open up a context menu,
which allows you to batch mark all related episodes of your selection.

***************
Updating Series
***************

To let SeriesMarker check if new episodes are available for your added series,
click on the *Update* button in the toolbar of the main window.

.. note::

    There is currently no visual feedback regarding the update progress.
    Depending on the size of your series collection, it may take a while.

.. warning::

    This feature is currently in an experimental state and bad things may happen.
    Please create a backup of your SeriesMarker database beforehand.