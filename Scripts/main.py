from PySide2.QtWidgets import *
from PySide2.QtUiTools import *
import os
from lib.share import SI
from lib.data import *
import sys
import time
import threading
import pandas as pd
from toolkit import *
from SubWindowBase import *



class MainWin(QMainWindow):

# region singlaton
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        time.sleep(1)
        if not hasattr(cls, "_instance"):
            with cls._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super().__new__(cls)
        return cls._instance
# endregion
    
    def __init__(self):
        super().__init__()
        self.pwd = os.path.abspath('.')  # 获取当前文件路径
        self.ui = QUiLoader().load(self.pwd + '.\\Ui\\mainWin.ui')  # 确定与工作路径一致
        QApplication.setStyle(QStyleFactory.create('Fusion'))
        

        # 初始化subwin防奇怪bug
        subWindow = QMdiSubWindow()
        subWindow.setParent(self.ui.mdiArea)
        subWindow.close()

        #初始化类参数
        self.outputNumber = {'SearchDirWin' : 1, 'SearchNameWin' : 1, 'SearchTypeWin' : 1, 'SearchDiffWin' : 1, 'SearchDupWin' : 1} #输出文件编号
        self.allThread = [] #所有线程
         
        # 绑定Menubar
        self.ui.newProject.triggered.connect(self.menuNewProject)
        self.ui.addFile.triggered.connect(self.menuSearchDiff)
        self.ui.addFolder.triggered.connect(self.menuSearchDup)
        self.ui.searchNull.triggered.connect(self.menuSearchNull)
        self.ui.searchDup.triggered.connect(self.menuSearchDup)
        self.ui.searchDiff.triggered.connect(self.menuSearchDiff)
        self.ui.searchFile.triggered.connect(self.menuSearchFile)
        self.ui.outList.triggered.connect(self.menuOutList)
        self.ui.help.triggered.connect(self.menuHelp)
        self.ui.exit.triggered.connect(self.menuExit)

        #绑定TreeWidget
        self.ui.treeWidget.itemClicked.connect(self.TreeWidgetClicked)
    
    def TreeWidgetClicked(self, item, n):
        selectedParent = item.parent()
        if selectedParent is None:
            return
        parentNumber = self.ui.treeWidget.indexOfTopLevelItem(selectedParent)
        childNumber = selectedParent.indexOfChild(item)
        # print(parentNumber,childNumber)
        if parentNumber == 0:
            if childNumber == 0:
                self.menuSearchDup()
            if childNumber == 1:
                self.menuSearchDiff()
        elif parentNumber == 1:
            if childNumber == 0:
                self.menuOutList()
        elif parentNumber == 2:
            if childNumber == 0:
                self.menuSearchFile()



    def closeEvent(self, event):
        print(1)
    

    def menuNewProject(self):
        t = SearchDirSubWindow()
        self.allThread.append(t)
        t.daemon = True
        t.start()
        print("new project")


    def menuAddFile(self):
        t = SearchDiffSubWindow()
        self.allThread.append(t)
        t.daemon = True
        t.start()
        print("Search Diff")

    def menuAddFolder(self):
        t = SearchTypeSubWindow()
        self.allThread.append(t)
        t.daemon = True
        t.start()
        print("add folder")

    def menuSearchNull(self):
        print("Search Null")
    def menuSearchDup(self):
        t = SearchDupSubWindow()
        self.allThread.append(t)
        t.daemon = True
        t.start()
        print("Search Dup")


    def menuSearchDiff(self):
        t = SearchDiffSubWindow()
        self.allThread.append(t)
        t.daemon = True
        t.start()
        print("Search Diff")

    def menuSearchFile(self):
        t = SearchNameSubWindow()
        self.allThread.append(t)
        t.daemon = True
        t.start()
        print("Search file")

    def menuOutList(self):
        print("Out List")
        activeWindow = self.ui.mdiArea.activeSubWindow()
        subWindow = SI.SubWindowManager.GetSubWindow(activeWindow)
        if subWindow == None: #如果未选中窗口
            return

        winType = subWindow.GetWindowType()
        outResualt = subWindow.Output(self.outputNumber[winType])
        if outResualt:
            if outResualt.split('.')[0] == f"Output{self.outputNumber[winType]}":
                self.outputNumber[winType] += 1
         
        


    def menuHelp(self):
        print("Help")


    def menuExit(self):
        self.ui.close()


        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    SI.SubWindowManager = SubWindowManager()
    SI.MainWin = MainWin()
    SI.MainWin.ui.show()
    sys.exit(app.exec_())


