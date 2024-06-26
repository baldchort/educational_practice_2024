import os
import random
import sys

import numpy as np
from PyQt6 import QtWidgets
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QFileDialog, QTableWidgetItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.figure import Figure

import gui
from src.libs.genetic_algorithm import *


class Data:
    def __init__(self):
        self.algParams = AlgorithmParameters(100, 0.5, 0.5, 25, 50)
        self.items = []
        self.geneticAlg = None
        self.iterationsInfo = list[IterationInfo]
        self.iteration = 0

        self.randomGenerationBackpackValue = -1
        self.inputFileName = ""

        self.algNum = -1

    def generateRandomItems(self):
        for i in range(self.randomGenerationBackpackValue):
            item = Item(random.randint(1, 50), random.randint(1, 50))
            self.items.append(item)


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class UILogic:
    def __init__(self):
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
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
        self.mainWindowUI.iterationTabLayout.addWidget(self.canvas)

    def drawPlot(self, maxFitness: list[float], averageFitness: list[float], iter: int) -> None:
        # x_len = self.data.algParams.maxAmountOfGenerations
        x_len = iter
        self.canvas.axes.clear()

        # Рисуем графики
        self.canvas.axes.plot(list(range(x_len)), averageFitness, 'r-', label='Средняя приспособленность')
        self.canvas.axes.plot(list(range(x_len)), maxFitness, 'b-', label='Максимальная приспособленность')

        # Устанавливаем сетку
        self.canvas.axes.grid()

        # Устанавливаем метки по оси X
        self.canvas.axes.set_xticks(np.arange(0, x_len + 1, 2))

        # Устанавливаем метки по оси Y
        max_fitness_value = max(maxFitness)
        # self.canvas.axes.set_yticks(np.arange(min(maxFitness), max_fitness_value + 1, 50))

        # Устанавливаем подписи к осям
        self.canvas.axes.set_xlabel('Поколение')
        self.canvas.axes.set_ylabel('Приспособленность')

        # Добавляем легенду
        self.canvas.axes.legend()

        # Перерисовываем график
        self.canvas.draw()

    def adjustLineEdits(self):
        validator = QIntValidator(1, 999)
        self.mainWindowUI.backpackValueLE.setValidator(validator)
        self.mainWindowUI.generationAmountLE.setValidator(validator)
        self.mainWindowUI.entityAmountLE.setValidator(validator)
        self.randGenDialogUI.AmountLineEdit.setValidator(validator)

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
        self.mainWindowUI.saveButton.clicked.connect(self.updateParams)
        self.mainWindowUI.forwardButton.clicked.connect(self.forwardButtonEvent)
        self.mainWindowUI.resultButton.clicked.connect(self.resultButtonEvent)

        self.handInputDialogUI.cancelButton.clicked.connect(self.closeHandInputDialogEvent)

        self.randGenDialogUI.CancelButton.clicked.connect(self.closeGenDialogEvent)
        self.randGenDialogUI.doneButton.clicked.connect(self.doneButtonEvent)

        self.mainWindowUI.resetDataButton.clicked.connect(self.resetButtonEvent)

    def resultButtonEvent(self):
        self.data.iteration = self.data.algParams.maxAmountOfGenerations
        self.iterateAlgorithm(self.data.iteration)

    def forwardButtonEvent(self):
        self.data.iteration += 1
        self.iterateAlgorithm(self.data.iteration)

    def updateParams(self):
        new_params = AlgorithmParameters(
            int(self.mainWindowUI.backpackValueLE.text()),
            float(self.mainWindowUI.crossingProbabilitySpin.value()),
            float(self.mainWindowUI.mutationProbabilitySpin.value()),
            int(self.mainWindowUI.entityAmountLE.text()),
            int(self.mainWindowUI.generationAmountLE.text())
        )

        self.data.algParams = new_params

    def openRandomGenDialog(self):
        self.randGenDialog.finished.connect(self.closeGenDialogEvent)
        self.mainWindow.setEnabled(False)

        self.randGenDialog.show()

    def switchAlgorithms(self, n: int):
        if n == 1:
            self.mainWindowUI.browseButton.setEnabled(False)
            self.mainWindowUI.inputButton.setEnabled(False)
            self.mainWindowUI.startButton.setEnabled(True)
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
        self.data.iteration = 0
        self.mainWindowUI.iterationDataFrame.setVisible(True)
        self.mainWindowUI.noDataLabel.setVisible(False)
        self.mainWindowUI.backpackTableWidget.clear()
        self.canvas.axes.clear()
        self.canvas.draw()
        self.mainWindowUI.backpackTableWidget.setRowCount(self.data.randomGenerationBackpackValue)
        self.mainWindowUI.iterationNumLabel.setText("0")

        self.data.generateRandomItems()
        self.data.geneticAlg = GeneticAlgorithm(self.data.items, self.data.algParams)

        self.data.iterationsInfo = self.data.geneticAlg.getSolution()

        for i in range(self.mainWindowUI.backpackTableWidget.rowCount()):
            self.mainWindowUI.backpackTableWidget.setItem(i, 0, QTableWidgetItem(str(self.data.items[i].weight)))
            self.mainWindowUI.backpackTableWidget.setItem(i, 1, QTableWidgetItem(str(self.data.items[i].cost)))

    def iterateAlgorithm(self, iter: int):
        # iteration = int(self.mainWindowUI.iterationNumLabel.text()) + 1
        iteration = iter
        print(iteration)
        if (iteration <= self.data.algParams.maxAmountOfGenerations):
            self.mainWindowUI.iterationNumLabel.setText(str(iteration))
            for i in range(self.mainWindowUI.backpackTableWidget.rowCount()):
                for j in range(3):
                    self.mainWindowUI.backpackTableWidget.setItem(i, 2 + j, QTableWidgetItem(
                        str(self.data.iterationsInfo[iteration - 1].bestBackpacks[j].genome[i])))

            self.mainWindowUI.curBPCostLabel.setText(str(self.data.iterationsInfo[iteration - 1].bestBackpacks[0].cost))
            self.mainWindowUI.curWeightLabel.setText(
                str(self.data.iterationsInfo[iteration - 1].bestBackpacks[0].weight))
            self.mainWindowUI.freeSpaveLabel.setText(str(self.data.algParams.maxBackpackWeight -
                                                         self.data.iterationsInfo[iteration - 1].bestBackpacks[
                                                             0].weight))

            self.mainWindowUI.curBPCostLabel_2.setText(
                str(self.data.iterationsInfo[iteration - 1].bestBackpacks[1].cost))
            self.mainWindowUI.curWeightLabel_2.setText(
                str(self.data.iterationsInfo[iteration - 1].bestBackpacks[1].weight))
            self.mainWindowUI.freeSpaveLabel_2.setText(str(self.data.algParams.maxBackpackWeight -
                                                           self.data.iterationsInfo[iteration - 1].bestBackpacks[
                                                               1].weight))

            self.mainWindowUI.curBPCostLabel_3.setText(
                str(self.data.iterationsInfo[iteration - 1].bestBackpacks[2].cost))
            self.mainWindowUI.curWeightLabel_3.setText(
                str(self.data.iterationsInfo[iteration - 1].bestBackpacks[2].weight))
            self.mainWindowUI.freeSpaveLabel_3.setText(str(self.data.algParams.maxBackpackWeight -
                                                           self.data.iterationsInfo[iteration - 1].bestBackpacks[
                                                               2].weight))

            self.drawPlot([x.currentMaxFitness for x in self.data.iterationsInfo[:iteration]],
                          [x.currentAverageFitness for x in self.data.iterationsInfo[:iteration]], iteration)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    logic = UILogic()
    logic.mainWindow.show()

    sys.exit(app.exec())
