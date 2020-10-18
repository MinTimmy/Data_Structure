'''
  使用 PyQt5 創建標籤、文字框、單選按鈕、複選框、下拉式選單、進度條、顏色對話框、文字對話框、文件對話框以及按鈕
'''
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QApplication, QComboBox, QCheckBox, QColorDialog, QFontDialog, QFileDialog, QLabel, 
                            QLineEdit, QMainWindow, QProgressBar, QPushButton, QRadioButton)
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

    def component_changed(self, name):
        '''
          每當一個元件被更動過，進度條就會增加 12.5，所以大家可以多按按哦！
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
          name: 元件名稱
        '''
        self.changed_list.add(name)
        self.progress_bar.setValue(len(self.changed_list) * 12.5) # 更新進度條

    def CreateButton(self):
        '''
          創建按鈕
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        button = QPushButton(self, text='OK') # 創建按鈕使用 QPushButton，第一個參數為視窗，第二個參數為按鈕內要顯示什麼文字
        button.resize(70, 30) # 調整按鈕大小
        button.move(250, 320) # 移動按鈕位置
        button.clicked.connect(lambda: print('OK')) # 設定點選按鈕要觸發的動作，lambda 為匿名函式，用法為 lambda x: 函式(x)
        button.clicked.connect(lambda: self.component_changed('button'))

    def CreateCheckBox(self):
        '''
          創建複選框
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        lb = QLabel(self, text='Check Box:') # 創建標籤使用 QLabel，第一個參數為視窗，第二個參數為標籤內要顯示什麼文字
        lb.move(165, 140) # 移動標籤位置
        checkbox = QCheckBox(self , text='Pizza') # 創建複選框使用 QCheckBox，第一個參數為視窗，第二個參數為複選框內要顯示什麼文字
        checkbox.move(250, 140) # 移動複選框位置
        checkbox.setChecked(True) # 預設打勾
        checkbox.clicked.connect(lambda: self.component_changed('checkbox'))
        checkbox2 = QCheckBox(self, text='Hamburger')
        checkbox2.move(315, 140)
        checkbox2.clicked.connect(lambda: self.component_changed('checkbox'))

    def CreateColorDialog(self):
        '''
          創建顏色對話框
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        def ShowColor(self):
            '''
              叫出顏色對話框
              參數：
              self: 用來創建專屬物件本身（class）的變數以及函式
            '''
            cd = QColorDialog.getColor()
            print(cd.name()) # 印出顏色字串，例如："#2a3b4c"

        bt = QPushButton(self, text='Select Color')
        bt.move(150, 260)
        bt.resize(80, 40)
        bt.clicked.connect(lambda: ShowColor(self))
        bt.clicked.connect(lambda: self.component_changed('colordialog'))

    def CreateComboBox(self):
        '''
          創建下拉式選單
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        lb = QLabel(self, text='Dropdown Box:')
        lb.move(140, 180)
        cm = QComboBox(self) # 創建下拉選單使用 QLabel，參數為視窗
        cm.resize(100, 30)
        cm.move(250, 180)
        cm.addItem('PyQT') # 新增選項
        cm.addItem('Kivy')
        cm.addItem('wx')
        cm.addItem('PySide')
        cm.setCurrentIndex(2) # 預設的選項，第一個數字從 0 開始
        cm.currentIndexChanged.connect(lambda: self.component_changed('dropdown'))

    def CreateFontDialog(self):
        '''
          創建文字對話框
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        def ShowFont(self):
            '''
              叫出文字對話框
              參數：
              self: 用來創建專屬物件本身（class）的變數以及函式
            '''
            fd = QFontDialog.getFont()
            print(fd[0].toString().split(',')[0]) # 印出字型字串，例如: "標楷體"

        bt = QPushButton(self , text='Select Font')
        bt.move(250, 260)
        bt.resize(80, 40)
        bt.clicked.connect(lambda: ShowFont(self))
        bt.clicked.connect(lambda: self.component_changed('fontdialog'))

    def CreateFileDialog(self):
        '''
          創建文件對話框
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        def ShowUpload(self):
            '''
              叫出文件對話框
              參數：
              self: 用來創建專屬物件本身（class）的變數以及函式
            '''
            '''
              開啟選擇文件介面
              參數：
              1. 視窗
              2. 文字框的敘述
              3. 從哪個路徑開啟
              4. 檔案類型的過濾器
            '''
            open_file = QFileDialog.getOpenFileName(self, "Open File" , '/', "Text (*.txt)")
            print(open_file) # 印出文件名稱
            print()
            print('ــــــــــــــــــــــــ')

            try:
                with open(open_file[0] , 'r', errors='ignore') as f : # 讀取文件，沒讀到檔案則顯示錯誤訊息。第三個參數 errors="ignore" 是防止程式以為讀不了編碼導致無法讀取檔案
                    print(f.read())
            except FileNotFoundError as e:
                print("No such file or directory!!!")


        bt = QPushButton(self , text="Select File")
        bt.move(350, 260)
        bt.resize(80, 40)
        bt.clicked.connect(lambda: ShowUpload(self))
        bt.clicked.connect(lambda: self.component_changed('filedialog'))

    def CreateProgressBar(self):
        '''
          創建進度條
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        lb = QLabel(self, text='Progress Bar:')
        lb.move(155, 220)
        pb = QProgressBar(self) # 創建進度條，參數為視窗
        pb.move(250, 220)
        pb.resize(150, 30)
        pb.setValue(0) # 預設進度條完成度
        return pb

    def CreateRadioButtton(self):
        '''
          創建單選按鈕
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        lb = QLabel(self, text='Radio Button:')
        lb.move(155, 100)
        rd1 = QRadioButton(self, text='Male') # 創建單選按鈕，第一個參數為視窗，第二個參數為按鈕要顯示什麼文字
        rd1.move(250, 100)
        rd1.clicked.connect(lambda: self.component_changed('radiobutton'))
        rd2 = QRadioButton(self, text='Female')
        rd2.move(315, 100)
        rd2.clicked.connect(lambda: self.component_changed('radiobutton'))

    def CreateTextBox(self):
        '''
          創建文字框
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        lb = QLabel(self, text='TextBox:')
        lb.move(180, 60)
        text_box = QLineEdit(self) # 創建文字框，參數為視窗
        text_box.resize(100, 30)
        text_box.move(250, 60)
        text_box.textChanged.connect(lambda: self.component_changed('textbox'))

    def InitUi(self):
        '''
          呼叫元件以及設定視窗參數
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        self.changed_list = set()
        self.button = self.CreateButton()
        self.check_box = self.CreateCheckBox()
        self.dropdown_box = self.CreateComboBox()
        self.color_dialog = self.CreateColorDialog()
        self.file_dialog = self.CreateFileDialog()
        self.font_dialog = self.CreateFontDialog()
        self.progress_bar = self.CreateProgressBar()
        self.radio_button = self.CreateRadioButtton()
        self.text_box = self.CreateTextBox()
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