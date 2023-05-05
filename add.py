from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3
con = sqlite3.connect('carRental.sqlite')
cur = con.cursor()

class Ui_AddWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 30, 221, 131))
        self.label.setAutoFillBackground(True)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(""))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 220, 91, 31))
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(460, 61, 351, 471))
        self.listWidget.setObjectName("listWidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 260, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 300, 121, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 340, 91, 31))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.create())
        self.pushButton.setGeometry(QtCore.QRect(180, 440, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(110, 380, 91, 31))
        self.label_10.setObjectName("label_10")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.reset())
        self.pushButton_2.setGeometry(QtCore.QRect(780, 18, 31, 31))
        self.pushButton_2.setText("⟳")
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(460, 17, 311, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit.textChanged.connect(self.update_list)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 220, 161, 28))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 260, 161, 28))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(260, 340, 161, 28))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.hide()

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(320, 300, 48, 29))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(320, 380, 48, 29))
        self.spinBox_2.setObjectName("spinBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.open())
        self.pushButton_2.setGeometry(QtCore.QRect(180, 180, 111, 29))
        self.pushButton_2.setObjectName("pushButton_2")
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

        cur.execute("SELECT marque FROM car")
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Marque"))
        self.label_3.setText(_translate("MainWindow", "Type de carburant"))
        self.label_4.setText(_translate("MainWindow", "Nombre de place"))
        self.label_5.setText(_translate("MainWindow", "Transmission"))
        self.pushButton.setText(_translate("MainWindow", "Ajouter"))
        self.label_10.setText(_translate("MainWindow", "Prix jounalié"))
        self.pushButton_2.setText(_translate("MainWindow", "Ajouter photo"))

    def open(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(None, 'Open Image File', r"C:\\Users\\PC\Downloads\\", "Image files (*.jpg)")
        self.label.setPixmap(QtGui.QPixmap(fname[0]))
        self.lineEdit_6.setText(fname[0])

    def update_list(self, text) :
        self.listWidget.clear()
        cur.execute("SELECT marque FROM car WHERE marque LIKE ?",(text+'%',))
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])
    
    def reset(self) :
        self.lineEdit.setText("")
        self.listWidget.clear()
        cur.execute("SELECT marque FROM car")
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])
    
    def create(self) :
        img = self.lineEdit_6.text()
        #sql = "INSERT INTO car (marque) VALUES (%s)"
        val = self.lineEdit_2.text()
        #sql = "INSERT INTO car (carburant) VALUES (%s)"
        val1 = self.lineEdit_3.text()
        #sql = "INSERT INTO car (place) VALUES (%s)"
        val2 = self.spinBox.text()
        #sql = "INSERT INTO car (transmission) VALUES (%s)"
        val3 = self.lineEdit_5.text()
        #sql = "INSERT INTO car (prix) VALUES (%s)"
        val4 = self.spinBox_2.text()
        cur.execute("INSERT INTO car (image,marque,carburant,place,transmission,prix) VALUES (?, ?, ?, ?, ?, ?)",(img,val, val1, val2, val3, val4))
        con.commit()
        msg = QMessageBox()
        msg.setWindowTitle("Reussit")
        msg.setText("La voiture été bien mise a jour!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.exec_()
    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AddWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
