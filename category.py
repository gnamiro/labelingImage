from PyQt5 import QtCore, QtGui, QtWidgets


class CategoryDialog:
    def __init__(self, ui, model):
        self.ui = ui
        self.model = model

        self.info = []
        self._category = []
        self.index = -1

        self.ui.addCategoryButton.clicked.connect(self.addNewCategory)

        self.model.itemChanged.connect(self.onCategorySelection)

    def set_cords(self, beginCord, size, boundingBoxIndex):
        self.index = boundingBoxIndex
        self.cords = (beginCord, size)

    def load_data(self, category):
        categoryList = category.split(',')
        print(categoryList)
        # pass
        for item in categoryList:
            if item not in self._category:
                checkboxItem = self.createCategoryItem(item)
                self.model.appendRow(checkboxItem)
                self._category.append(item)

        for index in range(self.model.rowCount()):
            item = self.model.item(index)
            if item.text() in categoryList:
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(QtCore.Qt.Unchecked)

    def addNewCategory(self):
        newCategory = self.ui.categoyrEdit.text()
        print(self._category)
        if(newCategory != ''):
            if newCategory not in self._category:
                item = self.createCategoryItem(newCategory)
                self.model.appendRow(item)
                self._category.append(newCategory)
        self.ui.categoyrEdit.setText('')

    def createCategoryItem(self, categoryName):
        item = QtGui.QStandardItem(categoryName)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setData(QtCore.QVariant(QtCore.Qt.Unchecked),
                     QtCore.Qt.CheckStateRole)

        return item

    def onCategorySelection(self, item):
        if item.checkState() == QtCore.Qt.Checked:
            item.setBackground(QtGui.QColor(0, 255, 255))
            item.setForeground(QtGui.QColor(0, 0, 0))
            # print(item.text())
            if item.text() not in self.info:
                self.info.append(item.text())
            # if item.text() not in self._category:
            #     self._category.append(item.text())
            pass
        else:
            item.setBackground(QtGui.QColor(255, 255, 255))
            item.setForeground(QtGui.QColor(0, 0, 0))
            # print(item.text())
            if item.text() in self.info:
                self.info.remove(item.text())

    def uncheckItems(self):
        for index in range(self.model.rowCount()):
            item = self.model.item(index)
            if item.isCheckable():
                item.setCheckState(QtCore.Qt.Unchecked)

    def saveInfo(self):
        if not self.info:
            return (-1, '', None)

        infoMessage = ','.join(str(e) for e in self.info)
        self.uncheckItems()
        _index = self.index
        self.index = -1
        return (_index, infoMessage, self.cords)
        self.sendMessage.emit(1, self.index, infoMessage,
                              self.cords[0], self.cords[1])
        self.close()

    def deleteInfo(self):
        self.info = []
        self.uncheckItems()

        if self.index == -1:
            print('no Bbox selected')
            return (-1, None)

        _index = self.index
        self.index = -1
        return (_index, self.cords)
        self.dialogStatus.emit(0, self.index, '', self.cords[0], self.cords[1])
        self.close()
