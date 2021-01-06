#!/usr/bin/python3
"""
Reworked code based on
http://trevorius.com/scrapbook/uncategorized/pyqt-custom-abstractitemmodel/
Adapted to Qt5 and fixed column/row bug.
TODO: handle changing data.
"""

import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from anytree import Node


class CustomNode(object):
    def __init__(self, data):
        self._data = data
        if type(data) == tuple:
            self._data = list(data)
        if type(data) is str or not hasattr(data, '__getitem__'):
            self._data = [data]

        self._columncount = len(self._data)
        self._children = []
        self._parent = None
        self._row = 0

    def data(self, column):
        if column >= 0 and column < len(self._data):
            return self._data[column]

    def columnCount(self):
        return self._columncount

    def childCount(self):
        return len(self._children)

    def child(self, row):
        if row >= 0 and row < self.childCount():
            return self._children[row]

    def parent(self):
        return self._parent

    def row(self):
        return self._row

    def addChild(self, child):
        child._parent = self
        child._row = len(self._children)
        self._children.append(child)
        self._columncount = max(child.columnCount(), self._columncount)


class CustomModel(QtCore.QAbstractItemModel):
    def __init__(self, nodes):
        QtCore.QAbstractItemModel.__init__(self)
        self._root = CustomNode(None)
        for node in nodes:
            self._root.addChild(node)

    def rowCount(self, index):
        if index.isValid():
            return index.internalPointer().childCount()
        return self._root.childCount()

    def addChild(self, node, _parent):
        if not _parent or not _parent.isValid():
            parent = self._root
        else:
            parent = _parent.internalPointer()
        parent.addChild(node)

    def index(self, row, column, _parent=None):
        if not _parent or not _parent.isValid():
            parent = self._root
        else:
            parent = _parent.internalPointer()

        if not QtCore.QAbstractItemModel.hasIndex(self, row, column, _parent):
            return QtCore.QModelIndex()

        child = parent.child(row)
        if child:
            return QtCore.QAbstractItemModel.createIndex(self, row, column, child)
        else:
            return QtCore.QModelIndex()

    def parent(self, index):
        if index.isValid():
            p = index.internalPointer().parent()
            if p:
                return QtCore.QAbstractItemModel.createIndex(self, p.row(), 0, p)
        return QtCore.QModelIndex()

    def columnCount(self, index):
        if index.isValid():
            return index.internalPointer().columnCount()
        return self._root.columnCount()

    def data(self, index, role):
        if not index.isValid():
            return None
        node = index.internalPointer()
        if role == QtCore.Qt.DisplayRole:
            return node.data(index.column())
        return None


class MyTree():
    """
    """
    def __init__(self):
        self.items = []

        # Set some random data:
        for i in 'abc':
            self.items.append(CustomNode(i))
            self.items[-1].addChild(CustomNode(['d', 'e', 'f']))
            self.items[-1].addChild(CustomNode(['g', 'h', 'i']))

        self.tw = QtWidgets.QTreeView()
        self.tw.setModel(CustomModel(self.items))

    def appendData(self, rowItems):
        """
        TODO: how to insert data, and update tree.
        """
        print("appendData")
        model = self.tw.model()
        rootIdx = model.index(0, 0, QtCore.QModelIndex())
        position = 3
        new = CustomNode("new")
        new.addChild(CustomNode(rowItems))
        model.beginInsertRows(rootIdx, position, position)
        model.addChild(new, None)
        model.endInsertRows()
        model.layoutChanged.emit()  # must call this otherwise nope!



if __name__ == "__main__":

    import sys
    import quamash
    import asyncio

    # hooking into Qt Event loop with Quamash do I don't 
    # have to bother adding buttons to trigger the row 
    # insert.
    app = QtWidgets.QApplication(sys.argv)
    loop = quamash.QEventLoop(app)
    asyncio.set_event_loop(loop)
    loop.set_debug(True)  # optional


    app = QtWidgets.QApplication(sys.argv)
    mytree = MyTree()

    def doAddData(tree):
        print("doAddData")
        tree.appendData([1,2,3])

    loop.call_later(1.0, doAddData, mytree)

    mytree.tw.show()
    with loop:
        loop.run_forever()
