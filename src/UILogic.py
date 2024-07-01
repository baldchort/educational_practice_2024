import os
import random
import sys

from PyQt6 import QtWidgets
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QFileDialog

import gui
from src.libs.objects import *


class AllInfo:
    def __init__(self, maxBackpackWeight: int, items: list[Item]):
        self.maxBackpackWeight = maxBackpackWeight
        self.items = items
        self.maxFitness = []
        self.averageFitness = []

    def appendMaxFitness(self, iteration: CurrentIterationInfo) -> None:
        self.maxFitness.append(iteration.currentMaxFitness)

    def appendAverageFitness(self, iteration: CurrentIterationInfo) -> None:
        self.averageFitness.append(iteration.currentAverageFitness)

    def drawPlot(self) -> None:
        pass


items = list()


def generateRandomItems(n: int) -> list[Item]:
    for i in range(n):
        item = Item(random.randint(1, 50), random.randint(1, 50))
        items.append(item)
    return items


class Data:
    def __init__(self):
        self.algParams = AlgorithmParameters(100, 0.5, 0.5, 25, 50)

        self.randomGenerationBackpackValue = -1
        self.inputFileName = ""

        self.algNum = -1
        self.info = None


class UILogic:
    def __init__(self):
        self.mainWindow = gui.MainWindow()
        self.mainWindowUI = self.mainWindow.mainWindowUI

        self.randGenDialog = gui.RandGenDialog()
        self.randGenDialogUI = self.randGenDialog.randGenDialogUI

        self.handInputDialog = gui.HandInputDialog()
        self.handInputDialogUI = self.handInputDialog.handInputDialogUI

        self.data = Data()

        self.mainWindowUI.startButton.setEnabled(False)
        self.mainWindowUI.iterationDataFrame.setVisible(False)
        self.connectButtons()
        self.adjustLineEdits()

    def adjustLineEdits(self):
        validator = QIntValidator(1, 999)
        self.mainWindowUI.backpackValueLE.setValidator(validator)
        self.mainWindowUI.generationAmountLE.setValidator(validator)
        self.mainWindowUI.entityAmountLE.setValidator(validator)

        self.mainWindowUI.backpackValueLE.setText(str(self.data.algParams.maxBackpackWeight))
        self.mainWindowUI.generationAmountLE.setText(str(self.data.algParams.maxAmountOfGenerations))
        self.mainWindowUI.entityAmountLE.setText(str(self.data.algParams.amountOfIndividsPerGeneration))
        self.mainWindowUI.crossingProbabilitySpin.setValue(self.data.algParams.crossingProbability)
        self.mainWindowUI.mutationProbabilitySpin.setValue(self.data.algParams.mutationProbability)

    def connectButtons(self):
        self.mainWindowUI.randomGenButton.clicked.connect(self.openRandomGenDialog)
        self.mainWindowUI.browseButton.clicked.connect(self.browseEvent)
        self.mainWindowUI.inputButton.clicked.connect(self.openHandInputDialog)
        self.mainWindowUI.startButton.clicked.connect(self.startButtonEvent)

        self.handInputDialogUI.cancelButton.clicked.connect(self.closeHandInputDialogEvent)

        self.randGenDialogUI.CancelButton.clicked.connect(self.closeGenDialogEvent)
        self.randGenDialogUI.doneButton.clicked.connect(self.doneButtonEvent)

        self.mainWindowUI.resetDataButton.clicked.connect(self.resetButtonEvent)

    def openRandomGenDialog(self):
        self.randGenDialog.finished.connect(self.closeGenDialogEvent)
        self.mainWindow.setEnabled(False)

        self.randGenDialog.show()

    def switchAlgorithms(self, n: int):
        if n == 1:
            self.mainWindowUI.browseButton.setEnabled(False)
            self.mainWindowUI.inputButton.setEnabled(False)
            self.mainWindowUI.startButton.setEnabled(True)
            self.data.info = AllInfo(self.data.algParams.maxBackpackWeight,
                                     generateRandomItems(self.data.randomGenerationBackpackValue))
        elif n == 2:
            self.mainWindowUI.randomGenButton.setEnabled(False)
            self.mainWindowUI.inputButton.setEnabled(False)
            self.mainWindowUI.startButton.setEnabled(True)
        elif n == 3:
            self.mainWindowUI.randomGenButton.setEnabled(False)
            self.mainWindowUI.browseButton.setEnabled(False)
            self.mainWindowUI.startButton.setEnabled(True)
        elif n == -1:
            self.mainWindowUI.randomGenButton.setEnabled(True)
            self.mainWindowUI.browseButton.setEnabled(True)
            self.mainWindowUI.inputButton.setEnabled(True)
            self.mainWindowUI.startButton.setEnabled(False)

    def startButtonEvent(self):
        self.mainWindowUI.iterationTabWidget_2.setCurrentIndex(1)

        self.startAlgorithm()

    def resetButtonEvent(self):
        self.data.algNum = -1

        self.data.inputFileName = ""
        self.data.randomGenerationBackpackValue = -1

        self.switchAlgorithms(self.data.algNum)

    def openHandInputDialog(self):
        # self.switchAllButtons(False)
        self.handInputDialog.show()
        self.handInputDialog.finished.connect(self.closeHandInputDialogEvent)
        self.handInputDialogUI.AmountLineEdit.textEdited.connect(self.handInputTextChanged)

    def handInputTextChanged(self):
        text = self.handInputDialogUI.AmountLineEdit.text()

        self.handInputDialogUI.tableWidget.setRowCount(int(text))

    def switchAllButtons(self, state: bool):
        self.mainWindowUI.inputButton.setEnabled(state)
        # self.mainWindowUI.startButton.setEnabled(state)
        self.mainWindowUI.browseButton.setEnabled(state)
        self.mainWindowUI.backButton.setEnabled(state)
        self.mainWindowUI.forwardButton.setEnabled(state)
        self.mainWindowUI.resultButton.setEnabled(state)
        self.mainWindowUI.randomGenButton.setEnabled(state)

    def closeHandInputDialogEvent(self):
        self.handInputDialog.close()
        # self.switchAllButtons(True)

    def closeGenDialogEvent(self):
        if self.randGenDialogUI.AmountLineEdit.text() != "" and self.data.randomGenerationBackpackValue != -1:
            self.randGenDialogUI.AmountLineEdit.setText(str(self.data.randomGenerationBackpackValue))

        self.randGenDialog.close()
        self.mainWindow.setEnabled(True)

    def doneButtonEvent(self):
        if self.randGenDialogUI.AmountLineEdit.text() != "":
            self.data.algNum = 1
            self.data.randomGenerationBackpackValue = int(self.randGenDialogUI.AmountLineEdit.text())
            self.switchAlgorithms(self.data.algNum)

            self.randGenDialog.close()
            self.mainWindowUI.startButton.setEnabled(True)

    # Открываем диалог (выбор файла)
    def browseEvent(self):
        self.mainWindow.setEnabled(False)

        file_filter = 'Text File (*.txt)'
        file_dialog = QFileDialog
        file_name = file_dialog.getOpenFileName(
            parent=self.mainWindow,
            caption='Открыть файл',
            directory=os.getcwd(),
            filter=file_filter,
            initialFilter='Text File (*.txt)'
        )
        if file_name[0] != "":
            self.data.algNum = 2
            self.data.inputFileName = file_name[0]

        self.mainWindow.setEnabled(True)
        self.switchAlgorithms(self.data.algNum)

        print(self.data.inputFileName)

    def startAlgorithm(self):
        self.mainWindowUI.iterationDataFrame.setVisible(True)
        self.mainWindowUI.noDataLabel.setVisible(False)
        self.mainWindowUI.backpackTableWidget.setRowCount(self.data.randomGenerationBackpackValue)
        self.mainWindowUI.backpackTableWidget_2.setRowCount(self.data.randomGenerationBackpackValue)
        self.mainWindowUI.backpackTableWidget_3.setRowCount(self.data.randomGenerationBackpackValue)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    logic = UILogic()
    logic.mainWindow.show()

    sys.exit(app.exec())
