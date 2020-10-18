from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QDial, QMainWindow, QPushButton, QWidget, QSlider)
import sys

class Main(QMainWindow):
    '''
      創建一個視窗
      物件（class 括號裡面第一個變數，看起來像參數的東西）：
      QMainWindow: 獨立的一個 class，在這裡的用法為繼承，因此呼叫 Main 時後面不需接任何參數就能執行繼承了
    '''
    def __init__(self, parent=None):
        '''
          __init__ 用來初始化 class 內的變數及物件，與 C++ 的 Constructor 等價，在這裡為初始化父物件，也就是 QMainWindow。
          呼叫父物件與呼叫 super() 等價，因此這裡也可以寫成 super().__init__()。
          self 的所有變數請在 InitUi 函式內設定，不然可能會出現預期外的錯誤哦！
        '''
        QMainWindow.__init__(self, parent)
        self.InitUi()

    def ResetValue(self):
        '''
          點擊按鈕則重設
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        print("Value has reseted")
        self.slider.setValue(50)
        
    def CreateButton(self):
        '''
          創建按鈕
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        button = QPushButton(self, text='Reset Value')
        button.move(200, 300)
        button.clicked.connect(self.ResetValue)

    def CreateDial(self):
        '''
          創建旋轉鈕
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        self.dial = QDial(self)
        self.dial.resize(80, 80)
        self.dial.move(120, 100)

    def CreateSlider(self):
        '''
          創建滑桿
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        self.slider = QSlider(self)
        self.slider.resize(80, 80)
        self.slider.move(280, 100)
        self.slider.setValue(30)

    def InitUi(self):
        '''
          呼叫元件以及設定視窗參數
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        self.button = self.CreateButton()
        self.CreateDial()
        self.CreateSlider()
        self.dial.valueChanged.connect(self.slider.setValue)
        self.slider.valueChanged.connect(self.dial.setValue)
        self.setGeometry(100,100,600,400)
        self.setWindowTitle('Basic Component')
        self.setWindowIcon(QIcon('icons/404.png'))

def main():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    app.exec_()

if __name__ == "__main__" :
    main()