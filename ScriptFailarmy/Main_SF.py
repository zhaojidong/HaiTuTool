import multiprocessing
import threading

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer
from qtpy import QtWidgets
from ScriptFailarmy.ScriptFailarmy import Ui_MainWindow
import time, sys
# from ModifyFileName import Main_MFN
# from ScriptFailarmy.ModifyFileName import Main_MFN
import ScriptFailarmy.Data2Shmoo as DS
import ScriptFailarmy.gloVal as glv
import ScriptFailarmy.SortFile as SS_UI

class HT_ScriptFailarmy_UI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):  # parent=None,so the HaiTu_UI is the topmost window
        super(HT_ScriptFailarmy_UI, self).__init__(
            parent)
        self.init()

    def init(self):
        self.setupUi(self)
        self.setWindowTitle('脚本集合')
        # self.progressBar.value(0)
        self.button_handler()

    def button_handler(self):
        self.btn_ModifyFileName.clicked.connect(lambda: HT_ScriptFailarmy_UI.MFN_Fun(self))
        self.btn_DataToShmoo.clicked.connect(lambda: HT_ScriptFailarmy_UI.Data2Shmoo_Folder(self))

    # def MFN_Fun(self):
    #     MFN = Main_MFN.HT_ModifyFileName_UI()
    #     MFN.show()

    def Data2Shmoo_File(self):
        selected_file_list, fileType = QFileDialog.getOpenFileNames(self, "文件选择",
                                                                    r"", "所有文件 (*);;文本文件 (*.txt)")
        print(selected_file_list)
        strT = '<span style=\" color: #ff0000;\">%s</span>' % ('正在运行...')  # 红色
        self.label_runStatus.setAlignment(Qt.AlignHCenter)
        self.label_runStatus.setStyleSheet("background-color:Yellow")
        self.label_runStatus.setFrameShape(QFrame.Box)
        self.label_runStatus.setText("%s" % (strT))
        self.label_runStatus.repaint()
        DS.Data2Shmoo(selected_file_list)
        self.label_runStatus.setStyleSheet("background-color:Yellow")
        strT = '<span style=\" color: #00ff00;\">%s</span>' % ('运行结束！')  # 红色
        self.label_runStatus.setText("%s" % (strT))

    def Data2Shmoo_Folder(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None,"选取文件夹","C:/")
        print(directory)
        strT = '<span style=\" color: #ff0000;\">%s</span>' % ('正在运行...')  # 红色
        self.label_runStatus.setAlignment(Qt.AlignHCenter)
        self.label_runStatus.setStyleSheet("background-color:Yellow")
        self.label_runStatus.setFrameShape(QFrame.Box)
        self.label_runStatus.setText("%s" % (strT))
        self.label_runStatus.repaint()
        DS.Data2Shmoo_Driver7Edge(directory)
        self.label_runStatus.setStyleSheet("background-color:Yellow")
        strT = '<span style=\" color: #00ff00;\">%s</span>' % ('运行结束！')  # 红色
        self.label_runStatus.setText("%s" % (strT))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = QMainWindow()
    HTUI = HT_ScriptFailarmy_UI()
    # SonUI_SF = SS_UI.Ui_SortFile()
    # HTUI.btn_SortFileToNES.clicked.connect(lambda: SonUI_SF.show())
    myWindow.show()
    sys.exit(app.exec_())