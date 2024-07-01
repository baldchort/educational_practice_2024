from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow

from UIs.UIMainWindow import Ui_MainWindow
from UIs.UIRandGenDialog import Ui_randGenDialog
from UIs.UIHandInputUI import Ui_HandInputDialog


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.mainWindowUI = Ui_MainWindow()
        self.mainWindowUI.setupUi(self)


class RandGenDialog(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.randGenDialogUI = Ui_randGenDialog()
        self.randGenDialogUI.setupUi(self)


class HandInputDialog(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.handInputDialogUI = Ui_HandInputDialog()
        self.handInputDialogUI.setupUi(self)
