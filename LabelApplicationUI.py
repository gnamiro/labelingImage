# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'retinal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PhotoViewer import PhotoViewer
import pathlib
import os
import sys
current_directory = str(pathlib.Path(__file__).parent.absolute())


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(1084, 810)
        self.gridLayout = QtWidgets.QGridLayout(dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(35, 35))
        self.label_3.setStyleSheet("")
        self.label_3.setText("")
        logo_image = resource_path("Images/logo.jpg")
        self.label_3.setPixmap(QtGui.QPixmap(logo_image))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
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
        self.horizontalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignLeft)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
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
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(
            QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.OpenFolderButton = QtWidgets.QPushButton(dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.OpenFolderButton.sizePolicy().hasHeightForWidth())
        self.OpenFolderButton.setSizePolicy(sizePolicy)
        self.OpenFolderButton.setMinimumSize(QtCore.QSize(132, 36))
        self.OpenFolderButton.setMaximumSize(QtCore.QSize(110, 59))
        self.OpenFolderButton.setBaseSize(QtCore.QSize(150, 35))
        self.OpenFolderButton.setStyleSheet("")
        icon = QtGui.QIcon()
        icon_image = resource_path("Images/OpenFolder.png")
        icon.addPixmap(QtGui.QPixmap(icon_image),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OpenFolderButton.setIcon(icon)
        self.OpenFolderButton.setIconSize(QtCore.QSize(37, 24))
        self.OpenFolderButton.setObjectName("OpenFolderButton")
        self.horizontalLayout_3.addWidget(self.OpenFolderButton)
        self.DataFilePathButton = QtWidgets.QPushButton(dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.DataFilePathButton.sizePolicy().hasHeightForWidth())
        self.DataFilePathButton.setSizePolicy(sizePolicy)
        self.DataFilePathButton.setMinimumSize(QtCore.QSize(146, 36))
        icon1 = QtGui.QIcon()
        icon1_image = resource_path("Images/dataa.jpg")
        icon1.addPixmap(QtGui.QPixmap(icon1_image),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DataFilePathButton.setIcon(icon1)
        self.DataFilePathButton.setIconSize(QtCore.QSize(32, 20))
        self.DataFilePathButton.setObjectName("DataFilePathButton")
        self.horizontalLayout_3.addWidget(self.DataFilePathButton)
        self.SaveButton = QtWidgets.QPushButton(dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.SaveButton.sizePolicy().hasHeightForWidth())
        self.SaveButton.setSizePolicy(sizePolicy)
        self.SaveButton.setMinimumSize(QtCore.QSize(129, 36))
        self.SaveButton.setMaximumSize(QtCore.QSize(110, 89))
        self.SaveButton.setStyleSheet("margin-left: ")
        icon2 = QtGui.QIcon()
        icon2_image = resource_path('Images/save1.jpg')
        icon2.addPixmap(QtGui.QPixmap(icon2_image),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveButton.setIcon(icon2)
        self.SaveButton.setIconSize(QtCore.QSize(37, 20))
        self.SaveButton.setAutoDefault(True)
        self.SaveButton.setDefault(False)
        self.SaveButton.setFlat(False)
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout_3.addWidget(
            self.SaveButton, 0, QtCore.Qt.AlignBottom)
        self.DeleteButton = QtWidgets.QPushButton(dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.DeleteButton.sizePolicy().hasHeightForWidth())
        self.DeleteButton.setSizePolicy(sizePolicy)
        self.DeleteButton.setMinimumSize(QtCore.QSize(135, 36))
        self.DeleteButton.setMaximumSize(QtCore.QSize(100, 23))
        icon3 = QtGui.QIcon()
        icon3_image = resource_path("Images/recDel.jpg")
        icon3.addPixmap(QtGui.QPixmap(icon3_image),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeleteButton.setIcon(icon3)
        self.DeleteButton.setIconSize(QtCore.QSize(40, 28))
        self.DeleteButton.setObjectName("DeleteButton")
        self.horizontalLayout_3.addWidget(
            self.DeleteButton, 0, QtCore.Qt.AlignBottom)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.dragModeButtton = QtWidgets.QPushButton(dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dragModeButtton.sizePolicy().hasHeightForWidth())
        self.dragModeButtton.setSizePolicy(sizePolicy)
        self.dragModeButtton.setMinimumSize(QtCore.QSize(104, 36))
        self.dragModeButtton.setObjectName("dragModeButtton")
        self.horizontalLayout.addWidget(self.dragModeButtton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 4, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.AutoSaveCheckbox = QtWidgets.QCheckBox(dialog)
        self.AutoSaveCheckbox.setStyleSheet("font-weight: 500")
        self.AutoSaveCheckbox.setIconSize(QtCore.QSize(55, 47))
        self.AutoSaveCheckbox.setObjectName("AutoSaveCheckbox")
        self.verticalLayout.addWidget(self.AutoSaveCheckbox)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
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
        self.gridLayout.addWidget(self.graphicsView, 2, 1, 2, 2)
        self.line_5 = QtWidgets.QFrame(dialog)
        self.line_5.setMidLineWidth(1)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 1, 0, 1, 6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.categoyrEdit = QtWidgets.QLineEdit(dialog)
        self.categoyrEdit.setObjectName("categoyrEdit")
        self.verticalLayout_5.addWidget(self.categoyrEdit)
        self.addCategoryButton = QtWidgets.QPushButton(dialog)
        self.addCategoryButton.setObjectName("addCategoryButton")
        self.verticalLayout_5.addWidget(self.addCategoryButton)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.categoryListView = QtWidgets.QListView(dialog)
        self.categoryListView.setObjectName("categoryListView")
        self.verticalLayout_3.addWidget(self.categoryListView)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cancelCategoryButton = QtWidgets.QPushButton(dialog)
        self.cancelCategoryButton.setObjectName("cancelCategoryButton")
        self.horizontalLayout_4.addWidget(self.cancelCategoryButton)
        self.saveCategoryButton = QtWidgets.QPushButton(dialog)
        self.saveCategoryButton.setObjectName("saveCategoryButton")
        self.horizontalLayout_4.addWidget(self.saveCategoryButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.completeImageButton = QtWidgets.QPushButton(dialog)
        self.completeImageButton.setObjectName("completeImageButton")
        self.verticalLayout_4.addWidget(self.completeImageButton)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 5, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Retinal Lesion Annotator"))
        # TODO: 1. ADD resource path of logo image to icon title
        logo_image = resource_path("Images/logo.jpg")
        dialog.setWindowIcon(QtGui.QIcon(logo_image))
        self.label.setText(_translate("dialog", "Retinal Lesion Annotator"))
        self.label_2.setText(_translate("dialog", "Folder content:"))
        self.OpenFolderButton.setText(
            _translate("dialog", "Open Image folder"))
        self.DataFilePathButton.setText(
            _translate("dialog", "Choose Data File Path"))
        self.SaveButton.setText(_translate("dialog", " Save Image Info"))
        self.DeleteButton.setText(_translate("dialog", "Delete Image Info"))
        self.dragModeButtton.setText(_translate("dialog", "DragMode"))
        self.AutoSaveCheckbox.setText(
            _translate("dialog", "AutoSave Image Info"))
        self.label_4.setText(_translate("dialog", "Enter category name"))
        self.addCategoryButton.setText(
            _translate("dialog", "Add Category to List"))
        self.cancelCategoryButton.setText(_translate("dialog", "Cancel"))
        self.saveCategoryButton.setText(_translate("dialog", "Save"))
        self.completeImageButton.setText(_translate("dialog", "Done"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
