# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mylogin.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from mysignup1 import  *
from PyQt5 import QtWidgets
import sqlite3
from lastmainpageUI import *


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.phone = QtWidgets.QLineEdit(self.centralwidget)
        self.phone.setObjectName("phone")
        self.verticalLayout.addWidget(self.phone)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setObjectName("login")
        self.verticalLayout.addWidget(self.login)
        self.signup = QtWidgets.QPushButton(self.centralwidget)
        self.signup.setObjectName("signup")
        self.verticalLayout.addWidget(self.signup)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        Form.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 18))
        self.menubar.setObjectName("menubar")
        Form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.signup.clicked.connect(self.btn_newuser_handler)
        self.login.clicked.connect(self.btn_login_handler)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ورود بیمار"))
        self.label_2.setText(_translate("Form", "شماره تلفن همراه"))
        self.label_3.setText(_translate("Form", "رمز عبور"))
        self.login.setText(_translate("Form", "ورود"))
        self.signup.setText(_translate("Form", "کاربر جدید؟"))

    def pop_window(self,text):

        msg = QtWidgets.QMessageBox()

        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("{}".format(text))
        # msg.setInformativeText('{}'.format(text))
        msg.setWindowTitle("خطا")

        msg.exec_()


    def btn_newuser_handler(self):
        self.openwindow()
    
    def openwindow(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Signup()
        self.ui.setupUi(self.window)
        self.window.show()
        # Form.hide()

    def pop_message(self,text,error):
        msg=QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.setWindowTitle(error)
        msg.exec_()

    def btn_login_handler(self):

        if len(self.password.text()) < 8:
            self.pop_window('رمزعبور کمتر از 8 حرف است')

        else:
            phone = self.phone.text()
            password = self.password.text()

            conn = sqlite3.connect('tabib.db')
            cursor = conn.cursor()

            cursor.execute("SELECT phone FROM USER WHERE phone = ?  ",(phone, ))
            val = cursor.fetchall()

            if len(val) != 1: 
                self.pop_message("کاربری یافت نشد","خطا")
            else:
                cursor.execute("SELECT phone,password FROM USER WHERE  phone = ? and password = ?  ",(phone,password, ))
                val = cursor.fetchall()
                if len(val) != 1:
                    self.pop_message('رمز عبور اشتباه است',"خطا")
                else:
                    self.pop_message('خوش آمدید','تبریک')
                    print('خوش آمدید')       #TODO: as notification
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Ui_MainWindow(phone)
                    self.ui.setupUi(self.window)
                    self.window.show()
            conn.commit()
            cursor.close()
            conn.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()

    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
