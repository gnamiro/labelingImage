from cmath import rect
from genericpath import getsize
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from RetinalApplicationUI import Ui_Dialog
from categoryDialog import CategoryApplication
# from retinal import PhotoViewer
# TODO: 1. import logging
# TODO: 3. remove all rectangles when changing to other image


class RetinalApplication(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.dir = None
        self.images = []

        self.rects = []
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.begin, self.destination = QtCore.QPoint(), QtCore.QPoint()
        self.currentRectTopLeft = QtCore.QPoint() 
        self.currentRectSize = QtCore.QSize()

        # signal connections
        self.ui.pushButton_3.clicked.connect(self.chooseFolder)
        self.ui.listWidget.itemClicked.connect(self.showImage)
        self.ui.graphicsView.photoClicked.connect(self.photoClicked)
        self.ui.graphicsView.photoReleased.connect(self.photoReleased)
        self.ui.graphicsView.photoMoved.connect(self.photoMoved)

    def paintEvent(self, event):
        super(RetinalApplication, self).paintEvent(event)

        painter = QtGui.QPainter(self)

        painter.drawLine(0, 0, 200, 0)

        if(self.ui.graphicsView.hasPhoto()):
            if not self.currentRectTopLeft.isNull() and not self.currentRectSize.isNull():
                rect_item = QtWidgets.QGraphicsRectItem(
                    QtCore.QRectF(self.currentRectTopLeft, self.currentRectSize))
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
            self.currentRectTopLeft = getTopLeftOfRect(self.begin, pos)
            self.currentRectSize = getSizeOfRect(self.begin, pos)
            # self.ui.graphicsView.items().clear()
            # print(self.destination)
            self.ui.graphicsView.removeRects(self.rects[:-1])
            self.update()

    def photoReleased(self, pos):
        if self.ui.graphicsView.dragMode() == QtWidgets.QGraphicsView.NoDrag:
            self.ui.graphicsView.removeRects(self.rects)
            self.currentRectTopLeft = getTopLeftOfRect(self.begin, pos)
            self.currentRectSize = getSizeOfRect(self.begin, pos)
            # self.begin, pos = standardizeRectangle(self.begin, pos)
            # if checkRectCoordinates(self.begin, pos):
            rect_item = QtWidgets.QGraphicsRectItem(
                QtCore.QRectF(self.currentRectTopLeft, self.currentRectSize))
            rect_item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
            self.ui.graphicsView._scene.addItem(rect_item)

            self.openCategoryDialog(self.begin, pos)

            # self.update()
            self.begin, self.destination = QtCore.QPoint(), QtCore.QPoint()

    def openCategoryDialog(self, beginCord, destinCord):
        dialog = CategoryApplication()
        dialog.exec_()

        print('after dialog')


def isAnImage(fileName):
    if fileName.endswith('.png') or fileName.endswith('.jpg') or fileName.endswith('.jpeg'):
        return True

    return False


def checkRectCoordinates(beginCord, destCord):
    if beginCord.x() > destCord.x() or beginCord.y() > destCord.y():
        return False
    return True


def getTopLeftOfRect(beginPoint, destPoint):
    x = min(beginPoint.x(), destPoint.x())
    y = min(beginPoint.y(), destPoint.y())

    return QtCore.QPoint(x, y)

def getSizeOfRect(beginPoint, destPoint):
    x = abs(beginPoint.x() - destPoint.x())
    y = abs(beginPoint.y() - destPoint.y())

    return QtCore.QSizeF(x, y)


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
