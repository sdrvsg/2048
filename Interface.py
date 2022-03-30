# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 736)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setEnabled(False)
        self.widget.setGeometry(QtCore.QRect(140, 170, 461, 431))
        self.widget.setStyleSheet("background-color: rgb(117, 117, 117);\n"
"border-radius: 10px;")
        self.widget.setObjectName("widget")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 771, 141))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.widget_2 = QtWidgets.QWidget(self.splitter)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.layoutWidget = QtWidgets.QWidget(self.widget_2)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 20, 651, 54))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("color: #616161;\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"font-family: sans-serif;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label__score = QtWidgets.QLabel(self.layoutWidget)
        self.label__score.setStyleSheet("color: #616161;\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"font-family: sans-serif;")
        self.label__score.setObjectName("label__score")
        self.verticalLayout.addWidget(self.label__score, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.label__title = QtWidgets.QLabel(self.layoutWidget)
        self.label__title.setStyleSheet("font-size: 30px;\n"
"font-weight: bold;\n"
"color: #616161;\n"
"font-family: sans-serif;")
        self.label__title.setObjectName("label__title")
        self.horizontalLayout.addWidget(self.label__title, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("color: #616161;\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"font-family: sans-serif;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.label__best = QtWidgets.QLabel(self.layoutWidget)
        self.label__best.setStyleSheet("color: #616161;\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"text-transform: uppercase;\n"
"font-family: sans-serif;")
        self.label__best.setObjectName("label__best")
        self.verticalLayout_2.addWidget(self.label__best, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn__restart = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn__restart.setEnabled(True)
        self.btn__restart.setTabletTracking(False)
        self.btn__restart.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn__restart.setAutoFillBackground(False)
        self.btn__restart.setStyleSheet("background-color: transparent;\n"
"color: red;\n"
"font-size: 14px;\n"
"font-weight: bold;")
        self.btn__restart.setObjectName("btn__restart")
        self.horizontalLayout_2.addWidget(self.btn__restart)
        self.btn__change_user = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn__change_user.setEnabled(True)
        self.btn__change_user.setTabletTracking(False)
        self.btn__change_user.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn__change_user.setAutoFillBackground(False)
        self.btn__change_user.setStyleSheet("background-color: transparent;\n"
"color: red;\n"
"font-size: 14px;\n"
"font-weight: bold;")
        self.btn__change_user.setObjectName("btn__change_user")
        self.horizontalLayout_2.addWidget(self.btn__change_user)
        self.btn__table = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn__table.setEnabled(True)
        self.btn__table.setTabletTracking(False)
        self.btn__table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn__table.setAutoFillBackground(False)
        self.btn__table.setStyleSheet("background-color: transparent;\n"
"color: red;\n"
"font-size: 14px;\n"
"font-weight: bold;")
        self.btn__table.setObjectName("btn__table")
        self.horizontalLayout_2.addWidget(self.btn__table)
        self.btn__undo = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn__undo.setEnabled(True)
        self.btn__undo.setTabletTracking(False)
        self.btn__undo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn__undo.setAutoFillBackground(False)
        self.btn__undo.setStyleSheet("background-color: transparent;\n"
"color: red;\n"
"font-size: 14px;\n"
"font-weight: bold;")
        self.btn__undo.setObjectName("btn__undo")
        self.horizontalLayout_2.addWidget(self.btn__undo)
        self.modal__lose = QtWidgets.QPushButton(self.centralwidget)
        self.modal__lose.setEnabled(False)
        self.modal__lose.setGeometry(QtCore.QRect(810, 720, 281, 231))
        self.modal__lose.setFocusPolicy(QtCore.Qt.NoFocus)
        self.modal__lose.setStyleSheet("background-color: #9E9E9E;\n"
"color: #F5F5F5;\n"
"font-weight: bold;\n"
"font-size: 24px;\n"
"border-radius: 10px;")
        self.modal__lose.setObjectName("modal__lose")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "2048"))
        self.label_2.setText(_translate("MainWindow", "score"))
        self.label__score.setText(_translate("MainWindow", "0"))
        self.label__title.setText(_translate("MainWindow", "2048"))
        self.label_4.setText(_translate("MainWindow", "best"))
        self.label__best.setText(_translate("MainWindow", "0"))
        self.btn__restart.setText(_translate("MainWindow", "Рестарт"))
        self.btn__change_user.setText(_translate("MainWindow", "Сменить пользователя"))
        self.btn__table.setText(_translate("MainWindow", "Таблица лидеров"))
        self.btn__undo.setText(_translate("MainWindow", "Отменить"))
        self.modal__lose.setText(_translate("MainWindow", "Вы проиграли"))
