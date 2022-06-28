from calendar import c
from cmath import rect
from genericpath import getsize
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from RetinalApplicationUI import Ui_Dialog
from categoryDialog import CategoryApplication

import pandas as pd
import numpy as np
# from retinal import PhotoViewer
# TODO: 1. import logging
# TODO: 3. remove all rectangles when changing to other image
# TODO: 4. define new rectItem to change its color

clickDistanceThreshold = 0.04

database = pd.DataFrame(
    columns=['image_id', 'bbox_id', 'topLeft', 'size', 'category'])


class BoundingBox():
    def __init__(self, rectF):
        self.rectF = rectF
        self.stack = 0

    def increment(self):
        self.stack = min(self.stack + 1, 2)

    def decrement(self):
        self.stack = max(self.stack - 1, 0)

    def __eq__(self, other):
        return other is not None and self.stack == other.stack and self.rectF == other.rectF


class RetinalApplication(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.dir = None
        self.images = []

        self.rects = []
        self.boundingBoxes = []
        self.rect_items = []
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.begin, self.destination = QtCore.QPoint(), QtCore.QPoint()
        self.currentRectTopLeft = QtCore.QPoint()
        self.currentRectSize = QtCore.QSize()
        self.prevSelectedBoundingBox = None

        self.dialog = CategoryApplication()

        # signal connections
        self.ui.pushButton_3.clicked.connect(self.chooseFolder)
        self.ui.listWidget.itemClicked.connect(self.showImage)
        self.ui.graphicsView.photoClicked.connect(self.photoClicked)
        self.ui.graphicsView.photoReleased.connect(self.photoReleased)
        self.ui.graphicsView.photoMoved.connect(self.photoMoved)
        self.dialog.dialogStatus.connect(self.handleDialogInfo)
        self.dialog.sendMessage.connect(self.handleDialogInfo)
        self.ui.pushButton_2.clicked.connect(self.saveImageData)
        self.ui.pushButton.clicked.connect(self.cancel)

    def refreshScene(self):
        self.ui.graphicsView.removeRects(self.rect_items)
        self.rect_items = []
        self.boundingBoxes = []
        self.currentRectTopLeft = QtCore.QPoint()
        self.currentRectSize = QtCore.QSize()
        self.prevSelectedBoundingBox = None

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
        print(self.rect_items)
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

            self.refreshScene()
            self.ui.graphicsView.setPhoto(pixmapRescaled)

            self.loadImageBboxes()
            # database[self.ui.listWidget.currentItem().text()] = []
        else:
            print(imagePath)
        pass

    def loadImageBboxes(self):
        self.rect_items = []
        currentPic = self.ui.listWidget.currentItem().text()
        dataReleventToImage = database.loc[database['image_id'].isin([
                                                                     currentPic])]
        # print(dataReleventToImage)
        for index, row in dataReleventToImage.iterrows():
            # print(row['topLeft'], row['size'])
            topLeftdim = [int(float(e)) for e in row['topLeft'].split('-')]
            rectSizedim = [float(e) for e in row['size'].split('-')]
            topLeft = QtCore.QPoint(
                topLeftdim[0], topLeftdim[1])
            rectSize = QtCore.QSizeF(
                rectSizedim[0], rectSizedim[1])

            self.createQrectItem(topLeft, rectSize)
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
            distance = (self.currentRectSize.width() ** 2 +
                        self.currentRectSize.height() ** 2) ** 0.5
            # self.begin, pos = standardizeRectangle(self.begin, pos)
            # if checkRectCoordinates(self.begin, pos):
            if (self.isItClick(distance)):
                boundingBox, index = self.findBoundingBox(pos)
                if (self.prevSelectedBoundingBox is not None and self.prevSelectedBoundingBox != boundingBox):
                    self.prevSelectedBoundingBox.decrement()
                if (boundingBox is not None):
                    boundingBox.increment()
                    if (boundingBox.stack == 2):
                        print(boundingBox.rectF.size())
                        self.openCategoryDialog(
                            boundingBox.rectF.topLeft(), boundingBox.rectF.size(), index)
                        boundingBox.decrement()
                    self.prevSelectedBoundingBox = boundingBox

            else:
                self.createQrectItem(
                    self.currentRectTopLeft, self.currentRectSize)

            # self.update()
            # self.begin, self.destination = QtCore.QPoint(), QtCore.QPoint()

    def createQrectItem(self, topLeft, rectSize):
        rectF = QtCore.QRectF(
            topLeft, rectSize)
        rect_item = QtWidgets.QGraphicsRectItem(rectF)
        rect_item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, True)
        self.ui.graphicsView._scene.addItem(rect_item)
        self.boundingBoxes.append(BoundingBox(rectF))
        self.rect_items.append(rect_item)
        pass

    def isItClick(self, distance):
        if (distance < clickDistanceThreshold):
            return True
        return False

    def findBoundingBox(self, pos):
        minimumArea = 100000000000
        minimumBoundedBox = None
        minimumBoundedBoxIndex = None
        for index in range(len(self.boundingBoxes)):
            boundingBox = self.boundingBoxes[index]
            if (boundingBox.rectF.contains(pos)):
                area = boundingBox.rectF.size().width() * boundingBox.rectF.size().height()
                if area < minimumArea:
                    minimumArea = area
                    minimumBoundedBox = boundingBox
                    minimumBoundedBoxIndex = index
        return minimumBoundedBox, minimumBoundedBoxIndex

    def openCategoryDialog(self, beginCord, size, boundingBoxIndex):
        topLeft, rectSize = [beginCord.x(), beginCord.y()], [
            size.width(), size.height()]
        currentPic = self.ui.listWidget.currentItem().text()

        bboxId = '-'.join(str(e) for e in topLeft + rectSize)
        self.dialog.set_cords(beginCord, size, boundingBoxIndex)

        idx = np.where((database['image_id'] ==
                        currentPic) & (database['bbox_id'] == bboxId))
        if(idx[0].size > 0):
            self.dialog.load_data(database.at[idx[0][0], 'category'])
        else:
            self.dialog.uncheckItems()

        self.dialog.exec_()

    def handleDialogInfo(self, status, index, info, beginPos, size):
        global database
        topLeft, rectSize = [beginPos.x(), beginPos.y()], [
            size.width(), size.height()]
        currentPic = self.ui.listWidget.currentItem().text()

        bboxId = '-'.join(str(e) for e in topLeft + rectSize)

        if status:
            # infoList = info.split(',')
            idx = np.where((database['image_id'] ==
                           currentPic) & (database['bbox_id'] == bboxId))
            if not idx[0].size > 0:
                appendToDatabase(currentPic, bboxId, topLeft, rectSize, info)
            else:
                database.at[idx[0][0], 'category'] = info
            print(database)
            pass
        else:
            boundingBox = self.findRectItem(topLeft, rectSize)
            if boundingBox != None:
                # print('founded')
                # print(len(self.rect_items))
                self.rect_items.remove(boundingBox)
                del self.boundingBoxes[index]
                # print(len(self.rect_items))
                self.ui.graphicsView.removeRect(boundingBox)
                idx = np.where((database['image_id'] ==
                                currentPic) & (database['bbox_id'] == bboxId))
                print(idx)
                if idx[0].size > 0:
                    database = database.drop(idx[0][0])
                    database = database.reset_index(drop=True)
            else:
                print('not founded')

    def findRectItem(self, topLeft, rectSize):
        print('find rect item: ', len(self.rect_items))
        for rect_item in self.rect_items:
            rectF = rect_item.rect()
            print(topLeft, rectF.x(), rectF.y())

            if(rectF.x() == topLeft[0] and rectF.y() == topLeft[1]):
                rectFSize = rectF.size()
                print(rectSize, rectFSize.width(), rectFSize.height())
                if(rectFSize.width() == rectSize[0] and rectFSize.height() == rectSize[1]):
                    return rect_item

        return None

    def saveImageData(self):
        database.to_csv('./data/data.csv', index=False)
        pass

    def cancel(self):
        self.refreshScene()


def appendToDatabase(imageId, bboxId, center, size, categorList):
    global database
    new_row = {'image_id': [imageId], 'bbox_id': [bboxId],
               'topLeft': ['-'.join(str(e) for e in center)], 'size': ['-'.join(str(e) for e in size)], 'category': [categorList]}
    df = pd.DataFrame.from_dict(new_row)

    database = pd.concat([database, df], ignore_index=True)
    # database.reset_index(drop=True)


def calculateRectFeatures(startPos, endPos):
    startPosX, startPosY, endPosX, endPosY = startPos.x(
    ), startPos.y(), endPos.x(), endPos.y()
    centerX, centerY = (startPosX + endPosX) / \
        2, (startPosY + endPosY)/2
    width, height = abs(startPosX - endPosX
                        ), abs(startPosY - endPosY)

    return [centerX, centerY], [width, height]


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
    database = pd.read_csv('./data/data.csv')
    print(database)
    retianl.show()
    # dialog = QtWidgets.QDialog()
    # ui = Ui_dialog()
    # ui.setupUi(dialog)
    # dialog.show()
    sys.exit(app.exec_())
