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
        self.createScroll() # Scroll Area which contains the widgets, set as the centralWidget
        
        self.textBox = self.CreateTextbox()
        self.button = self.CreateButton()
        self.vbox = QVBoxLayout()


        self.show()

        self.numbers = []
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
    def createScroll(self):
        self.widget = QWidget()
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)

    def createVbox(self):
        color = ["#5bc0de","#5cb85c","#0275d8","#f0ad4e","#d9534f","red"]
        count = 1
        for i in range(len(self.output_numbers)):
            object = QLabel(self.output_string[i])
            if self.output_numbers[i] >= (count+1) * 100:
                count += 1
            object.setStyleSheet("color : "+color[count-1])
            self.vbox.addWidget(object)

        self.widget.setLayout(self.vbox)
        self.widget.move(180,100)
        self.update()
    """
    def showAnswer(self):
        count = 0
        for i in self.lines:
            lb = QLabel(self, text = i)
            lb.move(50,100 + count * 20)
            lb.resize(2000,100)
            lb.show()
            count += 1
    """
    def counting_sort(self):
        TOTAL_NUMBER = len(self.numbers)
        MAX = 599
        self.output_string = ["" for i in range(len(self.numbers))] # 整個字串的結果
        self.output_numbers = [0 for i in range(len(self.numbers))] # http status code的結果

        count = [ 0 for i in range(MAX)]

        for i in range(TOTAL_NUMBER):
            count[self.numbers[i]] += 1
                
        for i in range(MAX):
            count[i] += count[i-1]

        for i in range(TOTAL_NUMBER):
            self.output_string[count[self.numbers[i]] - 1] = self.lines[i]
            self.output_numbers[count[self.numbers[i]] - 1] = self.numbers[i]
            count[self.numbers[i]] -= 1


    def setAmount(self):
        fp = open("access.log", "r")
        self.lines = fp.readlines()
        count = 0
        tmp = []
        for l in self.lines:
            for i in range(len(l)):
                if count == 2:
                    i += 1
                    for j in range(3):
                        tmp.append(int(l[i+j]))
                    self.numbers.append(100 * tmp[0] + 10 * tmp[1] + tmp[2])
                    count = 0
                    tmp.clear()
                    break
                if l[i] == '"':
                    count += 1
        fp.close()
        #self.showAnswer()
        
        self.counting_sort()
        self.createVbox()
        self.output_file()    

    def output_file(self):
        f = open("demofile2.txt", "w")

        for i in self.output_string:
            f.write(i+'\n')

def main():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.resize(10000,10000)
    main_window.show()
    app.exec_()

    
if __name__ == "__main__":
    main()

