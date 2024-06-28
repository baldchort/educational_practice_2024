from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QCloseEvent
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QLineEdit, QLabel, QDialog, \
    QFileDialog, QPlainTextEdit, QHBoxLayout, QMessageBox


class Window(QMainWindow):
    def __init__(self):
        super().__init__()  # наследуем от QMainWindow

        self.inputFileName = '~/'

        # Окно ввода вручную
        self.inputWindow = InputWindow()
        # Окно работы алгоритма
        self.iterationWindow = IterationWindow()
        # Окно параметров алгоритма
        self.algParamsWindow = AlgParamsWindow()

        # Название окна
        self.setWindowTitle("Задача о рюкзаках")
        # Размер окна
        self.setFixedSize(400, 300)

        # Вертикальная разметка виджетов
        layout = QVBoxLayout()
        # Массив виджетов (все виджеты, которые будут на этом окне)
        main_window_widgets = []

        # Создаем кнопку ввода параметров алгоритма
        # Добавляем в виджеты
        # Привязываем к событию clicked ивент paramsButtonEvent
        params_button = QPushButton("Параметры работы алгоритма")
        main_window_widgets.append(params_button)
        params_button.clicked.connect(self.paramsButtonEvent)

        # Создаем кнопку закгрузки данных из файла
        # Добавляем в виджеты
        # Привязываем к событию clicked ивент browseEvent
        browse_file_button = QPushButton("Загрузить данные из файла")
        browse_file_button.clicked.connect(self.browseEvent)
        main_window_widgets.append(browse_file_button)

        # Создаем кнопку ввода вручную
        # Добавляем в виджеты
        # Привязываем к событию clicked ивент paramsButtonEvent
        input_button = QPushButton("Ввод данных вручную")
        input_button.clicked.connect(self.InputButtonEvent)
        main_window_widgets.append(input_button)

        # Добавляем в разметку все наши элементы
        for w in main_window_widgets:
            layout.addWidget(w)

        # Превращаем нашу разметку в один большой виджет
        widget = QWidget()
        widget.setLayout(layout)

        # Устанавливаем центральный виджет окна. Виджет будет расширяться по умолчанию,
        # заполняя всё пространство окна.
        self.setCentralWidget(widget)

    # Обработка сигнала clicked для кнопки 1
    def paramsButtonEvent(self):
        self.algParamsWindow.show()

    # Обработка сигнала clicked для кнопки 2
    # Открываем диалог (выбор файла)
    def browseEvent(self):
        file_name = QFileDialog.getOpenFileName(self, 'Открыть файл', '~/')
        self.inputFileName = file_name[0]
        print(self.inputFileName)

        self.iterationWindow.show()

    # Обработка сигнала clicked для кнопки 3
    def InputButtonEvent(self):
        self.inputWindow.show()

    # Ивент запуска окна с алгоритмом
    def startAlgorithm(self):
        self.iterationWindow.show()

    # Ивент закрытия главного окна
    def closeEvent(self, event: QCloseEvent) -> None:
        closing_MB = QMessageBox(self)
        closing_MB.setText("Закрыть приложение?")
        closing_MB.setStandardButtons(QMessageBox.standardButtons(closing_MB).Yes |
                                      QMessageBox.standardButtons(closing_MB).Cancel)
        closed = closing_MB.exec()

        if closed == QMessageBox.standardButtons(closing_MB).Yes:
            event.accept()
            close_all_windows()
        else:
            event.ignore()


# Функция закрытия всех окон
def close_all_windows():
    win_list = QApplication.allWindows()
    for w in win_list:
        w.close()


class AlgParamsWindow(QMainWindow):
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
        self.close()
        self.iterationWindow.show()


class InputWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.iterationAlg = IterationWindow()

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
        self.startButton.clicked.connect(self.startAlg)
        widgets.append(self.startButton)

        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def startAlg(self):
        self.close()
        self.iterationAlg.show()


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
