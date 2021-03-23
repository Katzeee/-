from PySide2.QtWidgets import QApplication, QMessageBox, QTableWidgetItem  # 引用QTableWidgetItem是为了往表格里面放东西
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QIODevice
import os
from os import stat
from lib.share import SI
import time
import sys
from PySide2.QtWidgets import QApplication, QLabel
import win32file
import win32con


class GetFile:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.pwd = os.path.dirname(__file__)  # 获取当前文件路径
        self.ui = QUiLoader().load(self.pwd + '/getfile.ui')  # 确定与工作路径一致

        # 按钮定义
        self.ui.btn_myFile.clicked.connect(self.open_mainwindow)
        # 即时改变
        self.ui.wgt_table.setRowCount(50)
        self.ui.edt_getAddress.returnPressed.connect(self.edt_getAddress_text_changed)
        # self.ui.wgt_table.viewport().update()

    def open_mainwindow(self):

        SI.mainWin = MainWin()  # 实例化另外一个窗口
        SI.mainWin.ui.show()  # 显示新窗口
        self.ui.hide()  # 隐藏自己

    def edt_getAddress_text_changed(self):
        fileNeedSerching = self.ui.edt_getAddress.text()
        self.allFiles = {}  # 初始化保存目录
        self.allSizes = {}
        self.allTimes = {}  # time.localtime(statinfo.st_ctime)
        self.getDir(fileNeedSerching)
        print(self.allFiles)
        print(self.allSizes)
        self.wgt_table_show()

    def wgt_table_show(self):
        i = 0
        num = len(self.allFiles)
        self.ui.wgt_table.setRowCount(num)
        for dirName, dirIsFile in self.allFiles.items():
            self.ui.wgt_table.setItem(i, 0, QTableWidgetItem(dirName))

         #   if dirIsFile == 0:
         #       self.ui.wgt_table.setItem(i, 2, QTableWidgetItem(dirIsFile))
         #  else:
         #      self.ui.wgt_table.setItem(i, 2, QTableWidgetItem(dirIsFile))
            i = i + 1
        self.ui.wgt_table.viewport().update()

    def getDir(self, directory):
        # self.allFiles = {}!不能定义在这，因为在else中会被初始化，用于保存目录文件
        dirNames = os.listdir(directory)  # 获取目录下所有一层文件与文件夹名

        for dirName in dirNames:  # 遍历每个文件
            dirAddress = directory + '/' + dirName  # 获取绝对路径
            fileFlag = win32file.GetFileAttributesW(dirAddress)
            isHidden = fileFlag & win32con.FILE_ATTRIBUTE_HIDDEN
            isSystem = fileFlag & win32con.FILE_ATTRIBUTE_SYSTEM
            statInfo = os.stat(dirAddress)
            if os.path.isfile(dirAddress) and (not isHidden) and (not isSystem):  # 判断是否为隐藏、系统普通文件，若是则直接输出
                self.allFiles.update({dirName: 1})  # 将其加入字典
                self.allSizes.update({statInfo.st_size})

            else:
                self.allFiles.update({dirName: 0})
                self.getDir(dirAddress)


#                # 若不是则继续深入遍历

#       QMessageBox.about(self.ui)


class MainWin:
    def __init__(self):
        self.pwd = os.path.dirname(__file__)
        self.ui = QUiLoader().load(self.pwd + '/mainwin.ui')
        self.ui.btn_backFile.clicked.connect(self.open_getfile)
        self.ui.btn_manageCenter.clicked.connect(self.open_manageCenter)

    def open_getfile(self):
        SI.getfileWin = GetFile()
        SI.getfileWin.ui.show()
        self.ui.hide()

    def open_manageCenter(self):
        SI.manageCenterWin = ManageCenter()
        SI.manageCenterWin.ui.show()
        self.ui.hide()


class ManageCenter:
    def __init__(self):
        self.pwd = os.path.dirname(__file__)
        self.ui = QUiLoader().load(self.pwd + '/managecenter.ui')
        self.ui.btn_backMainWin.clicked.connect(self.open_mainwindow)

    def open_mainwindow(self):
        SI.mainWin = MainWin()
        SI.mainWin.ui.show()
        self.ui.hide()


if __name__ == "__main__":
    # print(str("123"))
    app = QApplication(sys.argv)
    SI.getfileWin = GetFile()
    SI.getfileWin.ui.show()
    sys.exit(app.exec_())

