import sys

from PyQt5.QtCore import Qt, QRectF, QPointF, pyqtSignal
from PyQt5.QtGui import QBrush, QPainterPath, QPainter, QColor, QPen, QPixmap
from PyQt5.QtWidgets import QGraphicsRectItem, QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem


class GraphicsRectItem(QGraphicsRectItem):
    itemInteractiveChange = pyqtSignal(QRectF, QRectF)

    handleTopLeft = 1
    handleTopMiddle = 2
    handleTopRight = 3
    handleMiddleLeft = 4
    handleMiddleRight = 5
    handleBottomLeft = 6
    handleBottomMiddle = 7
    handleBottomRight = 8

    handleSize = +8.0
    handleSpace = -4.0

    rectResized = 0

    rectThreshold = +24.0

    handleCursors = {
        handleTopLeft: Qt.SizeFDiagCursor,
        handleTopMiddle: Qt.SizeVerCursor,
        handleTopRight: Qt.SizeBDiagCursor,
        handleMiddleLeft: Qt.SizeHorCursor,
        handleMiddleRight: Qt.SizeHorCursor,
        handleBottomLeft: Qt.SizeBDiagCursor,
        handleBottomMiddle: Qt.SizeVerCursor,
        handleBottomRight: Qt.SizeFDiagCursor,
    }

    def __init__(self, *args):
        super().__init__(*args)

        self.handles = {}
        self.handleSelected = None
        self.mousePressPos = None
        self.mousePressRect = None
        self.setAcceptHoverEvents(True)
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
        self.setFlag(QGraphicsItem.ItemIsFocusable, True)
        self.selected = 0

        self.handleRectSizeThreshold = {
            self.handleTopLeft: self.TL,
            self.handleTopMiddle: self.TM,
            self.handleTopRight: self.TR,
            self.handleMiddleLeft: self.ML,
            self.handleMiddleRight: self.MR,
            self.handleBottomLeft: self.BL,
            self.handleBottomMiddle: self.BM,
            self.handleBottomRight: self.BR,
        }

        # assigning copy of rectF
        self._rectF = QRectF(args[0].topLeft(), args[0].size())
        # self._rectF = None
        self.updateHandlesPos()

    def handleAt(self, point):
        for k, v, in self.handles.items():
            if v.contains(point):
                return k
        return None

    def hoverMoveEvent(self, moveEvent):
        # print('69heelo')
        # Executed when the mouse moves over the shape (NOT PRESSED).

        if self.isSelected():
            handle = self.handleAt(moveEvent.pos())
            cursor = Qt.ArrowCursor if handle is None else self.handleCursors[handle]
            self.setCursor(cursor)
        super().hoverMoveEvent(moveEvent)

    def hoverLeaveEvent(self, moveEvent):
        # print('79heelo')
        # Executed when the mouse leaves the shape (NOT PRESSED).

        self.setCursor(Qt.ArrowCursor)
        super().hoverLeaveEvent(moveEvent)

    def mousePressEvent(self, mouseEvent):
        # Executed when the mouse is pressed on the item.
        self.handleSelected = self.handleAt(mouseEvent.pos())
        self.rectResized = 0
        if self.handleSelected:
            self.mousePressPos = mouseEvent.pos()
            self.mousePressRect = self.boundingRect()
        super().mousePressEvent(mouseEvent)

    def mouseMoveEvent(self, mouseEvent):
        # Executed when the mouse is being moved over the item while being pressed.
        if self.handleSelected is not None:
            self.interactiveResize(mouseEvent.pos())
        else:
            self.rectResized = 0
            super().mouseMoveEvent(mouseEvent)

    def mouseReleaseEvent(self, mouseEvent):
        # Executed when the mouse is released from the item.

        super().mouseReleaseEvent(mouseEvent)
        # print('108heelo')
        self.handleSelected = None
        self.mousePressPos = None
        self.mousePressRect = None
        self.update()
        self.scene().itemResizing.emit(self)

    def boundingRect(self):
        # Returns the bounding rect of the shape (including the resize handles).

        o = self.handleSize + self.handleSpace
        return self.rect().adjusted(-o, -o, o, o)

    def updateRectPos(self, diffX, diffY):
        self._rectF.translate(diffX, diffY)

    def updateRectSize(self, diffX, diffY, width, height):
        self._rectF.setHeight(height)
        self._rectF.setWidth(width)
        self.updateRectPos(diffX, diffY)

    def updateHandlesPos(self):
        # Update current resize handles according to the shape size and position.

        s = self.handleSize
        # print(s)
        b = self.boundingRect()
        # print(b.left(), b.top())
        self.handles[self.handleTopLeft] = QRectF(b.left(), b.top(), s, s)
        self.handles[self.handleTopMiddle] = QRectF(
            b.center().x() - s / 2, b.top(), s, s)
        self.handles[self.handleTopRight] = QRectF(
            b.right() - s, b.top(), s, s)
        self.handles[self.handleMiddleLeft] = QRectF(
            b.left(), b.center().y() - s / 2, s, s)
        self.handles[self.handleMiddleRight] = QRectF(
            b.right() - s, b.center().y() - s / 2, s, s)
        self.handles[self.handleBottomLeft] = QRectF(
            b.left(), b.bottom() - s, s, s)
        self.handles[self.handleBottomMiddle] = QRectF(
            b.center().x() - s / 2, b.bottom() - s, s, s)
        self.handles[self.handleBottomRight] = QRectF(
            b.right() - s, b.bottom() - s, s, s)

    def interactiveResize(self, mousePos):
        # Perform shape interactive resize.

        offset = self.handleSize + self.handleSpace
        boundingRect = self.boundingRect()
        rect = self.rect()
        diff = QPointF(0, 0)

        self.prepareGeometryChange()

        if self.handleSelected == self.handleTopLeft:
            self.rectResized = 2
            fromX = self.mousePressRect.left()
            fromY = self.mousePressRect.top()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            boundingRect.setLeft(toX)
            boundingRect.setTop(toY)

            rect = self.handleRectSizeThreshold[self.handleTopLeft](
                boundingRect, rect, offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleTopMiddle:
            self.rectResized = 2
            fromY = self.mousePressRect.top()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setY(toY - fromY)
            boundingRect.setTop(toY)

            rect = self.handleRectSizeThreshold[self.handleTopMiddle](
                boundingRect, rect, offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleTopRight:
            self.rectResized = 1  # TODO

            fromX = self.mousePressRect.right()
            fromY = self.mousePressRect.top()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            if abs(diff.y()) > 0.004:
                self.rectResized = 4
            boundingRect.setRight(toX)
            boundingRect.setTop(toY)

            rect = self.handleRectSizeThreshold[self.handleTopRight](
                boundingRect, rect, offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleMiddleLeft:
            self.rectResized = 2
            fromX = self.mousePressRect.left()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            diff.setX(toX - fromX)
            boundingRect.setLeft(toX)

            rect = self.handleRectSizeThreshold[self.handleMiddleLeft](
                boundingRect, rect, offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleMiddleRight:
            self.rectResized = 1
            fromX = self.mousePressRect.right()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            diff.setX(toX - fromX)
            boundingRect.setRight(toX)

            rect = self.handleRectSizeThreshold[self.handleMiddleRight](
                boundingRect, rect, offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleBottomLeft:
            print('hey')
            self.rectResized = 1  # TODO

            fromX = self.mousePressRect.left()
            fromY = self.mousePressRect.bottom()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            if abs(diff.x()) > 0.004:
                self.rectResized = 3
            boundingRect.setLeft(toX)
            boundingRect.setBottom(toY)

            rect = self.handleRectSizeThreshold[self.handleBottomLeft](
                boundingRect, rect, offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleBottomMiddle:
            self.rectResized = 1
            fromY = self.mousePressRect.bottom()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setY(toY - fromY)
            boundingRect.setBottom(toY)

            rect = self.handleRectSizeThreshold[self.handleBottomMiddle](
                boundingRect, rect, offset)
            self.setRect(rect)

        elif self.handleSelected == self.handleBottomRight:
            self.rectResized = 1
            fromX = self.mousePressRect.right()
            fromY = self.mousePressRect.bottom()
            toX = fromX + mousePos.x() - self.mousePressPos.x()
            toY = fromY + mousePos.y() - self.mousePressPos.y()
            diff.setX(toX - fromX)
            diff.setY(toY - fromY)
            boundingRect.setRight(toX)
            boundingRect.setBottom(toY)

        rect = self.handleRectSizeThreshold[self.handleBottomRight](
            boundingRect, rect, offset)
        self.setRect(rect)

        print(self.rect().topLeft().x(), self.rect().topLeft().y(),
              self.rect().size().width(), self.rect().size().height())

        self.updateHandlesPos()

    def checkPos2Pos(fromPos, toPos):
        pass

    def TL(self, boundingRect, rect, offset):
        # offset = self.handleSize + self.handleSpace
        if boundingRect.right() - boundingRect.left() > self.rectThreshold:
            rect.setLeft(boundingRect.left() + offset)
        else:
            rect.setLeft(boundingRect.right() - self.rectThreshold)

        if boundingRect.bottom() - boundingRect.top() > self.rectThreshold:
            rect.setTop(boundingRect.top() + offset)
        else:
            rect.setTop(boundingRect.bottom() - self.rectThreshold)

        return rect

    def TM(self, boundingRect, rect, offset):
        if boundingRect.bottom() - boundingRect.top() > self.rectThreshold:
            rect.setTop(boundingRect.top() + offset)
        else:
            rect.setTop(boundingRect.bottom() - self.rectThreshold)

        return rect

    def TR(self, boundingRect, rect, offset):
        # offset = self.handleSize + self.handleSpace
        if boundingRect.right() - boundingRect.left() > self.rectThreshold:
            rect.setRight(boundingRect.right() - offset)
        else:
            rect.setRight(boundingRect.left() + self.rectThreshold)

        if boundingRect.bottom() - boundingRect.top() > self.rectThreshold:
            rect.setTop(boundingRect.top() + offset)
        else:
            rect.setTop(boundingRect.bottom() - self.rectThreshold)

        return rect

    def ML(self, boundingRect, rect, offset):
        if boundingRect.right() - boundingRect.left() > self.rectThreshold:
            rect.setLeft(boundingRect.left() + offset)
        else:
            rect.setLeft(boundingRect.right() - self.rectThreshold)

        return rect

    def MR(self, boundingRect, rect, offset):
        if boundingRect.right() - boundingRect.left() > self.rectThreshold:
            rect.setRight(boundingRect.right() - offset)
        else:
            rect.setRight(boundingRect.left() + self.rectThreshold)

        return rect

    def BL(self, boundingRect, rect, offset):
        if boundingRect.right() - boundingRect.left() > self.rectThreshold:
            rect.setLeft(boundingRect.left() + offset)
        else:
            rect.setLeft(boundingRect.right() - self.rectThreshold)

        if boundingRect.bottom() - boundingRect.top() > self.rectThreshold:
            rect.setBottom(boundingRect.bottom() - offset)
        else:
            rect.setBottom(boundingRect.top() + self.rectThreshold)

        return rect

    def BM(self, boundingRect, rect, offset):
        if boundingRect.bottom() - boundingRect.top() > self.rectThreshold:
            rect.setBottom(boundingRect.bottom() - offset)
        else:
            rect.setBottom(boundingRect.top() + self.rectThreshold)

        return rect

    def BR(self, boundingRect, rect, offset):
        if boundingRect.right() - boundingRect.left() > self.rectThreshold:
            rect.setRight(boundingRect.right() - offset)
        else:
            rect.setRight(boundingRect.left() + self.rectThreshold)

        if boundingRect.bottom() - boundingRect.top() > self.rectThreshold:
            rect.setBottom(boundingRect.bottom() - offset)
        else:
            rect.setBottom(boundingRect.top() + self.rectThreshold)

        return rect

    def shape(self):
        # Returns the shape of this item as a QPainterPath in local coordinates.

        path = QPainterPath()
        path.addRect(self.rect())
        if self.isSelected():
            for shape in self.handles.values():
                path.addEllipse(shape)
        return path

    # def paint(self, painter, option, widget=None):
    #     # Paint the node in the graphic view.

    #     # painter.setBrush(QBrush(QColor(255, 255, 255, 255)))
    #     if self.selected == False:
    #         painter.setPen(QPen(QColor(0, 0, 0), 1.0, Qt.SolidLine))
    #     else:
    #         painter.setPen(QPen(QColor(255, 0, 0), 1.0, Qt.SolidLine))

    #     painter.drawRect(self.rect())

        # painter.setRenderHint(QPainter.Antialiasing)
        # painter.setBrush(QBrush(QColor(255, 0, 0, 255)))
        # painter.setPen(QPen(QColor(0, 0, 0, 255), 1.0,
        #                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        # if self.selected == 1:
        #     for handle, rect in self.handles.items():
        #         if self.handleSelected is None or handle == self.handleSelected:
        #             painter.drawEllipse(rect)

    def toggleRectSelection(self):
        self.selected = not self.selected


def main():

    app = QApplication(sys.argv)

    grview = QGraphicsView()
    grview.setDragMode(QGraphicsView.ScrollHandDrag)
    scene = QGraphicsScene()
    scene.setSceneRect(0, 0, 680, 459)

    grview.setScene(scene)

    item = GraphicsRectItem(0, 0, 300, 150)
    scene.addItem(item)

    item = GraphicsRectItem(400, 200, 100, 150)
    scene.addItem(item)

    grview.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
    grview.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
