import sys
import random
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


        self.amount = 0
        self.number = []

    def CreateTextbox(self):
        lb = QLabel(self, text = "TextBox: ")
        lb.move(180,60)
        textBox = QLineEdit(self)
        textBox.resize(100,30)
        textBox.move(250,60)
        return textBox

    def CreateButton(self):
        button = QPushButton(self, text = "OK")
        button.resize(30,30)
        button.move(400, 60)
        button.clicked.connect(lambda: self.setAmount())
        button.clicked.connect(lambda: print("OK"))

    
    def setAmount(self):
        self.amount = int(self.textBox.text())
        self.number.clear()
        
        for i in range(self.amount):
            self.number.append(random.randint(0, 100))
        
        self.start_sorting()
    
    def start_sorting(self):
        self.bubble_sort()

    def bubble_sort(self):
        str_num = "The Bubble sort: \n" 
        lb = QLabel(self, text = str_num)
        lb.move(50, 220)
        lb.show()

        num = self.number
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(num) - 1):
                if num[i] < num[i+1]:
                    num[i], num[i+1] = num[i+1], num[i]
                    swapped = True
def main():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.resize(1000,1000)
    main_window.show()
    app.exec_()

if __name__ == "__main__":
    main()


'''if __name__ == "__main__":
    app = QApplication(sys.argv)

    ex = Main()

    ex.resize(500, 500)
    ex.show()
    sys.exit(app.exec_())

'''