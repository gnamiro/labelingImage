# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'retinal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PhotoViewer import PhotoViewer
import pathlib
current_directory = str(pathlib.Path(__file__).parent.absolute())


class Ui_Dialog(object):
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
        self.pushButton_2.setText(_translate("dialog", "save"))
        self.pushButton.setText(_translate("dialog", "delete"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
