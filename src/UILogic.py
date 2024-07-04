import os
import sys

from PyQt6 import QtWidgets
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QFileDialog, QTableWidgetItem, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import gui
from src.libs.genetic_algorithm import *


class Data:
    def __init__(self):
        self.parent_selection_strategies = {
            "Турнир": TournamentSelection(),
            "Рулетка": RouletteSelection(),
            "Инбридинг": InbreedingSelection()
        }

        self.crossing_strategies = {
            "Равномерное скрещивание": UniformCrossing(),
            "Дискретная рекомбинация": DiscreteRecombination(),
            "Промежуточная рекомбинация": IntermediateRecombination()
        }

        self.mutation_strategies = {
            "Плотность мутации": DensityMutation(),
            "Мутация перестановкой": PermutationMutation(),
            "Мутация обменом": ExchangeMutation()
        }

        self.generation_selection_strategies = {
            "Элитарный отбор": EliteSelection(),
            "Отбор вытеснением": ExclusionSelection(),
            "Отбор усечением": TruncationSelection()
        }

        self.algParams = AlgorithmParameters(100,
                                             0.9,
                                             0.3,
                                             25,
                                             50,
                                             self.parent_selection_strategies["Турнир"],
                                             self.crossing_strategies["Равномерное скрещивание"],
                                             self.mutation_strategies["Плотность мутации"],
                                             self.generation_selection_strategies["Элитарный отбор"])
        self.geneticAlg = None
        self.iterationsInfo = list[IterationInfo]
        self.iteration = 0

        self.backpackAmount = -1
        self.inputFileName = ""
        self.items = []

        self.algNum = -1

    def generateRandomItems(self) -> None:
        self.items.clear()
        for i in range(self.backpackAmount):
            item = Item(random.randint(1, 100), random.randint(1, 100))
            self.items.append(item)

    def readItemsFromFile(self) -> bool:
        self.items.clear()
        self.backpackAmount = 0
        with open(self.inputFileName, 'r') as file:
            lines = file.readlines()
            if len(lines) < 1:
                return False
            for line in lines:
                try:
                    weight, cost = line.split()
                    self.items.append(Item(int(cost), int(weight)))
                    self.backpackAmount += 1
                except ValueError:
                    self.items.clear()
                    return False
        return True


