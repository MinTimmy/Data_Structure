import sys
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsTextItem, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QWheelEvent


class MyView(QGraphicsView):
    def wheelEvent(self, event: QWheelEvent):
        if event.modifiers() == Qt.ShiftModifier:
            self.horizontalScrollBar().wheelEvent(event)
        else:
            self.verticalScrollBar().wheelEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    scene = QGraphicsScene()
    view = MyView(scene)
    
    # Generate 200 objects, 100 on x and 100 on y.
    for i in range(100):
        obj_on_x = QGraphicsTextItem("X" + str(i))
        obj_on_x.setX(i * 100)
        scene.addItem(obj_on_x)

        obj_on_y = QGraphicsTextItem("Y" + str(i))
        obj_on_y.setY(i * 100)
        scene.addItem(obj_on_y)

    view.show()
    sys.exit(app.exec_())

