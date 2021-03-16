from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader

import os

from lib.share import SI

class GetFile :

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('getfile.ui')

        self.ui.btn_myFile.clicked.connect(self.open_mainwindow)


    def open_mainwindow(self):

        SI.mainWin = MainWin()    # 实例化另外一个窗口
        SI.mainWin.ui.show()      # 显示新窗口
        self.ui.hide()            # 隐藏自己

 #   def getDir(self):
 #       dirNames = os.listdir(self)  # 获取目录下所有一层文件与文件夹名
 #        for dirName in dirNames:  # 遍历每个文件
 #           dirName = self + '/' + dirName  # 获取绝对路径
 #           if os.path.isfile(dirName):  # 判断是否为文件，若是则直接输出
 #               print('[+]' + dirName)
 #           else:
 #               getDir(dirName)
 #               print('[-]' + dirName)  # 若不是则继续深入遍历

 #       QMessageBox.about(self.ui)


class MainWin :
    def __init__(self):
        self.ui = QUiLoader().load('mainwin.ui')
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

class ManageCenter :
    def __init__(self):
        self.ui = QUiLoader().load('managecenter.ui')
     #   self.ui.btn_backManWin.clicked.connect(self.open_mainwindow)



app = QApplication([])
#SI.getfileWin = GetFile()
#SI.getfileWin.ui.show()
app.exec_()