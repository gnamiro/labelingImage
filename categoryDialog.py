# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'categoryDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# from main import database


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(639, 505)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText('Category name ...')
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.pushButton_3)
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.gridLayout.addLayout(self.formLayout, 1, 1, 1, 1)
        self.listView = QtWidgets.QListView(Dialog)
        self.listView.setObjectName("listView")
        self.gridLayout.addWidget(self.listView, 0, 0, 2, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "save"))
        self.pushButton_2.setText(_translate("Dialog", "cancel"))
        self.pushButton_3.setText(_translate("Dialog", "Add Category to List"))
        self.label.setText(_translate("Dialog", "Enter category name"))


class CategoryApplication(QtWidgets.QDialog):
    dialogStatus = QtCore.pyqtSignal(int, str, QtCore.QPoint, QtCore.QPoint)
    sendMessage = QtCore.pyqtSignal(int, str, QtCore.QPoint, QtCore.QPoint)

    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
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
        # TODO: check if there exists name or not.
        newCategory = self.ui.lineEdit.text()
        # print(newCategory)
        if(newCategory != ''):
            item = self.createCategoryItem(newCategory)
            self.model.appendRow(item)
        self.ui.lineEdit.setText('')

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
        infoMessage = ','.join(str(e) for e in self.info)
        self.uncheckItems()
        self.sendMessage.emit(1, infoMessage, self.cords[0], self.cords[1])
        self.close()

    def deleteInfo(self):
        self.info = []
        self.uncheckItems()
        self.dialogStatus.emit(0, '', self.cords[0], self.cords[1])
        self.close()

    def uncheckItems(self):
        for index in range(self.model.rowCount()):
            item = self.model.item(index)
            if item.isCheckable():
                item.setCheckState(QtCore.Qt.Unchecked)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