class MplCanvas(FigureCanvas):
    # зачем аргумент parent?
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class UILogic:
    def __init__(self):
        self.mainWindow = gui.MainWindow()
        self.mainWindowUI = self.mainWindow.mainWindowUI

        self.randGenDialog = gui.RandGenDialog()
        self.randGenDialogUI = self.randGenDialog.randGenDialogUI

        self.handInputDialog = gui.HandInputDialog()
        self.handInputDialogUI = self.handInputDialog.handInputDialogUI

        self.data = Data()
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)

        self.mainWindowUI.startButton.setEnabled(False)
        self.mainWindowUI.iterationDataFrame.setVisible(False)
        self.mainWindowUI.iterationTabLayout.addWidget(self.canvas)

        self.connectButtons()
        self.adjustLineEdits()

    def drawPlot(self, maxFitness: list[float], averageFitness: list[float], iter: int) -> None:
        # x_len = self.data.algParams.maxAmountOfGenerations
        x_len = iter
        self.canvas.axes.clear()

        self.canvas.axes.plot(list(range(x_len)), averageFitness, 'r-', label='Средняя приспособленность')
        self.canvas.axes.plot(list(range(x_len)), maxFitness, 'b-', label='Максимальная приспособленность')

        self.canvas.axes.grid()

        self.canvas.axes.set_xticks(np.arange(0, x_len + 1, 2))

        self.canvas.axes.set_xlabel('Поколение')
        self.canvas.axes.set_ylabel('Приспособленность')

        # Добавляем легенду
        self.canvas.axes.legend()

        # Перерисовываем график
        self.canvas.draw()

    def showErrorMessage(self, title: str, message: str) -> None:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

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
        self.mainWindowUI.backButton.clicked.connect(self.backButtonEvent)
        self.mainWindowUI.resetDataButton.clicked.connect(self.resetButtonEvent)

        self.handInputDialogUI.cancelButton.clicked.connect(self.closeHandInputDialogEvent)
        self.handInputDialogUI.doneButton.clicked.connect(self.handInputDoneButtonEvent)

        self.randGenDialogUI.CancelButton.clicked.connect(self.closeGenDialogEvent)
        self.randGenDialogUI.doneButton.clicked.connect(self.randGenDoneButtonEvent)

    def handInputDoneButtonEvent(self):
        if self.isTableEmpty():
            for i in range(self.handInputDialogUI.tableWidget.rowCount()):
                weight = 0
                cost = 0

                if (self.handInputDialogUI.tableWidget.item(i, 0) is not None) and \
                        self.handInputDialogUI.tableWidget.item(i, 0).text().isdigit():
                    weight = int(self.handInputDialogUI.tableWidget.item(i, 0).text())
                if (self.handInputDialogUI.tableWidget.item(i, 1) is not None) and \
                        self.handInputDialogUI.tableWidget.item(i, 1).text().isdigit():
                    cost = int(self.handInputDialogUI.tableWidget.item(i, 1).text())
                new_item = Item(cost=cost, weight=weight)
                self.data.items.append(new_item)
            self.data.backpackAmount = int(self.handInputDialogUI.AmountLineEdit.text())
            self.data.algNum = 3
            self.switchAlgorithms(self.data.algNum)

            self.mainWindowUI.startButton.setEnabled(True)
            self.handInputDialog.close()

    def isTableEmpty(self) -> bool:
        for i in range(self.handInputDialogUI.tableWidget.rowCount()):
            for j in range(self.handInputDialogUI.tableWidget.columnCount()):
                if self.handInputDialogUI.tableWidget.item(i, j) is None or \
                        not self.handInputDialogUI.tableWidget.item(i, j).text().isdigit():
                    # print("poop " + str(i) + str(j))
                    return False
        return True

    def backButtonEvent(self):
        if self.data.iteration <= 1:
            return
        self.data.iteration -= 1
        self.iterateAlgorithm(self.data.iteration)

    def resultButtonEvent(self):
        self.data.iteration = self.data.algParams.maxAmountOfGenerations
        self.iterateAlgorithm(self.data.iteration)

    def forwardButtonEvent(self):
        self.data.iteration += 1
        self.iterateAlgorithm(self.data.iteration)

    def updateParams(self):
        self.data.algParams.maxBackpackWeight = int(self.mainWindowUI.backpackValueLE.text())
        self.data.algParams.crossingProbability = float(self.mainWindowUI.crossingProbabilitySpin.value())
        self.data.algParams.mutationProbability = float(self.mainWindowUI.mutationProbabilitySpin.value())
        self.data.algParams.amountOfIndividsPerGeneration = int(self.mainWindowUI.entityAmountLE.text())
        self.data.algParams.maxAmountOfGenerations = int(self.mainWindowUI.generationAmountLE.text())
        self.data.algParams.crossingStrategy = \
            self.data.crossing_strategies[self.mainWindowUI.crossing_method_comboBox.currentData(0)]

        self.data.algParams.generationSelectionStrategy = \
            self.data.generation_selection_strategies[
                self.mainWindowUI.methodOfSelectingIndividsComboBox.currentData(0)]

        self.data.algParams.parentsSelectionStrategy = \
            self.data.parent_selection_strategies[self.mainWindowUI.parent_selection_comboBox.currentData(0)]

        self.data.algParams.mutationStrategy = \
            self.data.mutation_strategies[self.mainWindowUI.mutation_method_comboBox.currentData(0)]

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
        self.data.items.clear()

        self.data.inputFileName = ""
        self.data.backpackAmount = -1

        self.switchAlgorithms(self.data.algNum)

    def openHandInputDialog(self):
        self.mainWindow.setEnabled(False)

        self.handInputDialog.show()
        self.handInputDialog.finished.connect(self.closeHandInputDialogEvent)
        self.handInputDialogUI.AmountLineEdit.textEdited.connect(self.handInputTextChanged)

    def handInputTextChanged(self):
        text = self.handInputDialogUI.AmountLineEdit.text()

        if text != "":
            self.handInputDialogUI.tableWidget.setRowCount(int(text))

    def switchAllButtons(self, state: bool):
        self.mainWindowUI.inputButton.setEnabled(state)
        self.mainWindowUI.browseButton.setEnabled(state)
        self.mainWindowUI.backButton.setEnabled(state)
        self.mainWindowUI.forwardButton.setEnabled(state)
        self.mainWindowUI.resultButton.setEnabled(state)
        self.mainWindowUI.randomGenButton.setEnabled(state)

    def closeHandInputDialogEvent(self):
        self.mainWindow.setEnabled(True)
        self.handInputDialog.close()

    def closeGenDialogEvent(self):
        if self.randGenDialogUI.AmountLineEdit.text() != "" and self.data.backpackAmount != -1:
            self.randGenDialogUI.AmountLineEdit.setText(str(self.data.backpackAmount))

        self.randGenDialog.close()
        self.mainWindow.setEnabled(True)

    def randGenDoneButtonEvent(self):
        if self.randGenDialogUI.AmountLineEdit.text() != "":
            self.data.algNum = 1
            self.switchAlgorithms(self.data.algNum)

            self.data.backpackAmount = int(self.randGenDialogUI.AmountLineEdit.text())

            self.data.generateRandomItems()

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
            self.data.inputFileName = file_name[0]
            if self.data.readItemsFromFile():
                self.data.algNum = 2
            else:
                self.data.inputFileName = ""
                self.showErrorMessage("Ошибка",
                                      "Ошибка при чтении файла: несоответствующий формат данных")

        self.mainWindow.setEnabled(True)
        self.switchAlgorithms(self.data.algNum)

    def startAlgorithm(self):
        self.data.iteration = 0
        self.mainWindowUI.iterationDataFrame.setVisible(True)
        self.mainWindowUI.noDataLabel.setVisible(False)
        self.mainWindowUI.backpackTableWidget.clearContents()
        self.canvas.axes.clear()
        self.canvas.draw()
        self.mainWindowUI.backpackTableWidget.setRowCount(self.data.backpackAmount)
        self.mainWindowUI.iterationNumLabel.setText("0")

        self.data.geneticAlg = GeneticAlgorithm(self.data.items, self.data.algParams)

        self.data.iterationsInfo = self.data.geneticAlg.getSolution()

        for i in range(self.mainWindowUI.backpackTableWidget.rowCount()):
            self.mainWindowUI.backpackTableWidget.setItem(i, 0, QTableWidgetItem(str(self.data.items[i].weight)))
            self.mainWindowUI.backpackTableWidget.setItem(i, 1, QTableWidgetItem(str(self.data.items[i].cost)))

    def iterateAlgorithm(self, iter: int):
        iteration = iter
        print(iteration)
        if iteration <= len(self.data.iterationsInfo):
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
