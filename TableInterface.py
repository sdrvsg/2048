# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\TableInterface.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(581, 518)
        Dialog.setModal(True)
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(40, 20, 501, 471))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tableWidget = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.btn__close = QtWidgets.QPushButton(self.splitter)
        self.btn__close.setStyleSheet("background-color: rgb(117, 117, 117);\n"
"border-radius: 10px;\n"
"color: #f5f5f5;\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"font-family: sans-serif;")
        self.btn__close.setObjectName("btn__close")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Таблица лидеров"))
        self.btn__close.setText(_translate("Dialog", "Закрыть"))
