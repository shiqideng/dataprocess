import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import QCoreApplication

from core.main import MainWindow
from lib.logger import uploadLogToServer

if __name__ == '__main__':
    app = QApplication([])
    icon = QIcon(r"Resource\logo.png")
    app.setWindowIcon(icon)
    window = MainWindow()
    window.show()
    QCoreApplication.instance().aboutToQuit.connect(lambda: uploadLogToServer('log/log.log'))
    sys.exit(app.exec())