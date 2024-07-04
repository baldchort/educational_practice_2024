# Form implementation generated from reading ui file 'backpackProblemUI.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1506, 810)
        self.wind = QtWidgets.QWidget(parent=MainWindow)
        self.wind.setEnabled(True)
        self.wind.setObjectName("wind")
        self.gridLayout = QtWidgets.QGridLayout(self.wind)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout.addLayout(self.verticalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backButton = QtWidgets.QPushButton(parent=self.wind)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)
        self.forwardButton = QtWidgets.QPushButton(parent=self.wind)
        self.forwardButton.setObjectName("forwardButton")
        self.horizontalLayout.addWidget(self.forwardButton)
        self.resultButton = QtWidgets.QPushButton(parent=self.wind)
        self.resultButton.setObjectName("resultButton")
        self.horizontalLayout.addWidget(self.resultButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.paramsDataFrame = QtWidgets.QFrame(parent=self.wind)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.paramsDataFrame.sizePolicy().hasHeightForWidth())
        self.paramsDataFrame.setSizePolicy(sizePolicy)
        self.paramsDataFrame.setMinimumSize(QtCore.QSize(100, 0))
        self.paramsDataFrame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.paramsDataFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.paramsDataFrame.setObjectName("paramsDataFrame")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.paramsDataFrame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 30, 471, 311))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.algParams = QtWidgets.QVBoxLayout()
        self.algParams.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetFixedSize)
        self.algParams.setContentsMargins(10, 20, 10, 20)
        self.algParams.setSpacing(10)
        self.algParams.setObjectName("algParams")
        self.backpackValueLabel = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.backpackValueLabel.setObjectName("backpackValueLabel")
        self.algParams.addWidget(self.backpackValueLabel)
        self.backpackValueLE = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backpackValueLE.sizePolicy().hasHeightForWidth())
        self.backpackValueLE.setSizePolicy(sizePolicy)
        self.backpackValueLE.setMinimumSize(QtCore.QSize(50, 0))
        self.backpackValueLE.setInputMask("")
        self.backpackValueLE.setText("")
        self.backpackValueLE.setClearButtonEnabled(False)
        self.backpackValueLE.setObjectName("backpackValueLE")
        self.algParams.addWidget(self.backpackValueLE)
        self.genAmountLabel = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.genAmountLabel.setObjectName("genAmountLabel")
        self.algParams.addWidget(self.genAmountLabel)
        self.generationAmountLE = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generationAmountLE.sizePolicy().hasHeightForWidth())
        self.generationAmountLE.setSizePolicy(sizePolicy)
        self.generationAmountLE.setObjectName("generationAmountLE")
        self.algParams.addWidget(self.generationAmountLE)
        self.entityAmountLabel = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.entityAmountLabel.setObjectName("entityAmountLabel")
        self.algParams.addWidget(self.entityAmountLabel)
        self.entityAmountLE = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entityAmountLE.sizePolicy().hasHeightForWidth())
        self.entityAmountLE.setSizePolicy(sizePolicy)
        self.entityAmountLE.setObjectName("entityAmountLE")
        self.algParams.addWidget(self.entityAmountLE)
        self.probabilityCrossingLabel = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.probabilityCrossingLabel.setObjectName("probabilityCrossingLabel")
        self.algParams.addWidget(self.probabilityCrossingLabel)
        self.crossingProbabilitySpin = QtWidgets.QDoubleSpinBox(parent=self.horizontalLayoutWidget_2)
        self.crossingProbabilitySpin.setMaximum(1.0)
        self.crossingProbabilitySpin.setSingleStep(0.1)
        self.crossingProbabilitySpin.setObjectName("crossingProbabilitySpin")
        self.algParams.addWidget(self.crossingProbabilitySpin)
        self.probabilityCrossingLabel_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.probabilityCrossingLabel_2.setObjectName("probabilityCrossingLabel_2")
        self.algParams.addWidget(self.probabilityCrossingLabel_2)
        self.mutationProbabilitySpin = QtWidgets.QDoubleSpinBox(parent=self.horizontalLayoutWidget_2)
        self.mutationProbabilitySpin.setMaximum(1.0)
        self.mutationProbabilitySpin.setSingleStep(0.1)
        self.mutationProbabilitySpin.setObjectName("mutationProbabilitySpin")
        self.algParams.addWidget(self.mutationProbabilitySpin)
        self.algParams.setStretch(0, 2)
        self.algParams.setStretch(1, 2)
        self.algParams.setStretch(2, 2)
        self.horizontalLayout_17.addLayout(self.algParams)
        self.params_layout_2 = QtWidgets.QVBoxLayout()
        self.params_layout_2.setContentsMargins(10, 20, 10, 20)
        self.params_layout_2.setSpacing(10)
        self.params_layout_2.setObjectName("params_layout_2")
        self.parent_selection_method_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.parent_selection_method_label.setObjectName("parent_selection_method_label")
        self.params_layout_2.addWidget(self.parent_selection_method_label)
        self.parent_selection_comboBox = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_2)
        self.parent_selection_comboBox.setObjectName("parent_selection_comboBox")
        self.parent_selection_comboBox.addItem("")
        self.parent_selection_comboBox.addItem("")
        self.parent_selection_comboBox.addItem("")
        self.params_layout_2.addWidget(self.parent_selection_comboBox)
        self.crossing_method_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.crossing_method_label.setObjectName("crossing_method_label")
        self.params_layout_2.addWidget(self.crossing_method_label)
        self.crossing_method_comboBox = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_2)
        self.crossing_method_comboBox.setObjectName("crossing_method_comboBox")
        self.crossing_method_comboBox.addItem("")
        self.crossing_method_comboBox.addItem("")
        self.crossing_method_comboBox.addItem("")
        self.params_layout_2.addWidget(self.crossing_method_comboBox)
        self.mutation_method_label = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.mutation_method_label.setObjectName("mutation_method_label")
        self.params_layout_2.addWidget(self.mutation_method_label)
        self.mutation_method_comboBox = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_2)
        self.mutation_method_comboBox.setObjectName("mutation_method_comboBox")
        self.mutation_method_comboBox.addItem("")
        self.mutation_method_comboBox.addItem("")
        self.mutation_method_comboBox.addItem("")
        self.params_layout_2.addWidget(self.mutation_method_comboBox)
        self.methodOfSelectingIndividsLabel = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.methodOfSelectingIndividsLabel.setObjectName("methodOfSelectingIndividsLabel")
        self.params_layout_2.addWidget(self.methodOfSelectingIndividsLabel)
        self.methodOfSelectingIndividsComboBox = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_2)
        self.methodOfSelectingIndividsComboBox.setObjectName("methodOfSelectingIndividsComboBox")
        self.methodOfSelectingIndividsComboBox.addItem("")
        self.methodOfSelectingIndividsComboBox.addItem("")
        self.methodOfSelectingIndividsComboBox.addItem("")
        self.params_layout_2.addWidget(self.methodOfSelectingIndividsComboBox)
        self.horizontalLayout_17.addLayout(self.params_layout_2)
        self.ParamsLabel = QtWidgets.QLabel(parent=self.paramsDataFrame)
        self.ParamsLabel.setEnabled(True)
        self.ParamsLabel.setGeometry(QtCore.QRect(120, 0, 221, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.ParamsLabel.setFont(font)
        self.ParamsLabel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.ParamsLabel.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.ParamsLabel.setScaledContents(False)
        self.ParamsLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ParamsLabel.setObjectName("ParamsLabel")
        self.verticalLayout.addWidget(self.paramsDataFrame)
        self.saveButton = QtWidgets.QPushButton(parent=self.wind)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)
        self.dataFrame = QtWidgets.QFrame(parent=self.wind)
        self.dataFrame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.dataFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.dataFrame.setMidLineWidth(0)
        self.dataFrame.setObjectName("dataFrame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.dataFrame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 481, 361))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.DataLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.DataLayout.setContentsMargins(20, 20, 20, 20)
        self.DataLayout.setSpacing(20)
        self.DataLayout.setObjectName("DataLayout")
        self.DataLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.DataLabel.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DataLabel.setFont(font)
        self.DataLabel.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.DataLabel.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.DataLabel.setScaledContents(False)
        self.DataLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.DataLabel.setObjectName("DataLabel")
        self.DataLayout.addWidget(self.DataLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.DataLayout.addItem(spacerItem)
        self.randomGenButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.randomGenButton.setObjectName("randomGenButton")
        self.DataLayout.addWidget(self.randomGenButton)
        self.browseButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.browseButton.setObjectName("browseButton")
        self.DataLayout.addWidget(self.browseButton)
        self.inputButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.inputButton.setObjectName("inputButton")
        self.DataLayout.addWidget(self.inputButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.DataLayout.addItem(spacerItem1)
        self.resetDataButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget_2)
        self.resetDataButton.setObjectName("resetDataButton")
        self.DataLayout.addWidget(self.resetDataButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.DataLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.dataFrame)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.iterationTabWidget_2 = QtWidgets.QTabWidget(parent=self.wind)
        self.iterationTabWidget_2.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.iterationTabWidget_2.setUsesScrollButtons(False)
        self.iterationTabWidget_2.setMovable(True)
        self.iterationTabWidget_2.setObjectName("iterationTabWidget_2")
        self.instructionTab_2 = QtWidgets.QWidget()
        self.instructionTab_2.setObjectName("instructionTab_2")
        self.iterationTabWidget_2.addTab(self.instructionTab_2, "")
        self.iterationTab_2 = QtWidgets.QWidget()
        self.iterationTab_2.setObjectName("iterationTab_2")
        self.noDataLabel = QtWidgets.QLabel(parent=self.iterationTab_2)
        self.noDataLabel.setGeometry(QtCore.QRect(290, 20, 301, 71))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.noDataLabel.setFont(font)
        self.noDataLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.noDataLabel.setObjectName("noDataLabel")
        self.iterationDataFrame = QtWidgets.QFrame(parent=self.iterationTab_2)
        self.iterationDataFrame.setGeometry(QtCore.QRect(0, 0, 851, 721))
        self.iterationDataFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.iterationDataFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.iterationDataFrame.setObjectName("iterationDataFrame")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=self.iterationDataFrame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 0, 859, 701))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.iterationTabLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.iterationTabLayout.setContentsMargins(0, 0, 0, 0)
        self.iterationTabLayout.setObjectName("iterationTabLayout")
        self.iterationLabelLayout = QtWidgets.QHBoxLayout()
        self.iterationLabelLayout.setObjectName("iterationLabelLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.iterationLabelLayout.addItem(spacerItem3)
        self.iterationLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.iterationLabel.setObjectName("iterationLabel")
        self.iterationLabelLayout.addWidget(self.iterationLabel)
        self.iterationNumLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.iterationNumLabel.setObjectName("iterationNumLabel")
        self.iterationLabelLayout.addWidget(self.iterationNumLabel)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.iterationLabelLayout.addItem(spacerItem4)
        self.iterationTabLayout.addLayout(self.iterationLabelLayout)
        self.backpackTableWidget = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backpackTableWidget.sizePolicy().hasHeightForWidth())
        self.backpackTableWidget.setSizePolicy(sizePolicy)
        self.backpackTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.backpackTableWidget.setRowCount(20)
        self.backpackTableWidget.setColumnCount(5)
        self.backpackTableWidget.setObjectName("backpackTableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.backpackTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.backpackTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.backpackTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.backpackTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.backpackTableWidget.setHorizontalHeaderItem(4, item)
        self.iterationTabLayout.addWidget(self.backpackTableWidget)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.textCurBPCostLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.textCurBPCostLabel.setObjectName("textCurBPCostLabel")
        self.horizontalLayout_11.addWidget(self.textCurBPCostLabel)
        self.curBPCostLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.curBPCostLabel.setObjectName("curBPCostLabel")
        self.horizontalLayout_11.addWidget(self.curBPCostLabel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textCurWeightLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.textCurWeightLabel.setObjectName("textCurWeightLabel")
        self.horizontalLayout_2.addWidget(self.textCurWeightLabel)
        self.curWeightLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.curWeightLabel.setObjectName("curWeightLabel")
        self.horizontalLayout_2.addWidget(self.curWeightLabel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.backpackData_1 = QtWidgets.QHBoxLayout()
        self.backpackData_1.setObjectName("backpackData_1")
        self.textFreeSpacLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.textFreeSpacLabel.setObjectName("textFreeSpacLabel")
        self.backpackData_1.addWidget(self.textFreeSpacLabel)
        self.freeSpaveLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.freeSpaveLabel.setObjectName("freeSpaveLabel")
        self.backpackData_1.addWidget(self.freeSpaveLabel)
        self.verticalLayout_5.addLayout(self.backpackData_1)
        self.horizontalLayout_9.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.textCurBPCostLabel_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.textCurBPCostLabel_2.setObjectName("textCurBPCostLabel_2")
        self.horizontalLayout_12.addWidget(self.textCurBPCostLabel_2)
        self.curBPCostLabel_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.curBPCostLabel_2.setObjectName("curBPCostLabel_2")
        self.horizontalLayout_12.addWidget(self.curBPCostLabel_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.textCurWeightLabel_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.textCurWeightLabel_2.setObjectName("textCurWeightLabel_2")
        self.horizontalLayout_8.addWidget(self.textCurWeightLabel_2)
        self.curWeightLabel_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.curWeightLabel_2.setObjectName("curWeightLabel_2")
        self.horizontalLayout_8.addWidget(self.curWeightLabel_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.backpackData_2 = QtWidgets.QHBoxLayout()
        self.backpackData_2.setObjectName("backpackData_2")
        self.textFreeSpacLabel_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.textFreeSpacLabel_2.setObjectName("textFreeSpacLabel_2")
        self.backpackData_2.addWidget(self.textFreeSpacLabel_2)
        self.freeSpaveLabel_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.freeSpaveLabel_2.setObjectName("freeSpaveLabel_2")
        self.backpackData_2.addWidget(self.freeSpaveLabel_2)
        self.verticalLayout_6.addLayout(self.backpackData_2)
        self.horizontalLayout_9.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.textCurBPCostLabel_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.textCurBPCostLabel_3.setObjectName("textCurBPCostLabel_3")
        self.horizontalLayout_14.addWidget(self.textCurBPCostLabel_3)
        self.curBPCostLabel_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.curBPCostLabel_3.setObjectName("curBPCostLabel_3")
        self.horizontalLayout_14.addWidget(self.curBPCostLabel_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.textCurWeightLabel_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.textCurWeightLabel_3.setObjectName("textCurWeightLabel_3")
        self.horizontalLayout_10.addWidget(self.textCurWeightLabel_3)
        self.curWeightLabel_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.curWeightLabel_3.setObjectName("curWeightLabel_3")
        self.horizontalLayout_10.addWidget(self.curWeightLabel_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.backpackData_3 = QtWidgets.QHBoxLayout()
        self.backpackData_3.setObjectName("backpackData_3")
        self.textFreeSpacLabel_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.textFreeSpacLabel_3.setObjectName("textFreeSpacLabel_3")
        self.backpackData_3.addWidget(self.textFreeSpacLabel_3)
        self.freeSpaveLabel_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_3)
        self.freeSpaveLabel_3.setObjectName("freeSpaveLabel_3")
        self.backpackData_3.addWidget(self.freeSpaveLabel_3)
        self.verticalLayout_7.addLayout(self.backpackData_3)
        self.horizontalLayout_9.addLayout(self.verticalLayout_7)
        self.iterationTabLayout.addLayout(self.horizontalLayout_9)
        self.line = QtWidgets.QFrame(parent=self.verticalLayoutWidget_3)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.iterationTabLayout.addWidget(self.line)
        self.iterationTabWidget_2.addTab(self.iterationTab_2, "")
        self.gridLayout.addWidget(self.iterationTabWidget_2, 0, 1, 1, 2)
        self.startButton = QtWidgets.QPushButton(parent=self.wind)
        self.startButton.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.gridLayout.addWidget(self.startButton, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.wind)

        self.retranslateUi(MainWindow)
        self.iterationTabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Задача о рюкзаках"))
        self.backButton.setText(_translate("MainWindow", "Шаг назад"))
        self.forwardButton.setText(_translate("MainWindow", "Шаг вперед"))
        self.resultButton.setText(_translate("MainWindow", "Результат"))
        self.backpackValueLabel.setText(_translate("MainWindow", "Допустимый вес рюкзака"))
        self.backpackValueLE.setPlaceholderText(_translate("MainWindow", "Вес рюкзака"))
        self.genAmountLabel.setText(_translate("MainWindow", "Количество поколений"))
        self.generationAmountLE.setPlaceholderText(_translate("MainWindow", "Кол-во поколений"))
        self.entityAmountLabel.setText(_translate("MainWindow", "Количество особей в поколении"))
        self.entityAmountLE.setPlaceholderText(_translate("MainWindow", "Кол-во особей в поколении"))
        self.probabilityCrossingLabel.setText(_translate("MainWindow", "Вероятность скрещевания"))
        self.probabilityCrossingLabel_2.setText(_translate("MainWindow", "Вероятность мутации"))
        self.parent_selection_method_label.setText(_translate("MainWindow", "Cпособ отбора родителей"))
        self.parent_selection_comboBox.setItemText(0, _translate("MainWindow", "Турнир"))
        self.parent_selection_comboBox.setItemText(1, _translate("MainWindow", "Рулетка"))
        self.parent_selection_comboBox.setItemText(2, _translate("MainWindow", "Аутбридинг"))
        self.crossing_method_label.setText(_translate("MainWindow", "Способ скрещевания"))
        self.crossing_method_comboBox.setItemText(0, _translate("MainWindow", "Равномерное скрещевание"))
        self.crossing_method_comboBox.setItemText(1, _translate("MainWindow", "Дискретная рекомбинация"))
        self.crossing_method_comboBox.setItemText(2, _translate("MainWindow", "Промежуточная рекомбинация"))
        self.mutation_method_label.setText(_translate("MainWindow", "Способ мутации"))
        self.mutation_method_comboBox.setItemText(0, _translate("MainWindow", "Плотность мутации"))
        self.mutation_method_comboBox.setItemText(1, _translate("MainWindow", "Мутация перестановкой"))
        self.mutation_method_comboBox.setItemText(2, _translate("MainWindow", "Мутация обменом"))
        self.methodOfSelectingIndividsLabel.setText(_translate("MainWindow", "Cпособ отбора особей в следующее поколение"))
        self.methodOfSelectingIndividsComboBox.setItemText(0, _translate("MainWindow", "Элитарный отбор"))
        self.methodOfSelectingIndividsComboBox.setItemText(1, _translate("MainWindow", "Отбор вытеснением"))
        self.methodOfSelectingIndividsComboBox.setItemText(2, _translate("MainWindow", "Отбор усечением"))
        self.ParamsLabel.setText(_translate("MainWindow", "Параметры работы алгоритма"))
        self.saveButton.setText(_translate("MainWindow", "Изменить"))
        self.DataLabel.setText(_translate("MainWindow", "Данные"))
        self.randomGenButton.setText(_translate("MainWindow", "Сгенерировать случайно"))
        self.browseButton.setText(_translate("MainWindow", "Загрузить из файла"))
        self.inputButton.setText(_translate("MainWindow", "Ввести вручную"))
        self.resetDataButton.setText(_translate("MainWindow", "Сбросить данные"))
        self.iterationTabWidget_2.setTabText(self.iterationTabWidget_2.indexOf(self.instructionTab_2), _translate("MainWindow", "Инструкция"))
        self.noDataLabel.setText(_translate("MainWindow", "Нет данных"))
        self.iterationLabel.setText(_translate("MainWindow", "Итерация номер "))
        self.iterationNumLabel.setText(_translate("MainWindow", "0"))
        self.backpackTableWidget.setSortingEnabled(True)
        item = self.backpackTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Вес"))
        item = self.backpackTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Стоимость"))
        item = self.backpackTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Количество в 1"))
        item = self.backpackTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Количество в 2"))
        item = self.backpackTableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Количество в 3"))
        self.label.setText(_translate("MainWindow", "Рюкзак 1"))
        self.textCurBPCostLabel.setText(_translate("MainWindow", "Текущая стоимость рюкзака:"))
        self.curBPCostLabel.setText(_translate("MainWindow", "-1"))
        self.textCurWeightLabel.setText(_translate("MainWindow", "Текущий вес рюкзака:"))
        self.curWeightLabel.setText(_translate("MainWindow", "-1"))
        self.textFreeSpacLabel.setText(_translate("MainWindow", "Оставшееся свободное место:"))
        self.freeSpaveLabel.setText(_translate("MainWindow", "-1"))
        self.label_2.setText(_translate("MainWindow", "Рюкзак 2"))
        self.textCurBPCostLabel_2.setText(_translate("MainWindow", "Текущая стоимость рюкзака:"))
        self.curBPCostLabel_2.setText(_translate("MainWindow", "-1"))
        self.textCurWeightLabel_2.setText(_translate("MainWindow", "Текущий вес рюкзака:"))
        self.curWeightLabel_2.setText(_translate("MainWindow", "-1"))
        self.textFreeSpacLabel_2.setText(_translate("MainWindow", "Оставшееся свободное место:"))
        self.freeSpaveLabel_2.setText(_translate("MainWindow", "-1"))
        self.label_3.setText(_translate("MainWindow", "Рюкзак 3"))
        self.textCurBPCostLabel_3.setText(_translate("MainWindow", "Текущая стоимость рюкзака:"))
        self.curBPCostLabel_3.setText(_translate("MainWindow", "-1"))
        self.textCurWeightLabel_3.setText(_translate("MainWindow", "Текущий вес рюкзака:"))
        self.curWeightLabel_3.setText(_translate("MainWindow", "-1"))
        self.textFreeSpacLabel_3.setText(_translate("MainWindow", "Оставшееся свободное место:"))
        self.freeSpaveLabel_3.setText(_translate("MainWindow", "-1"))
        self.iterationTabWidget_2.setTabText(self.iterationTabWidget_2.indexOf(self.iterationTab_2), _translate("MainWindow", "Итерация алгоритма"))
        self.startButton.setText(_translate("MainWindow", "Запуск"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
