# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'get_appointment.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from database_create import *
from datetime import date, datetime
import decimal


class Ui_Get_Appointment(object):

    def __init__(self, phone, medical_council_code, doctor_username):
        self.phone = phone
        self.medical_council_code = medical_council_code
        self.doctor_username = doctor_username


    def setupUi(self, Get_Appointment):
        Get_Appointment.setObjectName("Get_Appointment")
        Get_Appointment.resize(998, 811)
        self.centralwidget = QtWidgets.QWidget(Get_Appointment)
        self.centralwidget.setObjectName("centralwidget")
        self.appointed_patient = QtWidgets.QComboBox(self.centralwidget)
        self.appointed_patient.setGeometry(QtCore.QRect(720, 340, 271, 51))
        self.appointed_patient.setObjectName("appointed_patient")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(860, 310, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.appointment_accept = QtWidgets.QPushButton(self.centralwidget)
        self.appointment_accept.setGeometry(QtCore.QRect(10, 660, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(20)

        self.appointment_accept.setFont(font)
        self.appointment_accept.setObjectName("appointment_accept")
        self.doctor_photo = QtWidgets.QLabel(self.centralwidget)
        self.doctor_photo.setGeometry(QtCore.QRect(800, 70, 181, 171))
        self.doctor_photo.setText("")
        self.doctor_photo.setObjectName("doctor_photo")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(790, 10, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.doctor_profile = QtWidgets.QLabel(self.centralwidget)
        self.doctor_profile.setGeometry(QtCore.QRect(480, 70, 301, 221))
        self.doctor_profile.setText("")
        self.doctor_profile.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.doctor_profile.setObjectName("doctor_profile")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 50, 141, 20))
        self.label_2.setObjectName("label_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(340, 400, 121, 51))
        self.label_8.setObjectName("label_8")

        self.appointment_time = QtWidgets.QLabel(self.centralwidget)
        self.appointment_time.setGeometry(QtCore.QRect(30, 440, 281, 61))
        self.appointment_time.setText("")
        self.appointment_time.setObjectName("appointment_time")


        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(230, 550, 67, 17))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(330, 520, 101, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 560, 311, 81))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(610, 310, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.insurance = QtWidgets.QComboBox(self.centralwidget)
        self.insurance.setGeometry(QtCore.QRect(470, 340, 241, 51))
        self.insurance.setObjectName("insurance")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 80, 451, 308))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.year = QtWidgets.QListView(self.widget) 
        self.year.setObjectName("year")
        self.horizontalLayout_3.addWidget(self.year)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # self.month = QtWidgets.QListView(self.widget)
        # self.month.setObjectName("month")
        # self.horizontalLayout_2.addWidget(self.month)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        # self.day = QtWidgets.QListView(self.widget)
        # self.day.setObjectName("day")
        # self.horizontalLayout_4.addWidget(self.day)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        # self.hour = QtWidgets.QListView(self.widget)
        # self.hour.setObjectName("hour")
        # self.gridLayout.addWidget(self.hour, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        Get_Appointment.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Get_Appointment)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 998, 22))
        self.menubar.setObjectName("menubar")
        Get_Appointment.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Get_Appointment)
        self.statusbar.setObjectName("statusbar")
        Get_Appointment.setStatusBar(self.statusbar)
        self.retranslateUi(Get_Appointment)
        QtCore.QMetaObject.connectSlotsByName(Get_Appointment)
        self.Combo_family(self.appointed_patient)
        self.appointed_patient.currentTextChanged.connect(self.find_insurance)
        return_list_insurance = self.find_insurance(self.insurance.currentText())
        self.year.clicked.connect(self.cli)
       
        self.near_time = self.nearest_free_time()
        self.appointment_accept.clicked.connect(self.cli_appointment_accept)
        print("now")
        print(self.near_time)
        

        model = QtGui.QStandardItemModel()
        self.year.setModel(model)
        for i in self.near_time:                
            item = QtGui.QStandardItem(i[2]+"\n"+i[0]+" - "+i[1]+"\n")
            item.setEditable(False)
            model.appendRow(item)
        self.nearest_free_time()
    
    def cli_appointment_accept(self):
        conn=sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        # self.near_time
        # print("now")
        # print(self.appointment_time.text())
        date = self.appointment_time.text().split('\n')[0]
        start_hour = self.appointment_time.text().split('\n')[1].split(" - ")[0]
        end_hour = self.appointment_time.text().split('\n')[1].split(" - ")[1]
        # print(date)
        # print(start_hour)
        # print(end_hour)
        result = []
        for i in self.near_time:
            if i[0] == start_hour and i[1] == end_hour and i[2] == date:
                result = i
        phone = self.appointed_patient.currentText()
        cursor.execute(""" INSERT INTO APPOINTMENT
                    (
                    phone,
                    paymentId,
                    medical_council_code,
                    doc_username,
                    dhhId,
                    dohId,
                    score
                )
                VALUES(?,?,?,?,?,?,?)
            """,(phone,1,self.medical_council_code, self.doctor_username,result[3], result[4], None)) #
        cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        self.pop_message("نوبت شما با موفقیت ثبت شد", "\u2713")
        

    def pop_message(self,text,title):
        msg=QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.setWindowTitle(title)
        msg.exec_()

    def cli(self, index):
        doc_list_data = str(self.year.model().itemData(index)[0])
        self.appointment_time.setText(doc_list_data)
        

        

    def find_insurance(self,phone):
        conn=sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        cursor.execute("""select distinct INSURANCE.name from INSURANCE,USER,in_contract_with
        WHERE USER.insuranceId = INSURANCE.insuranceId
        AND   INSURANCE.insuranceId = in_contract_with.insuranceId
        AND   in_contract_with.doc_username = ?
        AND   in_contract_with.medical_council_code = ?
        AND   USER.phone = ?
        """,(self.doctor_username, self.medical_council_code, phone))
        commen_insurance = cursor.fetchall()
        # print("commenInsurance", commen_insurance)
        cursor.close()
        cursor = conn.cursor()
        cursor.execute("""select distinct INSURANCE.name from INSURANCE,in_contract_with
        WHERE 
        INSURANCE.insuranceId = in_contract_with.insuranceId
        AND   in_contract_with.doc_username = ?
        AND   in_contract_with.medical_council_code = ?
        ORDER BY INSURANCE.insuranceId ASC
        """,(self.doctor_username, self.medical_council_code,))
        doctor_inurance = cursor.fetchall()
        cursor.close()
        insurance_list = []
        if len(commen_insurance) != 0:
            for x in commen_insurance:
                insurance_list.append(x[0])
        else:
            for x in doctor_inurance:
                insurance_list.append(x[0])
        conn.close()
        self.insurance.clear()
        self.insurance.addItems(insurance_list)
        

    def Combo_family(self,ins):
        conn=sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        cursor.execute(""" select suserPhone,USER.fname, USER.lname from is_family_of, USER
            WHERE is_family_of.fuserPhone = ?
            AND USER.phone = is_family_of.fuserPhone
         """,(self.phone,))
        combo_family_list = cursor.fetchall()
        family_phone = [self.phone]
        for x in combo_family_list:
            family_phone.append(x[0])
        conn.commit()
        cursor.close()
        conn.close()
        ins.addItems(family_phone)

    def get_busy_doctor_time(self):
        # print("hi")
        conn=sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT WORK_HOUR.* FROM APPOINTMENT,DHH,WORK_HOUR ,DOCTOR
        WHERE 
        DOCTOR.medical_council_code = ?
        AND DOCTOR.username = ?
        AND DOCTOR.medical_council_code = APPOINTMENT.medical_council_code
        AND DOCTOR.username = APPOINTMENT.doc_username
        AND APPOINTMENT.appointmentId = DHH.appointmentId 
        AND DHH.dhhId =  APPOINTMENT.dhhId
        AND DHH.dhhId = WORK_HOUR.dhhId
        UNION
        SELECT WORK_HOUR.* FROM APPOINTMENT,DOH,WORK_HOUR,DOCTOR
        WHERE
        DOCTOR.medical_council_code = ?
        AND DOCTOR.username = ?
        AND DOCTOR.medical_council_code = APPOINTMENT.medical_council_code
        AND DOCTOR.username = APPOINTMENT.doc_username
        AND APPOINTMENT.appointmentId = DOH.appointmentId 
        AND DOH.dohId =  APPOINTMENT.dohId
        AND DOH.dohId = WORK_HOUR.dohId
         """,(self.medical_council_code, self.doctor_username, self.medical_council_code, self.doctor_username))
        doctor_busy_time = cursor.fetchall()
        # print("busy time: ", doctor_busy_time)
        cursor.close()
        conn.close()
        return doctor_busy_time


    def get_avalable_doctor_time(self):
        # print("hi avalable")
        conn=sqlite3.connect('tabib.db')
        cursor = conn.cursor()

        cursor.execute("""
        SELECT WORK_HOUR.* FROM DHH,WORK_HOUR ,DOCTOR
        WHERE 
        DOCTOR.medical_council_code = ?
        AND DOCTOR.username = ?
        AND DOCTOR.username = DHH.doc_username
        AND DHH.dhhId = WORK_HOUR.dhhId
        AND DOCTOR.medical_council_code = DHH.medical_council_code
        AND DOCTOR.username = DHH.doc_username
        
        
        UNION
        SELECT WORK_HOUR.* FROM DOH,WORK_HOUR,DOCTOR
        WHERE
        DOCTOR.medical_council_code = ?
        AND DOCTOR.username = ?
        AND DOCTOR.username = DOH.doc_username
        AND DOH.dohId = WORK_HOUR.dohId
        AND DOCTOR.medical_council_code = DOH.medical_council_code
        AND DOCTOR.username = DOH.doc_username 

        GROUP BY WORK_HOUR.date
        
        
        """,(self.medical_council_code, self.doctor_username, self.medical_council_code, self.doctor_username, ))
        
        doctor_avalable_time = cursor.fetchall() 
        print("ail:",doctor_avalable_time)
        doctor_busy_time = self.get_busy_doctor_time()
        print("busy",doctor_busy_time)
        doctor_free_time = []
        for x in range(len(doctor_avalable_time)):
            temp = 0
            for y in range(len(doctor_busy_time)):
                if doctor_avalable_time[x][3] != doctor_busy_time[y][3]:
                    # doctor_free_time.append(doctor_avalable_time[x][1:])
                    temp = 1
                elif doctor_avalable_time[x][3] == doctor_busy_time[y][3] and doctor_avalable_time[x][2] < doctor_busy_time[y][1]:
                    doctor_free_time.append(doctor_avalable_time[x][1:])
                    temp = 1
                elif doctor_avalable_time[x][3] == doctor_busy_time[y][3] and doctor_avalable_time[x][2] > doctor_busy_time[y][2] and doctor_avalable_time[x][1] < doctor_busy_time[y][1]:
                    temp = 1
                    date =  doctor_avalable_time[x][3]
                    dhhid = doctor_avalable_time[x][4]
                    dohid = doctor_avalable_time[x][5]
                    busy_start = doctor_busy_time[y][1].split(':')
                    busy_end = doctor_busy_time[y][2].split(':')
                    avalable_start = doctor_avalable_time[x][1].split(':')
                    avalable_end =  doctor_avalable_time[x][2].split(':')
                    for i in range(int(avalable_start[0]),int(busy_start[0])):
                        doctor_free_time.append((str(i)+":00", str(i+1)+":00", date, dhhid, dohid))
                    for i in range(int(busy_end[0]),int(avalable_end[0])):
                        doctor_free_time.append((str(i)+":00", str(i+1)+":00", date, dohid, dohid))
                else: 
                    temp = 0
                    x = x+1
            if temp == 1:
                doctor_free_time.append(doctor_avalable_time[x][1:])
        cursor.close()
        conn.close()
        print("*******free\n", doctor_free_time)
        return doctor_free_time


    def nearest_free_time(self):
        today = str(date.today()).split('-')
        today_y = int(today[0])
        today_m = int(today[1])
        today_d = int(today[2])
        now = str(datetime.now()).split(" ")[1][:5]
        now_min = int(now[1])
        now_hour = int(now[0])
        time_choce = []
        free_time = self.get_avalable_doctor_time()
        for i in free_time:
            y = int(i[2].split('-')[0])
            m = int(i[2].split('-')[1])
            d = int(i[2].split('-')[2])
            sh = int(i[0].split(':')[0])
            se = int(i[1].split(':')[0])
            if y > today_y:
                time_choce.append(i)
            elif y == today_y and m > today_m:
                time_choce.append(i)
            elif m == today_m and d > today_d:
                time_choce.append(i)
            elif d == today_d and se >now_hour:
                 time_choce.append(i)
            else:
                continue
        # print(time_choce)
        return time_choce
                



    

    def get_profile(self):
        d = Database_create()
        d.create()
        profile_data = []
        try:
            conn=sqlite3.connect('tabib.db')
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM APPOINTMENT, DOCTOR
                WHERE DOCTOR.username = ? AND DOCTOR.medical_council_code = ? AND APPOINTMENT.doc_username =  DOCTOR.username AND
                APPOINTMENT.medical_council_code = DOCTOR.medical_council_code
            """,(self.doctor_username,self.medical_council_code))
            score = cursor.fetchall()
            
            if len(score) == 0:
                score = 0
            profile_data.append(score)
            cursor.execute("""
                SELECT DOCTOR.*, SPECIALTY.name FROM DOCTOR JOIN SPECIALTY ON SPECIALTY.specialtyId = DOCTOR.specialtyId
                WHERE DOCTOR.username = ? AND DOCTOR.medical_council_code = ?
            """,(self.doctor_username,self.medical_council_code))
            about = cursor.fetchall()
            profile_data.append(about)
            conn.commit()
            cursor.close()
            conn.close()
            self.profile_data = profile_data
        except  :
            print("error connecting to db")
            self.profile_data = None
            self.pop_message("خطا","\u2717")
        return self.profile_data

    def retranslateUi(self, Get_Appointment):
        _translate = QtCore.QCoreApplication.translate
        Get_Appointment.setWindowTitle(_translate("Get_Appointment", "صفحه رزرو نوبت"))
        self.label.setText(_translate("Get_Appointment", "نوبت برای"))
        self.appointment_accept.setText(_translate("Get_Appointment", "+تایید نوبت"))

        # self.change_insurance.setText(_translate("Get_Appointment", "تغییر بیمه"))

        self.label_4.setText(_translate("Get_Appointment", "مشخصات پزشک"))
        self.label_2.setText(_translate("Get_Appointment", "تاریخ نوبت خالی از "))
        self.label_8.setText(_translate("Get_Appointment", "نوبت انتخاب شده"))
        self.label_10.setText(_translate("Get_Appointment", "هزینه نوبت "))
        self.label_12.setText(_translate("Get_Appointment", "انتخاب بیمه"))
        # self.label_5.setText(_translate("Get_Appointment", "تاریخ"))
        # self.label_3.setText(_translate("Get_Appointment", "ماه"))
        # self.label_6.setText(_translate("Get_Appointment", "روز"))
        # self.label_7.setText(_translate("Get_Appointment", "ساعت"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Get_Appointment = QtWidgets.QMainWindow()
    ui = Ui_Get_Appointment("0917","1","q")
    ui.setupUi(Get_Appointment)
    Get_Appointment.show()
    about_doctor = ""
    about_doctor += "کد نظام پزشکی"+"\t"+str(ui.get_profile()[1][0][0])+"\n"
    about_doctor +=  " نام "+"\t"+"\t"+str(ui.get_profile()[1][0][2])+"\n"
    about_doctor += "نام خانوادگی"+"\t"+str(ui.get_profile()[1][0][3])+ "\n"
    about_doctor += "هزینه ویزیت"+"\t"+str(ui.get_profile()[1][0][5])+ "\n"
    about_doctor +=  "تخصص"+"\t"+"\t"+str(ui.get_profile()[1][0][-1])+"\n"
    # print(str(ui.get_profile()))
    ui.doctor_profile.setText(about_doctor) #about doctor


    sys.exit(app.exec_())

    # sys.exit(app.exec_())