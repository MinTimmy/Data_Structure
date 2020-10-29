import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Person(object):
    """Name of the person along with his city"""
    def __init__(self,name,city):
        self.name = name
        self.city = city
 
class PersonDisplay(QMainWindow):
    def __init__(self,parent=None):
        super(PersonDisplay,self).__init__(parent)
        self.setWindowTitle('Person City')
        view = QTableView()
        tableData = PersonTableModel()
        view.setModel(tableData)
        self.setCentralWidget(view)
 
        tableData.addPerson(Person('Ramesh', 'Delhi'))
        tableData.addPerson(Person('Suresh', 'Chennai'))
        tableData.addPerson(Person('Kiran', 'Bangalore'))
 
class PersonTableModel(QAbstractTableModel):
    """Model class that drives the population of tabular display"""
    def __init__(self):
        super(PersonTableModel,self).__init__()
        self.headers = ['Name','City']
        self.persons  = []
 
    def rowCount(self,index=QModelIndex()):
        return len(self.persons)
 
    def addPerson(self,person):
        self.beginResetModel()
        self.persons.append(person)
        self.endResetModel()
 
    def columnCount(self,index=QModelIndex()):
        return len(self.headers)
 
    def data(self,index,role=Qt.DisplayRole):
        col = index.column()
        person = self.persons[index.row()]
        if role == Qt.DisplayRole:
            if col == 0:
                return QVariant(person.name)
            elif col == 1:
                return QVariant(person.city)
            return QVariant()
 
    def headerData(self,section,orientation,role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return QVariant()
 
        if orientation == Qt.Horizontal:
            return QVariant(self.headers[section])
        return QVariant(int(section + 1))
 
def start():
    app  = QApplication(sys.argv)
    appWin = PersonDisplay()
    appWin.show()
    app.exec_()
 
if __name__ == "__main__":
    start()