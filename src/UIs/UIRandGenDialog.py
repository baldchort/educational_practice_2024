# Form implementation generated from reading ui file 'randGenUI.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_randGenDialog(object):
    def setupUi(self, randGenDialog):
        randGenDialog.setObjectName("randGenDialog")
        randGenDialog.resize(400, 152)
        randGenDialog.setMinimumSize(QtCore.QSize(400, 152))
        randGenDialog.setMaximumSize(QtCore.QSize(400, 152))
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=randGenDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 30, 229, 49))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.amountLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.amountLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.amountLabel.setObjectName("amountLabel")
        self.verticalLayout.addWidget(self.amountLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.AmountLineEdit = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.AmountLineEdit.setObjectName("AmountLineEdit")
        self.horizontalLayout_2.addWidget(self.AmountLineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.doneButton = QtWidgets.QPushButton(parent=randGenDialog)
        self.doneButton.setGeometry(QtCore.QRect(230, 110, 158, 32))
        self.doneButton.setObjectName("doneButton")
        self.CancelButton = QtWidgets.QPushButton(parent=randGenDialog)
        self.CancelButton.setGeometry(QtCore.QRect(20, 110, 121, 32))
        self.CancelButton.setObjectName("CancelButton")

        self.retranslateUi(randGenDialog)
        QtCore.QMetaObject.connectSlotsByName(randGenDialog)

    def retranslateUi(self, randGenDialog):
        _translate = QtCore.QCoreApplication.translate
        randGenDialog.setWindowTitle(_translate("randGenDialog", "Случайная генерация"))
        self.amountLabel.setText(_translate("randGenDialog", "Введите количество предметов"))
        self.doneButton.setText(_translate("randGenDialog", "Готово"))
        self.CancelButton.setText(_translate("randGenDialog", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    randGenDialog = QtWidgets.QDialog()
    ui = Ui_randGenDialog()
    ui.setupUi(randGenDialog)
    randGenDialog.show()
    sys.exit(app.exec())
