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
        self.setStyleSheet('QFrame{background-color:rgb(0,0,255)}')
        self.numbers = [] # 使用者輸入的數字
        self.output_answer = [[0 for i in range(10)] for j in range(100)] # 紀錄要輸出的數字
        self.count = 0 # 紀錄要交換幾次
        
    def CreateTextbox(self):
        #lb = QLabel(self, text = "TextBox: ")
        #lb.move(180,60)
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
        #text = "5,2,7,1,7,3"
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
            print(tmp)
        c.append(int(tmp))
        #print(c)
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
        self.create_label()
        
    def create_label(self):
        x = 200
        y = 200
        for i in range(self.count):
            for j in range(len(self.numbers)):
                self.label(self.output_answer[i][j], x, y)
                x += 200
            y += 200
            x = 200
        self.numbers = []
        self.output_answer = [[0 for i in range(10)] for j in range(100)]
        self.count = 0
        
    def label(self, t, x, y):
        temp = t * 20
        lb = QLabel(self, text = str(t))
        lb.setAlignment(Qt.AlignCenter)
        lb.resize(temp, temp) 
        lb.move(x-temp/2,y-temp/2)
        lb.setStyleSheet("border: 3px solid blue; border-radius:"+str(temp/2)+"px;") 
        lb.show()
        self.button.clicked.connect(lambda: lb.hide()) #clear the label
    
def main():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.resize(10000,10000)
    main_window.show()
    app.exec_()

if __name__ == "__main__":
    main()

