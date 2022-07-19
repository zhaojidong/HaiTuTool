from PyQt5.QtWidgets import *
import sys, os, ntpath
# from ModifyFileName import Ui_MainWindow
# from About import Ui_MainWindow as About_UI
from About_Dialog import Ui_Dialog as About_Dialog_UI

class HT_ModifyFileName_UI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):  # parent=None,so the HaiTu_UI is the topmost window
        super(HT_ModifyFileName_UI, self).__init__(
            parent)
        self.files = None
        self.log_path = None
        self.init()

    def init(self):
        self.setupUi(myWindow)
        myWindow.setWindowTitle('修改文件名')
        self.button_handler()

    def button_handler(self):
        self.pushButton.clicked.connect(lambda: self.modifyName())
        self.actionOpen.triggered.connect(lambda: HT_ModifyFileName_UI.actionOpen(self))
        # self.actionAbout.triggered.connect(lambda: HT_ModifyFileName_UI.actionAbout(self))

    def actionOpen(self):
        self.log_path = QFileDialog.getExistingDirectory(self, 'Select a directory', r"C:\007\PythonProject")
        self.files = os.listdir(self.log_path)
        # print(selected_file_list)
        # print(fileType)
        print(self.log_path)

    def modifyName(self):
        add_item = self.add_item.text()
        delete_item = self.delete_item()
        print('target_text:', add_item)
        print(os.path.basename(self.log_path))
        for file in self.files:
            filename, extension = os.path.splitext(file)
            if len(filename) == 1:
                # add 00 to file name
                src = self.log_path + '\\' + file
                dsc = self.log_path + '\\' + '00' + filename + add_item + extension
                os.rename(src, dsc)
            elif len(filename) == 2:
                # add 0 to file name
                src = self.log_path + '\\' + file
                dsc = self.log_path + '\\' + '0' + filename + add_item + extension
                os.rename(src, dsc)
            else:
                src = self.log_path + '\\' + file
                dsc = self.log_path + '\\' + filename + add_item + extension
                os.rename(src, dsc)
        print(os.path.basename(self.log_path))
        if not len(delete_item):
            for file in self.files:
                filename, extension = os.path.splitext(file)
            pass

    def actionAbout(self):
        self.aboutWin = AboutWindow_UI()
        # self.aboutWin.show()
        # self.aboutWin.exec_()


class AboutWindow_UI(QMainWindow, About_UI):
    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        # aboutWin = QMainWindow()
        self.setupUi(self)
        self.setWindowTitle('About')
        self.displayInfo()
        # aboutWin.show()
        # aboutWin.exec_()
        self.pushButton.clicked.connect(lambda: self.close())
    def displayInfo(self):
        self.Info_text.setText('Hello world!!!!!!!')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = QMainWindow()
    HTUI = HT_ModifyFileName_UI()
    b1 = AboutWindow_UI()
    HTUI.actionAbout.triggered.connect(lambda: b1.show())
    myWindow.show()
    sys.exit(app.exec_())

