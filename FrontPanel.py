# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrontPanel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 399)
        MainWindow.setStyleSheet("background-image:url(:/icon/11.jfif)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_RawData = QtWidgets.QPushButton(self.centralwidget)
        self.btn_RawData.setGeometry(QtCore.QRect(80, 50, 250, 120))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_RawData.setFont(font)
        self.btn_RawData.setObjectName("btn_RawData")
        self.btn_DataLog = QtWidgets.QPushButton(self.centralwidget)
        self.btn_DataLog.setGeometry(QtCore.QRect(380, 50, 250, 120))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_DataLog.setFont(font)
        self.btn_DataLog.setStyleSheet("")
        self.btn_DataLog.setObjectName("btn_DataLog")
        self.btn_ScriptFailarmy = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ScriptFailarmy.setGeometry(QtCore.QRect(80, 210, 250, 120))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ScriptFailarmy.setFont(font)
        self.btn_ScriptFailarmy.setObjectName("btn_ScriptFailarmy")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 210, 250, 120))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_RawData.setText(_translate("MainWindow", "HANDLE\n"
" RAW DATA"))
        self.btn_DataLog.setText(_translate("MainWindow", "HANDLE\n"
" DATA LOG"))
        self.btn_ScriptFailarmy.setText(_translate("MainWindow", " SCRIPT\n"
" FAILARMY"))
        self.pushButton_4.setText(_translate("MainWindow", "......"))
import image