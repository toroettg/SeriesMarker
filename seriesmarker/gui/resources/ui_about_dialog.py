# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../resources/about_dialog.ui'
#
# Created: Fri Aug 16 23:38:34 2013
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.setWindowModality(QtCore.Qt.NonModal)
        AboutDialog.resize(428, 300)
        AboutDialog.setModal(True)
        self.verticalLayout_2 = QtGui.QVBoxLayout(AboutDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.title = QtGui.QLabel(AboutDialog)
        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(14)
        self.title.setFont(font)
        self.title.setFrameShape(QtGui.QFrame.NoFrame)
        self.title.setObjectName("title")
        self.verticalLayout_5.addWidget(self.title)
        self.version = QtGui.QLabel(AboutDialog)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.version.setFont(font)
        self.version.setFrameShape(QtGui.QFrame.NoFrame)
        self.version.setIndent(20)
        self.version.setObjectName("version")
        self.verticalLayout_5.addWidget(self.version)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.donate_button = QtGui.QToolButton(AboutDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.donate_button.sizePolicy().hasHeightForWidth())
        self.donate_button.setSizePolicy(sizePolicy)
        self.donate_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.donate_button.setAutoFillBackground(False)
        self.donate_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/donate_button.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.donate_button.setIcon(icon)
        self.donate_button.setIconSize(QtCore.QSize(92, 26))
        self.donate_button.setCheckable(False)
        self.donate_button.setAutoRaise(True)
        self.donate_button.setArrowType(QtCore.Qt.NoArrow)
        self.donate_button.setObjectName("donate_button")
        self.horizontalLayout.addWidget(self.donate_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(AboutDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.about_tab = QtGui.QWidget()
        self.about_tab.setObjectName("about_tab")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.about_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.about_browser = QtGui.QTextBrowser(self.about_tab)
        self.about_browser.setOpenExternalLinks(True)
        self.about_browser.setObjectName("about_browser")
        self.verticalLayout_4.addWidget(self.about_browser)
        self.tabWidget.addTab(self.about_tab, "")
        self.author_tab = QtGui.QWidget()
        self.author_tab.setObjectName("author_tab")
        self.verticalLayout = QtGui.QVBoxLayout(self.author_tab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.author_browser = QtGui.QTextBrowser(self.author_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.author_browser.sizePolicy().hasHeightForWidth())
        self.author_browser.setSizePolicy(sizePolicy)
        self.author_browser.setOpenExternalLinks(True)
        self.author_browser.setObjectName("author_browser")
        self.verticalLayout.addWidget(self.author_browser)
        self.tabWidget.addTab(self.author_tab, "")
        self.license_tab = QtGui.QWidget()
        self.license_tab.setObjectName("license_tab")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.license_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.license_browser = QtGui.QTextBrowser(self.license_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.license_browser.sizePolicy().hasHeightForWidth())
        self.license_browser.setSizePolicy(sizePolicy)
        self.license_browser.setOpenExternalLinks(True)
        self.license_browser.setObjectName("license_browser")
        self.verticalLayout_3.addWidget(self.license_browser)
        self.tabWidget.addTab(self.license_tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.buttonBox = QtGui.QDialogButtonBox(AboutDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(AboutDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), AboutDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "About SeriesMarker", None, QtGui.QApplication.UnicodeUTF8))
        self.title.setText(QtGui.QApplication.translate("AboutDialog", "SeriesMarker", None, QtGui.QApplication.UnicodeUTF8))
        self.version.setText(QtGui.QApplication.translate("AboutDialog", "Version:", None, QtGui.QApplication.UnicodeUTF8))
        self.donate_button.setToolTip(QtGui.QApplication.translate("AboutDialog", "If you really like this software, you can donate for coffee.", None, QtGui.QApplication.UnicodeUTF8))
        self.about_browser.setHtml(QtGui.QApplication.translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-weight:600;\">Website:</span><span style=\" font-family:\'DejaVu Sans\';\"> </span><a href=\"http://toroettg.github.io/SeriesMarker/\"><span style=\" text-decoration: underline; color:#0000ff;\">http://toroettg.github.io/SeriesMarker/</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This software is using data from <a href=\"http://www.thetvdb.com\"><span style=\" text-decoration: underline; color:#0000ff;\">TheTVDB.com</span></a>. You can help to improve it by contributing information!</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about_tab), QtGui.QApplication.translate("AboutDialog", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.author_browser.setHtml(QtGui.QApplication.translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\';\">Copyright (C) 2013 Tobias Röttger &lt;toroettg@gmail.com&gt;</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.author_tab), QtGui.QApplication.translate("AboutDialog", "Author", None, QtGui.QApplication.UnicodeUTF8))
        self.license_browser.setHtml(QtGui.QApplication.translate("AboutDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\';\">SeriesMarker is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License version 3 as published by the Free Software Foundation.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\';\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\';\">This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.</span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\';\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\';\">You should have received a copy of the GNU General Public License along with this program. If not, see </span><a href=\"http://www.gnu.org/licenses/\"><span style=\" font-family:\'Sans Serif\'; text-decoration: underline; color:#0000ff;\">http://www.gnu.org/licenses/</span></a><span style=\" font-family:\'Sans Serif\';\">.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.license_tab), QtGui.QApplication.translate("AboutDialog", "License", None, QtGui.QApplication.UnicodeUTF8))

from . import serieswatcher_rc
