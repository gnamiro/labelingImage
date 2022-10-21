#!/usr/bin/env python

from calendar import c
from cmath import rect
from genericpath import getsize
# from turtle import width
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from LabelApplicationUI import Ui_dialog
from categoryDialog import CategoryApplication
from category import CategoryDialog
from temp import GraphicsRectItem

import pandas as pd
import numpy as np
# from retinal import PhotoViewer
# TODO: 1. import logging
# TODO: 8*.

clickDistanceThreshold = 2

database = pd.DataFrame(
    columns=['image_id', 'bbox_id', 'bbox_x', 'bbox_y', 'bbox_w', 'bbox_h', 'category', 'root_dir'])

imageInfoDf = pd.DataFrame(
    columns=['image_id', 'image_dir', 'status']
)

folderListHighlightColour = QtGui.QColor(200, 200, 0, 255)
whiteColor = QtGui.QColor(255, 255, 255, 255)
bboxSecondColor = QtGui.QColor(255, 0, 0, 255)
bboxFirstColor = QtGui.QColor(0, 0, 0, 255)

imageInfoFileName = './imageInfo.csv'


class BoundingBox():
    def __init__(self, rectF):
        self.rectF = rectF
        self.stack = 0

    def increment(self):
        self.stack = min(self.stack + 1, 2)

    def decrement(self):
        self.stack = max(self.stack - 1, 0)

    def updateRectPos(self, diffX, diffY):
        self.rectF.translate(diffX, diffY)

    def updateRectSize(self, diffX, diffY, width, height):
        self.rectF.setHeight(height)
        self.rectF.setWidth(width)
        self.updateRectPos(diffX, diffY)

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

        self.xSize = 1
        self.ySize = 1

        self.ui = Ui_dialog()
        self.ui.setupUi(self)

        self.model = QtGui.QStandardItemModel(self)
        self.ui.categoryListView.setModel(self.model)

        self.chooseDataPath()
        self.readDataFromDatabase()

        self.begin, self.destination = QtCore.QPointF(), QtCore.QPointF()
        self.currentRectTopLeft = QtCore.QPointF()
        self.currentRectSize = QtCore.QSizeF()
        self.prevSelectedBoundingBox = None
        self.prevSelectedRectItem = None

        self.selectedRect = None
        self.selecting = 0

        # self.dialog = CategoryApplication()
        self.categoryDialog = CategoryDialog(self.ui, self.model)

        self.ui.graphicsView.show()

        # signal connections
        self.ui.OpenFolderButton.clicked.connect(self.chooseFolder)
        self.ui.listWidget.itemClicked.connect(self.showImage)
        self.ui.graphicsView.photoClicked.connect(self.photoClicked)
        self.ui.graphicsView.photoReleased.connect(self.photoReleased)
        self.ui.graphicsView.photoMoved.connect(self.photoMoved)
        self.ui.saveCategoryButton.clicked.connect(self.saveDialogInfo)
        self.ui.cancelCategoryButton.clicked.connect(self.deleteDialogInfo)
        self.ui.completeImageButton.clicked.connect(self.toggleImageCompletion)
        self.ui.SaveButton.clicked.connect(self.saveImageData)
        self.ui.DeleteButton.clicked.connect(self.deleteAllInfo)
        self.ui.DataFilePathButton.clicked.connect(self.chooseDataPath)
        self.ui.dragModeButtton.clicked.connect(self.toggleDragMode)
        self.ui.graphicsView._scene.itemResizing.connect(self.updateRectSize)

    def readDataFromDatabase(self):
        global database, imageInfoDf, imageInfoFileName
        print(self.dataFileName)
        if(self.dataFileName == ''):
            print("data doesn't exists")
            self.dataFileName = './data.csv'
            if not os.path.exists(self.dataFileName):
                database.to_csv(self.dataFileName, index=False)

        database = pd.read_csv(self.dataFileName)

        if not os.path.exists(imageInfoFileName):
            imageInfoDf.to_csv(imageInfoFileName, index=False)
        else:
            imageInfoDf = pd.read_csv(imageInfoFileName)

        print(database)

    def refreshScene(self):
        self.ui.graphicsView.removeRects(self.rect_items)
        self.rect_items = []
        self.boundingBoxes = []
        self.currentRectTopLeft = QtCore.QPointF()
        self.currentRectSize = QtCore.QSizeF()
        self.prevSelectedBoundingBox = None
        self.categoryDialog.uncheckItems()

    def paintEvent(self, event):
        super(RetinalApplication, self).paintEvent(event)

        painter = QtGui.QPainter(self)

        painter.drawLine(0, 0, 200, 0)

        if(self.ui.graphicsView.hasPhoto()):
            if not self.currentRectTopLeft.isNull() and not self.currentRectSize.isNull():
                rect_item = GraphicsRectItem(
                    QtCore.QRectF(self.currentRectTopLeft, self.currentRectSize))
                self.rects.append(rect_item)
                # if self.ui.graphicsView.dragMode() == QtWidgets.QGraphicsView.NoDrag:
                self.ui.graphicsView._scene.addItem(rect_item)

                self.currentRectTopLeft = QtCore.QPointF()
                self.currentRectSize = QtCore.QSizeF()

    def chooseDataPath(self):
        self.dataFileName = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Choose your data file')[0]
        print(self.dataFileName)

    def chooseFolder(self):
        # TODO: os.path.join
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

        self.highlightFinishedImages()
        print(images)

    def highlightFinishedImages(self):

        for index in range(self.ui.listWidget.count()):
            idx = self.findImageIndex(
                self.ui.listWidget.item(index).text(), self.dir)
            # print(idx[0])
            if idx[0].size > 0:
                if imageInfoDf.at[idx[0][0], 'status'] == 1:
                    self.ui.listWidget.item(index).setBackground(
                        folderListHighlightColour)
        pass

    def showImage(self):
        print(self.ui.listWidget.currentItem().text())
        self.selecting = 1
        self.toggleDragMode()
        imagePath = self.dir + '/' + self.ui.listWidget.currentItem().text()

        if(os.path.isfile(imagePath)):
            # scene = QtWidgets.QGraphicsScene(self)
            pixmap = QtGui.QPixmap(imagePath)
            width = self.ui.graphicsView.size().width()
            height = self.ui.graphicsView.size().height()
            pixmapRescaled = pixmap.scaled(
                width, height, QtCore.Qt.KeepAspectRatio)

            self.xSize = pixmapRescaled.size().width()
            self.ySize = pixmapRescaled.size().height()

            self.refreshScene()
            self.ui.graphicsView.setPhoto(pixmapRescaled)
            self.ui.graphicsView.resetDragMode()
            self.loadImageBboxes()

        else:
            print(imagePath)
        pass

    def toggleImageCompletion(self):
        global imageInfoDf, imageInfoFileName
        currentImage = self.ui.listWidget.currentItem()

        if currentImage is None:
            print('no image selected')
            return

        idx = self.findImageIndex(currentImage.text(), self.dir)
        print(idx)
        if idx[0].size > 0:
            if imageInfoDf.at[idx[0][0], 'status'] == 0:
                currentImage.setBackground(folderListHighlightColour)
                imageInfoDf.at[idx[0][0], 'status'] = 1
            else:
                currentImage.setBackground(whiteColor)
                imageInfoDf.at[idx[0][0], 'status'] = 0
        else:
            appendToImageInfo(currentImage.text(), self.dir, 1)
            currentImage.setBackground(folderListHighlightColour)

        print(imageInfoDf)
        imageInfoDf.to_csv(imageInfoFileName, index=False)

    def loadImageBboxes(self):
        self.rect_items = []
        currentPic = self.ui.listWidget.currentItem().text()
        dataReleventToImage = database.loc[database['image_id'].isin([
                                                                     currentPic])]
        for index, row in dataReleventToImage.iterrows():
            topLeftdim = [float(row['bbox_x']*self.xSize),
                          float(row['bbox_y']*self.ySize)]
            rectSizedim = [float(row['bbox_w'])*self.xSize,
                           float(row['bbox_h'])*self.ySize]
            topLeft = QtCore.QPointF(
                topLeftdim[0], topLeftdim[1])
            rectSize = QtCore.QSizeF(
                rectSizedim[0], rectSizedim[1])

            self.createQrectItem(topLeft, rectSize)
            pass

    def photoClicked(self, pos):
        self.begin = pos
        if self.ui.graphicsView.dragMode() == QtWidgets.QGraphicsView.NoDrag:
            # print(self.begin)
            self.update()

    def photoMoved(self, pos):
        self.ui.graphicsView.removeRects(self.rects[:-1])
        if self.ui.graphicsView.dragMode() == QtWidgets.QGraphicsView.NoDrag:
            self.currentRectTopLeft = getTopLeftOfRect(self.begin, pos)
            self.currentRectSize = getSizeOfRect(self.begin, pos)

            self.update()

    def photoReleased(self, pos):
        self.ui.graphicsView.removeRects(self.rects)
        self.rects = []
        self.currentRectTopLeft = getTopLeftOfRect(self.begin, pos)
        self.currentRectSize = getSizeOfRect(self.begin, pos)
        distance = (self.currentRectSize.width() ** 2 +
                    self.currentRectSize.height() ** 2) ** 0.5

        if self.ui.graphicsView.dragMode() == QtWidgets.QGraphicsView.NoDrag:
            if (self.isItClick(distance)):
                # TODO: AttributeError: 'NoneType' object has no attribute 'rectF'
                self.selectingRectItem(pos)
            else:
                self.createQrectItem(
                    self.currentRectTopLeft, self.currentRectSize)

        if self.ui.graphicsView.dragMode() == QtWidgets.QGraphicsView.ScrollHandDrag:
            if (self.isItClick(distance)):
                # TODO: AttributeError: 'NoneType' object has no attribute 'rectF'
                self.selectingRectItem(pos)
            else:
                try:
                    boundingBox, index = self.findBoundingBox(self.begin)
                    if boundingBox is not None:
                        print('found it')
                        if self.rect_items[index].rectResized == 0:
                            diffX, diffY = pos.x() - self.begin.x(), pos.y() - self.begin.y()
                            oldRectInfo = self.boundingBoxes[index]

                            topLeftRate, rectSizeRate = self.calculateRectSizeRate(
                                oldRectInfo.rectF.topLeft(), oldRectInfo.rectF.size())

                            bboxId = '-'.join(str(e)
                                              for e in topLeftRate + rectSizeRate)
                            currentPic = self.ui.listWidget.currentItem().text()

                            idx = self.findSelectedBbox(currentPic, bboxId)
                            print(idx)
                            self.boundingBoxes[index].updateRectPos(
                                diffX, diffY)

                            self.rect_items[index].updateRectPos(diffX, diffY)

                            self.boundingBoxes[index] = self.updateDatabase(
                                idx, self.boundingBoxes[index])
                    print(self.boundingBoxes, index)
                except:
                    print('possibly no bbox for begin coordinates')

        # print(self.rect_items)
        self.currentRectTopLeft = QtCore.QPointF()
        self.currentRectSize = QtCore.QSizeF()

    def selectingRectItem(self, pos):
        boundingBox, index = self.findBoundingBox(pos)
        if (self.prevSelectedBoundingBox is not None and self.prevSelectedBoundingBox != boundingBox):
            self.prevSelectedBoundingBox.decrement()

            if self.prevSelectedRectItem is not None:
                # self.prevSelectedRectItem.toggleRectSelection()
                self.prevSelectedRectItem.setPen(QtGui.QPen(bboxFirstColor))
        if (boundingBox is not None):
            print('found it2')
            boundingBox.increment()
            if (boundingBox.stack == 2):
                # twice clicked
                rect_item = self.rect_items[index]
                rect_item.setPen(
                    QtGui.QPen(bboxSecondColor))

                self.selectedRect = rect_item
                print(index)
                self.openCategoryDialog(
                    boundingBox.rectF.topLeft(), boundingBox.rectF.size(), index)

                boundingBox.decrement()

                self.prevSelectedRectItem = rect_item
            self.prevSelectedBoundingBox = boundingBox

    def createQrectItem(self, topLeft, rectSize):
        rectF = QtCore.QRectF(
            topLeft, rectSize)
        rect_item = GraphicsRectItem(rectF)
        self.ui.graphicsView._scene.addItem(rect_item)
        self.boundingBoxes.append(BoundingBox(rectF))
        self.selectedRect = rect_item
        self.rect_items.append(rect_item)

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

    def toggleDragMode(self):
        self.selecting = not self.selecting
        self.ui.graphicsView.toggleDragMode()

        if self.selecting:
            self.ui.dragModeButtton.setStyleSheet(
                'background-color: green; color: white')
            self.ui.dragModeButtton.setText('DrawMode')
        else:
            self.ui.dragModeButtton.setStyleSheet(
                'background-color: rgba(225,225,225,255;')
            self.ui.dragModeButtton.setText('DragMode')

    def openCategoryDialog(self, beginCord, size, boundingBoxIndex):
        topLeft, rectSize = [round(beginCord.x()/self.xSize, 14), round(beginCord.y()/self.ySize, 14)], [
            round(size.width()/self.xSize, 14), round(size.height()/self.ySize, 14)]
        currentPic = self.ui.listWidget.currentItem().text()

        bboxId = '-'.join(str(e) for e in topLeft + rectSize)
        self.categoryDialog.set_cords(beginCord, size, boundingBoxIndex)

        idx = self.findSelectedBbox(currentPic, bboxId)

        if(idx[0].size > 0):
            self.categoryDialog.load_data(database.at[idx[0][0], 'category'])
        else:
            self.categoryDialog.uncheckItems()

    def updateRectSize(self, rectItem):
        print(rectItem.rectResized)
        if rectItem.rectResized:
            bbox = rectItem._rectF
            rect = rectItem.rect()

            boundingBox, index = self.findBoundingBox(bbox.topLeft())

            if boundingBox != None:
                print('found it')
                oldRectInfo = self.boundingBoxes[index]

                topLeftRate, rectSizeRate = self.calculateRectSizeRate(
                    oldRectInfo.rectF.topLeft(), oldRectInfo.rectF.size())

                bboxId = '-'.join(str(e)
                                  for e in topLeftRate + rectSizeRate)
                currentPic = self.ui.listWidget.currentItem().text()

                idx = self.findSelectedBbox(currentPic, bboxId)
                print(idx)
                prevWidth = bbox.size().width()
                prevHeight = bbox.size().height()
                newWidth = rect.size().width()
                newHeight = rect.size().height()
                diffH = newHeight - prevHeight
                diffW = newWidth - prevWidth
                print(bbox.topLeft().x(), bbox.topLeft().y(),
                      newWidth, newHeight, diffH, diffW, rectItem.rectResized)
                if rectItem.rectResized == 4:  # handleTopRight
                    self.boundingBoxes[index].updateRectSize(
                        0, -diffH, newWidth, newHeight)

                    self.rect_items[index].updateRectSize(
                        0, -diffH, newWidth, newHeight)
                elif rectItem.rectResized == 3:  # handleBottomLeft
                    self.boundingBoxes[index].updateRectSize(
                        -diffW, 0, newWidth, newHeight)

                    self.rect_items[index].updateRectSize(
                        -diffW, 0, newWidth, newHeight)
                elif rectItem.rectResized == 2:
                    self.boundingBoxes[index].updateRectSize(
                        -diffW, -diffH, newWidth, newHeight)

                    self.rect_items[index].updateRectSize(
                        -diffW, -diffH, newWidth, newHeight)
                else:
                    self.boundingBoxes[index].updateRectSize(
                        0, 0, newWidth, newHeight)

                    self.rect_items[index].updateRectSize(
                        0, 0, newWidth, newHeight)

                self.boundingBoxes[index] = self.updateDatabase(
                    idx, self.boundingBoxes[index])
            else:
                print('not found')

    def updateDatabase(self, idx, newRectBbox):
        newRect = newRectBbox.rectF

        print(idx)
        if idx[0].size > 0:
            print('found it 3')
            index = idx[0][0]

            topLeftRate, rectSizeRate = self.calculateRectSizeRate(
                newRect.topLeft(), newRect.size())
            bboxId = '-'.join(str(e) for e in topLeftRate + rectSizeRate)
            print('-->', bboxId)
            if '--' in bboxId or topLeftRate[0] > 1 or topLeftRate[1] > 1:
                print('reverting back')
                newRectBbox = self.revertBboxChange(newRectBbox, index)
                return

            database.at[index, 'bbox_id'] = bboxId
            database.at[index, 'bbox_x'] = topLeftRate[0]
            database.at[index, 'bbox_y'] = topLeftRate[1]
            database.at[index, 'bbox_w'] = rectSizeRate[0]
            database.at[index, 'bbox_h'] = rectSizeRate[1]

            if self.isAutoSave():
                self.saveImageData()

            return newRectBbox

    def revertBboxChange(self, rectBox, index):
        topLeftdim = [float(database.at[index, 'bbox_x']*self.xSize),
                      float(database.at[index, 'bbox_y']*self.ySize)]
        rectSizedim = [float(database.at[index, 'bbox_w'])*self.xSize,
                       float(database.at[index, 'bbox_h'])*self.ySize]

        topLeft = QtCore.QPointF(
            topLeftdim[0], topLeftdim[1])
        rectSize = QtCore.QSizeF(
            rectSizedim[0], rectSizedim[1])
        rectF = QtCore.QRectF(
            topLeft, rectSize
        )
        rectBox = BoundingBox(rectF)
        return rectBox

    def saveDialogInfo(self):
        global database
        index, info, cords = self.categoryDialog.saveInfo()
        if index == -1:
            print('No data selected')
            return

        beginPos = self.boundingBoxes[index].rectF.topLeft()
        size = self.boundingBoxes[index].rectF.size()

        topLeftRate, rectSizeRate = [round(beginPos.x()/self.xSize, 14), round(beginPos.y()/self.ySize, 14)], [
            round(size.width()/self.xSize, 14), round(size.height()/self.ySize, 14)]

        currentPic = self.ui.listWidget.currentItem().text()

        bboxId = '-'.join(str(e) for e in topLeftRate + rectSizeRate)

        if info != '':
            topLeft, rectSize = [beginPos.x()/self.xSize, beginPos.y()/self.ySize], [
                size.width()/self.xSize, size.height()/self.ySize]
            # infoList = info.split(',')

            idx = self.findSelectedBbox(currentPic, bboxId)

            if not idx[0].size > 0:
                appendToDatabase(currentPic, bboxId,
                                 topLeft, rectSize, info, self.dir)
            else:
                database.at[idx[0][0], 'category'] = info

            if(self.isAutoSave()):
                self.saveImageData()
            print(database)

            rect_item = self.findRectItem(
                (beginPos.x(), beginPos.y()), (size.width(), size.height()))
            rect_item.setPen(
                QtGui.QPen(bboxFirstColor))
        else:
            self.deleteInfo(index, cords)

    def deleteDialogInfo(self):
        index, cords = self.categoryDialog.deleteInfo()

        if index == -1:
            return

        self.deleteInfo(index, cords)

    def deleteInfo(self, index, cords):
        global database
        print(index)

        beginPos = self.boundingBoxes[index].rectF.topLeft()
        size = self.boundingBoxes[index].rectF.size()

        topLeftRate, rectSizeRate = [round(beginPos.x()/self.xSize, 14), round(beginPos.y()/self.ySize, 14)], [
            round(size.width()/self.xSize, 14), round(size.height()/self.ySize, 14)]

        currentPic = self.ui.listWidget.currentItem().text()

        bboxId = '-'.join(str(e) for e in topLeftRate + rectSizeRate)
        print('-->', bboxId)
        topLeft, rectSize = [beginPos.x(), beginPos.y()], [
            size.width(), size.height()]
        boundingBox = self.findBoundingBox(beginPos)

        if boundingBox != None:

            del self.boundingBoxes[index]
            # print(len(self.rect_items))
            self.ui.graphicsView.removeRect(self.rect_items[index])
            self.rect_items.remove(self.rect_items[index])
            idx = self.findSelectedBbox(currentPic, bboxId)

            if idx[0].size > 0:
                database = database.drop(idx[0][0])
                database = database.reset_index(drop=True)
            if self.isAutoSave():
                self.saveImageData()
        else:
            print('not founded')

    def findSelectedBbox(self, imageId, bboxId):
        global database
        idx = np.where((database['image_id'] ==
                        imageId) & (database['bbox_id'] == bboxId))

        return idx

    def findImageIndex(self, imageName, imageDir):
        global imageInfoDf
        idx = np.where((imageInfoDf['image_id'] == imageName))

        return idx

    def findRectItem(self, topLeft, rectSize):
        print(topLeft, rectSize)
        for rect_item in self.rect_items:
            rectF = rect_item.rect()
            print(rectF.x(), rectF.y(), rectF.size().width(),
                  rectF.size().height())
            if(rectF.x() == topLeft[0] and rectF.y() == topLeft[1]):
                rectFSize = rectF.size()
                if(rectFSize.width() == rectSize[0] and rectFSize.height() == rectSize[1]):
                    return rect_item

        return None

    def calculateRectSizeRate(self, rectTopLeft, rectSize):
        return [round(rectTopLeft.x()/self.xSize, 14), round(rectTopLeft.y()/self.ySize, 14)], [
            round(rectSize.width()/self.xSize, 14), round(rectSize.height()/self.ySize, 14)]

    def saveImageData(self):
        database.to_csv(self.dataFileName, index=False)
        pass

        # TODO: 6. Remove data inside dataframe relevent to this picture
    def deleteAllInfo(self):
        if self.ui.listWidget.currentItem() is None:
            return
        deleteDataReleventToImage(self.ui.listWidget.currentItem().text())
        self.deleteImageStatus()

        if(self.isAutoSave()):
            self.saveImageData()

        self.refreshScene()

    def deleteImageStatus(self):
        global imageInfoDf, imageInfoFileName

        idx = self.findImageIndex(self.ui.listWidget.currentItem().text(), '')
        if idx[0].size > 0:
            imageInfoDf.drop(idx[0], axis=0, inplace=True)
            imageInfoDf = imageInfoDf.reset_index(drop=True)
            self.ui.listWidget.currentItem().setBackground(whiteColor)
            imageInfoDf.to_csv(imageInfoFileName, index=False)

        print(imageInfoDf)

    def isAutoSave(self):
        return self.ui.AutoSaveCheckbox.isChecked()


def deleteDataReleventToImage(ImageName):
    global database

    idx = np.where(database['image_id'] == ImageName)
    if idx[0].size > 0:
        database.drop(idx[0], axis=0, inplace=True)
        database = database.reset_index(drop=True)

    print(database)
    pass


def appendToDatabase(imageId, bboxId, center, size, categorList, dir):
    global database
    new_row = {'image_id': [imageId], 'bbox_id': [bboxId],
               'bbox_x': [center[0]], 'bbox_y': [center[1]], 'bbox_w': [size[0]], 'bbox_h': [size[1]], 'category': [categorList], 'root_dir': [dir]}
    df = pd.DataFrame.from_dict(new_row)

    database = pd.concat([database, df], ignore_index=True)


def appendToImageInfo(imageName, dir, status):
    global imageInfoDf
    new_row = {'image_id': [imageName],
               'image_dir': [dir], 'status': [status]}
    df = pd.DataFrame.from_dict(new_row)

    imageInfoDf = pd.concat([imageInfoDf, df], ignore_index=True)


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

    return QtCore.QPointF(x, y)


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
