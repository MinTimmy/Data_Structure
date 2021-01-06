#!/usr/bin/python3
import sys
import random
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Main(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.InitUi()

    def InitUi(self):
        self.textBox = self.CreateTextbox()
        self.button = self.CreateButton()
        self.show()
        

    def CreateTextbox(self):
        lb = QLabel(self, text = "TextBox: ")
        lb.move(180,60)
        textBox = QLineEdit(self)
        textBox.resize(500,30)
        textBox.move(250,60)
        return textBox

    def CreateButton(self):
        button = QPushButton(self, text = "OK")
        button.resize(30,30)
        button.move(800, 60)
        button.clicked.connect(lambda: self.setAmount())
        button.clicked.connect(lambda: print("OK"))
        return button

    def setAmount(self):
        #init data
        text = self.textBox.text()
        
    
        
    def showAnswer(self, Str):

        lb = QLabel(self, text = string)
        lb.move(50,100 + self.count * 20)
        lb.resize(200,100)

        lb.show()
        self.button.clicked.connect(lambda: lb.clear()) #clear the label
        self.count += 1
        
def main():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.resize(1000,1000)
    main_window.show()
    app.exec_()

if __name__ == "__main__":
    main()

