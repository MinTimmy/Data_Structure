from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Main(QMainWindow):

    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)
        self.InitUi()

    def InitUi(self):
        self.textboxValue = ""
        self.text_box = self.CreateTextBox()
        self.changed_list = set()
        self.progress_bar = self.CreateProgressBar()
        self.button = self.createButton()
        
        self.show()

    def component_changed(self, name):
        self.changed_list.add(name)
        self.progress_bar.setValue(len(self.changed_list) * 12.5 )

    def CreateProgressBar(self):
        lb = QLabel(self, text = "Progess Bar")
        lb.move(155, 220)
        pb = QProgressBar(self)
        pb.move(250, 220)
        pb.resize(150, 30)
        pb.setValue(0)
        return pb

    def createButton(self):
        button = QPushButton(self, text = "OK")
        button.resize(70,30)
        button.move(250, 320)
        button.clicked.connect(lambda: print("OK"))
        button.clicked.connect(lambda: print(self.text_box.text()))
        button.clicked.connect(lambda: self.component_changed('filedialog'))
        
    def on_click(self):
        pass        


    def CreateTextBox(self):
        lb = QLabel(self, text = "TextBox: ")
        lb.move(180,60)
        text_box = QLineEdit(self)
        text_box.resize(100, 30)
        text_box.move(250, 60)
        text_box.textChanged.connect(lambda: self.component_changed('textBox'))
        return text_box

        

    def setTextboxValue(value):
        self.textboxValue = value


def main():
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.resize(1000,1000)
    main_window.show()
    app.exec_()

if __name__ == "__main__":
    main()
