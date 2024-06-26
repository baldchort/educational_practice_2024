# Form implementation generated from reading ui file 'handInputDialogUI.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_HandInputDialog(object):
    def setupUi(self, HandInputDialog):
        HandInputDialog.setObjectName("HandInputDialog")
        HandInputDialog.resize(280, 391)
        HandInputDialog.setSizeGripEnabled(False)
        HandInputDialog.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(HandInputDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelButton = QtWidgets.QPushButton(parent=HandInputDialog)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.doneButton = QtWidgets.QPushButton(parent=HandInputDialog)
        self.doneButton.setObjectName("doneButton")
        self.horizontalLayout.addWidget(self.doneButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.amountLabel = QtWidgets.QLabel(parent=HandInputDialog)
        self.amountLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.amountLabel.setObjectName("amountLabel")
        self.verticalLayout.addWidget(self.amountLabel)
        self.AmountLineEdit = QtWidgets.QLineEdit(parent=HandInputDialog)
        self.AmountLineEdit.setObjectName("AmountLineEdit")
        self.verticalLayout.addWidget(self.AmountLineEdit)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=HandInputDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.tableWidget = QtWidgets.QTableWidget(parent=HandInputDialog)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.retranslateUi(HandInputDialog)
        QtCore.QMetaObject.connectSlotsByName(HandInputDialog)

    def retranslateUi(self, HandInputDialog):
        _translate = QtCore.QCoreApplication.translate
        HandInputDialog.setWindowTitle(_translate("HandInputDialog", "Ручной ввод"))
        self.cancelButton.setText(_translate("HandInputDialog", "Назад"))
        self.doneButton.setText(_translate("HandInputDialog", "Готово"))
        self.amountLabel.setText(_translate("HandInputDialog", "Введите количество предметов"))
        self.AmountLineEdit.setPlaceholderText(_translate("HandInputDialog", "Кол-во предметов"))
        self.label_2.setText(_translate("HandInputDialog", "Введите соответсвующую информацию"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("HandInputDialog", "Вес"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("HandInputDialog", "Цена"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HandInputDialog = QtWidgets.QDialog()
    ui = Ui_HandInputDialog()
    ui.setupUi(HandInputDialog)
    HandInputDialog.show()
    sys.exit(app.exec())
