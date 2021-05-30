import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Widget(QWidget):

    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.red)

        painter.drawLine(10, 10, 100, 140)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    ex = Widget()

    ex.resize(1000,1000)
    ex.setWindowTitle("Timmy")
    ex.show()

    sys.exit(app.exec_())