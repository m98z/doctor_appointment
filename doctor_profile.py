# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'doctor_profile2.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from database_create import *
from get_appointment import *

class Ui_Doctor_profile(object):

    def __init__(self, phone, medical_council_code, doctor_username):
        # print(phone,medical_council_code,doctor_username)
        self.phone = phone
        self.medical_council_code = medical_council_code
        self.doctor_username = doctor_username

    def setupUi(self, Doctor_profile):
        Doctor_profile.setObjectName("Doctor_profile")
        Doctor_profile.resize(1082, 930)
        self.centralwidget = QtWidgets.QWidget(Doctor_profile)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.doctor_save = QtWidgets.QPushButton(self.tab)
        self.doctor_save.setGeometry(QtCore.QRect(10, 60, 112, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doctor_save.setFont(font)
        self.doctor_save.setObjectName("doctor_save")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(50, 20, 739, 569))
        self.label_10.setObjectName("label_10")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(590, 60, 131, 31))
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(580, 50, 231, 61))
        self.label_9.setObjectName("label_9")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(700, 40, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.appointment_btn = QtWidgets.QPushButton(self.tab)
        self.appointment_btn.setGeometry(QtCore.QRect(90, 700, 739, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.appointment_btn.setFont(font)
        self.appointment_btn.setObjectName("appointment_btn")
        self.tabWidget.addTab(self.tab, "")

        self.tab_3 = QtWidgets.QWidget() #doctors page
        self.tab_3.setObjectName("tab_3")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(540, 30, 461, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_b = QtWidgets.QLabel(self.tab)
        self.label_b.setGeometry(QtCore.QRect(140, 400, 761, 411))
        # font = QtGui.QFont()
        # font.setPointSize(20)
        # font.setBold(True)
        # font.setWeight(75)
        # self.label_b.setFont(font)
        self.label_b.setObjectName("label_b")

        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_2.setGeometry(QtCore.QRect(670, 120, 331, 70))
        self.textEdit_2.setObjectName("textEdit_2")
        self.find = QtWidgets.QPushButton(self.tab_3)
        self.find.setGeometry(QtCore.QRect(540, 120, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.find.setFont(font)
        self.find.setObjectName("find")
        self.appointment = QtWidgets.QPushButton(self.tab_3) 
        self.appointment.setGeometry(QtCore.QRect(550, 250, 461, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.appointment.setFont(font)
        self.appointment.setObjectName("appointment") #reserve nobat tab_3
        self.appointment2 = QtWidgets.QPushButton(self.tab_3)
        self.appointment2.setGeometry(QtCore.QRect(550, 390, 461, 111))
        self.appointment2.setFont(font)
        self.appointment2.setObjectName("appointment2") #see profile
        self.listView_2 = QtWidgets.QListView(self.tab_3)
        self.listView_2.setGeometry(QtCore.QRect(10, 20, 511, 791))
        self.listView_2.setObjectName("listView_2")
        model = QtGui.QStandardItemModel()
        self.listView_2.setModel(model)
        list_doctor = self.db_get_doctor()
        for i in list_doctor:                
            item = QtGui.QStandardItem(str(i))
            item.setEditable(False)
            model.appendRow(item)
        self.find.clicked.connect(self.find_clicked)
        self.listView_2.clicked.connect(self.cli)
        self.listView_2.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
        self.tabWidget.addTab(self.tab_3, "")

        self.tab_2 = QtWidgets.QWidget() #comments page
        self.tab_2.setObjectName("tab_2")

        self.listView = QtWidgets.QListView(self.tab_2) #comments box
        self.listView.setGeometry(QtCore.QRect(70, 140, 971, 291))
        self.listView.setObjectName("listView")
        comment_list = self.get_comment()

        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)
        for i in comment_list:                
            item = QtGui.QStandardItem(i[0]+" "+i[1]+":"+" "+i[2])
            item.setEditable(False)
            model.appendRow(item)

        self.label_7 = QtWidgets.QLabel(self.tab_2) #comment lable
        self.label_7.setGeometry(QtCore.QRect(840, 450, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.lineEdit = QtWidgets.QLineEdit(self.tab_2) #comment editor box
        self.lineEdit.setGeometry(QtCore.QRect(190, 500, 851, 231))

        self.send = QtWidgets.QDialogButtonBox(self.tab_2)
        self.send.setGeometry(QtCore.QRect(190, 740, 166, 25))
        self.send.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)

        self.send.accepted.connect(self.accept)
        self.send.rejected.connect(self.reject)
        
        self.send.setObjectName("send")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(640, 60, 401, 101))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        Doctor_profile.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Doctor_profile)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1082, 22))
        self.menubar.setObjectName("menubar")
        Doctor_profile.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Doctor_profile)
        self.statusbar.setObjectName("statusbar")
        Doctor_profile.setStatusBar(self.statusbar)
        self.retranslateUi(Doctor_profile)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Doctor_profile)
        self.doctor_save.clicked.connect(self.save_doctor)
        self.appointment2.clicked.connect(self.open_new_profile)
        self.appointment_btn.clicked.connect(self.open_reseve)
        self.appointment.clicked.connect(self.open_reseve_2)

        if self.get_profile()[0]  == 0:
            self.label_9.setText("0"+"/5")
        else:
            self.label_9.setText(str(self.get_profile()[0][0][0])+"/5") #score
        
        # print(str(ui.get_profile()[0]))
        about_doctor = ""
        about_doctor += "کد نظام پزشکی "+":"+str(self.get_profile()[1][0][0])+"\n"
        about_doctor +=  "نام "+":"+str(self.get_profile()[1][0][2])+"\n"
        about_doctor += "نام خانوادگی "+":"+str(self.get_profile()[1][0][3])+ "\n"
        about_doctor += "هزینه ویزیت "+":"+str(self.get_profile()[1][0][5])+ "\n"
        about_doctor +=  "تخصص "+":"+str(self.get_profile()[1][0][-1])+"\n"
        self.label_10.setText(about_doctor) #about doctor
        self.busy()

    def busy(self):
        print("hi")
        conn=sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        cursor.execute("""
        SELECT WORK_HOUR.starthour,WORK_HOUR.endhour,WORK_HOUR.date,ADDRESS.street,ADDRESS.alley,ADDRESS.plaque FROM APPOINTMENT,DHH,WORK_HOUR ,DOCTOR,ADDRESS,HEALTHCARE
        WHERE 
        DOCTOR.medical_council_code = ?
        AND DOCTOR.username = ?
        AND DOCTOR.medical_council_code = APPOINTMENT.medical_council_code
        AND DOCTOR.username = APPOINTMENT.doc_username
        AND APPOINTMENT.appointmentId = DHH.appointmentId 
        AND DHH.dhhId =  APPOINTMENT.dhhId
        AND DHH.dhhId = WORK_HOUR.dhhId
        and DHH.healthcareId = HEALTHCARE.healthcareId
        and HEALTHCARE.addressId = ADDRESS.addressId
        and HEALTHCARE.healthcareId = ADDRESS.healthcareId
        UNION
        SELECT WORK_HOUR.starthour,WORK_HOUR.endhour,WORK_HOUR.date,ADDRESS.street,ADDRESS.alley,ADDRESS.plaque FROM APPOINTMENT,DOH,WORK_HOUR,DOCTOR,ADDRESS,DOCTOR_OFFICE
        WHERE
        DOCTOR.medical_council_code = ?
        AND DOCTOR.username = ?
        AND DOCTOR.medical_council_code = APPOINTMENT.medical_council_code
        AND DOCTOR.username = APPOINTMENT.doc_username
        AND APPOINTMENT.appointmentId = DOH.appointmentId 
        AND DOH.dohId =  APPOINTMENT.dohId
        AND DOH.dohId = WORK_HOUR.dohId
        and DOH.docofficeId = DOCTOR_OFFICE.docofficeId
        and DOCTOR_OFFICE.addressId = ADDRESS.addressId
        and DOCTOR_OFFICE.docofficeId = ADDRESS.docofficeId
         """,(self.medical_council_code, self.doctor_username, self.medical_council_code, self.doctor_username))
        doctor_busy_time = cursor.fetchall()
        print("busy time: ", doctor_busy_time)
        fin = ''
        for i in doctor_busy_time:
            fin += str(i)
            fin += '\n' 
        self.label_b.setText(fin)
        cursor.close()
        conn.close()
        return doctor_busy_time
    def open_reseve_2(self):
        # textEdit_2
        list_doc = self.textEdit_2.toPlainText().split('\n')
        if(len(list_doc) == 0 ):
            self.pop_message("پزشکی انتخاب نشده است")
        else:
            for i in list_doc:
                index = i.split(':')
                if index[0] == 'کد نظام پزشکی ':
                    # print(index[1])
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
                    self.ui = Ui_Get_Appointment(self.phone,val[0][0],val[0][1])
                    self.ui.setupUi(self.window)
                    self.window.show()

    def open_reseve(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Get_Appointment(self.phone,self.medical_council_code,self.doctor_username)
        self.ui.setupUi(self.window)
        self.window.show()

    def get_comment(self):
        conn = sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT USER.fname, USER.fname , COMMENT.comment_txt FROM USER, APPOINTMENT, DOCTOR, COMMENT
        WHERE
        USER.phone = APPOINTMENT.phone
        AND APPOINTMENT.doc_username = DOCTOR.username
        AND APPOINTMENT.medical_council_code = DOCTOR.medical_council_code
        AND COMMENT.appointmentId = APPOINTMENT.appointmentId
        AND DOCTOR.username = ?
        AND DOCTOR.medical_council_code = ?
        AND APPOINTMENT.doc_username = ?
        AND APPOINTMENT.medical_council_code =?
        ORDER BY APPOINTMENT.appointmentId
         """,(self.doctor_username, self.medical_council_code, self.doctor_username, self.medical_council_code))
        # print(self.phone, self.doctor_username, self.medical_council_code)
        comment_list = cursor.fetchall()
        cursor.fetchall()
        cursor.close()
        conn.close()
        # print(comment_list)
        return comment_list

    def accept(self):
        comment_text = self.lineEdit.text()
        conn=sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT APPOINTMENT.appointmentId,USER.fname, USER.lname FROM USER, APPOINTMENT
        WHERE USER.phone = ?
        AND APPOINTMENT.phone = USER.phone
        AND APPOINTMENT.medical_council_code = ?
        AND APPOINTMENT.doc_username = ?
        """,(self.phone, self.medical_council_code, self.doctor_username))
        appointments = cursor.fetchall()
        cursor.close()
        if len(appointments) != 0:
            cursor = conn.cursor()
            cursor.execute(""" INSERT INTO COMMENT 
                (
                    comment_txt,
                    appointmentId
                )
                VALUES(?,?)
            """,(comment_text, appointments[0][0])) #
            self.pop_message("نظر شما با موفقیت ثبت شد", "\u2713") #
            conn.commit()
            cursor.close()
            conn.close()
            model = QtGui.QStandardItemModel()
            comment_list = self.get_comment()
            self.listView.setModel(model)
            for i in comment_list:                
                item = QtGui.QStandardItem(i[0]+" "+i[1]+":"+" "+i[2])
                item.setEditable(False)
                model.appendRow(item)
            self.reject()
        else:
            self.pop_message("شما تاکنون با این دکتر نوبت نداشته اید\n لزا نمیتوانید نظری ارسال کنید","\u2717")
            self.reject()
            conn.commit()
            cursor.close()
            conn.close()

    
    def reject(self):
        self.lineEdit.setText(None)
    

    def openwndow(self, Ui):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui(self.phone,self.medid, self.user)
        self.ui.setupUi(self.window)
        self.window.show()
        if self.ui.get_profile()[0]  == 0:
            self.ui.label_9.setText("0"+"/5")
        else:
            self.ui.label_9.setText(str(self.ui.get_profile()[0][0][0])+"/5") #score
        about_doctor = ""
        about_doctor += "کد نظام پزشکی "+":"+str(self.ui.get_profile()[1][0][0])+"\n"
        about_doctor +=  "نام "+":"+str(self.ui.get_profile()[1][0][2])+"\n"
        about_doctor += "نام خانوادگی "+":"+str(self.ui.get_profile()[1][0][3])+ "\n"
        about_doctor += "هزینه ویزیت "+":"+str(self.ui.get_profile()[1][0][5])+ "\n"
        about_doctor +=  "تخصص "+":"+str(self.ui.get_profile()[1][0][-1])+"\n"
        self.ui.label_10.setText(about_doctor) #about #TODO khoskel sazi
        # self.ui.label_9.setText(str(ui.get_profile()[1][0][0])+"/5") #score
        
    def open_new_profile(self):
        self.openwndow(Ui_Doctor_profile)

    def find_clicked(self):
        filter_text = str(self.textEdit_2.toPlainText())        
        for row in range(self.listView_2.model().rowCount()):
            if filter_text in str(self.listView_2.model().item(row).text()).lower():
                self.listView_2.setRowHidden(row, False)
            else:
                self.listView_2.setRowHidden(row, True)


    def cli(self, index):
        doc_list_data = str(self.listView_2.model().itemData(index)[0]).split("\n")
        conn = sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT username FROM DOCTOR WHERE
        DOCTOR.medical_council_code = ? 
        """,(doc_list_data[0],))
        val = cursor.fetchall()
        self.user = val[0][0]
        self.medid = doc_list_data[0]
        doc_data = ""
        doc_data_list = []
        doc_data += "کد نظام پزشکی "+":"+doc_list_data[0]+"\n"
        doc_data_list = [doc_list_data[0], doc_list_data[1], doc_list_data[2], doc_list_data[3],doc_list_data[4]]
        doc_data += "نام "+":"+doc_list_data[1]+"\n"
        doc_data += "نام خانوادگی "+":"+doc_list_data[2]+"\n"
        doc_data += "هزینه ویزیت "+":"+doc_list_data[3]+"\n"
        doc_data +=  "تخصص "+":"+doc_list_data[4]+"\n"
        self.textEdit_2.setText(doc_data)
 
   
    def db_get_doctor(self):
        conn = sqlite3.connect('tabib.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT specialtyId FROM DOCTOR 
        WHERE DOCTOR.medical_council_code = ? 
        AND DOCTOR.username = ?
        """,(self.medical_council_code, self.doctor_username))
        specialtyId = cursor.fetchall()
        specialtyId = specialtyId[0][0]
        cursor = conn.cursor()
        cursor.execute("""SELECT DOCTOR.*, SPECIALTY.name FROM DOCTOR JOIN SPECIALTY ON
        DOCTOR.medical_council_code <> ? 
        AND DOCTOR.username <> ?
        AND DOCTOR.specialtyId = ? 
        AND DOCTOR.specialtyId = SPECIALTY.specialtyId """,(self.medical_council_code, self.doctor_username, specialtyId))
        val = cursor.fetchall()
        newlist =[]
        for i in val:
            newlist.append(f"{i[0]}\n{i[2]}\n{i[3]}\n{i[5]}\n{i[-1]}") #medi,fname,lname,photo,specialty
        conn.commit()
        cursor.close()
        conn.close()
        return newlist
        

    def get_profile(self):
        d = Database_create()
        d.create()
        profile_data = []
        try:
            conn=sqlite3.connect('tabib.db')
            cursor = conn.cursor()
            cursor.execute("""
                SELECT avg(score) FROM APPOINTMENT, DOCTOR
                WHERE DOCTOR.username = ? AND DOCTOR.medical_council_code = ? AND APPOINTMENT.doc_username =  DOCTOR.username AND
                APPOINTMENT.medical_council_code = DOCTOR.medical_council_code
            """,(self.doctor_username, self.medical_council_code))
            score = cursor.fetchall()
            # print(score)
            if score[0][0] == None:
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
        # print(self.profile_data)
        return self.profile_data


    def retranslateUi(self, Doctor_profile):
        _translate = QtCore.QCoreApplication.translate
        Doctor_profile.setWindowTitle(_translate("Doctor_profile","صفحه پروفایل پزشک"))
        self.doctor_save.setText(_translate("Doctor_profile", "ذخیره پزشک")) 
        self.label_2.setText(_translate("Doctor_profile", "امتیاز پزشک")) 
        self.label.setText(_translate("Doctor_profile", "مشخصات پزشک"))
        self.appointment_btn.setText(_translate("Doctor_profile", "رزرو نوبت"))        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Doctor_profile", "پروفایل پزشک"))
        self.label_3.setText(_translate("Doctor_profile", "سایر پزشکان هم متخصص"))
        self.find.setText(_translate("Doctor_profile", "جستجو"))
        self.label_b.setText(_translate("Doctor_profile", "ساعت کاری"))
        self.appointment.setText(_translate("Doctor_profile", "رزرو نوبت"))
        self.appointment2.setText(_translate("Doctor_profile", "مشاهده پروفایل"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Doctor_profile", "سایر پزشکان"))
        self.label_7.setText(_translate("Doctor_profile", "ارسال نظر "))
        self.label_8.setText(_translate("Doctor_profile", "نظرات بیماران پزشک"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Doctor_profile", "نظرات"))


    def save_doctor(self):
        d = Database_create()
        d.create()
        try:
            conn=sqlite3.connect('tabib.db')
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM saved
                WHERE phone = ? AND medical_council_code = ? and doc_username = ?           
            """,(self.phone, self.medical_council_code, self.doctor_username,))
            val = cursor.fetchall()
            if len(val) == 0:
                cursor.execute(""" INSERT INTO saved
                    (phone,
                    medical_council_code,
                    doc_username
                    )
                VALUES(?,?,?)
                """,(self.phone, self.medical_council_code, self.doctor_username,))
                conn.commit()
                cursor.close()
                conn.close()
                self.pop_message("پزشک با موفقیت ذخیره شد", "\u2713")
            else:
                self.pop_message("پزشک  قبلا ذخیره شده است", "\u2717")
        except :
            self.pop_message("خطا","\u2717")
    

    def pop_message(self,text,title):
        msg=QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.setWindowTitle(title)
        msg.exec_()
    

    def readBlobData(self,empId):
        try:
            sqliteConnection = sqlite3.connect('tabib.db')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            sql_fetch_blob_query = """SELECT * from USER where phone = ?"""
            cursor.execute(sql_fetch_blob_query, (empId,))
            record = cursor.fetchall()
            for row in record:
                phone  = row[0]
                photo = row[3]
                print("Storing employee image and resume on disk \n")
                photoPath = "D:\\" + phone + ".jpg"
                self.writeTofile(photo, photoPath)
                qimg = QtGui.QImage.fromData(photo)
                pixmap = QtGui.QPixmap.fromImage(qimg)
                self.imagepath.setPixmap(pixmap)
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to read blob data from sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
                print("sqlite connection is closed")

            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Doctor_profile = QtWidgets.QMainWindow()
    ui = Ui_Doctor_profile("09175606163","1","q")
    ui.setupUi(Doctor_profile)
    Doctor_profile.show()
    # print(ui.get_profile()[0][0][0])
    if ui.get_profile()[0]  == 0:
        ui.label_9.setText("0"+"/5")
    else:
        ui.label_9.setText(str(ui.get_profile()[0][0][0])+"/5") #score
       
    # print(str(ui.get_profile()[0]))
    about_doctor = ""
    about_doctor += "کد نظام پزشکی "+":"+str(ui.get_profile()[1][0][0])+"\n"
    about_doctor +=  "نام "+":"+str(ui.get_profile()[1][0][2])+"\n"
    about_doctor += "نام خانوادگی "+":"+str(ui.get_profile()[1][0][3])+ "\n"
    about_doctor += "هزینه ویزیت "+":"+str(ui.get_profile()[1][0][5])+ "\n"
    about_doctor +=  "تخصص "+":"+str(ui.get_profile()[1][0][-1])+"\n"
    ui.label_10.setText(about_doctor) #about doctor

    sys.exit(app.exec_())