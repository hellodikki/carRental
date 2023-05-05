from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import webbrowser
import sqlite3
import hashlib
from main import Ui_MainWindow
con = sqlite3.connect('carRental.sqlite')
cur = con.cursor()

class Ui_LoginWindow(object):
    def openMain(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.inscriptionButton())
        self.pushButton.setGeometry(QtCore.QRect(410, 351, 83, 29))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.conectionButton())
        self.pushButton_2.setGeometry(QtCore.QRect(320, 351, 83, 29))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 310, 171, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(320, 220, 171, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 280, 171, 28))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 50, 431, 131))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(380, 190, 51, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 250, 71, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 510, 211, 31))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "SignIn"))
        self.pushButton_2.setText(_translate("MainWindow", "LogIn"))
        self.label.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "Name :"))
        self.label_4.setText(_translate("MainWindow", "Password :"))
        self.label_5.setText(_translate("MainWindow", "DAHBI Ayoub/MOUSSAOUI Anwar"))
    
    def conectionButton(self):
        username=self.lineEdit.text()
        password=self.lineEdit_2.text()
        husername = hashlib.sha256(username.encode()).hexdigest()
        hpassword = hashlib.sha256(password.encode()).hexdigest()
        cur.execute("SELECT * FROM user WHERE username = ? AND password = ?",(husername,hpassword,))
        users=cur.fetchall()
        if(len(users) > 0):
            self.openMain()
        else:
            self.label.setText("Invalid!")
    
    def inscriptionButton(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        husername = hashlib.sha256(username.encode()).hexdigest()
        hpassword = hashlib.sha256(password.encode()).hexdigest()
        cur.execute("SELECT * FROM user WHERE username = ?",(husername,))
        users=cur.fetchall()
        if(len(users) > 0):
            self.label.setText("Username exist!")
        else:
            con.execute("INSERT INTO user(username, password) VALUES(?,?)",(husername,hpassword,))
            self.label.setText("Account created!")
            con.commit()     


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
