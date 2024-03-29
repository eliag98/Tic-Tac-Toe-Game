from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from game import Ui_MainWindowGame
import sys


class MainGameScreen(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindowGame()
        self.ui.setupUi(self)

        MainWindow.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 439)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("xo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.welcomelabel = QtWidgets.QLabel(self.centralwidget)
        self.welcomelabel.setGeometry(QtCore.QRect(70, 110, 221, 61))
        self.welcomelabel.setStyleSheet("font: 40pt \"Tw Cen MT Condensed Extra Bold\";")
        self.welcomelabel.setObjectName("welcomelabel")
        self.welcomelabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.welcomelabel_2.setGeometry(QtCore.QRect(150, 190, 61, 61))
        self.welcomelabel_2.setStyleSheet("font: 40pt \"Tw Cen MT Condensed Extra Bold\";")
        self.welcomelabel_2.setObjectName("welcomelabel_2")
        self.welcomelabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.welcomelabel_3.setGeometry(QtCore.QRect(50, 270, 261, 61))
        self.welcomelabel_3.setStyleSheet("font: 40pt \"Tw Cen MT Condensed Extra Bold\";")
        self.welcomelabel_3.setObjectName("welcomelabel_3")
        self.new_playerlabel_4 = QtWidgets.QLabel(self.centralwidget)
        self.new_playerlabel_4.setGeometry(QtCore.QRect(410, 40, 161, 41))
        self.new_playerlabel_4.setStyleSheet("font: 20pt \"Tw Cen MT Condensed Extra Bold\";")
        self.new_playerlabel_4.setObjectName("new_playerlabel_4")
        self.existin_playerlabel_5 = QtWidgets.QLabel(self.centralwidget)
        self.existin_playerlabel_5.setGeometry(QtCore.QRect(410, 230, 191, 41))
        self.existin_playerlabel_5.setStyleSheet("font: 20pt \"Tw Cen MT Condensed Extra Bold\";")
        self.existin_playerlabel_5.setObjectName("existin_playerlabel_5")
        self.new_playerlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.new_playerlineEdit.setGeometry(QtCore.QRect(410, 110, 241, 51))
        self.new_playerlineEdit.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    border-style: none;\n"
"    border-radius: 17px;\n"
"    text-align: center;\n"
"     font: 16pt \"Tw Cen MT Condensed Extra Bold\";\n"
"}")
        self.new_playerlineEdit.setText("")
        self.new_playerlineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.new_playerlineEdit.setObjectName("new_playerlineEdit")
        self.create_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.create_new_account())
        self.create_pushButton.setGeometry(QtCore.QRect(670, 110, 93, 51))
        self.create_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.create_pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(77, 231, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: none;\n"
"    border-radius: 17px;\n"
"    text-align: center;\n"
"    font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"}")
        self.create_pushButton.setObjectName("create_pushButton")
        self.existing_playerlineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.existing_playerlineEdit_2.setGeometry(QtCore.QRect(410, 300, 241, 51))
        self.existing_playerlineEdit_2.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"    border-style: none;\n"
"    border-radius: 17px;\n"
"    text-align: center;\n"
"     font: 16pt \"Tw Cen MT Condensed Extra Bold\";\n"
"}")
        self.existing_playerlineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.existing_playerlineEdit_2.setObjectName("existing_playerlineEdit_2")
        self.login_pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.login_to_existing_accout())
        self.login_pushButton_2.setGeometry(QtCore.QRect(670, 300, 93, 51))
        self.login_pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color: rgb(77, 231, 0);\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: none;\n"
"    border-radius: 17px;\n"
"    text-align: center;\n"
"    font: 10pt \"Tw Cen MT Condensed Extra Bold\";\n"
"}")
        self.login_pushButton_2.setObjectName("login_pushButton_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(350, 50, 20, 341))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(-6, -5, 811, 451))
        self.Background.setStyleSheet("background-color: rgb(154, 231, 231);\n"
"")
        self.Background.setText("")
        self.Background.setObjectName("Background")
        self.Background.raise_()
        self.welcomelabel.raise_()
        self.welcomelabel_2.raise_()
        self.welcomelabel_3.raise_()
        self.new_playerlabel_4.raise_()
        self.existin_playerlabel_5.raise_()
        self.new_playerlineEdit.raise_()
        self.create_pushButton.raise_()
        self.existing_playerlineEdit_2.raise_()
        self.login_pushButton_2.raise_()
        self.line.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def username_var():
        username_variable = username

    def create_new_account(self):
        username = self.new_playerlineEdit.text()
        global new_username_file
        try:
            new_username_file = open( str(username) + '.txt')
            msg = QMessageBox()
            msg.setWindowTitle("")
            msg.setText("Username already exists.")
            msg.setInformativeText("Please try with another username.")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("xo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            msg.setWindowIcon(icon)
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()
        except:
            new_username_file = open( str(username) + '.txt', 'w')
            new_username_file.write("0")
            new_username_file.close()
            current_user = open("current_user.txt", "w")
            current_user.write(str(username))
            current_user.close()
            self.main = MainGameScreen()
            self.main.show()


    def login_to_existing_accout(self):
        username = self.existing_playerlineEdit_2.text()
        global existing_username_file
        try:
            existing_username_file = open( str(username) + '.txt')
            current_user = open("current_user.txt", "w")
            current_user.write(str(username))
            current_user.close()
            self.main = MainGameScreen()
            self.main.show()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("")
            msg.setText("Username does not exist.")
            msg.setInformativeText("Please try with another username, or create a new one.")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("xo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
            msg.setWindowIcon(icon)
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic-Tac_Toe"))
        self.welcomelabel.setText(_translate("MainWindow", "Welcome"))
        self.welcomelabel_2.setText(_translate("MainWindow", "To"))
        self.welcomelabel_3.setText(_translate("MainWindow", "Tic Tac Toe"))
        self.new_playerlabel_4.setText(_translate("MainWindow", "New player?"))
        self.existin_playerlabel_5.setText(_translate("MainWindow", "Played before?"))
        self.create_pushButton.setText(_translate("MainWindow", "Create"))
        self.login_pushButton_2.setText(_translate("MainWindow", "Sign in"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
