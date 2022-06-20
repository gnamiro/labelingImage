# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'retinal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def __init__(self) -> None:
        self.dir = None

    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(762, 685)
        self.gridLayout_2 = QtWidgets.QGridLayout(dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setMaximumSize(QtCore.QSize(16777215, 160000))
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 0, 3, 1)
        self.label = QtWidgets.QLabel(dialog)
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
        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)

        self.pushButton_3.clicked.connect(self.chooseFolder)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.pushButton_2 = QtWidgets.QPushButton(dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(
            self.pushButton_2, 0, QtCore.Qt.AlignBottom)

        self.pushButton = QtWidgets.QPushButton(dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(
            self.pushButton, 0, QtCore.Qt.AlignBottom)

        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)

        self.listWidget = QtWidgets.QListWidget(dialog)
        self.listWidget.setMinimumSize(QtCore.QSize(200, 350))
        self.listWidget.setMaximumSize(QtCore.QSize(200, 387))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(
            self.listWidget, 1, 1, 2, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))
        self.label.setText(_translate(
            "dialog", "برنامه تعیین ناهنجاری در عکس‌های مربوط به چشم"))
        self.pushButton_3.setText(_translate("dialog", "انتخاب پوشه عکس‌ها"))
        self.pushButton_2.setText(_translate("dialog", "ذخیره"))
        self.pushButton.setText(_translate("dialog", "لغو"))

    def chooseFolder(self):
        self.dir = QtWidgets.QFileDialog.getExistingDirectory(
            None, 'Select a folder:', 'C:\\', QtWidgets.QFileDialog.ShowDirsOnly)

        print(self.dir)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
