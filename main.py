from PySide2.QtWidgets import QApplication, QMessageBox, QTableWidgetItem, QFileDialog  # 引用QTableWidgetItem是为了往表格里面放东西
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, QIODevice, QUrl
from PySide2.QtGui import QDesktopServices
import os
from os import stat
from lib.share import SI
import time
import sys
from PySide2.QtWidgets import QApplication, QLabel
import win32file
import win32con
import pandas as pd
from toolkit import *

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
        self.ui.wgt_table.setRowCount(50)
        self.ui.edt_getAddress.returnPressed.connect(self.edt_getAddress_text_changed)

    def open_mainwindow(self):


        SI.mainWin = MainWin()  # 实例化另外一个窗口
        SI.mainWin.ui.show()  # 显示新窗口
        self.ui.hide()  # 隐藏自己

    def edt_getAddress_text_changed(self):
        #QDesktopServices.openUrl(QUrl("C:/", QUrl.TolerantMode))
        #QFileDialog.getOpenFileName(dir="C:/")
        fileNeedSerching = QFileDialog.getExistingDirectory(dir="C:/")


        #fileNeedSerching = self.ui.edt_getAddress.text()
        # time.localtime(statinfo.st_ctime)
        self.allFileInfo = pd.DataFrame(columns = ['fileName', 'fileType', 'fileModifyDate', 'fileSize'])

        self.getDir(fileNeedSerching)

        self.wgt_table_show()

    def wgt_table_show(self):
        #print(self.allFileInfo)
        num = len(self.allFileInfo.index)
        self.ui.wgt_table.setRowCount(num)
        for index, row in self.allFileInfo.iterrows():
            self.ui.wgt_table.setItem(index, 0, QTableWidgetItem(row['fileName']))
            self.ui.wgt_table.setItem(index, 1, QTableWidgetItem(row['fileType']))
            self.ui.wgt_table.setItem(index, 2, QTableWidgetItem(row['fileModifyDate']))
            self.ui.wgt_table.setItem(index, 3, QTableWidgetItem(f"{row['fileSize']}"))#此行不同的原因是什么呢？


    def getDir(self, directory):
        # self.allFiles = {}!不能定义在这，因为在else中会被初始化，用于保存目录文件
        dirNames = os.listdir(directory)  # 获取目录下所有一层文件与文件夹名

        for dirName in dirNames:  # 遍历每个文件
            dirAddress = directory + '/' + dirName  # 获取绝对路径
            fileFlag = win32file.GetFileAttributesW(dirAddress)
            isHidden = fileFlag & win32con.FILE_ATTRIBUTE_HIDDEN
            isSystem = fileFlag & win32con.FILE_ATTRIBUTE_SYSTEM
            statInfo = os.stat(dirAddress)
            '''
            statInfo返回一个tuple，os.stat_result(st_mode=33206, st_ino=1125899906860840, st_dev=4199183826, st_nlink=1, 
            st_uid=0, st_gid=0, st_size=80, st_atime=1616486743, st_mtime=1616485640, st_ctime=1616485640)
            采取数字索引，size(6)代表其大小，单位为字节，mtime（8）代表其修改时间
            '''
            # 这里这么判断是有问题的，建议好好思考一下
            if os.path.isfile(dirAddress) and (not isHidden) and (not isSystem):  # 判断是否为隐藏、系统普通文件，若是则直接输出
                new = pd.DataFrame({'fileName' : dirName, 'fileType' : '', 'fileModifyDate' : stamp2string(statInfo[8]), 'fileSize' : statInfo[6]}, index=[1])
                self.allFileInfo = self.allFileInfo.append(new,ignore_index=True)

            else:
                new = pd.DataFrame({'fileName' : dirName, 'fileType' : 'Folder', 'fileModifyDate' : stamp2string(statInfo[8]), 'fileSize' : statInfo[6]}, index=[1])
                self.allFileInfo = self.allFileInfo.append(new,ignore_index=True)
                self.getDir(dirAddress)

#测试地址：E:\github codes\FileManager\lib


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
    app = QApplication(sys.argv)
    SI.getfileWin = GetFile()
    SI.getfileWin.ui.show()
    sys.exit(app.exec_())

