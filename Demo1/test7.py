import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Main(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.InitUi()
    def InitUi(self):
        ql = QLabel(self)       
        ql.setText("<font color=\"blue\">Hello</font><font color=\"red\">Hello</font>")

def main():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    app.exec_()

if  __name__ == "__main__":
    main()

   
