# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../resources/main_window.ui'
#
# Created: Sat Feb  7 14:47:31 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(761, 642)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tree_view = QtGui.QTreeView(self.splitter)
        self.tree_view.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tree_view.setAlternatingRowColors(False)
        self.tree_view.setSortingEnabled(True)
        self.tree_view.setAllColumnsShowFocus(True)
        self.tree_view.setObjectName("tree_view")
        self.list_view = QtGui.QListView(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_view.sizePolicy().hasHeightForWidth())
        self.list_view.setSizePolicy(sizePolicy)
        self.list_view.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.list_view.setMovement(QtGui.QListView.Static)
        self.list_view.setFlow(QtGui.QListView.LeftToRight)
        self.list_view.setResizeMode(QtGui.QListView.Adjust)
        self.list_view.setViewMode(QtGui.QListView.IconMode)
        self.list_view.setWordWrap(True)
        self.list_view.setObjectName("list_view")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolBar.setStyleSheet("QToolBar {border-bottom: 1px solid grey; }")
        self.toolBar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_add = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/list-add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_add.setIcon(icon)
        self.action_add.setObjectName("action_add")
        self.action_remove = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/list-remove.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_remove.setIcon(icon1)
        self.action_remove.setObjectName("action_remove")
        self.action_about = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/help-browser.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_about.setIcon(icon2)
        self.action_about.setObjectName("action_about")
        self.action_about_qt = QtGui.QAction(MainWindow)
        self.action_about_qt.setObjectName("action_about_qt")
        self.action_update = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/view-refresh.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_update.setIcon(icon3)
        self.action_update.setObjectName("action_update")
        self.action_home = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/go-home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_home.setIcon(icon4)
        self.action_home.setObjectName("action_home")
        self.action_exit = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/system-log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_exit.setIcon(icon5)
        self.action_exit.setObjectName("action_exit")
        self.action_mark_watched = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Koloria/icons/Checkmark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_mark_watched.setIcon(icon6)
        self.action_mark_watched.setObjectName("action_mark_watched")
        self.action_mark_unwatched = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Koloria/icons/Error_Symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_mark_unwatched.setIcon(icon7)
        self.action_mark_unwatched.setObjectName("action_mark_unwatched")
        self.menuAbout.addAction(self.action_about_qt)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.action_home)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_add)
        self.toolBar.addAction(self.action_remove)
        self.toolBar.addAction(self.action_update)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_about)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_exit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "SeriesMarker", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.action_add.setText(QtGui.QApplication.translate("MainWindow", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.action_add.setToolTip(QtGui.QApplication.translate("MainWindow", "Add a new Series", None, QtGui.QApplication.UnicodeUTF8))
        self.action_add.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.action_remove.setText(QtGui.QApplication.translate("MainWindow", "&Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.action_remove.setToolTip(QtGui.QApplication.translate("MainWindow", "Remove a Series", None, QtGui.QApplication.UnicodeUTF8))
        self.action_remove.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.action_about.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_about.setToolTip(QtGui.QApplication.translate("MainWindow", "About SeriesMarker", None, QtGui.QApplication.UnicodeUTF8))
        self.action_about_qt.setText(QtGui.QApplication.translate("MainWindow", "About Qt", None, QtGui.QApplication.UnicodeUTF8))
        self.action_update.setText(QtGui.QApplication.translate("MainWindow", "&Update", None, QtGui.QApplication.UnicodeUTF8))
        self.action_update.setToolTip(QtGui.QApplication.translate("MainWindow", "Update Database", None, QtGui.QApplication.UnicodeUTF8))
        self.action_update.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+U", None, QtGui.QApplication.UnicodeUTF8))
        self.action_home.setText(QtGui.QApplication.translate("MainWindow", "&Home", None, QtGui.QApplication.UnicodeUTF8))
        self.action_home.setToolTip(QtGui.QApplication.translate("MainWindow", "Return to Main View", None, QtGui.QApplication.UnicodeUTF8))
        self.action_home.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+H", None, QtGui.QApplication.UnicodeUTF8))
        self.action_exit.setText(QtGui.QApplication.translate("MainWindow", "E&xit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_exit.setToolTip(QtGui.QApplication.translate("MainWindow", "Exit SeriesMarker", None, QtGui.QApplication.UnicodeUTF8))
        self.action_exit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.action_mark_watched.setText(QtGui.QApplication.translate("MainWindow", "Mark watched", None, QtGui.QApplication.UnicodeUTF8))
        self.action_mark_watched.setToolTip(QtGui.QApplication.translate("MainWindow", "Mark all Episodes as watched", None, QtGui.QApplication.UnicodeUTF8))
        self.action_mark_unwatched.setText(QtGui.QApplication.translate("MainWindow", "Mark unwatched", None, QtGui.QApplication.UnicodeUTF8))
        self.action_mark_unwatched.setToolTip(QtGui.QApplication.translate("MainWindow", "Mark all Episodes as unwatched", None, QtGui.QApplication.UnicodeUTF8))

from . import serieswatcher_rc
