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

        self.numbers = []
        self.now_x = 200
        self.now_y = 200
        self.output_answer = [[0 for i in range(10)] for j in range(100)]
        self.count = 0
        self.check = False
        self.x = [[0 for i in range(10)] for j in range(100)]
        self.y = [[0 for i in range(10)] for j in range(100)]
        self.radix = [[0 for i in range(10)] for j in range(100)]

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
        text = "5,2,7,1,7,3"
        self.check = True

        #處理字串
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
                    self.draw_circle()
                    swapped = True    
        #print(self.numbers)
        self.check = True
        
    
    def draw_circle(self):
        for i in range(len(self.numbers)):
            self.x[self.count][i] = self.now_x - self.output_answer[self.count][i] *10
            self.y[self.count][i] = self.now_y - self.output_answer[self.count][i] *10
            self.radix[self.count][i] = self.output_answer[self.count][i] * 2 *10
            #self.create_label()
            self.now_x += 200 
            print(self.x[self.count][i]," ",self.y[self.count][i]," ")
            QWidget.update(self)
        print("-------------------------------------------------------")
        self.now_y += 200
        self.now_x = 200
    #從這裡開始
    """    
    def create_label(self):
        x = 200
        y = 200
        for i in range(self.count):
            for j in range(len(self.numbers))
                lb = QLabel(self, text = char(self.output_answer[i][j]))
                lb.move(x,y)
                x += 200
            y +=200

        #lb.resize(200,100)

        lb.show()
        self.button.clicked.connect(lambda: lb.clear()) #clear the label
    """
    def paintEvent(self, event):
        painter = QPainter(self) # 呼叫畫筆
        painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
        painter.setPen(QPen(Qt.blue, 3, Qt.SolidLine))
        #painter.drawLine(0,200,1000,200)
        if self.check:
            for i in range(self.count):
                for j in range(len(self.numbers)):
                    painter.drawEllipse(self.x[i][j], self.y[i][j], self.radix[i][j], self.radix[i][j])
            self.check = False
            self.count = 0
            self.output_answer = [[0 for i in range(10)] for j in range(100)]
            self.now_y = 200
        
        
        #self.count += 1
        
        painter.end()

        #return painter
       
    
def main():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.resize(10000,10000)
    main_window.show()
    app.exec_()

if __name__ == "__main__":
    main()

