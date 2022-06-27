from cmath import rect
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from retinalApplicationUI import Ui_Dialog
from categoryDialog import Category_Dialog
# from retinal import PhotoViewer
# TODO: 1. import logging
# TODO: 3. remove all rectangles when changing to other image


database = {}


class RetinalApplication(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.dir = None
        self.images = []

        self.rects = []
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.begin, self.destination = QtCore.QPoint(), QtCore.QPoint()

        self.dialog = CategoryApplication()

        # signal connections
        self.ui.pushButton_3.clicked.connect(self.chooseFolder)
        self.ui.listWidget.itemClicked.connect(self.showImage)
        self.ui.graphicsView.photoClicked.connect(self.photoClicked)
        self.ui.graphicsView.photoReleased.connect(self.photoReleased)
        self.ui.graphicsView.photoMoved.connect(self.photoMoved)
        self.dialog.dialogStatus.connect(self.handleDialogInfo)

    def paintEvent(self, event):
        super(RetinalApplication, self).paintEvent(event)

        painter = QtGui.QPainter(self)

        painter.drawLine(0, 0, 200, 0)

        if(self.ui.graphicsView.hasPhoto()):

            if not self.begin.isNull() and not self.destination.isNull():
                # self.begin, self.destination = standardizeRectangle(
                #     self.begin, self.destination)
                rect_item = QtWidgets.QGraphicsRectItem(
                    QtCore.QRectF(self.begin, self.destination))
                rect_item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
                self.rects.append(rect_item)
                # self.ui.graphicsView.items().clear()
                self.ui.graphicsView._scene.addItem(rect_item)

    def chooseFolder(self):
        self.dir = QtWidgets.QFileDialog.getExistingDirectory(
            None, 'Select a folder:', 'C:\\', QtWidgets.QFileDialog.ShowDirsOnly)
        if self.dir != '':
            self.readFolder(self.dir)

    def readFolder(self, folder):
        self.images = []
        files = os.listdir(folder)
        # TODO: 2. this method don't recursively search in whole directories inside chosen directory.
        for file in files:
            if isAnImage(file):
                self.images.append(file)

        self.importInsideListWidget(self.images)

    def importInsideListWidget(self, images):
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(images)
        print(images)

    def showImage(self):
        print(self.ui.listWidget.currentItem().text())
        imagePath = self.dir + '/' + self.ui.listWidget.currentItem().text()
        if(os.path.isfile(imagePath)):
            # scene = QtWidgets.QGraphicsScene(self)
            pixmap = QtGui.QPixmap(imagePath)
            width = self.ui.graphicsView.size().width()
            height = self.ui.graphicsView.size().height()
            pixmapRescaled = pixmap.scaled(
                width, height, QtCore.Qt.KeepAspectRatio)
            # item = QtWidgets.QGraphicsPixmapItem(pixmapRescaled)
            # scene.addItem(item)

            self.ui.graphicsView.setPhoto(pixmapRescaled)

            database[self.ui.listWidget.currentItem().text()] = []
        else:
            print(imagePath)
        pass

    def photoClicked(self, pos):
        if self.ui.graphicsView.dragMode() == QtWidgets.QGraphicsView.NoDrag:
            self.begin = pos
            # print(self.begin)
            self.update()

            # print('%d, %d' % (pos.x(), pos.y()))

    def photoMoved(self, pos):
        if self.ui.graphicsView.dragMode() == QtWidgets.QGraphicsView.NoDrag:
            self.destination = pos
            # self.ui.graphicsView.items().clear()
            # print(self.destination)
            self.ui.graphicsView.removeRects(self.rects[:-1])
            self.update()

    def photoReleased(self, pos):
        if self.ui.graphicsView.dragMode() == QtWidgets.QGraphicsView.NoDrag:
            self.ui.graphicsView.removeRects(self.rects)
            # self.begin, pos = standardizeRectangle(self.begin, pos)
            if checkRectCoordinates(self.begin, pos):
                rect_item = QtWidgets.QGraphicsRectItem(
                    QtCore.QRectF(self.begin, pos))
                rect_item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
                self.ui.graphicsView._scene.addItem(rect_item)

                self.openCategoryDialog(self.begin, pos)

            # self.update()
            self.begin, self.destination = QtCore.QPoint(), QtCore.QPoint()

    def openCategoryDialog(self, beginCord, destCord):
        self.dialog.set_cords(beginCord, destCord,
                              self.ui.listWidget.currentItem().text())
        self.dialog.exec_()

    def handleDialogInfo(self, status, beginPos, destPos):
        if status:
            print('save data')
        else:
            print('remove data')


class CategoryApplication(QtWidgets.QDialog):
    dialogStatus = QtCore.pyqtSignal(int, QtCore.QPoint, QtCore.QPoint)

    def __init__(self):
        super().__init__()

        self.ui = Category_Dialog()
        self.ui.setupUi(self)

        self.model = QtGui.QStandardItemModel(self)
        self.ui.listView.setModel(self.model)

        self.info = []

        # signal connections
        self.ui.pushButton_3.clicked.connect(self.addNewCategory)
        self.ui.pushButton.clicked.connect(self.saveInfo)
        self.ui.pushButton_2.clicked.connect(self.deleteInfo)
        self.model.itemChanged.connect(self.onCategorySelection)

    def set_cords(self, beginCord, destCord, imageName):
        self.imageName = imageName
        self.cords = (beginCord, destCord)

    def addNewCategory(self):
        newCategory = self.ui.lineEdit.text()
        # print(newCategory)
        item = self.createCategoryItem(newCategory)
        self.model.appendRow(item)

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
            pass
        else:
            item.setBackground(QtGui.QColor(255, 255, 255))
            item.setForeground(QtGui.QColor(0, 0, 0))
            # print(item.text())
            if item.text() in self.info:
                self.info.remove(item.text())

    def saveInfo(self):
        pass

    def deleteInfo(self):
        self.info = []
        self.uncheckItems()
        self.dialogStatus.emit(0, self.cords[0], self.cords[1])
        self.close()

    def uncheckItems(self):
        for index in range(self.model.rowCount()):
            item = self.model.item(index)
            if item.isCheckable():
                item.setCheckState(QtCore.Qt.Unchecked)


def isAnImage(fileName):
    if fileName.endswith('.png') or fileName.endswith('.jpg') or fileName.endswith('.jpeg'):
        return True

    return False


def checkRectCoordinates(beginCord, destCord):
    if beginCord.x() > destCord.x() or beginCord.y() > destCord.y():
        return False
    return True


def standardizeRectangle(beginCord, destCord):
    # Incomplete
    # TODO: if destination coordinate is not standard (Sx < Dx and Sy < Dy)
    if beginCord.x() > destCord.x() or beginCord.y() > destCord.y():
        print(beginCord.x(), beginCord.y(), destCord.x(), destCord.y())
        return destCord, beginCord

    return beginCord, destCord


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    retianl = RetinalApplication()
    retianl.show()
    # dialog = QtWidgets.QDialog()
    # ui = Ui_dialog()
    # ui.setupUi(dialog)
    # dialog.show()
    sys.exit(app.exec_())
