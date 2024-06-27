import sys  # Только для доступа к аргументам командной строки

from PyQt6.QtWidgets import QApplication

from src.gui import Window

if __name__ == "__main__":
    app = QApplication(sys.argv)

    wind = Window()
    wind.show()

    app.exec()
