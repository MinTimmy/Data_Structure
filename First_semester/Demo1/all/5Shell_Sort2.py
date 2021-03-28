import sys
import random
import time
import csv
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class AnotherWindow(QMainWindow):
    """
    This "window" is a QWidget. If it has no parent, it 
    will appear as a free-floating window as we want.
    """
    def __init__(self, data):
        super().__init__()
        self.resize(2000,2000)
        self.widget = QWidget()
        self.createScroll() # Scroll Area which contains the widgets, set as the centralWidget
        self.show()
        self.data_string = data
        self.vbox = QVBoxLayout()
        self.createVbox()
        
    def createScroll(self):
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)
        
    def createVbox(self):
        color = ["#d9534f","#f0ad4e","#5cb85c","#0275d8","red"]
        count = 1
        for i in range(len(self.data_string)):
            temp = ""
            object = QLabel(self)
            for j in range(len(self.data_string[i])):
                if j == 0:
                    temp += self.data_string[i][j]
                elif float(self.data_string[i][10]) < 0 and j == 10:
                    temp += " , <font color=\"#d9534f\">" + self.data_string[i][10] + "</font>"
                elif float(self.data_string[i][10]) == 0 and j == 10:
                    temp += " , <font color=\"#f0ad4e\">" + self.data_string[i][10] + "</font>"
                elif float(self.data_string[i][10]) < 10000000000 and j == 10:
                    temp += " , <font color=\"#5cb85c\">" + self.data_string[i][10] + "</font>"
                elif float(self.data_string[i][10]) > 10000000000 and j == 10:
                    temp += " , <font color=\"#0275d8\">" + self.data_string[i][10] + "</font>"
                else:
                    temp += " , " + self.data_string[i][j]
            object.setText(temp)
            object.move(100,100+i)
            self.vbox.addWidget(object)

        self.widget.setLayout(self.vbox)
        self.move(180,100)


class Main(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.InitUi()

    def InitUi(self):
        self.button = self.CreateButton()
        self.w = None  # No external window yet.
        self.data_string = []
    
    def CreateButton(self):
        button = QPushButton(self, text = "OK")
        button.resize(30,30)
        button.clicked.connect(lambda: self.setAmount())
        button.clicked.connect(lambda: print("OK"))
        return button
    
    def shell_sort(self):
        n = len(self.data_string)
        # Rearrange elements at each n/2, n/4, n/8, ... intervals
        interval = n // 2
        while interval > 0:
            for i in range(interval, n):
                temp = self.data_string[i]
                j = i
                while j >= interval and float(self.data_string[j - interval][10]) > float(temp[10]):
                    self.data_string[j] = self.data_string[j - interval]
                    j -= interval
                self.data_string[j] = temp
            interval //= 2

    def setAmount(self):
        self.data_string = []
        #把 csv 檔的資料存成 list(data_string,data_number)
        with open('500_constituents_financial.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            check = False #第一列不存取
            for row in csv_reader:
                if check:
                    self.data_string.append(row)
                check = True
        self.shell_sort()
        self.w = AnotherWindow(self.data_string)
        self.output_file()    

    def output_file(self):
        f = open("demofile2.txt", "w")
        for i in self.data_string:
            for j in i:
                f.write(j+'\n')

def main():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    app.exec_()
   
if __name__ == "__main__":
    main()

