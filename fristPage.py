# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\term5\tabibPy\GUI-using-PyQT5-python-master\GUI-using-PyQT5-python-master\Login Page with Database\firstPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from login import *
from database_create import *

class Ui_First(object):
    # switch_window = QtCore.pyqtSignal(str)

    def setupUi(self, First):
        d = Database_create()
        d.create()

        First.setObjectName("First")
        First.resize(574, 335)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        First.setFont(font)
        self.centralwidget = QtWidgets.QWidget(First)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.doctor = QtWidgets.QPushButton(self.centralwidget)
        self.doctor.setObjectName("doctor")
        self.gridLayout.addWidget(self.doctor, 1, 0, 1, 1)
        self.patient = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.patient.setFont(font)
        self.patient.setObjectName("patient")
        self.gridLayout.addWidget(self.patient, 1, 1, 1, 1)
        self.admin = QtWidgets.QPushButton(self.centralwidget)
        self.admin.setObjectName("admin")
        self.gridLayout.addWidget(self.admin, 2, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        First.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(First)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 574, 18))
        self.menubar.setObjectName("menubar")
        First.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(First)
        self.statusbar.setObjectName("statusbar")
        First.setStatusBar(self.statusbar)

        self.retranslateUi(First)
        QtCore.QMetaObject.connectSlotsByName(First)

        self.patient.clicked.connect(self.btn_patient)
        self.doctor.clicked.connect(self.btn_doctor)
        self.admin.clicked.connect(self.btn_admin)
    
    def btn_admin(self):
        self.openwindow(Ui_Form_admin)
    def btn_doctor(self):
        self.openwindow(Ui_Form_doctor)
    def btn_patient(self):
        self.openwindow(Ui_Form)

    def openwindow(self,Ui):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui()
        self.ui.setupUi(self.window)
        self.window.show()
        First.hide()

    def pop_message(self,text):
        msg=QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def retranslateUi(self, First):
        _translate = QtCore.QCoreApplication.translate
        First.setWindowTitle(_translate("First", "First"))
        self.label.setText(_translate("First", "طبیب یاب"))
        self.doctor.setText(_translate("First", "ورود پزشک"))
        self.patient.setText(_translate("First", "ورود بیمار"))
        self.admin.setText(_translate("First", "مدیر"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    First = QtWidgets.QMainWindow()
    ui = Ui_First()
    ui.setupUi(First)
    First.show()
    sys.exit(app.exec_())

    # app = QtWidgets.QApplication(sys.argv)
    # controller = Controller()
    # controller.show_login()
    # sys.exit(app.exec_())

# class Controller:

#     def __init__(self):
#         pass

#     def show_login(self):
#         self.login = Login()
#         self.login.switch_window.connect(self.show_main)
#         self.login.show()

#     def show_main(self):
#         self.window = MainWindow()
#         self.window.switch_window.connect(self.show_window_two)
#         self.login.close()
#         self.window.show()

#     def show_window_two(self, text):
#         self.window_two = WindowTwo(text)
#         self.window.close()
#         self.window_two.show()

