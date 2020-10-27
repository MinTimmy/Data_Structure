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

        self.cards_amount = 0
        self.cards = []
        self.cards_number = []
        self.answer_string = ""
        self.count = 0

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
        self.cards_amount = 0
        self.cards = []
        self.cards_number = []
        self.answer_string = ""
        self.count = 0
        text = "dQ,h8,h6,c4,c5,h2,d7"

        #convert string to number of list 
        i = 0
        tmp = ""
        while i < len(text):
            if text[i] == ",":
                self.cards.append(tmp)
                tmp = ""

            if text[i] != ",":
                tmp = tmp + text[i]
            i += 1
        self.cards.append(tmp)
        
        self.cards_amount = len(self.cards)
        switcher_flower = {
            'c': 0,
            'd': 1,
            'h': 2,
            's': 3
        }
        switcher_number = {
            '2': 1,
            '3': 2,
            '4': 3,
            '5': 4,
            '6': 5,
            '7': 6,
            '8': 7,
            '9': 8,
            'J': 10,
            'Q': 11,
            'K': 12,
            'A': 13
        }
        for i in range(self.cards_amount):
            tmp = switcher_flower.get(self.cards[i][0], 0)*13 + switcher_number.get(self.cards[i][1], 10)
            self.cards_number.append(tmp)   
        
        self.start_sorting()
    
    def start_sorting(self):
        #self.insertion_sort()
        self.selection_sort()
        
    def selection_sort(self):
        numbers = self.cards_number
        numbers_str = self.cards
        self.showAnswer(numbers_str)
        for i in range(len(numbers)):
            max = i
            for j in range(i + 1, len(numbers)):
                if numbers[j] > numbers[max]:
                    max = j
            if max != i:
                numbers[i] , numbers[max] = numbers[max] , numbers[i]
                numbers_str[i] , numbers_str[max] = numbers_str[max] , numbers_str[i]
                self.showAnswer(numbers_str)    

    def showAnswer(self, Str):
        string = str(self.count) + ': '
        string =  string + Str[0]
        for i in range(1,len(Str)):
            string =  string  + ',' + Str[i]

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

