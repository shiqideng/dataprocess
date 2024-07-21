import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QScrollArea
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建QScrollArea
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)

        # 创建QDockWidget作为可折叠的侧边栏
        dock = QDockWidget("Collapsible Sidebar", self)
        dock.setFeatures(QDockWidget.DockWidgetMovable)
        dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

        # 创建一个小部件作为QScrollArea的内容
        widget = QScrollArea()
        widget.setStyleSheet("background-color: blue;")

        # 设置QScrollArea的小部件
        scrollArea.setWidget(widget)
        dock.setWidget(scrollArea)

        # 将QDockWidget添加到主窗口
        self.addDockWidget(Qt.RightDockWidgetArea, dock)

        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('Floating Collapsible Sidebar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    sys.exit(app.exec())