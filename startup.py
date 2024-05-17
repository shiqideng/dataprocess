'''
Author: dengshiqi shiqideng@genome.cn
Date: 2024-05-16 10:55:54
LastEditors: dengshiqi shiqideng@genome.cn
LastEditTime: 2024-05-16 11:34:42
FilePath: \dataprocess\startup.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from PySide6.QtWidgets import QApplication

from main import MainWindow

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show
    app.exec()