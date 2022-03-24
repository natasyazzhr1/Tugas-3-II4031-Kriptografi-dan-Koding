import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap


from rsa import initialize, process, to_hex, export

import sqlite3
import os
import csv
import datetime


class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        loadUi("home.ui", self)
        self.pushButton.clicked.connect(self.Text_Encrypt)
        self.pushButton_2.clicked.connect(self.File_Encrypt)

    def init(self):
        p = int(self.lineEdit.text())
        q = int(self.lineEdit_2.text())
        global data
        data = initialize(p, q)
        # return data

    def Text_Encrypt(self):
        Menu.init(self)
        text_encrypt = Text_Encrypt()
        widget.addWidget(text_encrypt)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def File_Encrypt(self):
        Menu.init(self)
        file_encrypt = File_Encrypt()
        widget.addWidget(file_encrypt)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Text_Encrypt(QMainWindow):
    def __init__(self):
        super(Text_Encrypt, self).__init__()
        loadUi("text.ui", self)
        self.pushButton.clicked.connect(self.Menu)
        self.pushButton_2.clicked.connect(self.Compute)
    #     self.pushButton_5.clicked.connect(self.Encrypt)
    #     self.pushButton_3.clicked.connect(self.Import)
    #     self.pushButton_4.clicked.connect(self.Export)

    def Menu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Compute(self):
        global data
        plaintext = self.textEdit.toPlainText()

        encrypted = process(plaintext, data[1], data[0])
        self.textBrowser.setText(to_hex(encrypted))

        ciphertext = self.textBrowser.toPlainText()
        export(ciphertext)

        decrypted = process(plaintext, data[2], data[0])
        self.textBrowser_2.setText(to_hex(decrypted))


class File_Encrypt(QMainWindow):
    def __init__(self):
        super(File_Encrypt, self).__init__()
        loadUi("file.ui", self)
    #     self.pushButton_7.clicked.connect(self.File)
    #     self.pushButton_6.clicked.connect(self.Menu)
    #     self.pushButton_5.clicked.connect(self.Decrypt)
    #     self.pushButton_3.clicked.connect(self.Import)
    #     self.pushButton_4.clicked.connect(self.Export)

    # def Menu(self):
    #     menu = Menu()
    #     widget.addWidget(menu)
    #     widget.setCurrentIndex(widget.currentIndex() + 1)

    # def Decrypt(self):
    #     plaintext = self.textEdit.toPlainText()
    #     key = self.textEdit_2.toPlainText()
    #     res = rc4_Process(plaintext, key)
    #     print(res)
    #     self.textBrowser.setText(res)

    # def File(self):
    #     filename = self.textEdit.toPlainText()
    #     key = self.textEdit_2.toPlainText()
    #     res = rc4_file(filename, key)
    #     print(res)
    #     self.textBrowser.setText(res)

    # def Import(self):
    #     with open('plaintext.txt', 'r') as file:
    #         lines = file.read().rstrip()
    #     self.textEdit.setPlainText(str(lines))

    # def Export(self):
    #     plaintext = self.textEdit.toPlainText()
    #     key = self.textEdit_2.toPlainText()
    #     return(rc4_Export(plaintext, key))


# main
app = QApplication(sys.argv)
welcome = Menu()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
