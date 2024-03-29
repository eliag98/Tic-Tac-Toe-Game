from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMessageBox
import sys
import os
import random

global player_choice
global value
global enabled_buttons
global score
global new_score
global current_username

# old size MainWindow.resize(898, 450)

x_sign = "x.png"
o_sign = "o.png"
e_sign = "e.png"
enabled_buttons = [1,2,3,4,5,6,7,8,9]

class Ui_MainWindowGame(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(899, 473)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("xo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Game Frame
        self.game_frame = QtWidgets.QFrame(self.centralwidget)
        self.game_frame.setGeometry(QtCore.QRect(0, 0, 450, 450))
        self.game_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.game_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.game_frame.setObjectName("game_frame")
        # Buttons
        self.button_1 = QtWidgets.QPushButton(self.game_frame, clicked= lambda: self.click(self.button_1, 1))
        self.button_1.setGeometry(QtCore.QRect(0, 0, 150, 150))
        self.button_1.setText("")
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(self.game_frame, clicked= lambda: self.click(self.button_2, 2))
        self.button_2.setGeometry(QtCore.QRect(150, 0, 150, 150))
        self.button_2.setText("")
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(self.game_frame, clicked= lambda: self.click(self.button_3, 3))
        self.button_3.setGeometry(QtCore.QRect(300, 0, 150, 150))
        self.button_3.setText("")
        self.button_3.setObjectName("button_3")
        self.button_6 = QtWidgets.QPushButton(self.game_frame, clicked= lambda: self.click(self.button_6, 6))
        self.button_6.setGeometry(QtCore.QRect(300, 150, 150, 150))
        self.button_6.setText("")
        self.button_6.setObjectName("button_6")
        self.button_4 = QtWidgets.QPushButton(self.game_frame, clicked= lambda: self.click(self.button_4, 4))
        self.button_4.setGeometry(QtCore.QRect(0, 150, 150, 150))
        self.button_4.setText("")
        self.button_4.setObjectName("button_4")
        self.button_5 = QtWidgets.QPushButton(self.game_frame, clicked= lambda: self.click(self.button_5, 5))
        self.button_5.setGeometry(QtCore.QRect(150, 150, 150, 150))
        self.button_5.setText("")
        self.button_5.setObjectName("button_5")
        self.button_9 = QtWidgets.QPushButton(self.game_frame, clicked= lambda: self.click(self.button_9, 9))
        self.button_9.setGeometry(QtCore.QRect(300, 300, 150, 150))
        self.button_9.setText("")
        self.button_9.setObjectName("button_9")
        self.button_7 = QtWidgets.QPushButton(self.game_frame, clicked= lambda: self.click(self.button_7, 7))
        self.button_7.setGeometry(QtCore.QRect(0, 300, 150, 150))
        self.button_7.setText("")
        self.button_7.setObjectName("button_7")
        self.button_8 = QtWidgets.QPushButton(self.game_frame, clicked= lambda: self.click(self.button_8, 8))
        self.button_8.setGeometry(QtCore.QRect(150, 300, 150, 150))
        self.button_8.setText("")
        self.button_8.setObjectName("button_8")
        # Score Frame
        self.name_score_frame = QtWidgets.QFrame(self.centralwidget)
        self.name_score_frame.setGeometry(QtCore.QRect(459, 10, 431, 131))
        self.name_score_frame.setStyleSheet("background-color: rgb(154, 231, 231);")
        self.name_score_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name_score_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_score_frame.setObjectName("name_score_frame")
        # Labels in the Score Frame
        self.score_label = QtWidgets.QLabel(self.name_score_frame)
        self.score_label.setGeometry(QtCore.QRect(270, 20, 131, 31))
        self.score_label.setStyleSheet("font: 20pt \"Tw Cen MT Condensed Extra Bold\";")
        self.score_label.setObjectName("score_label")
        self.score_number = QtWidgets.QLabel(self.name_score_frame)
        self.score_number.setGeometry(QtCore.QRect(270, 60, 120, 65))
        self.score_number.setStyleSheet("font: 20pt \"Tw Cen MT Condensed Extra Bold\";")
        self.score_number.setAlignment(QtCore.Qt.AlignCenter)
        self.score_number.setObjectName("score_number")
        self.welcome_name = QtWidgets.QLabel(self.name_score_frame)
        self.welcome_name.setGeometry(QtCore.QRect(60, 70, 91, 51))
        self.welcome_name.setStyleSheet("font: 20pt \"Tw Cen MT Condensed Extra Bold\";")
        self.welcome_name.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_name.setObjectName("welcome_name")
        self.welcome_label = QtWidgets.QLabel(self.name_score_frame)
        self.welcome_label.setGeometry(QtCore.QRect(40, 20, 131, 31))
        self.welcome_label.setStyleSheet("font: 20pt \"Tw Cen MT Condensed Extra Bold\";\n"
"")
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")
        self.line = QtWidgets.QFrame(self.name_score_frame)
        self.line.setGeometry(QtCore.QRect(208, 10, 20, 111))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        # Turns and New Game Frame
        self.new_game_turns_frame = QtWidgets.QFrame(self.centralwidget)
        self.new_game_turns_frame.setGeometry(QtCore.QRect(460, 160, 431, 281))
        self.new_game_turns_frame.setStyleSheet("background-color: rgb(154, 231, 231);")
        self.new_game_turns_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.new_game_turns_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.new_game_turns_frame.setObjectName("new_game_turns_frame")
        # Turns Labels
        self.player_1 = QtWidgets.QLabel(self.new_game_turns_frame)
        self.player_1.setGeometry(QtCore.QRect(155, 130, 200, 31))
        self.player_1.setStyleSheet("QLabel{\n"
"    color: rgb(255, 29, 37);\n"
"    font: 20pt \"Tw Cen MT Condensed Extra Bold\";\n"
"}")
        self.player_1.setObjectName("player_1")
        self.player_2 = QtWidgets.QLabel(self.new_game_turns_frame)
        self.player_2.setGeometry(QtCore.QRect(155, 200, 200, 31))
        self.player_2.setStyleSheet("font: 20pt \"Tw Cen MT Condensed Extra Bold\";")
        self.player_2.setObjectName("player_2")
        # New Game Button
        self.new_gamepushButton = QtWidgets.QPushButton(self.new_game_turns_frame, clicked= lambda: self.new_game())
        self.new_gamepushButton.setGeometry(QtCore.QRect(140, 40, 151, 51))
        self.new_gamepushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.new_gamepushButton.setStyleSheet("QPushButton{\n"
        "    background-color: rgb(72, 216, 0);\n"
        "    color: rgb(255, 255, 255);\n"
        "    border-style: none;\n"
        "    border-radius: 17px;\n"
        "    text-align: center;\n"
        "    font: 12pt \"Tw Cen MT Condensed Extra Bold\";\n"
        "}")
        self.new_gamepushButton.setObjectName("new_gamepushButton")

        # Email label
        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(595, 450, 161, 16))
        self.email.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.info()

        self.counter = 0
        self.x = 0

        # Setting X | O Icons
        global x_icon
        global o_icon
        global e_icon
        x_icon = QtGui.QIcon("x.png")
        o_icon = QtGui.QIcon("o.png")
        e_icon = QtGui.QIcon("e.png")


    def info(self):
        # Retrieve information about the current user
        current_user = open("current_user.txt", "r")
        current_username = current_user.read()
        current_user.close()
        self.welcome_name.setText(str(current_username))
        self.player_1.setText(str(current_username))

        # Retrieve the score information from user's file
        user_score_file = open(str(current_username) + '.txt')
        score = user_score_file.read()
        user_score_file.close()
        self.score_number.setText(str(score))

    def win(self, player):
        msg = QMessageBox()
        msg.setWindowTitle("Result")
        if player == 'x':
            new_score = int(self.score_number.text()) + 1
            user_score_file = open(str(self.welcome_name.text()) + '.txt', "w")
            user_score_file.write(str(new_score))
            user_score_file.close()
            msg.setText(f"Congrats!! {self.player_1.text()}")
            msg.setInformativeText("You won!! 1 Point will be added to your score.")
        elif player == 'o':
            msg.setText("Sorry :( Player 2 Wins.")
            msg.setInformativeText("You lost!! Good luck next time.")
        elif player == '2':
            msg.setText("A tie *-*")
            msg.setInformativeText("It's a tie!! Good luck next time.")
        msg.addButton('Ok', QtWidgets.QMessageBox.YesRole)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("xo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        msg.setWindowIcon(icon)
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def chk(self):
        buttons_l = [
        self.button_1,
        self.button_2,
        self.button_3,
        self.button_4,
        self.button_5,
        self.button_6,
        self.button_7,
        self.button_8,
        self.button_9]
        for b in buttons_l:
            b.setEnabled(False)

    def check_winner(self):
        if self.x == 10:
            self.win("2")
        # 1
        if self.button_1.text() != "" and self.button_1.text() == self.button_2.text() and self.button_1.text() == self.button_3.text():
            self.win(self.button_1.text())
            self.chk()
        # 2
        elif self.button_1.text() != "" and self.button_1.text() == self.button_4.text() and self.button_1.text() == self.button_7.text():
            self.win(self.button_1.text())
            self.chk()
        # 3
        elif self.button_1.text() != "" and self.button_1.text() == self.button_5.text() and self.button_1.text() == self.button_9.text():
            self.win(self.button_1.text())
            self.chk()
        # 4
        elif self.button_2.text() != "" and self.button_2.text() == self.button_5.text() and self.button_2.text() == self.button_8.text():
            self.win(self.button_2.text())
            self.chk()
        # 5
        elif self.button_3.text() != "" and self.button_3.text() == self.button_6.text() and self.button_3.text() == self.button_9.text():
            self.win(self.button_3.text())
            self.chk()
        # 6
        elif self.button_3.text() != "" and self.button_3.text() == self.button_5.text() and self.button_3.text() == self.button_7.text():
            self.win(self.button_3.text())
            self.chk()
        # 7
        elif self.button_4.text() != "" and self.button_4.text() == self.button_5.text() and self.button_4.text() == self.button_6.text():
            self.win(self.button_4.text())
            self.chk()
        # 8
        elif self.button_7.text() != "" and self.button_7.text() == self.button_8.text() and self.button_7.text() == self.button_9.text():
            self.win(self.button_7.text())
            self.chk()




    def restart(self):
        buttons_lst = [
        self.button_1,
        self.button_2,
        self.button_3,
        self.button_4,
        self.button_5,
        self.button_6,
        self.button_7,
        self.button_8,
        self.button_9]

        for btn in buttons_lst :
            btn.setIcon(e_icon)
            btn.setText("")
            btn.setEnabled(True)
        for n in range(10):
            if n == 0:
                continue
            else:
                enabled_buttons.append(n)
        self.counter = 0
        self.x = 1
        self.player_1.setGeometry(QtCore.QRect(155, 130, 200, 31))
        self.player_1.setStyleSheet("QLabel{\n"
"    color: rgb(255, 29, 37);\n"
"    font: 20pt \"Tw Cen MT Condensed Extra Bold\";\n"
"}")
        self.player_2.setGeometry(QtCore.QRect(155, 200, 200, 31))
        self.player_2.setStyleSheet("QLabel{\n"
"    color: rgb(0, 0, 0);\n"
"    font: 20pt \"Tw Cen MT Condensed Extra Bold\";\n"
"}")
        self.info()


        # When player clicks a button
    def click(self, value, n):
        if self.counter % 2 == 0:
            if n in enabled_buttons:

                value.setText('x')
                value.setStyleSheet("color: rgb(232,244,252)")
                value.setIcon(x_icon)
                value.setIconSize(QSize(100, 100))
                enabled_buttons.remove(n)
                self.player_1.setGeometry(QtCore.QRect(155, 130, 200, 31))
                self.player_1.setStyleSheet("QLabel{\n"
            "    color: rgb(0, 0, 0);\n"
            "    font: 20pt \"Tw Cen MT Condensed Extra Bold\";\n"
            "}")
                self.player_2.setGeometry(QtCore.QRect(155, 200, 200, 31))
                self.player_2.setStyleSheet("QLabel{\n"
            "    color: rgb(72, 216, 0);\n"
            "    font: 20pt \"Tw Cen MT Condensed Extra Bold\";\n"
            "}")
        else:
            if n in enabled_buttons:
                value.setText('o')
                value.setStyleSheet("color: rgb(232,244,252)")
                value.setIcon(o_icon)
                value.setIconSize(QSize(100, 100))
                enabled_buttons.remove(n)
                self.player_1.setGeometry(QtCore.QRect(155, 130, 200, 31))
                self.player_1.setStyleSheet("QLabel{\n"
            "    color: rgb(255, 29, 37);\n"
            "    font: 20pt \"Tw Cen MT Condensed Extra Bold\";\n"
            "}")
                self.player_2.setGeometry(QtCore.QRect(155, 200, 200, 31))
                self.player_2.setStyleSheet("QLabel{\n"
            "    color: rgb(0, 0, 0);\n"
            "    font: 20pt \"Tw Cen MT Condensed Extra Bold\";\n"
            "}")
        self.counter += 1
        self.x += 1
        self.check_winner()

    def new_game(self):
        self.restart()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic-Tac_Toe"))
        self.score_label.setText(_translate("MainWindow", "Your score"))
        self.score_number.setText(_translate("MainWindow", "0"))
        self.welcome_name.setText(_translate("MainWindow", "Name"))
        self.welcome_label.setText(_translate("MainWindow", "Welcome"))
        self.player_1.setText(_translate("MainWindow", "Player 1"))
        self.player_2.setText(_translate("MainWindow", "Player 2"))
        self.new_gamepushButton.setText(_translate("MainWindow", "New Game"))
        self.email.setText(_translate("MainWindow", "By: eliework98@gmail.com"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowGame()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
