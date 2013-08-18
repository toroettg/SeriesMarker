# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../resources/search_dialog.ui'
#
# Created: Fri Aug 16 23:38:34 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.search_button = QtGui.QPushButton(Dialog)
        self.search_button.setAutoDefault(True)
        self.search_button.setObjectName("search_button")
        self.gridLayout.addWidget(self.search_button, 1, 1, 1, 1)
        self.search_text_field = QtGui.QLineEdit(Dialog)
        self.search_text_field.setObjectName("search_text_field")
        self.gridLayout.addWidget(self.search_text_field, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_button = QtGui.QPushButton(Dialog)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.ok_button = QtGui.QPushButton(Dialog)
        self.ok_button.setObjectName("ok_button")
        self.horizontalLayout.addWidget(self.ok_button)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 2, 2)
        self.result_view = QtGui.QTableView(Dialog)
        self.result_view.setFocusPolicy(QtCore.Qt.NoFocus)
        self.result_view.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.result_view.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.result_view.setAlternatingRowColors(True)
        self.result_view.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.result_view.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.result_view.setShowGrid(False)
        self.result_view.setObjectName("result_view")
        self.result_view.horizontalHeader().setVisible(False)
        self.result_view.horizontalHeader().setCascadingSectionResizes(True)
        self.result_view.horizontalHeader().setHighlightSections(False)
        self.result_view.horizontalHeader().setStretchLastSection(False)
        self.result_view.verticalHeader().setVisible(False)
        self.result_view.verticalHeader().setCascadingSectionResizes(False)
        self.result_view.verticalHeader().setDefaultSectionSize(70)
        self.result_view.verticalHeader().setHighlightSections(False)
        self.result_view.verticalHeader().setMinimumSectionSize(70)
        self.result_view.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.result_view, 4, 0, 1, 2)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.search_text_field, QtCore.SIGNAL("returnPressed()"), self.search_button.click)
        QtCore.QObject.connect(self.ok_button, QtCore.SIGNAL("clicked()"), Dialog.accept)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL("clicked()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.search_text_field, self.search_button)
        Dialog.setTabOrder(self.search_button, self.result_view)
        Dialog.setTabOrder(self.result_view, self.cancel_button)
        Dialog.setTabOrder(self.cancel_button, self.ok_button)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Series Search", None, QtGui.QApplication.UnicodeUTF8))
        self.search_button.setText(QtGui.QApplication.translate("Dialog", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_button.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_button.setText(QtGui.QApplication.translate("Dialog", "Ok", None, QtGui.QApplication.UnicodeUTF8))

