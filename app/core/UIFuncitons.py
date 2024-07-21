# 标准库

# 第三方库
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QPropertyAnimation, QEasingCurve
from PySide6.QtGui import *
from PySide6.QtWidgets import *

# 本地库


class UIFuncitons(QMainWindow):
    # Expand left menu
    # self.ui.Hide.clicked.connect(lambda:UIFuncitons.toggleMenu(self.ui,True))
    def toggleMenu(self, enable):
        if enable:
            # 未伸缩宽68
            standard = 68
            # 伸缩后200
            maxExtend = 200
            # 获取当前侧边栏LeftBar的宽
            width = self.LeftBar.width()
            # 判段伸缩后的侧边栏宽度
            if width == 200:
                widthExtended = standard

            else:
                widthExtended = maxExtend
            # 动画实现
            # animation
            self.animation = QPropertyAnimation(self.LeftBar, b"minimumWidth")
            self.animation.setDuration(500)  # ms
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuint)
            self.animation.start()


