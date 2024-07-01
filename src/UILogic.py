import os
import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog

import gui


class UILogic:
    def __init__(self):
        self.mainWindow = gui.MainWindow()
        self.mainWindowUI = self.mainWindow.mainWindowUI

        self.randGenDialog = gui.RandGenDialog()
        self.randGenDialogUI = self.randGenDialog.randGenDialogUI

        self.handInputDialog = gui.HandInputDialog()
        self.handInputDialogUI = self.handInputDialog.handInputDialogUI

        self.inputFileName = '~/'

        self.connectButtons()

    def connectButtons(self):
        self.mainWindowUI.randomGenButton.clicked.connect(self.openRandomGenDialog)
        self.randGenDialogUI.CancelButton.clicked.connect(self.closeGenDialogEvent)
        self.mainWindowUI.browseButton.clicked.connect(self.browseEvent)
        self.mainWindowUI.inputButton.clicked.connect(self.openHandInputDialog)
        self.handInputDialogUI.cancelButton.clicked.connect(self.closeHandInputDialogEvent)

    def openRandomGenDialog(self):
        self.switchAllButtons(False)
        self.randGenDialog.finished.connect(self.closeGenDialogEvent)
        self.randGenDialog.show()

    def openHandInputDialog(self):
        self.switchAllButtons(False)
        self.handInputDialog.show()
        self.handInputDialog.finished.connect(self.closeHandInputDialogEvent)
        self.handInputDialogUI.AmountLineEdit.textEdited.connect(self.handInputTextChanged)

    def handInputTextChanged(self):
        text = self.handInputDialogUI.AmountLineEdit.text()

        self.handInputDialogUI.tableWidget.setRowCount(int(text))

    def switchAllButtons(self, state: bool):
        self.mainWindowUI.inputButton.setEnabled(state)
        self.mainWindowUI.startButton.setEnabled(state)
        self.mainWindowUI.browseButton.setEnabled(state)
        self.mainWindowUI.backButton.setEnabled(state)
        self.mainWindowUI.forwardButton.setEnabled(state)
        self.mainWindowUI.resultButton.setEnabled(state)
        self.mainWindowUI.randomGenButton.setEnabled(state)

    def closeHandInputDialogEvent(self):
        self.handInputDialog.close()
        self.switchAllButtons(True)

    def closeGenDialogEvent(self):
        self.randGenDialog.close()
        self.switchAllButtons(True)

    # Открываем диалог (выбор файла)
    def browseEvent(self):
        self.switchAllButtons(False)
        file_filter = 'Text File (*.txt)'
        file_dialog = QFileDialog
        file_name = file_dialog.getOpenFileName(
            parent=self.mainWindow,
            caption='Открыть файл',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Text File (*.txt)'
        )
        self.inputFileName = file_name[0]
        print(self.inputFileName)
        self.switchAllButtons(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    logic = UILogic()
    logic.mainWindow.show()

    sys.exit(app.exec())
