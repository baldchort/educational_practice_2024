
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QCloseEvent
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QLineEdit, QLabel, QDialog, \
    QFileDialog, QPlainTextEdit, QHBoxLayout, QMessageBox


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.close = None
        self.fileName = None
        self.dialog = QDialog

        self.inputWindow = InputWindow()
        self.iterationWindow = IterationWindow()
        self.randWindow = RandomWindow()

        self.setWindowTitle("Рюкзачки")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()
        widgets = []

        butt1 = QPushButton("Параметры работы алгоритма")
        widgets.append(butt1)
        butt1.clicked.connect(self.clickOnRandom)

        butt2 = QPushButton("Загрузить данные из файла")
        butt2.clicked.connect(self.browse)
        widgets.append(butt2)

        butt3 = QPushButton("Ввод данных вручную")
        butt3.clicked.connect(self.clickOnInputByHand)

        widgets.append(butt3)

        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)

        # Устанавливаем центральный виджет окна. Виджет будет расширяться по умолчанию,
        # заполняя всё пространство окна.
        self.setCentralWidget(widget)

    def clickOnRandom(self):
        self.randWindow.show()

    def browse(self):
        fname = QFileDialog.getOpenFileName(self, 'Открыть файл', '~/')
        self.fileName = fname[0]
        print(self.fileName)

    def clickOnInputByHand(self):
        self.inputWindow.show()

    def startAlgorithm(self):
        self.iterationWindow.show()

    def closeEvent(self, event: QCloseEvent) -> None:
        self.close = QMessageBox(self)
        self.close.setText("Закрыть приложение?")
        self.close.setStandardButtons(QMessageBox.standardButtons(self.close).Yes |
                                      QMessageBox.standardButtons(self.close).Cancel)
        close = self.close.exec()

        if close == QMessageBox.standardButtons(self.close).Yes:
            event.accept()
            self.close_all_windows()
        else:
            event.ignore()

    def close_all_windows(self):
        win_list = QApplication.allWindows()
        for w in win_list:
            w.close()


class RandomWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Параметры работы алгоритма")
        self.setFixedSize(300, 200)
        self.move(1000, 300)

        self.iterationWindow = IterationWindow()

        layout = QVBoxLayout()
        widgets = []

        self.label1 = QLabel("Максимальное кол-во итераций:")
        self.label1.adjustSize()
        widgets.append(self.label1)

        self.label2 = QLabel("Вероятность скрещевания:")
        self.label2.adjustSize()

        self.label3 = QLabel("Вероятность мутации:")
        self.label3.adjustSize()

        self.inputText1 = QLineEdit()
        widgets.append(self.inputText1)
        widgets.append(self.label2)
        self.inputText2 = QLineEdit()
        widgets.append(self.inputText2)
        widgets.append(self.label3)
        self.inputText3 = QLineEdit()
        widgets.append(self.inputText3)

        self.startButton = QPushButton("Запуск!")
        self.startButton.adjustSize()
        self.startButton.clicked.connect(self.startAlgorithm)
        widgets.append(self.startButton)

        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def startAlgorithm(self):
        self.iterationWindow.show()


class InputWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ввод данных")
        # self.setFixedSize(300, 500)
        self.move(1000, 300)

        layout = QVBoxLayout()
        layout.setSpacing(5)
        # layout.addStretch(1)
        # layout.setContentsMargins(0, 0, 0, 0)
        widgets = []

        self.label1 = QLabel("Введите вес рюкзака: ")
        widgets.append(self.label1)

        self.inputAmount = QLineEdit()
        widgets.append(self.inputAmount)

        self.label2 = QLabel("Далее введите данные в формате:\nВес Цена (каждый премедет с новой строки)")
        self.label2.adjustSize()
        widgets.append(self.label2)

        self.inputData = QPlainTextEdit()
        self.inputData.setFixedSize(200, 200)
        widgets.append(self.inputData)

        self.startButton = QPushButton("Запуск!")
        widgets.append(self.startButton)

        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


class IterationWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.iteration = 0
        self.someData = list()
        self.iterationLine = "Итерация № "

        self.setWindowTitle("Работа алгоритма")
        # self.setFixedSize(300, 500)
        # self.move(1000, 300)

        layout = QVBoxLayout()
        widgets = []

        self.iterationLabel = QLabel((self.iterationLine + str(self.iteration)))
        widgets.append(self.iterationLabel)
        self.dataLabel = QLabel("какая то дата")
        widgets.append(self.dataLabel)

        self.graphicLabel = QLabel()
        self.graphicAlgorithm = QPixmap('/Users/raregod/Downloads/cat.jpg')
        smaller_pixmap = self.graphicAlgorithm.scaled(250, 250, Qt.AspectRatioMode.KeepAspectRatio)
        self.graphicLabel.setPixmap(smaller_pixmap)
        widgets.append(self.graphicLabel)

        self.hLayout = QHBoxLayout()
        HWidgets = []

        self.backButton = QPushButton("<")
        HWidgets.append(self.backButton)
        self.forwardButton = QPushButton(">")
        HWidgets.append(self.forwardButton)
        self.finishButton = QPushButton(">>")
        HWidgets.append(self.finishButton)

        for w in HWidgets:
            self.hLayout.addWidget(w)

        for w in widgets:
            layout.addWidget(w)

        layout.addLayout(self.hLayout)
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

