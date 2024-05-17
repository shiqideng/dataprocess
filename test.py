'''
Author: dengshiqi shiqideng@genome.cn
Date: 2024-05-16 11:40:34
LastEditors: dengshiqi shiqideng@genome.cn
LastEditTime: 2024-05-17 14:06:43
FilePath: \dataprocess\test.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from PySide6.QtGui import QStandardItemModel, QStandardItem

def createModel(path: str) -> QStandardItemModel:
    """
    :param path: 文件路径
    :return: QStandardItemModel
    """
    # 初始化模型
    model = QStandardItemModel()
    # 初始化表格数据
    data = pd.read_csv(path)
    rows, columns = data.shape
    # 设置model表头
    model.setHorizontalHeaderLabels(list(data.columns))
    for row in range(rows):
        for col in range(columns):
            item = QStandardItem(str(data.iloc[row][col]))
            model.setItem(row, col, item)

    model.setColumnCount(columns)
    model.setRowCount(rows)
    return model