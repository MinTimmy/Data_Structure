from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QAction, 
                                QApplication,
                                QColorDialog,
                                QFileDialog,
                                QFontComboBox, 
                                QMainWindow, 
                                QTextEdit,
                                QSpinBox)
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

    def Menubar(self):
        '''
          建立 Menubar
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        menubar = self.menuBar() # 建立 Menubar
        file = menubar.addMenu("File") # 新增 menu 元件
        edit = menubar.addMenu('Edit')
        view = menubar.addMenu('View')

        file.addAction(self.newAction) # 新增 menu 元件的觸發動作
        file.addAction(self.openAction)
        file.addAction(self.saveAction)

    def Toolbar(self):
        '''
          建立 Toolbar
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        self.newAction = QAction("New" , self) # 建立一個動作事件
        self.newAction.triggered.connect(self.new) # 觸發時開啟一個新視窗
        self.newAction.setShortcut("ctrl+N") # 建立快捷鍵

        self.openAction = QAction("Open" , self)
        self.openAction.triggered.connect(self.open) # 觸發時跳出開啟檔案視窗
        self.openAction.setShortcut('ctrl+O')

        self.saveAction = QAction("Save" , self)
        self.saveAction.triggered.connect(self.save) # 觸發時跳出存檔視窗
        self.saveAction.setShortcut('ctrl+S')

    def Formatbar(self):
        '''
          建立 Formatbar
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        fontbox = QFontComboBox(self) # 建立字型下拉式選單
        fontbox.currentFontChanged.connect(lambda font: self.text.setCurrentFont(font)) # 選擇新字體後變更現有字體

        fontsize = QSpinBox(self) # 建立字體大小調整方框
        fontsize.setSuffix(" pt") # 建立字體大小的單位
        fontsize.valueChanged.connect(lambda size: self.text.setFontPointSize(size)) # 調整字體大小後變更現有字體大小
        fontsize.setValue(14) # 字體大小初始值為 14

        fontcolors = QAction(QIcon("icons/font-color.png"), "Change Font Color", self)
        bold = QAction(QIcon("icons/bold.png"), "Change Font To Bold", self)
        italic = QAction(QIcon("icons/italic.png"),"Change Font To Italic", self)
        underline = QAction(QIcon("icons/underline.png"), "Put A Line Under Words", self)
        strike = QAction(QIcon("icons/strike.png"), "Put A Line On Your Words", self)

        align_left = QAction(QIcon("icons/align-left.png"), "Align Words To Left", self)
        align_right =QAction(QIcon("icons/align-right.png"), "Align Words To Right", self)
        align_center = QAction(QIcon("icons/align-center.png"), "Align Words To Center", self)
        align_justify = QAction(QIcon("icons/align-justify.png"), "Justify Your Words", self)

        fontcolors.triggered.connect(self.SetColor) # 觸發後設定文字顏色
        bold.triggered.connect(self.SetBold) # 觸發後決定文字是否變為粗體
        italic.triggered.connect(self.SetItalic) # 觸發後決定文字是否變為斜體
        underline.triggered.connect(self.SetUnderline) # 觸發後決定文字是否加底線
        strike.triggered.connect(self.SetStrikeOut) # 觸發後決定文字是否加上剔除線

        align_left.triggered.connect(lambda: self.text.setAlignment(Qt.AlignLeft)) # 觸發後將文字向左對齊
        align_center.triggered.connect(lambda: self.text.setAlignment(Qt.AlignCenter)) # 觸發後將文字向中對齊
        align_right.triggered.connect(lambda: self.text.setAlignment(Qt.AlignRight)) # 觸發後將文字向右對齊
        align_justify.triggered.connect(lambda: self.text.setAlignment(Qt.AlignJustify)) # 觸發後將文字向預設位置對齊（本例為左）

        self.formatbar = self.addToolBar("Format")
        self.formatbar.addWidget(fontbox)
        self.formatbar.addWidget(fontsize)
        self.formatbar.addSeparator() # 增加小黑線區隔工具種類

        self.formatbar.addAction(fontcolors)
        self.formatbar.addAction(bold)
        self.formatbar.addAction(italic)
        self.formatbar.addAction(underline)
        self.formatbar.addAction(strike)
        self.formatbar.addSeparator()

        self.formatbar.addAction(align_left)
        self.formatbar.addAction(align_center)
        self.formatbar.addAction(align_right)
        self.formatbar.addAction(align_justify)
        self.formatbar.addSeparator()

    def new(self):
        '''
          建立新視窗
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        window = Main(self)
        window.show()

    def open(self):
        '''
          開啟檔案
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
        self.filename = QFileDialog.getOpenFileName(self, "Open File" , '.', "Text (*.txt)")

        if self.filename:
            with open(self.filename ,"rt", errors='ignore') as file : # 讀取文件，沒讀到檔案則顯示錯誤訊息。第二個參數中的 t 代表 text mode，第三個參數 errors="ignore" 是防止程式以為讀不了編碼導致無法讀取檔案
                self.text.setText(file.read())

    def save(self):
        '''
          存檔
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        if not self.filename:
            self.filename = QFileDialog.getSaveFileName(self , "Save File") # 存檔

        if not self.filename.endswith(".txt"):
            self.filename += ".txt"

        with open(self.filename , "wt") as file :
            file.write(self.text.toHtml())


    def InitUi(self):
        '''
          呼叫元件以及設定視窗參數
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        ## Start With The GUI
        self.text = QTextEdit(self)
        self.Toolbar()
        self.Formatbar()
        self.Menubar()
        self.setWindowTitle('Text Editor')
        self.setCentralWidget(self.text)
        self.setGeometry(100,100,900,600)
        self.filename = ""
        self.isBold = False
        self.isItalic = False
        self.isUnderline = False
        self.isStrike = False
        self.textFont = QFont()

    def SetColor(self):
        '''
          用顏色對話框來設定顏色
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        cd = QColorDialog.getColor()
        color_name = cd.name()
        self.text.setStyleSheet("Color: " + color_name)

    def SetBold(self):
        '''
          設定粗體
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        self.isBold ^= True
        self.textFont.setBold(self.isBold)
        self.text.setFont(self.textFont)

    def SetItalic(self):
        '''
          設定斜體
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        self.isItalic ^= True
        self.textFont.setItalic(self.isItalic)
        self.text.setFont(self.textFont)

    def SetUnderline(self):
        '''
          設定底線
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        self.isUnderline ^= True
        self.textFont.setUnderline(self.isUnderline)
        self.text.setFont(self.textFont)
    
    def SetStrikeOut(self):
        '''
          設定剃除線
          參數：
          self: 用來創建專屬物件本身（class）的變數以及函式
        '''
        self.isStrike ^= True
        self.textFont.setStrikeOut(self.isStrike)
        self.text.setFont(self.textFont)

def main():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    app.exec_()


if __name__ == "__main__" :
    main()