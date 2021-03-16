# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\github codes\FileManager\FM\getfile.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 501, 431))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_myFile = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_myFile.setObjectName("btn_myFile")
        self.gridLayout.addWidget(self.btn_myFile, 0, 1, 1, 1)
        self.edt_getAddress = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.edt_getAddress.setObjectName("edt_getAddress")
        self.gridLayout.addWidget(self.edt_getAddress, 0, 0, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 2, 1, 1, 1)
        self.wgt_table = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.wgt_table.setObjectName("wgt_table")
        self.wgt_table.setColumnCount(5)
        self.wgt_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.wgt_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.wgt_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.wgt_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.wgt_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.wgt_table.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.wgt_table, 1, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "File Management"))
        self.btn_myFile.setText(_translate("Form", "我的文件"))
        self.edt_getAddress.setPlaceholderText(_translate("Form", "请输入文件所在盘"))
        self.btn_clear.setText(_translate("Form", "清除缓存"))
        item = self.wgt_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "名称"))
        item = self.wgt_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "类型"))
        item = self.wgt_table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "修改日期"))
        item = self.wgt_table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "文件大小"))
