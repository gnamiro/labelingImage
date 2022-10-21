from PyQt5 import QtCore, QtGui, QtWidgets


class GraphicsScene(QtWidgets.QGraphicsScene):
    itemResizing = QtCore.pyqtSignal(object)


class PhotoViewer(QtWidgets.QGraphicsView):
    photoClicked = QtCore.pyqtSignal(QtCore.QPointF)
    photoReleased = QtCore.pyqtSignal(QtCore.QPointF)
    photoMoved = QtCore.pyqtSignal(QtCore.QPointF)

    def __init__(self, parent):
        super(PhotoViewer, self).__init__(parent)
        self._zoom = 0
        self._empty = True
        self._scene = GraphicsScene(self)
        self._photo = QtWidgets.QGraphicsPixmapItem()
        self._scene.addItem(self._photo)
        self.setScene(self._scene)
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(250, 250, 250)))
        self.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.begin, self.destination = QtCore.QPointF(), QtCore.QPointF()

    def removeRects(self, rectsList):
        # print(len(rectsList))
        if(len(rectsList) != 0):
            for rect in rectsList:
                self._scene.removeItem(rect)

    def removeRect(self, rectItem):
        self._scene.removeItem(rectItem)

    def mousePressEvent(self, event):
        if self._photo.isUnderMouse() and event.button() == QtCore.Qt.LeftButton:
            self.begin = event.pos()
            self.destination = self.begin
            self.photoClicked.emit(self.mapToScene(self.begin))
            # if self.dragMode() == QtWidgets.QGraphicsView.NoDrag:
            #     self.update()

        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._photo.isUnderMouse() and (event.buttons() & QtCore.Qt.LeftButton):
            self.destination = event.pos()

            self.photoMoved.emit(
                self.mapToScene(self.destination))
            # self.update()
            # print(self.destination, self.begin)

        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        if self._photo.isUnderMouse() and (event.button() & QtCore.Qt.LeftButton):
            self.destination = event.pos()
            self.photoReleased.emit(
                self.mapToScene(self.destination))
            # if self.dragMode() == QtWidgets.QGraphicsView.NoDrag:
            #     # rect = QtCore.QRect(self.begin, self.destination)
            #     # painter = QtGui.QPainter(self._photo.pixmap())
            #     # painter.drawRect(rect.normalized())

            #     # self.begin, self.destination = QtCore.QPoint(), QtCore.QPoint()
            #     self.update()

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
        print(self.dragMode())
        if self.dragMode() == QtWidgets.QGraphicsView.ScrollHandDrag:
            self.setDragMode(QtWidgets.QGraphicsView.NoDrag)
        elif self.dragMode() == QtWidgets.QGraphicsView.NoDrag:
            self.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)

    def resetDragMode(self):
        self.setDragMode(QtWidgets.QGraphicsView.NoDrag)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 300, 800, 600)
    window.show()
    sys.exit(app.exec_())
