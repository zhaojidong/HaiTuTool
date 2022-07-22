from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from FrontPanel import Ui_MainWindow
import sys, re, linecache, os, time
from HnadleDataLog import Main_HDL
from ScriptFailarmy import Main_SF
from HandleRAW import Main_HA

class HT_Tool_UI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(HT_Tool_UI, self).__init__(parent)
        self.setupUi(HT_Tool_Win)
        HT_Tool_Win.setWindowTitle('海图微')
        self.init()

    def init(self):
        self.button_events()

    def button_events(self):
        pass
        # self.btn_DataLog.clicked.connect(self.btn_HandleDataLog)  # 点击pushBotton弹出B窗口

    def btn_HandleDataLog(self):
        # self.ui = uic.loadUi(r"C:/007/PythonProject/HaiTuTool/HnadleDataLog/DataAnalysis.ui")
        # self.ui.show()

        # self.UI_HandleDataLog = QMainWindow()
        # UI_HDL = Main_HDL.Ui_MainWindow()
        # UI_HDL.setupUi(self.UI_HandleDataLog)
        # self.UI_HandleDataLog.show()
        # Main_HDL.HT_DataAnalysis_UI()
        pass





if __name__ == '__main__':
    app = QApplication(sys.argv)
    HT_Tool_Win = QMainWindow()
    HTUI = HT_Tool_UI()
    HT_Tool_Win.setFixedSize(HT_Tool_Win.width(), HT_Tool_Win.height())  # Fix the window's size
    UI_HDL = Main_HDL.HT_DataAnalysis_UI()
    UI_SF = Main_SF.HT_ScriptFailarmy_UI()
    UI_HA = Main_HA.HT_HandleRAW_UI()
    HTUI.btn_DataLog.clicked.connect(lambda: UI_HDL.show())
    HTUI.btn_ScriptFailarmy.clicked.connect(lambda: UI_SF.show())
    HTUI.btn_RawData.clicked.connect(lambda: UI_HA.show())
    HT_Tool_Win.show()
    sys.exit(app.exec_())


