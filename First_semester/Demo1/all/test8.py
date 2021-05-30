from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

import sys

from random import randint


class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it 
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        #layout = QVBoxLayout()
        #self.label = QLabel("Another Window % d" % randint(0,100))
        #layout.addWidget(self.label)
        #self.setLayout(layout)


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.w = [[None] for i in range(10)]  # No external window yet.
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)
        
    def show_new_window(self, checked):
        #print(self.w)
        self.w[0] = AnotherWindow()
        self.w[0].show()

        self.w[1] = AnotherWindow()
        self.w[1].show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()