from PyQt5.QtWidgets import *
import sys, os, ntpath
from ScriptFailarmy.ScriptFailarmy import Ui_MainWindow
# from ModifyFileName import Main_MFN
# from ScriptFailarmy.ModifyFileName import Main_MFN


class HT_ScriptFailarmy_UI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):  # parent=None,so the HaiTu_UI is the topmost window
        super(HT_ScriptFailarmy_UI, self).__init__(
            parent)
        self.init()

    def init(self):
        self.setupUi(self)
        self.setWindowTitle('脚本集合')
        # self.button_handler()

    def button_handler(self):
        self.btn_ModifyFileName.clicked.connect(lambda: self.MFN_Fun())

    def MFN_Fun(self):
        MFN = Main_MFN.HT_ModifyFileName_UI()
        MFN.show()