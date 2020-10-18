import sys
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class Widget(QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setPen(Qt.red)
        painter.drawLine(10,10,20,20)
        
        
        painter.setPen(Qt.blue)
        painter.drawRect(90,60,100,70)

        p2 = [QPoint(120, 110), QPoint(220, 110), QPoint(220,190)]
        painter.drawPolygon(QPolygon(p2))

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Widget()
    ex.resize(4000, 280)
    ex.setWindowTitle("Demo")
    ex.show()
    sys.exit(app.exec_())
