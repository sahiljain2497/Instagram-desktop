# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(673, 856)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/app-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color:white;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QTabBar::Tab{\n"
"    background-color:white;\n"
"}\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setIconSize(QtCore.QSize(88, 65))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(136, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(138, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/camera(1).png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setStyleSheet("font:16pt \"MV Boli\";")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/newPrefix/message.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 4, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 90))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 90))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.story1 = QtWidgets.QLabel(self.groupBox_2)
        self.story1.setGeometry(QtCore.QRect(20, 30, 51, 51))
        self.story1.setMaximumSize(QtCore.QSize(61, 61))
        self.story1.setStyleSheet("border-radius:25px;\n"
"background-color:black;\n"
"border:2px solid;\n"
"border-color: rgb(0, 85, 255);")
        self.story1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.story1.setText("")
        self.story1.setPixmap(QtGui.QPixmap(":/story/Story images/0.png"))
        self.story1.setScaledContents(True)
        self.story1.setObjectName("story1")
        self.story1_2 = QtWidgets.QLabel(self.groupBox_2)
        self.story1_2.setGeometry(QtCore.QRect(80, 30, 51, 51))
        self.story1_2.setMaximumSize(QtCore.QSize(61, 61))
        self.story1_2.setStyleSheet("border-radius:25px;\n"
"background-color:black;\n"
"border:2px solid;\n"
"border-color: rgb(0, 85, 255);")
        self.story1_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.story1_2.setText("")
        self.story1_2.setPixmap(QtGui.QPixmap(":/story/Story images/1.png"))
        self.story1_2.setScaledContents(True)
        self.story1_2.setObjectName("story1_2")
        self.story1_3 = QtWidgets.QLabel(self.groupBox_2)
        self.story1_3.setGeometry(QtCore.QRect(140, 30, 51, 51))
        self.story1_3.setMaximumSize(QtCore.QSize(61, 61))
        self.story1_3.setStyleSheet("border-radius:25px;\n"
"background-color:black;\n"
"border:2px solid;\n"
"border-color: rgb(0, 85, 255);")
        self.story1_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.story1_3.setText("")
        self.story1_3.setPixmap(QtGui.QPixmap(":/story/Story images/2.png"))
        self.story1_3.setScaledContents(True)
        self.story1_3.setObjectName("story1_3")
        self.story1_4 = QtWidgets.QLabel(self.groupBox_2)
        self.story1_4.setGeometry(QtCore.QRect(320, 30, 51, 51))
        self.story1_4.setMaximumSize(QtCore.QSize(61, 61))
        self.story1_4.setStyleSheet("border-radius:25px;\n"
"background-color:black;\n"
"border:2px solid;\n"
"border-color: rgb(0, 85, 255);")
        self.story1_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.story1_4.setText("")
        self.story1_4.setPixmap(QtGui.QPixmap(":/story/Story images/5.png"))
        self.story1_4.setScaledContents(True)
        self.story1_4.setObjectName("story1_4")
        self.story1_5 = QtWidgets.QLabel(self.groupBox_2)
        self.story1_5.setGeometry(QtCore.QRect(260, 30, 51, 51))
        self.story1_5.setMaximumSize(QtCore.QSize(61, 61))
        self.story1_5.setStyleSheet("border-radius:25px;\n"
"background-color:black;\n"
"border:2px solid;\n"
"border-color: rgb(0, 85, 255);")
        self.story1_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.story1_5.setText("")
        self.story1_5.setPixmap(QtGui.QPixmap(":/story/Story images/4.png"))
        self.story1_5.setScaledContents(True)
        self.story1_5.setObjectName("story1_5")
        self.story1_6 = QtWidgets.QLabel(self.groupBox_2)
        self.story1_6.setGeometry(QtCore.QRect(200, 30, 51, 51))
        self.story1_6.setMaximumSize(QtCore.QSize(61, 61))
        self.story1_6.setStyleSheet("border-radius:25px;\n"
"background-color:black;\n"
"border:2px solid;\n"
"border-color: rgb(0, 85, 255);")
        self.story1_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.story1_6.setText("")
        self.story1_6.setPixmap(QtGui.QPixmap(":/story/Story images/3.png"))
        self.story1_6.setScaledContents(True)
        self.story1_6.setObjectName("story1_6")
        self.story1_7 = QtWidgets.QLabel(self.groupBox_2)
        self.story1_7.setGeometry(QtCore.QRect(500, 30, 51, 51))
        self.story1_7.setMaximumSize(QtCore.QSize(61, 61))
        self.story1_7.setStyleSheet("border-radius:25px;\n"
"background-color:black;\n"
"border:2px solid;\n"
"border-color: rgb(0, 85, 255);")
        self.story1_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.story1_7.setText("")
        self.story1_7.setPixmap(QtGui.QPixmap(":/story/Story images/8.png"))
        self.story1_7.setScaledContents(True)
        self.story1_7.setObjectName("story1_7")
        self.story1_8 = QtWidgets.QLabel(self.groupBox_2)
        self.story1_8.setGeometry(QtCore.QRect(380, 30, 51, 51))
        self.story1_8.setMaximumSize(QtCore.QSize(61, 61))
        self.story1_8.setStyleSheet("border-radius:25px;\n"
"background-color:black;\n"
"border:2px solid;\n"
"border-color: rgb(0, 85, 255);")
        self.story1_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.story1_8.setText("")
        self.story1_8.setPixmap(QtGui.QPixmap(":/story/Story images/6.png"))
        self.story1_8.setScaledContents(True)
        self.story1_8.setObjectName("story1_8")
        self.story1_9 = QtWidgets.QLabel(self.groupBox_2)
        self.story1_9.setGeometry(QtCore.QRect(440, 30, 51, 51))
        self.story1_9.setMaximumSize(QtCore.QSize(61, 61))
        self.story1_9.setStyleSheet("border-radius:25px;\n"
"background-color:black;\n"
"border:2px solid;\n"
"border-color: rgb(0, 85, 255);")
        self.story1_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.story1_9.setText("")
        self.story1_9.setPixmap(QtGui.QPixmap(":/story/Story images/7.png"))
        self.story1_9.setScaledContents(True)
        self.story1_9.setObjectName("story1_9")
        self.gridLayout_4.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_4.addWidget(self.textBrowser, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 5)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-warehouse-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/icons8-positive-500.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/heart1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_4, icon4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_10 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_5)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_5)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_5)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_5)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/profile pic/index.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 4, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_5)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_5)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 6, 0, 1, 2)
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_5)
        self.tabWidget_2.setIconSize(QtCore.QSize(112, 60))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/icons/block.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_6, icon5, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/icons/view_list-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_8, icon6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/icons/tag.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_7, icon7, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/newPrefix/icons/collection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget_2.addTab(self.tab_9, icon8, "")
        self.gridLayout_2.addWidget(self.tabWidget_2, 7, 0, 1, 6)
        self.label_13 = QtWidgets.QLabel(self.tab_5)
        self.label_13.setMaximumSize(QtCore.QSize(34, 16777215))
        self.label_13.setStyleSheet("")
        self.label_13.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_13.setLineWidth(2)
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/newPrefix/icons/setting.png"))
        self.label_13.setScaledContents(False)
        self.label_13.setWordWrap(False)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 2, 5, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_5)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 2, 1, 3)
        self.tabWidget_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_12.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.pushButton.raise_()
        self.label_11.raise_()
        self.label_13.raise_()
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/newPrefix/profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_5, icon9, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ToonGram"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Stories  "))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://en.wikipedia.org/wiki/Bugs_Bunny\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">Bugs Bunny </span></a></p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/feed/myfeed/new5.jpg\" /></p>\n"
"<hr />\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt;\">  👍 ♥ </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Bugs Bunny Just Did See Some New Tricks.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://en.wikipedia.org/wiki/Mickey_Mouse\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">Micky Mouse</span></a></p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/feed/myfeed/new1.jpg\" /></p>\n"
"<hr />\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt;\">  👍 ♥ </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Micky Just Went on a trip To USA</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://en.wikipedia.org/wiki/Pikachu\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">Pikachu</span></a></p>\n"
"<hr />\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/feed/myfeed/new2.png\" /></p>\n"
"<hr />\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt;\">  👍 ♥ </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Pikachu is learning how to speak.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://en.wikipedia.org/wiki/Popeye\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">Popeye</span></a></p>\n"
"<hr />\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/feed/myfeed/new3.jpg\" /></p>\n"
"<hr />\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt;\">  👍 ♥ </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Popeye Just Went to Gym to pump his Biceps.</span></p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://en.wikipedia.org/wiki/Wile_E._Coyote_and_the_Road_Runner\"><span style=\" font-size:18pt; text-decoration: underline; color:#0000ff;\">Grinder</span></a></p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/feed/myfeed/new4.jpg\" /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<hr />\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Grinder just ate too much and is sleeping.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">He loves food.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "Following"))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "Posts"))
        self.label_7.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "    Followers   "))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "   My Name Here"))
        self.label_12.setText(_translate("MainWindow", "   My Bio Here"))
        self.pushButton.setText(_translate("MainWindow", "Edit Profile"))

import New_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

