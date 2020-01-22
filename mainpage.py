# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\term5\tabibPy\GUI-using-PyQT5-python-master\GUI-using-PyQT5-python-master\Login Page with Database\tap.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
# path = "find.gif"
# img = Image.open(path)
# img = img.convert("RGBA")
# pix = img.load()
# for y in range(img.size[1]):
#     for x in range(img.size[0]):
#         if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
#             pix[x, y] = (0, 0, 0, 255)
#         else:
#             pix[x, y] = (255, 255, 255, 255)
#     img.save("temp.jpg")
# text = pytesseract.image_to_string(Image.open("temp.jpg"))
# # os.remove(‘temp.jpg’)
# print(text)#print image_to_string(Image.open(‘find.jpg’))

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(597, 435)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.sfdg = QtWidgets.QWidget()
        self.sfdg.setObjectName("sfdg")
        self.tabWidget.addTab(self.sfdg, "")
        self.dfb = QtWidgets.QWidget()
        self.dfb.setObjectName("dfb")
        self.tabWidget.addTab(self.dfb, "")
        self.dfbg = QtWidgets.QWidget()
        self.dfbg.setObjectName("dfbg")
        self.listView_2 = QtWidgets.QListView(self.dfbg)
        self.listView_2.setGeometry(QtCore.QRect(6, 56, 271, 301))
        self.listView_2.setObjectName("listView_2")


        model = QtGui.QStandardItemModel()
        self.listView_2.setModel(model)

        list_doctor = self.db_fetch_doctor()

        for i in list_doctor:                
            item = QtGui.QStandardItem(str(i))
            item.setEditable(False)
            model.appendRow(item)

        self.listView_2.clicked.connect(self.cli)
        self.listView_2.setStyleSheet("QListView::item:!selected { border-bottom: 1px solid black; padding: 2px; }")
        
        self.label = QtWidgets.QLabel(self.dfbg)
        self.label.setGeometry(QtCore.QRect(10, 0, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.search = QtWidgets.QLineEdit(self.dfbg)
        self.search.setGeometry(QtCore.QRect(390, 90, 161, 31))
        self.search.setObjectName("search")
        self.label_2 = QtWidgets.QLabel(self.dfbg)
        self.label_2.setGeometry(QtCore.QRect(290, 60, 280, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.find = QtWidgets.QPushButton(self.dfbg)
        self.find.setGeometry(QtCore.QRect(310, 90, 71, 31))
        self.find.setObjectName("find")

        self.find.clicked.connect(self.find_clicked)

        self.widget = QtWidgets.QWidget(self.dfbg)
        self.widget.setGeometry(QtCore.QRect(290, 130, 261, 231))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.appointment = QtWidgets.QPushButton(self.widget)
        self.appointment.setObjectName("appointment")
        self.verticalLayout.addWidget(self.appointment)

        self.appointment.clicked.connect(self.appointment_clicked)

        self.profile = QtWidgets.QPushButton(self.widget)
        self.profile.setObjectName("profile")
        self.verticalLayout.addWidget(self.profile)

        self.profile.clicked.connect(self.profile_clicked)
        
        self.tabWidget.addTab(self.dfbg, "")
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
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


   
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sfdg), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dfb), _translate("MainWindow", "Page"))
        self.label.setText(_translate("MainWindow", "لیست پزشکان"))
        self.label_2.setText(_translate("MainWindow", "جستجو نام یا تخصص پزشک"))
        self.find.setText(_translate("MainWindow", "جستجو"))
        self.appointment.setText(_translate("MainWindow", "رزرو نوبت"))
        self.profile.setText(_translate("MainWindow", "مشاهده پروفایل"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dfbg), _translate("MainWindow", "Tab 2"))
    
    def cli(self,index):
        # row = index.row()
        # print(self.listView_2.model().itemData(index)[0])
        self.search.setText(str(self.listView_2.model().itemData(index)[0]))

    def find_clicked(self):
        filter_text = str(self.search.text()).lower()
        for row in range(self.listView_2.model().rowCount()):
            if filter_text in str(self.listView_2.model().item(row).text()).lower():
                self.listView_2.setRowHidden(row, False)
            else:
                self.listView_2.setRowHidden(row, True)

    # def searchItem(self, model):
    #     search_string = self.search.text() # Created a QlineEdit to input search strings
    #     items = self.listView_2.model().findItems(search_string, QtCore.Qt.MatchStartsWith)
    #     print(search_string)
    #     print(items)
    #     if len(items) > 0:
    #         for item in items:
    #             if search_string:
    #                 self.model.takeRow(item.row()) #take row of item
    #                 self.model.insertRow(0, item)  # and bring it to the top
    #     else:
    #         print ("not found")
    def pop_message(self,text):
        msg=QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.setWindowTitle("خطا")
        msg.exec_()

    def profile_clicked(self):
        profile_text = str(self.search.text()).lower()
        if(len(profile_text) == 0 ):
            self.pop_message("پزشکی انتخاب نشده است")
        else:
            profile_list = profile_text.split("\n")
            # profile_list[0] = medical_code
            # go to profile doctor with this medical_code



    def appointment_clicked(self):
        # pixmap = QtGui.QPixmap(imagePath)
        # self.label.setPixmap(pixmap)
        # self.resize(pixmap.size())
        # self.adjustSize()
        pass
                

    def db_fetch_doctor(self):
        conn = sqlite3.connect('tabib.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM DOCTOR")
        val = cursor.fetchall()
        newlist =[]
        for i in val:
            newlist.append(f"{i[0]}\n{i[2]}\n{i[3]}\n{i[4]}\n{i[7]}") #medi,fname,lname,photo,specialty
        # print(newlist)
        
        conn.commit()
        cursor.close()
        conn.close()

        return newlist


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
