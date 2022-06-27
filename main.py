from cmath import rect
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import pathlib
current_directory = str(pathlib.Path(__file__).parent.absolute())
# from retinal import PhotoViewer
# TODO: 1. import logging
# TODO: 3. remove all rectangles when changing to other image


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(1020, 747)
        self.gridLayout = QtWidgets.QGridLayout(dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = PhotoViewer(dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(17)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMinimumSize(QtCore.QSize(589, 0))
        self.graphicsView.setMaximumSize(QtCore.QSize(16777215, 160000))
        self.graphicsView.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.graphicsView.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 2, 0, 4, 3)
        self.label = QtWidgets.QLabel(dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font-weight: 500")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 35))
        self.pushButton_3.setMaximumSize(QtCore.QSize(150, 39))
        self.pushButton_3.setBaseSize(QtCore.QSize(150, 35))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(
            self.pushButton_3, 0, 3, 1, 1, QtCore.Qt.AlignRight)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setMaximumSize(QtCore.QSize(100, 20))
        self.label_2.setStyleSheet("font-weight: 599")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(
            self.label_2, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.listWidget = QtWidgets.QListWidget(dialog)
        self.listWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(220, 538))
        self.listWidget.setMaximumSize(QtCore.QSize(256, 16777215))
        self.listWidget.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(
            self.listWidget, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 3, 3, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(
            QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(111, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(162, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(
            self.pushButton_2, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.pushButton = QtWidgets.QPushButton(dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(89, 23))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(
            self.pushButton, 0, QtCore.Qt.AlignBottom)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Retinal Lesion Annotator"))
        dialog.setWindowIcon(QtGui.QIcon(current_directory+'/images/logo.jpg'))
        self.label.setText(_translate("dialog", "Retinal Lesion Annotator"))
        self.pushButton_3.setText(_translate("dialog", "select folder"))
        self.label_2.setText(_translate("dialog", "Folder content:"))
        self.pushButton_2.setText(_translate("dialog", "ذخیره"))
        self.pushButton.setText(_translate("dialog", "لغو"))
        # self.label_3.setText(_translate("dialog", "TextLabel"))
        # _translate = QtCore.QCoreApplication.translate
        # dialog.setWindowTitle(_translate("dialog", "Retinal Lesion Annotator"))
        # dialog.setWindowIcon(QtGui.QIcon(current_directory+'/images/logo.jpg'))
        # self.pushButton_3.setText(_translate("dialog", "Select image folder"))
        # self.label_2.setText(_translate("dialog", "محتوای پوشه عکس‌ها"))
        # self.pushButton_2.setText(_translate("dialog", "save image content"))
        # self.pushButton.setText(_translate("dialog", "cancel"))
        # self.label.setText(_translate(
        #     "dialog", "Retinal Lesion Annotator"))
        pixmap = QtGui.QPixmap(current_directory+'/images/logo.jpg')
        pixmapRescaled = pixmap.scaled(
            35, 35, QtCore.Qt.KeepAspectRatio)
        self.label_3.setPixmap(pixmapRescaled)


class PhotoViewer(QtWidgets.QGraphicsView):
    photoClicked = QtCore.pyqtSignal(QtCore.QPoint)
    photoReleased = QtCore.pyqtSignal(QtCore.QPoint)
    photoMoved = QtCore.pyqtSignal(QtCore.QPoint)

    def __init__(self, parent):
        super(PhotoViewer, self).__init__(parent)
        self._zoom = 0
        self._empty = True
        self._scene = QtWidgets.QGraphicsScene(self)
        self._photo = QtWidgets.QGraphicsPixmapItem()
        self._scene.addItem(self._photo)
        self.setScene(self._scene)
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(250, 250, 250)))
        self.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.begin, self.destination = QtCore.QPoint(), QtCore.QPoint()

    def removeRects(self, rectsList):
        print(len(rectsList))
        if(rectsList != []):
            for rect in rectsList:
                self._scene.removeItem(rect)

    def mousePressEvent(self, event):
        if self._photo.isUnderMouse():
            if self.dragMode() == QtWidgets.QGraphicsView.NoDrag and event.button() == QtCore.Qt.LeftButton:
                self.begin = event.pos()
                self.destination = self.begin
                self.photoClicked.emit(self.mapToScene(self.begin).toPoint())
                self.update()

    def mouseMoveEvent(self, event):
        if self._photo.isUnderMouse() and (event.buttons() & QtCore.Qt.LeftButton):
            self.destination = event.pos()
            self.photoMoved.emit(
                self.mapToScene(self.destination).toPoint())
            # self.update()
            # print(self.destination, self.begin)

        super(PhotoViewer, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self._photo.isUnderMouse() and (event.button() & QtCore.Qt.LeftButton):
            print('hello')
            self.photoReleased.emit(
                self.mapToScene(self.destination).toPoint())
            # rect = QtCore.QRect(self.begin, self.destination)
            # painter = QtGui.QPainter(self._photo.pixmap())
            # painter.drawRect(rect.normalized())

            # self.begin, self.destination = QtCore.QPoint(), QtCore.QPoint()
            self.update()

    def hasPhoto(self):
        return not self._empty

    def fitInView(self, scale=True):
        rect = QtCore.QRectF(self._photo.pixmap().rect())
        if not rect.isNull():
            self.setSceneRect(rect)
            if self.hasPhoto():
                unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
                self.scale(1 / unity.width(), 1 / unity.height())
                viewrect = self.viewport().rect()
                scenerect = self.transform().mapRect(rect)
                factor = min(viewrect.width() / scenerect.width(),
                             viewrect.height() / scenerect.height())
                self.scale(factor, factor)
            self._zoom = 0

    def setPhoto(self, pixmap=None):
        self._zoom = 0
        if pixmap and not pixmap.isNull():
            self._empty = False
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
            self._photo.setPixmap(pixmap)
        else:
            self._empty = True
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
            self._photo.setPixmap(QtGui.QPixmap())
        self.fitInView()

    def wheelEvent(self, event):
        if self.hasPhoto():
            if event.angleDelta().y() > 0:
                factor = 1.25
                self._zoom += 1
            else:
                factor = 0.8
                self._zoom -= 1
            if self._zoom > 0:
                self.scale(factor, factor)
            elif self._zoom == 0:
                self.fitInView()
            else:
                self._zoom = 0

    def toggleDragMode(self):
        self.setDragMode(QtWidgets.QGraphicsView.NoDrag)


class RetinalApplication(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.dir = None
        self.images = []

        self.rects = []
        self.ui = Ui_dialog()
        self.ui.setupUi(self)

        self.begin, self.destination = QtCore.QPoint(), QtCore.QPoint()

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

            # self.update()
            self.begin, self.destination = QtCore.QPoint(), QtCore.QPoint()


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
