import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from main import MainWindow

if __name__ == '__main__':
    app = QApplication([])
    icon = QIcon(r"Resource\logo.png")
    app.setWindowIcon(icon)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())