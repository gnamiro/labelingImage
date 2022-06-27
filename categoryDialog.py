# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'categoryDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


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
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.model = QtGui.QStandardItemModel()

        self.ui.listView.setModel(self.model)

        # signal connections
        self.ui.pushButton_3.clicked.connect(self.addNewCategory)

    def addNewCategory(self):
        newCategory = self.ui.lineEdit.text()
        # print(newCategory)
        item = self.createCategoryItem(newCategory)
        self.model.appendRow(item)

    def createCategoryItem(self, categoryName):
        item = QtGui.QStandardItem(categoryName)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        item.setData(QtCore.QVariant(QtCore.Qt.Unchecked),
                     QtCore.Qt.CheckStateRole)

        return item


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
