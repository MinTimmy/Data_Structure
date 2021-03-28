#!/usr/bin/python3

import sys
import random
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it 
    will appear as a free-floating window as we want.
    """
    def __init__(self,n,o):
        super().__init__()
        self.setStyleSheet('QFrame{background-color:rgb(0,0,255)}')
        self.number = n # 第幾個視窗
        self.output = o 
        self.count = len(self.output)
        self.setWindowTitle(str(n))
        self.create_label()

    def create_label(self):
        x = 100
        y = 50
        for i in range(0, self.count):
            self.number_label(i + self.number * 10, 10, y) 
            for j in range(len(self.output[0])):
                self.label(self.output[i][j], x, y)
                x += 100
            y += 110
            x = 100

    def number_label(self, t, x, y):
        nlb = QLabel(self, text = "<font color=\"yellow\">" + str(t+1) + "</font>")
        nlb.setStyleSheet(("font: 18pt;"))
        nlb.move(x,y)
    def label(self, t, x, y):
        temp = t * 10
        lb = QLabel(self, text = "<font color=\"red\">" + str(t) + "</font>")
        lb.setAlignment(Qt.AlignCenter)
        lb.resize(temp, temp) 
        lb.move(x-temp/2,y-temp/2)
        lb.setStyleSheet("border: 3px solid blue; border-radius:"+str(temp/2)+"px; QFrame{background-color:rgb(0,0,255)}") 
        
class Main(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.InitUi()

    def InitUi(self):
        self.textBox = self.CreateTextbox()
        self.button = self.CreateButton()
        self.w = [[None] for i in range(10)]  # No external window yet.
        self.show()
        self.numbers = [] # 使用者輸入的數字
        self.output_answer = [[0 for i in range(10)] for j in range(100)] # 紀錄要輸出的數字
        self.count = 0 # 紀錄要交換幾次
        
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
        text = self.textBox.text()
        if text == "":
            text = "5,2,7,1,7,3,10,8,4,6"
        self.check = True

        #處理字串 從 "5,2,7,1,7,3" 變成 self.numbers = [5,2,7,1,7,3]
        i = 0
        tmp = ""
        c = []
        while i < len(text):
            if text[i] == ",":
                c.append(int(tmp))
                tmp = ""
            if text[i] != ",":
                tmp = tmp + text[i]
            i += 1
        c.append(int(tmp))
        self.numbers = c
        self.bubble_sort()
        
    def bubble_sort(self):
        for i in range(len(self.numbers)):
            self.output_answer[self.count][i] = self.numbers[i]
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(self.numbers) - 1):
                if self.numbers[i] < self.numbers[i + 1]: 
                    self.numbers[i], self.numbers[i + 1] = self.numbers[i + 1], self.numbers[i]
                    self.count += 1
                    for i in range(len(self.numbers)):
                        self.output_answer[self.count][i] = self.numbers[i]
                    swapped = True
        self.count += 1

        for i in range(len(self.numbers)):
            self.output_answer[self.count][i] = self.numbers[i] 

        #輸出結果
        i = 0
        for i in range(self.count // 10):
            self.w[i] = AnotherWindow(i,self.output_answer[i * 10 : i * 10 + 10])
            self.w[i].show()
        i += 1
        self.w[i] = AnotherWindow(i,self.output_answer[i * 10 : i * 10 + self.count % 10 + 1])
        self.w[i].show()

        self.numbers = []
        self.output_answer = [[0 for i in range(10)] for j in range(100)]
        self.count = 0
    
def main():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.resize(10000,10000)
    main_window.show()
    app.exec_()

if __name__ == "__main__":
    main()

