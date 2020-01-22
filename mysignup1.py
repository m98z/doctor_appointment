# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\term5\tabibPy\GUI-using-PyQT5-python-master\GUI-using-PyQT5-python-master\Login Page with Database\signup.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from login import *
import sqlite3
from database_create import *


class Ui_Signup(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SignUp")
        MainWindow.resize(702, 371)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setAutoFillBackground(False)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.lastname = QtWidgets.QLineEdit(self.centralwidget)
        self.lastname.setObjectName("lastname")
        self.verticalLayout.addWidget(self.lastname)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.female = QtWidgets.QRadioButton(self.centralwidget)
        self.female.setObjectName("female")
        self.horizontalLayout.addWidget(self.female)
        self.male = QtWidgets.QRadioButton(self.centralwidget)
        self.male.setObjectName("male")
        self.horizontalLayout.addWidget(self.male)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.insurance = QtWidgets.QComboBox(self.centralwidget)
        self.insurance.setObjectName("insurance")
        self.verticalLayout.addWidget(self.insurance)

        self.selectCombobox(self.insurance)
        
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.phone = QtWidgets.QLineEdit(self.centralwidget)
        self.phone.setObjectName("phone")
        self.verticalLayout_2.addWidget(self.phone)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.firstname = QtWidgets.QLineEdit(self.centralwidget)
        self.firstname.setObjectName("firstname")
        self.verticalLayout_2.addWidget(self.firstname)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_2.addWidget(self.dateEdit)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.photo = QtWidgets.QLineEdit(self.centralwidget)
        self.photo.setObjectName("photo")
        self.verticalLayout_2.addWidget(self.photo)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setObjectName("submit")
        self.verticalLayout_3.addWidget(self.submit)
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setObjectName("exit")
        self.verticalLayout_3.addWidget(self.exit)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 506, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.exit.clicked.connect(self.btn_exit_handler)
        self.submit.clicked.connect(self.database)

    def pop_window(self,text):

        msg = QtWidgets.QMessageBox()

        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("{}".format(text))
        msg.setWindowTitle("خطا")

        msg.exec_()

    def btn_exit_handler(self):
        self.openwindow()

    def openwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form() #go to login user
        self.ui.setupUi(self.window)
        self.window.show()
        

    def pop_message(self,text):
        msg=QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.setWindowTitle("خطا")
        msg.exec_()

    def selectCombobox(self,ins):
        # self.insurance = ins
        conn=sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        cursor.execute(""" select * from INSURANCE """)
        insurance_list = cursor.fetchall()
        insurance_name = []
        for x in insurance_list:
            insurance_name.append(x[1])
        

        conn.commit()
        cursor.close()
        conn.close()
        ins.addItems(insurance_name)


    def database(self):
        d = Database_create()
        d.create()
        try:
            db_phone = self.phone.text()
            db_password = self.password.text()
            if len(db_password) < 8:
                self.pop_window('رمزعبور کمتر از 8 حرف است')
            else:
                
                db_firstname = self.firstname.text()
                db_lastname = self.lastname.text()
                db_photo = self.photo.text()

                db_insurance_name = str(self.insurance.currentText())    
                if self.female.isChecked() == True:
                    db_gender_id = 0
                elif self.male.isChecked()== True:
                    db_gender_id = 1
                else:
                    db_gender_id = None

                db_date = str(self.dateEdit.date().year()) +"/" + str(self.dateEdit.date().month())+"/"+str(self.dateEdit.date().day())

                conn=sqlite3.connect('tabib.db')
                cursor = conn.cursor()

                cursor.execute("""
                    SELECT insuranceId FROM INSURANCE
                    WHERE name = ?            
                """,(db_insurance_name,))
                db_insurance_id = cursor.fetchall()[0][0] 
                

                cursor.execute(""" INSERT INTO USER 
                    (phone,
                    fname,
                    lname,
                    photo,
                    Birth_day,
                    password, 
                    genderId,
                    insuranceId
                    )
                    
                VALUES(?,?,?,?,?,?,?,?)
                """,(db_phone,db_firstname,db_lastname,db_photo,db_date,db_password,db_gender_id,db_insurance_id))

                conn.commit()
                cursor.close()
                conn.close()
                self.pop_message("Added to  Database ")
        except :
            # print(err)
            self.pop_message("شماره تلفن همراه تکراریست")
            # self.btn_exit_handler()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_1.setText(_translate("MainWindow", "رمز ورود"))
        self.label_3.setText(_translate("MainWindow", "نام خانوادگی"))
        self.label_5.setText(_translate("MainWindow", "جنسیت"))
        self.female.setText(_translate("MainWindow", "زن"))
        self.male.setText(_translate("MainWindow", "مرد"))
        self.label_7.setText(_translate("MainWindow", "بیمه"))
        self.label_2.setText(_translate("MainWindow", "شماره تلفن همراه"))
        self.label_4.setText(_translate("MainWindow", "نام"))
        self.label_6.setText(_translate("MainWindow", "تاریخ تولد"))
        self.label_8.setText(_translate("MainWindow", "عکس"))
        self.submit.setText(_translate("MainWindow", "ثبت نام"))
        self.exit.setText(_translate("MainWindow", "خروج"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Signup()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
