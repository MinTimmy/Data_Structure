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
        #button.clicked.connect(lambda: print("OK"))
        return button

    def setAmount(self):
        #init data
        text = self.textBox.text()
        self.cards_amount = 0
        self.cards = []
        self.cards_number = []
        self.answer_string = ""
        self.count = 0
        if text == "":
            text = "c3,d5,hA,c5,sK,hJ,s10"

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
        self.insertion_sort()

    def insertion_sort(self):
        
        # Traverse through 1 to len(arr) 
        arr = self.cards_number
        arr_card = self.cards
        self.showAnswer(arr_card)
        for i in range(1, len(arr)): 
            key = arr[i]
            key_card =  arr_card[i]
            # Move elements of arr[0..i-1], that are 
            # greater than key, to one position ahead 
            # of their current position 
            j = i-1
            while j >= 0 and key > arr[j] : 
                arr[j + 1] = arr[j]
                arr_card[j + 1] = arr_card[j]
                
                j -= 1
            arr[j + 1] = key
            arr_card[j + 1] = key_card
            self.showAnswer(arr_card)

        print(self.answer_string)
        
    def showAnswer(self, Str):
        string = str(self.count + 1) + ': '
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

