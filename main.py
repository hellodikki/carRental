from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import webbrowser
from add import Ui_AddWindow
from update import Ui_UpdateWindow
from reservation import Ui_ReservationWindow
import sqlite3
con = sqlite3.connect('carRental.sqlite')
cur = con.cursor()

class Ui_MainWindow(object):
    def openAdd(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AddWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def openUpdate(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_UpdateWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def openReservation(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ReservationWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
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

        self.listWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listWidget.itemClicked.connect(self.clicked)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 260, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 300, 121, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 340, 91, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(260, 220, 91, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(260, 260, 91, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(260, 300, 91, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(260, 340, 91, 31))
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.reserver())
        self.pushButton.setGeometry(QtCore.QRect(180, 440, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.openReservation())
        self.pushButton_3.setGeometry(QtCore.QRect(150, 490, 151, 29))
        self.pushButton_3.setObjectName("pushButton_3")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(110, 380, 91, 31))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(260, 380, 91, 31))
        self.label_11.setObjectName("label_11")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(460, 17, 311, 31))
        self.lineEdit.setText("")

        self.lineEdit.textChanged.connect(self.update_list)

        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.hide()

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.reset())
        self.pushButton_2.setGeometry(QtCore.QRect(780, 18, 31, 31))
        self.pushButton_2.setText("⟳")
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 25))
        self.menubar.setObjectName("menubar")

        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuDahbi_Ayoub = QtWidgets.QMenu(self.menuAbout)
        self.menuDahbi_Ayoub.setObjectName("menuDahbi_Ayoub")
        self.menuMoussaoui_Anwar = QtWidgets.QMenu(self.menuAbout)
        self.menuMoussaoui_Anwar.setObjectName("menuMoussaoui_Anwar")
        self.menuSearch = QtWidgets.QMenu(self.menubar)
        self.menuSearch.setObjectName("menuSearch")
        self.menuType_de_carburant = QtWidgets.QMenu(self.menuSearch)
        self.menuType_de_carburant.setObjectName("menuType_de_carburant")
        self.menuNombre_de_place = QtWidgets.QMenu(self.menuSearch)
        self.menuNombre_de_place.setObjectName("menuNombre_de_place")
        self.menuTransmission = QtWidgets.QMenu(self.menuSearch)
        self.menuTransmission.setObjectName("menuTransmission")
        self.menuPrix_journali = QtWidgets.QMenu(self.menuSearch)
        self.menuPrix_journali.setObjectName("menuPrix_journali")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd = QtWidgets.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")

        self.actionAdd.triggered.connect(self.openAdd)

        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")

        self.actionDelete.triggered.connect(self.deleteCar)

        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")

        self.actionUpdate.triggered.connect(self.openUpdate)

        self.actionLinkedIn = QtWidgets.QAction(MainWindow)
        self.actionLinkedIn.setObjectName("actionLinkedIn")

        self.actionLinkedIn.triggered.connect(self.ayoubLinked)

        self.actionGithub = QtWidgets.QAction(MainWindow)
        self.actionGithub.setObjectName("actionGithub")

        self.actionGithub.triggered.connect(self.ayoubGit)

        self.actionLinkedIn_2 = QtWidgets.QAction(MainWindow)
        self.actionLinkedIn_2.setObjectName("actionLinkedIn_2")

        self.actionLinkedIn_2.triggered.connect(self.anwarLinked)

        self.actionGithub_2 = QtWidgets.QAction(MainWindow)
        self.actionGithub_2.setObjectName("actionGithub_2")

        self.actionGithub_2.triggered.connect(self.anwarGit)

        self.actionHybride = QtWidgets.QAction(MainWindow)
        self.actionHybride.setObjectName("actionHybride")

        self.actionHybride.triggered.connect(self.findHybride)

        self.actionEssence = QtWidgets.QAction(MainWindow)
        self.actionEssence.setObjectName("actionEssence")

        self.actionEssence.triggered.connect(self.findEssence)

        self.actionDiesel = QtWidgets.QAction(MainWindow)
        self.actionDiesel.setObjectName("actionDiesel")

        self.actionDiesel.triggered.connect(self.findDiesel)

        self.actionElectrique = QtWidgets.QAction(MainWindow)
        self.actionElectrique.setObjectName("actionElectrique")

        self.actionElectrique.triggered.connect(self.findElectrique)

        self.actionDeux = QtWidgets.QAction(MainWindow)
        self.actionDeux.setObjectName("actionDeux")

        self.actionDeux.triggered.connect(self.findDeux)

        self.actionQuatre = QtWidgets.QAction(MainWindow)
        self.actionQuatre.setObjectName("actionQuatre")

        self.actionQuatre.triggered.connect(self.findQuatre)

        self.actionCinq = QtWidgets.QAction(MainWindow)
        self.actionCinq.setObjectName("actionCinq")

        self.actionCinq.triggered.connect(self.findCinq)

        self.actionAutomatique = QtWidgets.QAction(MainWindow)
        self.actionAutomatique.setObjectName("actionAutomatique")

        self.actionAutomatique.triggered.connect(self.findAutomatique)

        self.actionManuelle = QtWidgets.QAction(MainWindow)
        self.actionManuelle.setObjectName("actionManuelle")

        self.actionManuelle.triggered.connect(self.findManuelle)

        self.action200 = QtWidgets.QAction(MainWindow)
        self.action200.setObjectName("action200")

        self.action200.triggered.connect(self.find200)

        self.action400 = QtWidgets.QAction(MainWindow)
        self.action400.setObjectName("action400")

        self.action400.triggered.connect(self.find400)

        self.action500 = QtWidgets.QAction(MainWindow)
        self.action500.setObjectName("action500")

        self.action500.triggered.connect(self.find500)

        self.action600 = QtWidgets.QAction(MainWindow)
        self.action600.setObjectName("action600")

        self.action600.triggered.connect(self.find600)

        self.menuOptions.addAction(self.actionAdd)
        self.menuOptions.addAction(self.actionUpdate)
        self.menuOptions.addAction(self.actionDelete)
        self.menuDahbi_Ayoub.addAction(self.actionLinkedIn)
        self.menuDahbi_Ayoub.addAction(self.actionGithub)
        self.menuMoussaoui_Anwar.addAction(self.actionLinkedIn_2)
        self.menuMoussaoui_Anwar.addAction(self.actionGithub_2)
        self.menuAbout.addAction(self.menuDahbi_Ayoub.menuAction())
        self.menuAbout.addAction(self.menuMoussaoui_Anwar.menuAction())
        self.menuAbout.addSeparator()

        self.menuType_de_carburant.addAction(self.actionHybride)
        self.menuType_de_carburant.addAction(self.actionEssence)
        self.menuType_de_carburant.addAction(self.actionDiesel)
        self.menuType_de_carburant.addAction(self.actionElectrique)

        self.menuNombre_de_place.addAction(self.actionDeux)
        self.menuNombre_de_place.addAction(self.actionQuatre)
        self.menuNombre_de_place.addAction(self.actionCinq)

        self.menuTransmission.addAction(self.actionAutomatique)
        self.menuTransmission.addAction(self.actionManuelle)

        self.menuPrix_journali.addAction(self.action200)
        self.menuPrix_journali.addAction(self.action400)
        self.menuPrix_journali.addAction(self.action500)
        self.menuPrix_journali.addAction(self.action600)

        self.menuSearch.addAction(self.menuType_de_carburant.menuAction())
        self.menuSearch.addAction(self.menuNombre_de_place.menuAction())
        self.menuSearch.addAction(self.menuTransmission.menuAction())
        self.menuSearch.addAction(self.menuPrix_journali.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuSearch.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        cur.execute("SELECT marque FROM car WHERE reserver=0")
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])

    def update_list(self, text) :
        self.listWidget.clear()
        cur.execute("SELECT marque FROM car WHERE marque LIKE ? AND reserver=0",(text+'%',))
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])
    
    def reset(self) :
        self.lineEdit.setText("")
        self.listWidget.clear()
        cur.execute("SELECT marque FROM car WHERE reserver=0")
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])

    def clicked(self, item):
        cur.execute("SELECT * FROM car WHERE marque=? AND reserver=0",(item.text(),))
        car=cur.fetchone()
        self.lineEdit_7.setText(str(car[0]))
        self.label.setPixmap(QtGui.QPixmap(car[1]))
        self.label_6.setText(car[2])
        self.label_7.setText(car[3])
        self.label_8.setText(str(car[4]))
        self.label_9.setText(car[5])
        self.label_11.setText(str(car[6]) + " DH")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Marque"))
        self.label_3.setText(_translate("MainWindow", "Type de carburant"))
        self.label_4.setText(_translate("MainWindow", "Nombre de place"))
        self.label_5.setText(_translate("MainWindow", "Transmission"))
        self.pushButton.setText(_translate("MainWindow", "Reserver"))

        self.pushButton_3.setText(_translate("MainWindow", "Voir Reservation"))

        self.label_10.setText(_translate("MainWindow", "Prix jounalié"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuDahbi_Ayoub.setTitle(_translate("MainWindow", "Dahbi Ayoub"))
        self.menuMoussaoui_Anwar.setTitle(_translate("MainWindow", "Moussaoui Anwar"))
        self.menuSearch.setTitle(_translate("MainWindow", "Search"))
        self.menuType_de_carburant.setTitle(_translate("MainWindow", "Type de carburant"))
        self.menuNombre_de_place.setTitle(_translate("MainWindow", "Nombre de place"))
        self.menuTransmission.setTitle(_translate("MainWindow", "Transmission"))
        self.menuPrix_journali.setTitle(_translate("MainWindow", "Prix journalié"))
        self.actionAdd.setText(_translate("MainWindow", "Add"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionLinkedIn.setText(_translate("MainWindow", "LinkedIn"))
        self.actionGithub.setText(_translate("MainWindow", "Github"))
        self.actionLinkedIn_2.setText(_translate("MainWindow", "LinkedIn"))
        self.actionGithub_2.setText(_translate("MainWindow", "Github"))

        self.actionHybride.setText(_translate("MainWindow", "Hybride"))
        self.actionEssence.setText(_translate("MainWindow", "Essence"))
        self.actionDiesel.setText(_translate("MainWindow", "Diesel"))
        self.actionElectrique.setText(_translate("MainWindow", "Electrique"))
        
        self.actionDeux.setText(_translate("MainWindow", "Deux"))
        self.actionQuatre.setText(_translate("MainWindow", "Quatre"))
        self.actionCinq.setText(_translate("MainWindow", "Cinq"))

        self.actionAutomatique.setText(_translate("MainWindow", "Automatique"))
        self.actionManuelle.setText(_translate("MainWindow", "Manuelle"))

        self.action200.setText(_translate("MainWindow", "200 DH"))
        self.action400.setText(_translate("MainWindow", "400 DH"))
        self.action500.setText(_translate("MainWindow", "500 DH"))
        self.action600.setText(_translate("MainWindow", "600 DH"))

        cur.execute("SELECT * FROM car WHERE reserver=0")
        car=cur.fetchone()
        self.lineEdit_7.setText(str(car[0]))
        self.label.setPixmap(QtGui.QPixmap(car[1]))
        self.label_6.setText(car[2])
        self.label_7.setText(car[3])
        self.label_8.setText(str(car[4]))
        self.label_9.setText(car[5])
        self.label_11.setText(str(car[6]) + " DH")

    def deleteCar(self):
        val = self.lineEdit_7.text()
        con.execute("DELETE FROM car WHERE idCar=?",(val,))
        con.commit()
        cur.execute("SELECT marque FROM car WHERE reserver=0")
        self.lineEdit_7.clear()
        self.listWidget.clear()
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])
        cur.execute("SELECT * FROM car WHERE reserver=0")
        car=cur.fetchone()
        self.lineEdit_7.setText(str(car[0]))
        self.label.setPixmap(QtGui.QPixmap(car[1]))
        self.label_6.setText(car[2])
        self.label_7.setText(car[3])
        self.label_8.setText(str(car[4]))
        self.label_9.setText(car[5])
        self.label_11.setText(str(car[6]) + " DH")
        msg = QMessageBox()
        msg.setWindowTitle("Reussit")
        msg.setText("La voiture été bien supprimée!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.exec_()
    def reserver(self):
        val = self.lineEdit_7.text()
        con.execute("UPDATE car SET reserver=1 WHERE idCar=?",(val,))
        con.commit()
        cur.execute("SELECT marque FROM car WHERE reserver=0")
        self.lineEdit_7.clear()
        self.listWidget.clear()
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])
        cur.execute("SELECT * FROM car WHERE reserver=0")
        car=cur.fetchone()
        self.lineEdit_7.setText(str(car[0]))
        self.label.setPixmap(QtGui.QPixmap(car[1]))
        self.label_6.setText(car[2])
        self.label_7.setText(car[3])
        self.label_8.setText(str(car[4]))
        self.label_9.setText(car[5])
        self.label_11.setText(str(car[6]) + " DH")
        msg = QMessageBox()
        msg.setWindowTitle("Reussit")
        msg.setText("La reservation été bien effectuée!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        msg.exec_()

    def findHybride(self):
        self.listWidget.clear()
        cur.execute("SELECT marque FROM car WHERE carburant='Hybride'")
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])
    def findEssence(self):
        self.listWidget.clear()
        cur.execute("SELECT marque FROM car WHERE carburant='Essence'")
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])
    def findDiesel(self):
        self.listWidget.clear()
        cur.execute("SELECT marque FROM car WHERE carburant='Diesel'")
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])
    def findElectrique(self):
        self.listWidget.clear()
        cur.execute("SELECT marque FROM car WHERE carburant='Electrique'")
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])
    def findDeux(self):
        self.listWidget.clear()
        cur.execute("SELECT marque FROM car WHERE place=2")
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])
    def findQuatre(self):
        self.listWidget.clear()
        cur.execute("SELECT marque FROM car WHERE place=4")
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])
    def findCinq(self):
        self.listWidget.clear()
        cur.execute("SELECT marque FROM car WHERE place=5")
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])
    def findManuelle(self):
        self.listWidget.clear()
        cur.execute("SELECT marque FROM car WHERE transmission='manuelle'")
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])
    def findAutomatique(self):
        self.listWidget.clear()
        cur.execute("SELECT marque FROM car WHERE transmission='automatique'")
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])
    def find200(self):
        self.listWidget.clear()
        cur.execute("SELECT marque FROM car WHERE prix=200")
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])
    def find400(self):
        self.listWidget.clear()
        cur.execute("SELECT marque FROM car WHERE prix=400")
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])
    def find500(self):
        self.listWidget.clear()
        cur.execute("SELECT marque FROM car WHERE prix=500")
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])
    def find600(self):
        self.listWidget.clear()
        cur.execute("SELECT marque FROM car WHERE prix=600")
        cars=cur.fetchall()
        for car in cars:
            self.listWidget.addItem(car[0])
    def ayoubLinked(self):
        webbrowser.open('https://www.linkedin.com/in/dahbiayoub/')
    def ayoubGit(self):
        webbrowser.open('https://github.com/hellodikki')
    def anwarLinked(self):
        webbrowser.open('https://www.linkedin.com/in/anwar-moussaoui/')
    def anwarGit(self):
        webbrowser.open('https://github.com/anwarmoussaoui')

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
