# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SortFile.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SortFile(object):
    def setupUi(self, SortFile):
        SortFile.setObjectName("SortFile")
        SortFile.resize(305, 199)
        self.centralwidget = QtWidgets.QWidget(SortFile)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_SortFile = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_SortFile.setGeometry(QtCore.QRect(110, 20, 181, 31))
        self.lineEdit_SortFile.setObjectName("lineEdit_SortFile")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 90, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 72, 15))
        self.label.setObjectName("label")
        SortFile.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SortFile)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 305, 26))
        self.menubar.setObjectName("menubar")
        SortFile.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SortFile)
        self.statusbar.setObjectName("statusbar")
        SortFile.setStatusBar(self.statusbar)

        self.retranslateUi(SortFile)
        QtCore.QMetaObject.connectSlotsByName(SortFile)

    def retranslateUi(self, SortFile):
        _translate = QtCore.QCoreApplication.translate
        SortFile.setWindowTitle(_translate("SortFile", "MainWindow"))
        self.pushButton.setText(_translate("SortFile", "START"))
        self.label.setText(_translate("SortFile", "输入日期"))
