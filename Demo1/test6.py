import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QHBoxLayout

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        hbox = QHBoxLayout()
        lb1 = QLabel("falcon")
        lb1.resize(946,946)
        lb1.setStyleSheet("border: 3px solid blue; border-radius:473px;") 

        lb2 = QLabel("eagle")
        lb2.resize(946,946)
        lb2.setStyleSheet("border: 3px solid blue; border-radius:473px;") 
        hbox.addWidget(lb1)
        hbox.addWidget(lb2)
        #hbox.addWidget(QLabel("eagle"))
        #hbox.addWidget(QLabel("skylark"))

        hbox.addWidget(lb1)
        hbox.addWidget(lb2)
        #hbox.addWidget(lb)

        #self.setLayout(hbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QLabel')
        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    ex.resize(200,200)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
