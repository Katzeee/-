from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_getfile import Ui_Form
import sys

"""
class SimpleDialogForm(Ui_Form):#从自动生成的界面类继承

    def __init__(self, parent = None):

        super(SimpleDialogForm, self).__init__()

    def yourFunctions(self):

        Pass

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    main = QtWidgets.QMainWindow()#创建一个主窗体（必须要有一个主窗体）

    content = SimpleDialogForm()#创建对话框

    content.setupUi(main)#将对话框依附于主窗体

    main.show()#主窗体显示

sys.exit(app.exec_())
"""
class SimpleDialogForm(Ui_Form, QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(SimpleDialogForm, self).__init__()
        self.setupUi(self)#在此设置界面

        #在此，可添加自定义的信号绑定
        #self.pushButton.clicked.connect(self.openFile)
        #self.pushButton_2.clicked.connect(self.closeApp)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = SimpleDialogForm()
    main.show()#在外面只需要调用simpleDialogForm显示就行，不需要关注内部如何实现了。
    sys.exit(app.exec_())