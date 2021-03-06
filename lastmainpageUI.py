# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\term5\tabibPy\GUI-using-PyQT5-python-master\GUI-using-PyQT5-python-master\Login Page with Database\tap.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import sqlite3
from login import *
from mysignup1 import *
from doctor_profile import *
from get_appointment import *

class Ui_MainWindow(object):
    def __init__(self,phone):
        self.phone = phone

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.sfdg = QtWidgets.QWidget()
        self.sfdg.setObjectName("sfdg")
        self.label_6 = QtWidgets.QLabel(self.sfdg)
        self.label_6.setGeometry(QtCore.QRect(150, 10, 371, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(self.sfdg)
        self.label_12.setGeometry(QtCore.QRect(414, 50, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        
        self.ph = QtWidgets.QLabel(self.sfdg)
        self.ph.setGeometry(QtCore.QRect(524, 50, 231, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ph.setFont(font)
        self.ph.setObjectName("ph")
        self.ph.setText("شماره تلفن همراه:")

        self.ph1 = QtWidgets.QLabel(self.sfdg)
        self.ph1.setGeometry(QtCore.QRect(624, 80, 151, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ph1.setFont(font)
        self.ph1.setObjectName("ph1")

        self.fname = QtWidgets.QLineEdit(self.sfdg)
        self.fname.setGeometry(QtCore.QRect(392, 80, 161, 25))
        self.fname.setObjectName("fname")
        self.label_15 = QtWidgets.QLabel(self.sfdg)
        self.label_15.setGeometry(QtCore.QRect(214, 50, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.lname = QtWidgets.QLineEdit(self.sfdg)
        self.lname.setGeometry(QtCore.QRect(192, 80, 161, 25))
        self.lname.setObjectName("lname")
        self.label_16 = QtWidgets.QLabel(self.sfdg)
        self.label_16.setGeometry(QtCore.QRect(414, 120, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.combo_insurance_panel = QtWidgets.QComboBox(self.sfdg)
        self.combo_insurance_panel.setGeometry(QtCore.QRect(392, 150, 161, 25))
        self.combo_insurance_panel.setObjectName("combo_insurance_panel")
        
        self.Combo_insurance(self.combo_insurance_panel)
        self.label_17 = QtWidgets.QLabel(self.sfdg)
        self.label_17.setGeometry(QtCore.QRect(230, 120, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")

        self.imagepath = QtWidgets.QLineEdit(self.sfdg)
        self.imagepath.setGeometry(QtCore.QRect(200, 150, 171, 25))
        self.imagepath.setObjectName("imagepath")

        self.imagepath.textChanged.connect(self.Change_image)

        self.image = QtWidgets.QLabel(self.sfdg)
        self.image.setGeometry(QtCore.QRect(20, 60, 151, 141))
        self.image.setObjectName("image")

        self.browseimage = QtWidgets.QPushButton(self.sfdg)
        self.browseimage.setGeometry(QtCore.QRect(192, 180, 161, 30))
        self.browseimage.setObjectName("browseimage")

        self.browseimage.clicked.connect(self.Browse_Image)
        self.update_panel = QtWidgets.QPushButton(self.sfdg)
        self.update_panel.setGeometry(QtCore.QRect(195, 320, 361, 31))
        self.update_panel.setObjectName("update_panel")

        self.update_panel.clicked.connect(self.Update_Panel)
        self.label_19 = QtWidgets.QLabel(self.sfdg)
        self.label_19.setGeometry(QtCore.QRect(420, 180, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.dateEdit = QtWidgets.QDateEdit(self.sfdg)
        self.dateEdit.setGeometry(QtCore.QRect(389, 210, 161, 25))
        self.dateEdit.setObjectName("dateEdit")
        self.label_20 = QtWidgets.QLabel(self.sfdg)
        self.label_20.setGeometry(QtCore.QRect(230, 210, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.female = QtWidgets.QRadioButton(self.sfdg)
        self.female.setGeometry(QtCore.QRect(201, 240, 61, 20))
        self.female.setObjectName("female")
        self.male = QtWidgets.QRadioButton(self.sfdg)
        self.male.setGeometry(QtCore.QRect(291, 240, 61, 20))
        self.male.setObjectName("male")
        self.label_21 = QtWidgets.QLabel(self.sfdg)
        self.label_21.setGeometry(QtCore.QRect(420, 250, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.password = QtWidgets.QLineEdit(self.sfdg)
        self.password.setGeometry(QtCore.QRect(390, 280, 161, 25))
        self.password.setObjectName("password")
        self.tabWidget.addTab(self.sfdg, "")
        self.asdfg = QtWidgets.QWidget()
        self.asdfg.setObjectName("asdfg")
        self.label_8 = QtWidgets.QLabel(self.asdfg)
        self.label_8.setGeometry(QtCore.QRect(244, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_18 = QtWidgets.QLabel(self.asdfg)
        self.label_18.setGeometry(QtCore.QRect(570, 50, 191, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.chose_family = QtWidgets.QComboBox(self.asdfg)
        self.chose_family.setGeometry(QtCore.QRect(570, 80, 191, 25))
        self.chose_family.setObjectName("chose_family")

        self.Combo_family(self.chose_family)
        
        self.list_appointment = QtWidgets.QListView(self.asdfg)
        self.list_appointment.setGeometry(QtCore.QRect(10, 11, 201, 421))
        self.list_appointment.setObjectName("list_appointment")

        self.chose_family.currentTextChanged.connect(self.db_fetch_appointment)
        list_appointment_model = QtGui.QStandardItemModel()
        self.list_appointment.setModel(list_appointment_model)

        return_list_appointment = self.db_fetch_appointment(self.chose_family.currentText())

        for i in return_list_appointment:                
            item = QtGui.QStandardItem(str(i))
            item.setEditable(False)
            list_appointment_model.appendRow(item)

        self.list_appointment.clicked.connect(self.set_label_appointment)
        self.list_appointment.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
        
        
        self.label_22 = QtWidgets.QLabel(self.asdfg)
        self.label_22.setGeometry(QtCore.QRect(274, 50, 241, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.appointment_label = QtWidgets.QLabel(self.asdfg)
        self.appointment_label.setGeometry(QtCore.QRect(274, 71, 241, 262))
        self.appointment_label.setObjectName("appointment_label")
        self.label_24 = QtWidgets.QLabel(self.asdfg)
        self.label_24.setGeometry(QtCore.QRect(570, 100, 141, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.combo_specialty_appointment = QtWidgets.QComboBox(self.asdfg)
        self.combo_specialty_appointment.setGeometry(QtCore.QRect(570, 203, 191, 25))
        self.combo_specialty_appointment.setObjectName("combo_specialty_appointment")

        self.Combo_specilaty(self.combo_specialty_appointment)
        # self.combo_specialty_appointment.currentTextChanged.connect(self.db_fetch_appointment)
        self.label_25 = QtWidgets.QLabel(self.asdfg)
        self.label_25.setGeometry(QtCore.QRect(570, 180, 191, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.search_doctor_appointment = QtWidgets.QLineEdit(self.asdfg)
        self.search_doctor_appointment.setGeometry(QtCore.QRect(570, 158, 191, 25))
        self.search_doctor_appointment.setObjectName("search_doctor_appointment")
        self.label_26 = QtWidgets.QLabel(self.asdfg)
        self.label_26.setGeometry(QtCore.QRect(570, 130, 191, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        # self.label_27 = QtWidgets.QLabel(self.asdfg)
        # self.label_27.setGeometry(QtCore.QRect(570, 223, 191, 25))
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.label_27.setFont(font)
        # self.label_27.setObjectName("label_27")
        self.find_appointment = QtWidgets.QPushButton(self.asdfg)
        self.find_appointment.setGeometry(QtCore.QRect(570, 250, 141, 25))
        self.find_appointment.setObjectName("find_appointment")

        self.find_appointment.clicked.connect(self.Find_Appointment)

        self.refresh_appointment = QtWidgets.QPushButton(self.asdfg)
        self.refresh_appointment.setGeometry(QtCore.QRect(570, 310, 141, 25))
        self.refresh_appointment.setObjectName("refresh_appointment")

        self.refresh_appointment.clicked.connect(self.Refresh_Appointment)
        # self.dateEdit_appointment = QtWidgets.QDateEdit(self.asdfg)
        # self.dateEdit_appointment.setGeometry(QtCore.QRect(570, 253, 191, 25))
        # self.dateEdit_appointment.setObjectName("dateEdit_appointment")
        # self.label_28 = QtWidgets.QLabel(self.asdfg)
        # self.label_28.setGeometry(QtCore.QRect(570, 273, 191, 25))
        # font = QtGui.QFont()
        # font.setPointSize(10)
        # self.label_28.setFont(font)
        # self.label_28.setObjectName("label_28")
        # self.timeEdit_appointment = QtWidgets.QTimeEdit(self.asdfg)
        # self.timeEdit_appointment.setGeometry(QtCore.QRect(570, 300, 191, 25))
        # self.timeEdit_appointment.setObjectName("timeEdit_appointment")
        self.profile_doctor_appointment = QtWidgets.QPushButton(self.asdfg)
        self.profile_doctor_appointment.setGeometry(QtCore.QRect(220, 380, 300, 29))
        self.profile_doctor_appointment.setObjectName("profile_doctor_appointment")

        self.profile_doctor_appointment.clicked.connect(self.Profile_Doctor_Appointment)
        self.score_doctor = QtWidgets.QSpinBox(self.asdfg)
        self.score_doctor.setGeometry(QtCore.QRect(320, 330, 82, 25))
        self.score_doctor.setMaximum(5)
        self.score_doctor.setObjectName("score_doctor")
        
        self.label_34 = QtWidgets.QLabel(self.asdfg)
        self.label_34.setGeometry(QtCore.QRect(420, 330, 115, 25))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.score_clicked = QtWidgets.QPushButton(self.asdfg)
        self.score_clicked.setGeometry(QtCore.QRect(220, 330, 96, 27))
        self.score_clicked.setObjectName("score_clicked")

        self.score_clicked.clicked.connect(self.Score_Clicked)
        self.tabWidget.addTab(self.asdfg, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_29 = QtWidgets.QLabel(self.tab_2)
        self.label_29.setGeometry(QtCore.QRect(250, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        
        self.label_ph = QtWidgets.QLabel(self.tab_2)
        self.label_ph.setGeometry(QtCore.QRect(380, 40, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_ph.setFont(font)
        self.label_ph.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ph.setObjectName("label_ph")
        self.label_ph.setText("شماره تلفن را برای اضافه کردن وارد کنید:")

        self.family_phone = QtWidgets.QLineEdit(self.tab_2)
        self.family_phone.setGeometry(QtCore.QRect(490, 80, 251, 30))
        self.family_phone.setObjectName("family_phone")

        self.add_family = QtWidgets.QPushButton(self.tab_2)
        self.add_family.setGeometry(QtCore.QRect(400, 130, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_family.setFont(font)
        self.add_family.setObjectName("add_family")

        self.add_family.clicked.connect(self.Add_Family)
        self.list_family = QtWidgets.QListView(self.tab_2)
        self.list_family.setGeometry(QtCore.QRect(15, 51, 271, 381))
        self.list_family.setObjectName("list_family")

        list_family_model = QtGui.QStandardItemModel()
        self.list_family.setModel(list_family_model)

        return_list_family = self.db_fetch_family()

        for i in return_list_family:                
            item = QtGui.QStandardItem(str(i))
            item.setEditable(False)
            list_family_model.appendRow(item)

        self.list_family.clicked.connect(self.set_label_family)
        self.list_family.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
        
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setGeometry(QtCore.QRect(410, 220, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.selected_family = QtWidgets.QLabel(self.tab_2)
        self.selected_family.setGeometry(QtCore.QRect(410, 260, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.selected_family.setFont(font)
        self.selected_family.setText("")
        self.selected_family.setObjectName("selected_family")
        self.delete_selected_family = QtWidgets.QPushButton(self.tab_2)
        self.delete_selected_family.setGeometry(QtCore.QRect(420, 310, 301, 30))
        self.delete_selected_family.setObjectName("delete_selected_family")

        self.delete_selected_family.clicked.connect(self.Delete_Selected_Family)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_32 = QtWidgets.QLabel(self.tab_3)
        self.label_32.setGeometry(QtCore.QRect(244, 10, 231, 91))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.tab_3)
        self.label_33.setGeometry(QtCore.QRect(371, 116, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")

        self.pay = QtWidgets.QLabel(self.tab_3)
        self.pay.setGeometry(QtCore.QRect(30, 20, 251, 421))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pay.setFont(font)
        self.pay.setObjectName("pay")
        
        self.code_paygiry = QtWidgets.QLineEdit(self.tab_3)
        self.code_paygiry.setGeometry(QtCore.QRect(281, 148, 351, 30))
        self.code_paygiry.setObjectName("code_paygiry")
        self.paygiry = QtWidgets.QPushButton(self.tab_3)
        self.paygiry.setGeometry(QtCore.QRect(280, 210, 231, 31))
        self.paygiry.setObjectName("pushButton")

        self.paygiry.clicked.connect(self.Paygiry)
        self.tabWidget.addTab(self.tab_3, "")
        self.dfbg = QtWidgets.QWidget()
        self.dfbg.setObjectName("dfbg")
        self.list_doctor = QtWidgets.QListView(self.dfbg)
        self.list_doctor.setGeometry(QtCore.QRect(6, 56, 300, 381))
        self.list_doctor.setObjectName("list_doctor")

        list_doctor_model = QtGui.QStandardItemModel()
        self.list_doctor.setModel(list_doctor_model)

        return_list_doctor = self.db_fetch_doctor()

        for i in return_list_doctor:                
            item = QtGui.QStandardItem(str(i))
            item.setEditable(False)
            list_doctor_model.appendRow(item)

        self.list_doctor.clicked.connect(self.set_label_doctor)
        self.list_doctor.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
        
        self.label = QtWidgets.QLabel(self.dfbg)
        self.label.setGeometry(QtCore.QRect(10, 0, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.find_doctor = QtWidgets.QPushButton(self.dfbg)
        self.find_doctor.setGeometry(QtCore.QRect(350, 130, 100, 61))
        self.find_doctor.setObjectName("find_doctor")

        self.find_doctor.clicked.connect(self.Find_Doctor)
        self.label_4 = QtWidgets.QLabel(self.dfbg)
        self.label_4.setGeometry(QtCore.QRect(400, 20, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.sort_vistprice = QtWidgets.QPushButton(self.dfbg)
        self.sort_vistprice.setGeometry(QtCore.QRect(500, 260, 241, 30))
        self.sort_vistprice.setObjectName("sort_vistprice")

        self.sort_vistprice.clicked.connect(self.Sort_Vistprice)
        self.show_all = QtWidgets.QPushButton(self.dfbg)
        self.show_all.setGeometry(QtCore.QRect(350, 260, 141, 30))
        self.show_all.setObjectName("show_all")

        self.show_all.clicked.connect(self.db_fetch_doctor_all)

        self.find_inc = QtWidgets.QPushButton(self.dfbg)
        self.find_inc.setGeometry(QtCore.QRect(350, 220, 150, 31))
        self.find_inc.setObjectName("find_inc")

        self.find_inc.clicked.connect(self.Find_inc)

        self.widget = QtWidgets.QWidget(self.dfbg)
        self.widget.setGeometry(QtCore.QRect(520, 60, 230, 190))
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.search_name_doctor = QtWidgets.QLineEdit(self.widget)
        self.search_name_doctor.setObjectName("search_name_doctor")
        self.verticalLayout_6.addWidget(self.search_name_doctor)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.combo_specialty = QtWidgets.QComboBox(self.widget)
        self.combo_specialty.setObjectName("combo_specialty")

        self.Combo_specilaty(self.combo_specialty)
        self.verticalLayout_6.addWidget(self.combo_specialty)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.combo_insurance = QtWidgets.QComboBox(self.widget)
        self.combo_insurance.setObjectName("combo_insurance")

        self.Combo_insurance(self.combo_insurance)
        self.verticalLayout_6.addWidget(self.combo_insurance)
        self.widget1 = QtWidgets.QWidget(self.dfbg)
        self.widget1.setGeometry(QtCore.QRect(450, 290, 301, 151))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.selected_doctor = QtWidgets.QLabel(self.widget1)
        self.selected_doctor.setText("")
        self.selected_doctor.setObjectName("selected_doctor")
        self.verticalLayout_7.addWidget(self.selected_doctor)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.appointment = QtWidgets.QPushButton(self.widget1)
        self.appointment.setObjectName("appointment")
        self.verticalLayout.addWidget(self.appointment)

        self.appointment.clicked.connect(self.Reserve_Appointment_Doctor_List)
        self.profile = QtWidgets.QPushButton(self.widget1)
        self.profile.setObjectName("profile")
        self.verticalLayout.addWidget(self.profile)
        self.verticalLayout_7.addLayout(self.verticalLayout)

        self.profile.clicked.connect(self.Profile_Doctor_List)
        self.tabWidget.addTab(self.dfbg, "")
        self.dfb = QtWidgets.QWidget()
        self.dfb.setObjectName("dfb")
        self.label_13 = QtWidgets.QLabel(self.dfb)
        self.label_13.setGeometry(QtCore.QRect(400, 20, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.dfb)
        self.label_14.setGeometry(QtCore.QRect(15, 0, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.list_healthcare = QtWidgets.QListView(self.dfb)
        self.list_healthcare.setGeometry(QtCore.QRect(11, 56, 300, 381))
        self.list_healthcare.setObjectName("list_healthcare")

        list_healthcare_model = QtGui.QStandardItemModel()
        self.list_healthcare.setModel(list_healthcare_model)

        return_list_healthcare = self.db_fetch_healthcare()

        for i in return_list_healthcare:                
            item = QtGui.QStandardItem(str(i))
            item.setEditable(False)
            list_healthcare_model.appendRow(item)

        self.list_healthcare.clicked.connect(self.set_label_healthcare)
        self.list_healthcare.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
        
        self.find_healthcare = QtWidgets.QPushButton(self.dfb)
        self.find_healthcare.setGeometry(QtCore.QRect(350, 110, 100, 31))
        self.find_healthcare.setObjectName("find_healthcare")

        self.find_healthcare.clicked.connect(self.Find_Healthcare)

        
        self.find_healthcare_doctor = QtWidgets.QPushButton(self.dfb)
        self.find_healthcare_doctor.setGeometry(QtCore.QRect(350, 190, 100, 31))
        self.find_healthcare_doctor.setObjectName("find_healthcare_doctor")

        self.find_healthcare_doctor.clicked.connect(self.Find_Healthcare_Doctor)

        self.find_all = QtWidgets.QPushButton(self.dfb)
        self.find_all.setGeometry(QtCore.QRect(350, 190, 150, 31))
        self.find_all.setObjectName("find_all")

        self.find_all.clicked.connect(self.Find_Healthcare_All)

        self.widget2 = QtWidgets.QWidget(self.dfb)
        self.widget2.setGeometry(QtCore.QRect(520, 70, 230, 151))
        self.widget2.setObjectName("widget2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.name_healthcare = QtWidgets.QLineEdit(self.widget2)
        self.name_healthcare.setObjectName("name_healthcare")
        self.verticalLayout_4.addWidget(self.name_healthcare)
        self.label_10 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.name_doctor = QtWidgets.QLineEdit(self.widget2)
        self.name_doctor.setObjectName("name_doctor")
        self.verticalLayout_4.addWidget(self.name_doctor)
        self.widget3 = QtWidgets.QWidget(self.dfb)
        self.widget3.setGeometry(QtCore.QRect(500, 220, 231, 151))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.select_healthcare = QtWidgets.QLabel(self.widget3)
        self.select_healthcare.setText("")
        self.select_healthcare.setObjectName("select_healthcare")
        self.verticalLayout_5.addWidget(self.select_healthcare)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.list_doctors_healthcare = QtWidgets.QPushButton(self.widget3)
        self.list_doctors_healthcare.setObjectName("list_doctors_healthcare")

        self.list_doctors_healthcare.clicked.connect(self.List_Doctors_Healthcare)
        self.verticalLayout_3.addWidget(self.list_doctors_healthcare)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.dfb, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(250, 0, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.list_saved_doctor = QtWidgets.QListView(self.tab)
        self.list_saved_doctor.setGeometry(QtCore.QRect(6, 56, 300, 381))
        self.list_saved_doctor.setObjectName("list_saved_doctor")

        list_saved_model = QtGui.QStandardItemModel()
        self.list_saved_doctor.setModel(list_saved_model)

        return_list_saved = self.db_fetch_saved()

        for i in return_list_saved:                
            item = QtGui.QStandardItem(str(i))
            item.setEditable(False)
            list_saved_model.appendRow(item)

        self.list_saved_doctor.clicked.connect(self.set_label_saved)
        self.list_saved_doctor.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
        
        self.selected_saved_doctor = QtWidgets.QLabel(self.tab)
        self.selected_saved_doctor.setGeometry(QtCore.QRect(520, 230, 229, 25))
        self.selected_saved_doctor.setText("")
        self.selected_saved_doctor.setObjectName("selected_saved_doctor")
        self.profile_saved_doctor = QtWidgets.QPushButton(self.tab)
        self.profile_saved_doctor.setGeometry(QtCore.QRect(520, 350, 229, 30))
        self.profile_saved_doctor.setObjectName("profile_saved_doctor")

        self.profile_saved_doctor.clicked.connect(self.Profile_Saved_Doctor)
        self.label_31 = QtWidgets.QLabel(self.tab)
        self.label_31.setGeometry(QtCore.QRect(520, 200, 229, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.reserve_saved_doctor = QtWidgets.QPushButton(self.tab)
        self.reserve_saved_doctor.setGeometry(QtCore.QRect(520, 310, 227, 30))
        self.reserve_saved_doctor.setObjectName("reserve_saved_doctor")

        self.reserve_saved_doctor.clicked.connect(self.Reserve_Saved_Doctor)
        self.delete_saved_doctor = QtWidgets.QPushButton(self.tab)
        self.delete_saved_doctor.setGeometry(QtCore.QRect(520, 270, 227, 30))
        self.delete_saved_doctor.setObjectName("delete_saved_doctor")

        self.delete_saved_doctor.clicked.connect(self.Delete_Saved_Doctor)

        self.refresh_saved = QtWidgets.QPushButton(self.tab)
        self.refresh_saved.setGeometry(QtCore.QRect(520, 390, 227, 30))
        self.refresh_saved.setObjectName("refresh_saved")

        self.refresh_saved.clicked.connect(self.Refresh_Saved)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 597, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.fill_panel()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "مشخصات"))
        self.label_12.setText(_translate("MainWindow", "نام"))
        self.label_15.setText(_translate("MainWindow", "نام خانوادگی"))
        self.label_16.setText(_translate("MainWindow", "بیمه"))
        self.label_17.setText(_translate("MainWindow", "عکس"))
        self.image.setText(_translate("MainWindow", "عکس"))
        self.browseimage.setText(_translate("MainWindow", "بارگذاری عکس"))
        self.update_panel.setText(_translate("MainWindow", "ثبت تغییرات"))
        self.label_19.setText(_translate("MainWindow", "تاریخ تولد"))
        self.label_20.setText(_translate("MainWindow", "جنسیت"))
        self.female.setText(_translate("MainWindow", "زن"))
        self.male.setText(_translate("MainWindow", "مرد"))
        self.label_21.setText(_translate("MainWindow", "رمز عبور"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sfdg), _translate("MainWindow", "پنل کاربری"))
        self.label_8.setText(_translate("MainWindow", "نوبت های من و خانواده"))
        self.label_18.setText(_translate("MainWindow", "انتخاب اعضای خانواده"))
        self.label_22.setText(_translate("MainWindow", "مشخصات نوبت انتخاب شده:"))
        # self.appointment_label.setText(_translate("MainWindow", "مشخصات"))
        self.label_24.setText(_translate("MainWindow", "جستجو"))
        self.label_25.setText(_translate("MainWindow", "تخصص"))
        self.label_26.setText(_translate("MainWindow", "نام پزشک"))
        # self.label_27.setText(_translate("MainWindow", "تاریخ"))
        self.find_appointment.setText(_translate("MainWindow", "جستجو"))
        self.refresh_appointment.setText(_translate("MainWindow", "بارگذاری مجدد"))
        # self.label_28.setText(_translate("MainWindow", "ساعت"))
        self.profile_doctor_appointment.setText(_translate("MainWindow", "مشاهده پروفایل پزشک نوبت انتخاب شده"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.asdfg), _translate("MainWindow", "نوبت ها"))
        self.label_29.setText(_translate("MainWindow", "خانواده"))

        self.selected_family.setText(_translate("MainWindow",""))
        self.add_family.setText(_translate("MainWindow", "افزودن عضو +"))
        self.label_30.setText(_translate("MainWindow", "عضو انتخاب شده:"))
        self.delete_selected_family.setText(_translate("MainWindow", "حذف عضو انتخاب شده"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "خانواده"))
        self.label_32.setText(_translate("MainWindow", "پیگیری نوبت"))
        self.label_33.setText(_translate("MainWindow", "کد پیگیری"))
        self.paygiry.setText(_translate("MainWindow", "پیگیری"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "پیگیری نوبت"))
        self.label.setText(_translate("MainWindow", "لیست پزشکان"))
        self.find_doctor.setText(_translate("MainWindow", "جستجو"))
        self.label_4.setText(_translate("MainWindow", "جستجو"))
        self.sort_vistprice.setText(_translate("MainWindow", "مرتب کردن بر اساس هزینه ویزیت"))
        self.show_all.setText(_translate("MainWindow", "همه ی پزشکان"))
        self.label_2.setText(_translate("MainWindow", "نام پزشک"))
        self.label_3.setText(_translate("MainWindow", "تخصص"))
        self.label_5.setText(_translate("MainWindow", "بیمه"))
        self.label_7.setText(_translate("MainWindow", "پزشک انتخاب شده:"))
        self.appointment.setText(_translate("MainWindow", "رزرو نوبت"))
        self.profile.setText(_translate("MainWindow", "مشاهده پروفایل"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dfbg), _translate("MainWindow", "پزشکان"))
        self.label_13.setText(_translate("MainWindow", "جستجو"))
        self.label_14.setText(_translate("MainWindow", "لیست مراکز درمانی"))
        self.find_healthcare.setText(_translate("MainWindow", "جستجو"))
        self.find_healthcare_doctor.setText(_translate("MainWindow", "جستجو"))
        self.find_all.setText(_translate("MainWindow", "همه مراکز درمانی"))
        self.find_inc.setText(_translate("MainWindow", "جستجو بیمه"))
        self.label_11.setText(_translate("MainWindow", "نام مرکز درمانی"))
        self.label_10.setText(_translate("MainWindow", "نام پزشک"))
        self.label_9.setText(_translate("MainWindow", "مرکز درمانی انتخاب شده:"))
        self.list_doctors_healthcare.setText(_translate("MainWindow", "مشاهده لیست پزشکان"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dfb), _translate("MainWindow", "مراکز درمانی"))
        self.label_23.setText(_translate("MainWindow", "پزشکان ذخیره شده"))
        self.profile_saved_doctor.setText(_translate("MainWindow", "مشاهده پروفایل"))
        self.label_31.setText(_translate("MainWindow", "پزشک انتخاب شده:"))
        self.label_34.setText(_translate("MainWindow","امتیازدهی پزشک"))
        self.score_clicked.setText(_translate("MainWindow","ثبت امتیاز"))
        self.reserve_saved_doctor.setText(_translate("MainWindow", "رزرو نوبت"))
        self.delete_saved_doctor.setText(_translate("MainWindow", "حذف از لیست ذخیره شده ها"))
        self.refresh_saved.setText(_translate("MainWindow", "بارگذاری مجدد"))        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "پزشکان ذخیره شده"))
    
    def Refresh_Saved(self):
        self.selected_saved_doctor.setText('')
        list_saved_model = QtGui.QStandardItemModel()
        self.list_saved_doctor.setModel(list_saved_model)

        return_list_saved = self.db_fetch_saved()

        for i in return_list_saved:                
            item = QtGui.QStandardItem(str(i))
            item.setEditable(False)
            list_saved_model.appendRow(item)

        self.list_saved_doctor.clicked.connect(self.set_label_saved)
        self.list_saved_doctor.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
    def Find_inc(self):
        filter_insurance = str(self.combo_insurance.currentText()).lower()
        conn=sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM INSURANCE,in_contract_with,DOCTOR,SPECIALTY
            WHERE INSURANCE.name = ?  and
            INSURANCE.insuranceId = in_contract_with.insuranceId  and
            in_contract_with.medical_council_code = DOCTOR.medical_council_code AND
            in_contract_with.doc_username = DOCTOR.username and
            DOCTOR.specialtyId = SPECIALTY.specialtyId
        """,(filter_insurance,))
        val = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        newlist = []
        for i in val:
            newlist.append(f"نام :{i[8]} {i[9]}\nکد نظام پزشکی :{i[3]}\nهزینه ویزیت :{i[11]}\nتخصص :{i[14]}")
        list_doctor_model = QtGui.QStandardItemModel()
        self.list_doctor.setModel(list_doctor_model)

        for i in newlist:                
            item = QtGui.QStandardItem(str(i))
            item.setEditable(False)
            list_doctor_model.appendRow(item)

        self.list_doctor.clicked.connect(self.set_label_doctor)
        self.list_doctor.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
           
    def convert(self,image_path):
        try:
            with open(image_path, 'rb') as file:
                blobData = file.read()
            return blobData
        except:
            return None

    def Browse_Image(self):
        imagePath, _ = QtWidgets.QFileDialog.getOpenFileName()
        self.imagepath.setText(imagePath)
        return imagePath
    def Update_Panel(self):
        db_phone = self.ph1.text()
        db_password = self.password.text()
        if len(db_password) < 8:
            self.pop_window('رمزعبور کمتر از 8 حرف است')
        else:
            db_firstname = self.fname.text()
            db_lastname = self.lname.text()
            if self.imagepath.text() != '':
                dataimage = self.convert(self.imagepath.text())
                db_photo = dataimage
            else:
                db_photo = None
            db_insurance_name = str(self.combo_insurance_panel.currentText())    
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
            if db_photo == None:
                cursor.execute("""UPDATE USER SET 
                fname = ?,lname = ?,Birth_day = ?,password = ?,genderId = ?,insuranceId = ?
                WHERE USER.phone = ?
                """,(db_firstname,db_lastname,db_date,db_password,db_gender_id,db_insurance_id,db_phone,))
            else:
                cursor.execute("""UPDATE USER SET 
                fname = ?,lname = ?,photo = ?,Birth_day = ?,password = ?,genderId = ?,insuranceId = ?
                WHERE USER.phone = ?
                """,(db_firstname,db_lastname,db_photo,db_date,db_password,db_gender_id,db_insurance_id,db_phone,))
            conn.commit()
            cursor.close()
            conn.close()
            self.pop_message("Updated in Database ")

    def Find_Appointment(self):
        self.clik_doc_find = True
        filter_name = str(self.search_doctor_appointment.text()).lower()
        
        filter_specialty = str(self.combo_specialty_appointment.currentText()).lower()
        for row in range(self.list_appointment.model().rowCount()):
            listdoc = str(self.list_appointment.model().item(row).text()).lower()
            ls  = listdoc.split('\n')[6].split(':')[1] #fname
            ls += (listdoc.split('\n')[7].split(':')[1])#lname
            if filter_name in ls:
                self.list_appointment.setRowHidden(row, False)
            else:
                self.list_appointment.setRowHidden(row, True)
            if self.list_doctor.isRowHidden(row):
                pass
            else:
                if filter_specialty in listdoc:
                    self.list_doctor.setRowHidden(row,False)
                else:
                    self.list_doctor.setRowHidden(row, True)
                
    def Profile_Doctor_Appointment(self):
        text = self.appointment_label.text().split('\n')
        if len(text) == 1 and text[0] == '':
            self.pop_message("نوبتی انتخاب نشده است")
        else:
            for i in text:
                index = i.split(':')
                # print(f"'{index[0]}'")
                if index[0] ==  'کد نظام پزشکی پزشک ':
                    #index[1] => medical_code
                    medi = int(index[1])
                    conn=sqlite3.connect('tabib.db')
                    cursor = conn.cursor()
                    cursor.execute(f" select medical_council_code,username from DOCTOR where DOCTOR.medical_council_code = {medi}")
                    val = cursor.fetchall()
                    # print(val)
                    conn.commit()
                    cursor.close()
                    conn.close()
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Ui_Doctor_profile(self.phone,val[0][0],val[0][1])
                    self.ui.setupUi(self.window)
                    self.window.show()
                    ##########################

    def Add_Family(self):
        phone = self.family_phone.text()
        if phone == self.phone:
            self.pop_message("شما نمیتوانید خودتان را به لیست خانواده اضافه کنید")
        else:
            conn=sqlite3.connect('tabib.db')
            cursor = conn.cursor()
            cursor.execute(""" select * from is_family_of WHERE
                fuserPhone = ? AND suserPhone = ?
            """,(self.phone,phone,))
            has = cursor.fetchall()
            if len(has) != 0:
                self.pop_message("این عضو قبلا به لیست خانواده اضافه شده است")
            else:
                cursor.execute("""select phone from USER where phone = ?""",(phone,))
                exists = cursor.fetchall()
                if len(exists) == 0:
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Ui_Signup() #go to signup page
                    self.ui.setupUi(self.window)
                    self.window.show()
                else:
                    cursor.execute(""" INSERT INTO is_family_of 
                    (fuserPhone,suserPhone)
                    VALUES(?,?)
                    """,(self.phone,phone,))
                    self.pop_message(f"{phone} به خانواده اضافه شد")
            conn.commit()
            cursor.close()
            conn.close()            
            list_family_model = QtGui.QStandardItemModel()
            self.list_family.setModel(list_family_model)

            return_list_family = self.db_fetch_family()
            for i in return_list_family:                
                item = QtGui.QStandardItem(str(i))
                item.setEditable(False)
                list_family_model.appendRow(item)

            self.list_family.clicked.connect(self.set_label_family)
            self.list_family.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")

    def Delete_Selected_Family(self):
        list_profile = self.selected_family.text().split(',')
        #list_profile[2] => phone
        if (len(list_profile) == 1 and list_profile[0] == ''):
            self.pop_message("کسی را انتخاب نکرده اید") 
        else:
            conn=sqlite3.connect('tabib.db')
            cursor = conn.cursor()
            cursor.execute(""" delete from is_family_of WHERE
                fuserPhone = ? AND suserPhone = ?
            """,(self.phone,list_profile[2],))
            self.pop_message("Successfully Deleted")
            self.selected_family.setText("")
            conn.commit()
            cursor.close()
            conn.close()

            list_family_model = QtGui.QStandardItemModel()
            self.list_family.setModel(list_family_model)

            newlist = self.db_fetch_family()
            for i in newlist:                
                item = QtGui.QStandardItem(str(i))
                item.setEditable(False)
                list_family_model.appendRow(item)

            self.list_family.clicked.connect(self.set_label_family)
            self.list_family.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
   
    def Paygiry(self):
        text = self.code_paygiry.text()
        conn=sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        cursor.execute(f"create temp view if not exists payg as select is_family_of.suserPhone from is_family_of where is_family_of.fuserPhone = '{self.phone}' union select distinct is_family_of.fuserPhone from is_family_of where is_family_of.fuserPhone = '{self.phone}'")
        cursor.execute("""select * from payg,APPOINTMENT,PAYMENT
            where payg.suserPhone = APPOINTMENT.phone and
            APPOINTMENT.paymentId = PAYMENT.paymentId
         """)
        val = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        seted = 0
        for i in val:
            if text == i[10]:
                #i[1] => appId
                newlist = self.paygery_info(i[0],i[1])
                seted = 1
                self.pay.setText(newlist[0])
                break
        if seted == 0 :
            self.pop_message("شما مجاز به دیدن اطلاعات این نوبت نیستید")
        else:
            pass
    clik_doc_find = False
    def Find_Doctor(self):
        self.clik_doc_find = True
        filter_name = str(self.search_name_doctor.text()).lower()
        
        filter_specialty = str(self.combo_specialty.currentText()).lower()
        
        for row in range(self.list_doctor.model().rowCount()):
            listdoc = str(self.list_doctor.model().item(row).text()).lower()
            listname = listdoc.split('\n')[0].split(':')[1]
            if filter_name in listname:
                self.list_doctor.setRowHidden(row, False)
            else:
                self.list_doctor.setRowHidden(row, True)
            if self.list_doctor.isRowHidden(row):
                pass
            else:
                if filter_specialty in listdoc:
                    self.list_doctor.setRowHidden(row,False)
                else:
                    self.list_doctor.setRowHidden(row, True)
                    
    def Sort_Vistprice(self):
        list_tuple = []
        list_hidden = []
        model = self.list_doctor.model()
        for index in range(model.rowCount()):
            hide = (self.list_doctor.isRowHidden(index))
            if hide == False:
                item = model.item(index).text()
                list_item_line = item.split('\n')
                name = ""
                code = None
                price = None
                specialty = ""
                for i in list_item_line:
                    temp_list = i.split(':')
                    if temp_list[0] == 'هزینه ویزیت ':
                        price = temp_list[1]
                    elif temp_list[0] == 'نام ':
                        name = temp_list[1]
                    elif temp_list[0] == 'تخصص ':
                        specialty = temp_list[1]
                    elif temp_list[0] == 'کد نظام پزشکی ':
                        code = temp_list[1]
                list_tuple.append((price,code,name,specialty))
            else:
                item = model.item(index).text()
                list_hidden.append(item)
        
        sort = sorted(list_tuple)
        final = []
        list_doctor_model = QtGui.QStandardItemModel()
        self.list_doctor.setModel(list_doctor_model)
        for i in sort:
            string = (f"نام :{i[2]}\nکد نظام پزشکی :{i[1]}\nهزینه ویزیت :{i[0]}\nتخصص :{i[3]}")        
            item = QtGui.QStandardItem(string)
            item.setEditable(False)
            list_doctor_model.appendRow(item)
        for i in list_hidden:
            item = QtGui.QStandardItem(i)
            item.setEditable(False)
            list_doctor_model.appendRow(item)
        if self.clik_doc_find == True:
            self.Find_Doctor()
        self.list_doctor.clicked.connect(self.set_label_doctor)
        self.list_doctor.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
    def db_fetch_doctor_all(self):
        list_doctor_model = QtGui.QStandardItemModel()
        self.list_doctor.setModel(list_doctor_model)

        return_list_doctor = self.db_fetch_doctor()

        for i in return_list_doctor:                
            item = QtGui.QStandardItem(str(i))
            item.setEditable(False)
            list_doctor_model.appendRow(item)

        self.list_doctor.clicked.connect(self.set_label_doctor)
        self.list_doctor.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
        self.search_name_doctor.setText('')
        self.combo_specialty.setCurrentIndex(0)
        self.combo_insurance.setCurrentIndex(0)    
    def Find_Healthcare_All(self):
        list_hel_model = QtGui.QStandardItemModel()
        self.list_healthcare.setModel(list_hel_model)

        return_list_hel = self.db_fetch_healthcare()

        for i in return_list_hel:                
            item = QtGui.QStandardItem(str(i))
            item.setEditable(False)
            list_hel_model.appendRow(item)

        self.list_healthcare.clicked.connect(self.set_label_healthcare)
        self.list_healthcare.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
        self.name_healthcare.setText('')
        self.name_doctor.setText('')
    def Reserve_Appointment_Doctor_List(self):
        profile_text = str(self.selected_doctor.text()).lower()
        if(len(profile_text) == 0 ):
            self.pop_message("پزشکی انتخاب نشده است")
        else:
            profile_list = profile_text.split(",")
            # profile_list[1] => medical_code
            medi = int(profile_list[1])
            conn=sqlite3.connect('tabib.db')
            cursor = conn.cursor()
            cursor.execute(f" select medical_council_code,username from DOCTOR where DOCTOR.medical_council_code = {medi}")
            val = cursor.fetchall()
            # print(val)
            conn.commit()
            cursor.close()
            conn.close()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Get_Appointment(self.phone,val[0][0],val[0][1])
            self.ui.setupUi(self.window)
            self.window.show()
    def Profile_Doctor_List(self):
        profile_text = str(self.selected_doctor.text()).lower()
        if(len(profile_text) == 0 ):
            self.pop_message("پزشکی انتخاب نشده است")
        else:
            profile_list = profile_text.split(",")
            # profile_list[1] => medical_code
            medi = int(profile_list[1])
            conn=sqlite3.connect('tabib.db')
            cursor = conn.cursor()
            cursor.execute(f" select medical_council_code,username from DOCTOR where DOCTOR.medical_council_code = {medi}")
            val = cursor.fetchall()
            # print(val)
            conn.commit()
            cursor.close()
            conn.close() 
            # go to profile doctor with this medical_code 
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Doctor_profile(self.phone,val[0][0],val[0][1])
            self.ui.setupUi(self.window)
            self.window.show()

    def Find_Healthcare(self):
        name = self.name_healthcare.text()
        self.select_healthcare.setText('')
        if name != '':
            conn=sqlite3.connect('tabib.db')
            cursor = conn.cursor()
            cursor.execute(f" select * from HEALTHCARE,ADDRESS where HEALTHCARE.name like '%{name}%' AND HEALTHCARE.addressId = ADDRESS.addressId")
            val = cursor.fetchall()
            # print(val)
            newlist =[]
            for i in val:
                newlist.append(f"نام :{i[3]}\nشماره تلفن :{i[1]}\nآدرس :خیابان {i[7]}\nکوچه :{i[8]}\nپلاک :{i[9]}")        
            conn.commit()
            cursor.close()
            conn.close()
        
            list_healthcare_model = QtGui.QStandardItemModel()
            self.list_healthcare.setModel(list_healthcare_model)
            for i in newlist:                
                item = QtGui.QStandardItem(str(i))
                item.setEditable(False)
                list_healthcare_model.appendRow(item)

            self.list_healthcare.clicked.connect(self.set_label_healthcare)
            self.list_healthcare.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
        else:
            self.pop_message("نامی وارد نکرده اید")
    def Find_Healthcare_Doctor(self):
        name = self.name_doctor.text()
        self.select_healthcare.setText('')
        if name != '':
            conn=sqlite3.connect('tabib.db')
            cursor = conn.cursor()
            cursor.execute(f"create temp view if not exists seldoc as select DOCTOR.medical_council_code,DHH.healthcareId from DOCTOR,DHH where DOCTOR.fname like '%{name}%' and DOCTOR.medical_council_code = DHH.medical_council_code OR DOCTOR.lname like '%{name}%' and DOCTOR.medical_council_code = DHH.medical_council_code")
            cursor.execute("""create temp view if not exists dochel as select * from seldoc,HEALTHCARE,ADDRESS where HEALTHCARE.healthcareId = seldoc.healthcareId and HEALTHCARE.addressId = ADDRESS.addressId group by HEALTHCARE.healthcareId""")
            cursor.execute("""select * from dochel""")
            val = cursor.fetchall()
            # print(val)
            newlist =[]
            for i in val:
                newlist.append(f"نام :{i[5]}\nشماره تلفن :{i[3]}\nآدرس :خیابان {i[9]}\nکوچه :{i[10]}\nپلاک :{i[11]}")        
            conn.commit()
            cursor.close()
            conn.close()
        
            list_healthcare_model = QtGui.QStandardItemModel()
            self.list_healthcare.setModel(list_healthcare_model)
            for i in newlist:                
                item = QtGui.QStandardItem(str(i))
                item.setEditable(False)
                list_healthcare_model.appendRow(item)

            self.list_healthcare.clicked.connect(self.set_label_healthcare)
            self.list_healthcare.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
        else:
            self.pop_message("نامی وارد نکرده اید")
    def List_Doctors_Healthcare(self):
        text = self.select_healthcare.text().split(',')
        # text[0] => name_healthcare
        if text[0] != '':
            conn=sqlite3.connect('tabib.db')
            cursor = conn.cursor()
            cursor.execute(f"create temp view if not exists hel as select * from HEALTHCARE,DHH where HEALTHCARE.name = '{text[0]}' and HEALTHCARE.healthcareId = DHH.healthcareId")
            cursor.execute("""select DOCTOR.*,SPECIALTY.name from hel,DOCTOR,SPECIALTY
                 WHERE hel.medical_council_code = DOCTOR.medical_council_code 
                 and SPECIALTY.specialtyId = DOCTOR.specialtyId 
                 group by hel.medical_council_code""")
            val = cursor.fetchall()
            # print(val)
            newlist =[]
            for i in val:
                newlist.append(f"نام :{i[2]} {i[3]}\nکد نظام پزشکی :{i[0]}\nهزینه ویزیت :{i[5]}\nتخصص :{i[8]}")        
            conn.commit()
            cursor.close()
            conn.close()

            list_healthcare_doc_model = QtGui.QStandardItemModel()
            self.list_doctor.setModel(list_healthcare_doc_model)
            for i in newlist:                
                item = QtGui.QStandardItem(str(i))
                item.setEditable(False)
                list_healthcare_doc_model.appendRow(item)

            self.list_doctor.clicked.connect(self.set_label_doctor)
            self.list_doctor.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
        
            self.name_doctor.setText('')
            self.combo_specialty.setCurrentIndex(0)
            self.combo_insurance.setCurrentIndex(0)
            self.tabWidget.setCurrentIndex(4)
        else:
            self.pop_message("مرکز درمانی وارد نکرده اید")
    def Profile_Saved_Doctor(self):
        profile_text = str(self.selected_saved_doctor.text()).lower()
        if(len(profile_text) == 0 ):
            self.pop_message("پزشکی انتخاب نشده است")
        else:
            profile_list = profile_text.split(",")
            # profile_list[1] => medical_code
            medi = int(profile_list[1])
            conn=sqlite3.connect('tabib.db')
            cursor = conn.cursor()
            cursor.execute(f" select medical_council_code,username from DOCTOR where DOCTOR.medical_council_code = {medi}")
            val = cursor.fetchall()
            # print(val)
            conn.commit()
            cursor.close()
            conn.close()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Doctor_profile(self.phone,val[0][0],val[0][1])
            self.ui.setupUi(self.window)
            self.window.show()
    def Reserve_Saved_Doctor(self):
        profile_text = str(self.selected_saved_doctor.text()).lower()
        if(len(profile_text) == 0 ):
            self.pop_message("پزشکی انتخاب نشده است")
        else:
            profile_list = profile_text.split(",")
            # profile_list[1] => medical_code
            medi = int(profile_list[1])
            conn=sqlite3.connect('tabib.db')
            cursor = conn.cursor()
            cursor.execute(f" select medical_council_code,username from DOCTOR where DOCTOR.medical_council_code = {medi}")
            val = cursor.fetchall()
            # print(val)
            conn.commit()
            cursor.close()
            conn.close()
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_Get_Appointment(self.phone,val[0][0],val[0][1])
            self.ui.setupUi(self.window)
            self.window.show()
            
    def Delete_Saved_Doctor(self):
        list_profile = self.selected_saved_doctor.text().split(',')
        #list_profile[1] => phone
        # print(list_profile)
        if (len(list_profile) == 1 and list_profile[0] == ''):
            self.pop_message("کسی را انتخاب نکرده اید") 
        else:
            conn=sqlite3.connect('tabib.db')
            cursor = conn.cursor()
            cursor.execute(""" delete from saved WHERE
                phone = ? AND medical_council_code = ?
            """,(self.phone,list_profile[1],))
            self.pop_message("Successfully Deleted")
            self.selected_saved_doctor.setText("")
            conn.commit()
            cursor.close()
            conn.close()

            list_save_model = QtGui.QStandardItemModel()
            self.list_saved_doctor.setModel(list_save_model)

            newlist = self.db_fetch_saved()
            for i in newlist:                
                item = QtGui.QStandardItem(str(i))
                item.setEditable(False)
                list_save_model.appendRow(item)

            self.list_saved_doctor.clicked.connect(self.set_label_saved)
            self.list_saved_doctor.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
   
    def Score_Clicked(self):
        score = self.score_doctor.text()
        text = self.appointment_label.text().split('\n')
        if len(text) == 1 and text[0] == '':
            self.pop_message("نوبتی انتخاب نکرده اید")
        else:
            for i in text:
                sp = i.split(':')
                if sp[0] in ['شماره نوبت ']:
                    #sp[1] => appointmentId
                    conn=sqlite3.connect('tabib.db')
                    cursor = conn.cursor()
                    cursor.execute("""UPDATE APPOINTMENT SET 
                    score = ?
                    WHERE APPOINTMENT.appointmentId = ?
                    """,(score,sp[1],))
                    self.pop_message("Successfully Updated")
                    conn.commit()
                    cursor.close()
                    conn.close()
    def Refresh_Appointment(self):
        self.appointment_label.setText('')
        list_appointment_model = QtGui.QStandardItemModel()
        self.list_appointment.setModel(list_appointment_model)
        return_list_appointment = self.db_fetch_appointment(self.chose_family.currentText())

        for i in return_list_appointment:                
            item = QtGui.QStandardItem(str(i))
            item.setEditable(False)
            list_appointment_model.appendRow(item)

        self.list_appointment.clicked.connect(self.set_label_appointment)
        self.list_appointment.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
   
    def set_label_doctor(self,index):
        list_doc = (str(self.list_doctor.model().itemData(index)[0]).split('\n'))
        list_asli = ""
        for i in list_doc:
            list_i = i.split(':')
            if list_i[0] in ['نام ','کد نظام پزشکی ']:
                list_asli += list_i[1]
                list_asli += ','
        self.selected_doctor.setText(list_asli) 
    def set_label_appointment(self,index):
        self.appointment_label.setText(str(self.list_appointment.model().itemData(index)[0]))
    def set_label_family(self,index):
        list_profile = (str(self.list_family.model().itemData(index)[0]).split('\n'))
        list_asli = ""
        for i in list_profile:
            list_i = i.split(':')
            if list_i[0] in ['نام ','نام خانوادگی ','شماره تلفن ']:
                list_asli += list_i[1]
                list_asli += ','
        self.selected_family.setText(list_asli)        
    def set_label_healthcare(self,index):
        list_h = str(self.list_healthcare.model().itemData(index)[0]).split('\n')
        list_asli = ""
        for i in list_h:
            list_i = i.split(':')
            if list_i[0] in ['نام ','شماره تلفن ']:
                list_asli += list_i[1]
                list_asli += ','
        self.select_healthcare.setText(list_asli)
    def set_label_saved(self,index):
        list_saved_doc = (str(self.list_saved_doctor.model().itemData(index)[0]).split('\n'))
        list_asli = ""
        for i in list_saved_doc:
            list_i = i.split(':')
            if list_i[0] in ['نام ','کد نظام پزشکی ']:
                list_asli += list_i[1]
                list_asli += ','
        self.selected_saved_doctor.setText(list_asli) 

    def pop_message(self,text):
        msg=QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.setWindowTitle("")
        msg.exec_()  
    def Change_image(self):
        dataimage = self.convert(self.imagepath.text())        
        qimg = QtGui.QImage.fromData(dataimage)
        pixmap = QtGui.QPixmap.fromImage(qimg)
        self.image.setPixmap(pixmap)
        self.image.setScaledContents(True)
    def fill_panel(self):
        conn=sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        cursor.execute(""" select * from USER,INSURANCE
            WHERE USER.phone = ? AND USER.insuranceId = INSURANCE.insuranceId
         """,(self.phone,))
        panel = cursor.fetchall()
        self.ph1.setText(panel[0][0])
        self.fname.setText(panel[0][1])
        self.lname.setText(panel[0][2])
        self.combo_insurance_panel.setCurrentText(panel[0][9])
        date = QtCore.QDate.fromString(panel[0][4], 'yyyy/M/d')
        self.dateEdit.setDate(date)
        self.password.setText(panel[0][5])
        if panel[0][6] == 2:
            self.female.setChecked(True)
        elif panel[0][6] == 1:
            self.male.setChecked(True)
        #panel[0][3] => BlobDate
        qimg = QtGui.QImage.fromData(panel[0][3])
        pixmap = QtGui.QPixmap.fromImage(qimg)
        self.image.setPixmap(pixmap)
        self.image.setScaledContents(True)
        # self.image.setSizePolicy(QSizePolicyPolicy= False)
        conn.commit()
        cursor.close()
        conn.close()
    def Combo_family(self,ins):
        conn=sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        cursor.execute(""" select suserPhone from is_family_of
            WHERE is_family_of.fuserPhone = ?
         """,(self.phone,))
        combo_family_list = cursor.fetchall()
        family_phone = [self.phone]
        for x in combo_family_list:
            family_phone.append(x[0])
        conn.commit()
        cursor.close()
        conn.close()
        ins.addItems(family_phone)
    def Combo_specilaty(self,ins):
        conn=sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        cursor.execute(""" select DISTINCT name from SPECIALTY""")
        combo_special_list = cursor.fetchall()
        special_item = [None]
        for x in combo_special_list:
            special_item.append(x[0])
        conn.commit()
        cursor.close()
        conn.close()
        ins.addItems(special_item)
    def Combo_insurance(self,ins):
        conn=sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        cursor.execute("""select distinct name from INSURANCE """)
        combo_inc_list = cursor.fetchall()
        inc = []
        for x in combo_inc_list:
            inc.append(x[0])
        conn.commit()
        cursor.close()
        conn.close()
        ins.addItems(inc)

    def paygery_info(self,phone,appId):
        conn = sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        # cursor.execute("""select USER.phone,APPOINTMENT.appointmentId from APPOINTMENT,USER where USER.phone = ? and APPOINTMENT.phone = USER.phone""",(phone,))
        # print(cursor.fetchall())
        cursor.execute("""select APPOINTMENT.score,USER.phone,USER.fname,USER.lname,INSURANCE.name,PAYMENT.code
            ,SPECIALTY.name,DOCTOR.fname,DOCTOR.lname,DOCTOR.medical_council_code,
            WORK_HOUR.starthour,WORK_HOUR.endhour,WORK_HOUR.date,APPOINTMENT.appointmentId,ADDRESS.street,ADDRESS.alley,ADDRESS.plaque
            from APPOINTMENT,USER,PAYMENT,DOCTOR,SPECIALTY,DHH,WORK_HOUR,INSURANCE,HEALTHCARE,ADDRESS
            where USER.phone = ? and
            USER.insuranceId = INSURANCE.insuranceId AND
            APPOINTMENT.phone = USER.phone and
            APPOINTMENT.paymentId = PAYMENT.paymentId and
            DOCTOR.medical_council_code = APPOINTMENT.medical_council_code AND
            DOCTOR.username = APPOINTMENT.doc_username and
            SPECIALTY.specialtyId = DOCTOR.specialtyId AND
            APPOINTMENT.appointmentId = ? and
            APPOINTMENT.appointmentId = DHH.appointmentId and
            APPOINTMENT.dhhId = DHH.dhhID and
            DHH.dhhId = WORK_HOUR.dhhId and
            DHH.healthcareId = HEALTHCARE.healthcareId and
            HEALTHCARE.addressId = ADDRESS.addressId 
            UNION 
            select APPOINTMENT.score,USER.phone,USER.fname,USER.lname,INSURANCE.name,PAYMENT.code
            ,SPECIALTY.name,DOCTOR.fname,DOCTOR.lname,DOCTOR.medical_council_code,
            WORK_HOUR.starthour,WORK_HOUR.endhour,WORK_HOUR.date,APPOINTMENT.appointmentId,ADDRESS.street,ADDRESS.alley,ADDRESS.plaque
            from APPOINTMENT,USER,PAYMENT,DOCTOR,SPECIALTY,DOH,WORK_HOUR,INSURANCE,ADDRESS,DOCTOR_OFFICE
            where USER.phone = ? and
            USER.insuranceId = INSURANCE.insuranceId AND
            APPOINTMENT.phone = USER.phone and
            APPOINTMENT.paymentId = PAYMENT.paymentId and
            DOCTOR.medical_council_code = APPOINTMENT.medical_council_code AND
            DOCTOR.username = APPOINTMENT.doc_username and
            SPECIALTY.specialtyId = DOCTOR.specialtyId AND
            APPOINTMENT.appointmentId = ? and
            APPOINTMENT.appointmentId = DOH.appointmentId and
            APPOINTMENT.dohId = DOH.dohID and
            DOH.dohId = WORK_HOUR.dohId and
            DOH.docofficeId = DOCTOR_OFFICE.docofficeId and
            DOCTOR_OFFICE.addressId = ADDRESS.addressId 
        """,(phone,appId,phone,appId,))
        newval = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        newlist = []
        for i in newval:
            newlist.append(f"نام :{i[2]}\nنام خانوادگی :{i[3]}\nشماره تلفن :{i[1]}\nبیمه :{i[4]}\nامتیاز :{i[0]}\nکد پیگیری :{i[5]}\nنام پزشک :{i[7]}\nنام خانوادگی پزشک :{i[8]}\nتخصص پزشک :{i[6]}\nکد نظام پزشکی پزشک :{i[9]}\nساعت شروع نوبت :{i[10]}\nساعت اتمام نوبت :{i[11]}\nتاریخ نوبت :{i[12]}\nشماره نوبت :{i[13]}\nآدرس :{i[14]}\nکوچه :{i[15]}\nپلاک :{i[16]}")        
        return newlist
    def db_fetch_appointment(self,phone):
        conn = sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        # cursor.execute("""select USER.phone,APPOINTMENT.appointmentId from APPOINTMENT,USER where USER.phone = ? and APPOINTMENT.phone = USER.phone""",(phone,))
        # print(cursor.fetchall())
        cursor.execute("""select APPOINTMENT.score,USER.phone,USER.fname,USER.lname,INSURANCE.name,PAYMENT.code
            ,SPECIALTY.name,DOCTOR.fname,DOCTOR.lname,DOCTOR.medical_council_code,
            WORK_HOUR.starthour,WORK_HOUR.endhour,WORK_HOUR.date,APPOINTMENT.appointmentId,ADDRESS.street,ADDRESS.alley,ADDRESS.plaque
            from APPOINTMENT,USER,PAYMENT,DOCTOR,SPECIALTY,DHH,WORK_HOUR,INSURANCE,HEALTHCARE,ADDRESS
            where USER.phone = ? and
            USER.insuranceId = INSURANCE.insuranceId AND
            APPOINTMENT.phone = USER.phone and
            APPOINTMENT.paymentId = PAYMENT.paymentId and
            DOCTOR.medical_council_code = APPOINTMENT.medical_council_code AND
            DOCTOR.username = APPOINTMENT.doc_username and
            SPECIALTY.specialtyId = DOCTOR.specialtyId AND
            APPOINTMENT.appointmentId = DHH.appointmentId and
            APPOINTMENT.dhhId = DHH.dhhID and
            DHH.dhhId = WORK_HOUR.dhhId and
            DHH.healthcareId = HEALTHCARE.healthcareId and
            HEALTHCARE.addressId = ADDRESS.addressId 
            UNION 
            select APPOINTMENT.score,USER.phone,USER.fname,USER.lname,INSURANCE.name,PAYMENT.code
            ,SPECIALTY.name,DOCTOR.fname,DOCTOR.lname,DOCTOR.medical_council_code,
            WORK_HOUR.starthour,WORK_HOUR.endhour,WORK_HOUR.date,APPOINTMENT.appointmentId,ADDRESS.street,ADDRESS.alley,ADDRESS.plaque
            from APPOINTMENT,USER,PAYMENT,DOCTOR,SPECIALTY,DOH,WORK_HOUR,INSURANCE,ADDRESS,DOCTOR_OFFICE
            where USER.phone = ? and
            USER.insuranceId = INSURANCE.insuranceId AND
            APPOINTMENT.phone = USER.phone and
            APPOINTMENT.paymentId = PAYMENT.paymentId and
            DOCTOR.medical_council_code = APPOINTMENT.medical_council_code AND
            DOCTOR.username = APPOINTMENT.doc_username and
            SPECIALTY.specialtyId = DOCTOR.specialtyId AND
            APPOINTMENT.appointmentId = DOH.appointmentId and
            APPOINTMENT.dohId = DOH.dohID and
            DOH.dohId = WORK_HOUR.dohId and
            DOH.docofficeId = DOCTOR_OFFICE.docofficeId and
            DOCTOR_OFFICE.addressId = ADDRESS.addressId 
        """,(phone,phone,))
        newval = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        newlist = []
        for i in newval:
            newlist.append(f"نام :{i[2]}\nنام خانوادگی :{i[3]}\nشماره تلفن :{i[1]}\nبیمه :{i[4]}\nامتیاز :{i[0]}\nکد پیگیری :{i[5]}\nنام پزشک :{i[7]}\nنام خانوادگی پزشک :{i[8]}\nتخصص پزشک :{i[6]}\nکد نظام پزشکی پزشک :{i[9]}\nساعت شروع نوبت :{i[10]}\nساعت اتمام نوبت :{i[11]}\nتاریخ نوبت :{i[12]}\nشماره نوبت :{i[13]}\nآدرس :{i[14]},{i[15]},{i[16]}")        

        list_appointment_model = QtGui.QStandardItemModel()
        self.list_appointment.setModel(list_appointment_model)
        for i in newlist:                
            item = QtGui.QStandardItem(str(i))
            item.setEditable(False)
            list_appointment_model.appendRow(item)

        self.list_appointment.clicked.connect(self.set_label_appointment)
        self.list_appointment.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
        
        return newlist
    def db_fetch_family(self):
        conn = sqlite3.connect('tabib.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM is_family_of
            JOIN USER ON 
            is_family_of.fuserPhone = ? AND
            is_family_of.suserPhone = USER.phone
            JOIN INSURANCE ON
            INSURANCE.insuranceId = USER.insuranceId
        """,(self.phone,))
        val = cursor.fetchall()
        newlist =[]
        for i in val:
            newlist.append(f"نام :{i[3]}\nنام خانوادگی :{i[4]}\nشماره تلفن :{i[1]}\nبیمه :{i[11]}")        
        conn.commit()
        cursor.close()
        conn.close()
        return newlist
    def db_fetch_healthcare(self):
        conn = sqlite3.connect('tabib.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM HEALTHCARE JOIN ADDRESS ON 
            HEALTHCARE.addressId = ADDRESS.addressId
        """)
        val = cursor.fetchall()
        newlist =[]
        for i in val:
            newlist.append(f"نام :{i[3]}\nشماره تلفن :{i[1]}\nآدرس :خیابان {i[7]}\nکوچه :{i[8]}\nپلاک :{i[9]}")        
        conn.commit()
        cursor.close()
        conn.close()
        return newlist
    def db_fetch_saved(self):
        conn = sqlite3.connect('tabib.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT DOCTOR.*,SPECIALTY.name FROM saved JOIN DOCTOR ON 
            DOCTOR.medical_council_code = saved.medical_council_code AND
            DOCTOR.username = saved.doc_username AND
            ? = saved.phone
            JOIN SPECIALTY ON
            DOCTOR.specialtyId = SPECIALTY.specialtyId
        """,(self.phone,))
        val = cursor.fetchall()
        newlist =[]
        for i in val:
            newlist.append(f"نام :{i[2]} {i[3]}\nکد نظام پزشکی :{i[0]}\nهزینه ویزیت :{i[5]}\nتخصص :{i[8]}")        
        conn.commit()
        cursor.close()
        conn.close()
        return newlist
    def db_fetch_doctor(self):
        conn = sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        # CREATE VIEW IF NOT EXISTS DOC AS
        cursor.execute("""
            SELECT DOCTOR.*,SPECIALTY.name FROM DOCTOR JOIN SPECIALTY ON
            DOCTOR.specialtyId = SPECIALTY.specialtyId    
            """)

        # cursor.execute("""select DOC.*,INSURANCE.* from DOC JOIN in_contract_with 
        #     ON DOC.medical_council_code = in_contract_with.medical_council_code AND
        #     DOC.username = in_contract_with.doc_username
        #     JOIN INSURANCE ON 
        #     INSURANCE.insuranceId = in_contract_with.insuranceId
        # """)
        # temp=cursor.fetchall()
        # print(len(temp))
        # cursor.execute("""SELECT * FROM DOC""")
        val = cursor.fetchall()
        # print(len(val))
        newlist =[]
        for i in val:
            newlist.append(f"نام :{i[2]} {i[3]}\nکد نظام پزشکی :{i[0]}\nهزینه ویزیت :{i[5]}\nتخصص :{i[8]}")        
        # write frist appointment khali
        conn.commit()
        cursor.close()
        conn.close()
        return newlist
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow("09175606163")
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
