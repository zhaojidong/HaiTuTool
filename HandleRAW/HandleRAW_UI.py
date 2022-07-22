# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HandleRAW_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(854, 855)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 20, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(410, 20, 431, 781))
        self.textEdit.setObjectName("textEdit")
        self.plot_wave = QtWidgets.QPushButton(self.centralwidget)
        self.plot_wave.setGeometry(QtCore.QRect(210, 20, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.plot_wave.setFont(font)
        self.plot_wave.setIconSize(QtCore.QSize(30, 50))
        self.plot_wave.setObjectName("plot_wave")
        self.btn_display_raw = QtWidgets.QPushButton(self.centralwidget)
        self.btn_display_raw.setGeometry(QtCore.QRect(30, 100, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.btn_display_raw.setFont(font)
        self.btn_display_raw.setIconSize(QtCore.QSize(30, 50))
        self.btn_display_raw.setObjectName("btn_display_raw")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(400, 0, 451, 801))
        self.groupBox.setObjectName("groupBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 854, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Open Folder"))
        self.plot_wave.setText(_translate("MainWindow", "Plot Wave"))
        self.btn_display_raw.setText(_translate("MainWindow", "Display RAW"))
        self.groupBox.setTitle(_translate("MainWindow", "MESSAGE:"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))