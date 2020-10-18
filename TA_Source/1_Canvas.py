'''
  使用 PyQt5 畫線、長方形、圓角長方形、三角形
'''
import sys
#from PyQt5.QtGui     import (QIcon, QPainter, QPolygon)
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
#from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget)
from PyQt5.QtWidgets import *
# import linter

class Widget(QWidget):
    '''
      創建一個頁面
      物件（class 括號裡面第一個變數，看起來像參數的東西）：
      QWidget: 獨立的一個 class，在這裡的用法為繼承，因此呼叫 Widget 時後面不需接任何參數就能執行繼承了
    '''
    def __init__(self):
        '''
          __init__ 用來初始化 class 內的變數及物件，與 C++ 的 Constructor 等價，在這裡為初始化父物件，也就是 QWidget。
          呼叫 super() 與呼叫父物件等價，因此這裡也可以寫成 QWidget.__init__()。
        '''
        super().__init__()

    def paintEvent(self, event):
        '''
          畫圖，不需要特別呼叫這個函式，這個函式定義在 QWidget 內部，在 QWidget 初始化的時候就會直接執行了
          參數：
          self: 與 C++ 中的 this 等價，用來創建專屬物件本身（class）的變數以及函式
          event: 畫畫事件，裡面包括視窗以及畫畫的一些屬性和設定，不需要特別傳遞
        '''
        painter = QPainter(self) # 呼叫畫筆
        painter.setPen(Qt.red) # 把畫筆顏色變紅色
        
        painter.drawLine(10, 10, 100, 140) # 畫線，方法為 (start_x, start_y, end_x, end_y)
        
        painter.setPen(Qt.blue) # 把畫筆顏色變藍色
        painter.drawRect(120, 10, 80, 80) # 畫長方形，方法為 (start_x, start_y, end_x, end_y)

        rectf = QRectF(230.0, 10.0, 80.0, 80.0) # 畫圓角長方形，方法為 (start_x, start_y, end_x, end_y)
        painter.drawRoundedRect(rectf, 20, 20)
'''
        p2 = [QPoint(120, 110), QPoint(220, 110), QPoint(220, 190)] # 畫多邊形，一個 QPoint 代表一個點
        painter.drawPolygon(QPolygon(p2))
'''

if __name__ == "__main__": # 當執行這個檔案的時候，__name__ 被賦予 "__main__" 這個字串，如果只是單純將檔案引用 （import），則 __name__ 會等於檔案名稱
    app = QApplication(sys.argv) # 創建 QApplication，注意括號內 sys.argv 一定要寫，才能將檔案名稱（argv[0]）傳給 QApplication

    ex = Widget() # 創建 QWidget
    ex.resize(400, 280) # 調整視窗大小
    ex.setWindowTitle('Canvas') # 設定視窗名稱
    ex.setWindowIcon(QIcon('404.png')) # 設定視窗 Icon
    ex.show() # 顯示視窗，一定要寫，不然執行續會卡住（app 開始執行了，但沒有顯示視窗，所以也無從點選叉叉）

    sys.exit(app.exec_()) # 執行 QApplication，一定要寫，不然視窗不會定格在螢幕上，只會快速出現視窗，執行完程式碼，然後消失