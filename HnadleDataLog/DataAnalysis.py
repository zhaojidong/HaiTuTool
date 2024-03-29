# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataAnalysis.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1604, 801)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tree = QtWidgets.QTreeWidget(self.centralwidget)
        self.tree.setGeometry(QtCore.QRect(10, 0, 351, 451))
        self.tree.setAutoExpandDelay(-1)
        self.tree.setObjectName("tree")
        self.tree.headerItem().setText(0, "请选择目标文件夹...")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 460, 351, 311))
        self.textEdit.setObjectName("textEdit")
        self.btn_yeild = QtWidgets.QPushButton(self.centralwidget)
        self.btn_yeild.setGeometry(QtCore.QRect(370, 10, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.btn_yeild.setFont(font)
        self.btn_yeild.setStyleSheet("color: rgb(0, 170, 127);")
        self.btn_yeild.setObjectName("btn_yeild")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(890, 551, 711, 181))
        self.tableWidget.setStyleSheet("selection-background-color: rgb(85, 255, 127);")
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(255, 170, 0))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(85, 170, 127))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(480, 50, 131, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.btn_abort = QtWidgets.QPushButton(self.centralwidget)
        self.btn_abort.setGeometry(QtCore.QRect(480, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_abort.setFont(font)
        self.btn_abort.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 127);")
        self.btn_abort.setObjectName("btn_abort")
        self.tabel_WaferMap = QtWidgets.QTableWidget(self.centralwidget)
        self.tabel_WaferMap.setGeometry(QtCore.QRect(365, 501, 321, 271))
        self.tabel_WaferMap.setObjectName("tabel_WaferMap")
        self.tabel_WaferMap.setColumnCount(0)
        self.tabel_WaferMap.setRowCount(0)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(371, 84, 239, 104))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox_chart = QtWidgets.QComboBox(self.widget)
        self.comboBox_chart.setObjectName("comboBox_chart")
        self.comboBox_chart.addItem("")
        self.comboBox_chart.addItem("")
        self.comboBox_chart.addItem("")
        self.comboBox_chart.addItem("")
        self.comboBox_chart.addItem("")
        self.comboBox_chart.addItem("")
        self.comboBox_chart.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_chart)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox_report = QtWidgets.QComboBox(self.widget)
        self.comboBox_report.setObjectName("comboBox_report")
        self.comboBox_report.addItem("")
        self.comboBox_report.addItem("")
        self.comboBox_report.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_report)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboBox_SaveOpt = QtWidgets.QComboBox(self.widget)
        self.comboBox_SaveOpt.setObjectName("comboBox_SaveOpt")
        self.comboBox_SaveOpt.addItem("")
        self.comboBox_SaveOpt.addItem("")
        self.comboBox_SaveOpt.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_SaveOpt)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox_logMode = QtWidgets.QComboBox(self.widget)
        self.comboBox_logMode.setObjectName("comboBox_logMode")
        self.comboBox_logMode.addItem("")
        self.comboBox_logMode.addItem("")
        self.comboBox_logMode.addItem("")
        self.comboBox_logMode.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_logMode)
        self.ChartHtml = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.ChartHtml.setGeometry(QtCore.QRect(689, 1, 911, 541))
        self.ChartHtml.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ChartHtml.setAutoFillBackground(False)
        self.ChartHtml.setStyleSheet("")
        self.ChartHtml.setUrl(QtCore.QUrl("about:blank"))
        self.ChartHtml.setObjectName("ChartHtml")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1604, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_yeild.setText(_translate("MainWindow", "Start"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "TestItem"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Average"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Median"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Stdev"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Cp"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Cpk"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Yeild"))
        self.btn_abort.setText(_translate("MainWindow", "Stop Working"))
        self.label_2.setText(_translate("MainWindow", "ChartOption"))
        self.comboBox_chart.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox_chart.setItemText(1, _translate("MainWindow", "BoxPlots"))
        self.comboBox_chart.setItemText(2, _translate("MainWindow", "LineChart"))
        self.comboBox_chart.setItemText(3, _translate("MainWindow", "ScatterDiagram"))
        self.comboBox_chart.setItemText(4, _translate("MainWindow", "Histogram"))
        self.comboBox_chart.setItemText(5, _translate("MainWindow", "CurveChart"))
        self.comboBox_chart.setItemText(6, _translate("MainWindow", "NormalDistribution"))
        self.label_3.setText(_translate("MainWindow", "ReportOption"))
        self.comboBox_report.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox_report.setItemText(1, _translate("MainWindow", "VP"))
        self.comboBox_report.setItemText(2, _translate("MainWindow", "Normal"))
        self.label.setText(_translate("MainWindow", "SaveOption"))
        self.comboBox_SaveOpt.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox_SaveOpt.setItemText(1, _translate("MainWindow", "Separation"))
        self.comboBox_SaveOpt.setItemText(2, _translate("MainWindow", "Combination"))
        self.label_4.setText(_translate("MainWindow", "LogMode"))
        self.comboBox_logMode.setItemText(0, _translate("MainWindow", "Debug"))
        self.comboBox_logMode.setItemText(1, _translate("MainWindow", "Wafer"))
        self.comboBox_logMode.setItemText(2, _translate("MainWindow", "FT"))
        self.comboBox_logMode.setItemText(3, _translate("MainWindow", "CP"))
        self.ChartHtml.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Chart</span></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
from PyQt5 import QtWebEngineWidgets
