# 标准库
import datetime

# 第三方库
import pandas as pd
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMessageBox, QAbstractButton
from PySide6.QtCore import Qt, Signal, Slot

def detectEncoding(filePath):
    encodings = ['utf-8', 'utf-8-sig', 'utf-16', 'utf-16-le', 'utf-16-be', 'latin1']
    error_msg = "Unknown encoding"
    
    try:
        for encoding in encodings:
            try:
                df = pd.read_csv(filePath, encoding=encoding)
                return df
            except UnicodeDecodeError:
                pass
        raise UnicodeDecodeError(error_msg)
    except UnicodeDecodeError as e:
        if str(e) != error_msg:
            print(e)
        return None
    

def logFormat(Type, message):
    if Type == "DEBUG":
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "<span style='color:#ffff00;'> [Waring] </span>" + message
    elif Type == "INFO":
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "<span style='color:#00aa00;'> [INFO] </span>" + message
    elif Type == "WARRING":
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "<span style='color:#ffaa00;'> [Waring] </span>" + message
    elif Type == "ERROR":
        return  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "<span style='color:#aa00ff;'> [Error] </span>" + message
    elif Type == "FATAL":
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "<span style='color:#ff0000;'> [FATAL] </span>" + message

def createModel(variable: dict) -> QStandardItemModel:
    """
    :param path: {type, path} -> 类型：1 dataform， 2 file Path
    :return: QStandardItemModel
    """
    # 初始化模型
    model = MyQStandardItemModelModel()
    # 初始化表格数据
    if variable["type"] == 1:
        data = variable["path"]
    elif variable["type"] == 2:
        data = pd.read_csv(variable["path"])
    rows, columns = data.shape
    # 设置model表头
    model.setHorizontalHeaderLabels(list(data.columns))

    try:
        # 优化性能：尽量减少对data.iloc的重复调用
        for row in range(rows):
            # 提取一行数据到列表
            row_data = data.iloc[row].tolist()
            for col in range(columns):
                item = QStandardItem(str(row_data[col]))
                model.setItem(row, col, item)
    except IndexError:
        print("Error: Index out of bounds while accessing data.")
    except Exception as e:
        # 捕获其他潜在异常，比如类型转换错误等
        print(f"Error: An unexpected error occurred: {e}")


    model.setColumnCount(columns)
    model.setRowCount(rows)
    return model
def caculateResult(DataFramePath:dict):
    '''判断5400结果，并输出为dataframe
    : param DataFramePath: dict
    : return DataFrame
    '''
    SampleType = DataFramePath["SampleType"]
    if SampleType == "核酸":
        try:
            qualityTable = pd.read_csv(DataFramePath["qualityTablepath"])
            smearTable = pd.read_csv(DataFramePath["smearTablepath"])
            peakTable = pd.read_csv(DataFramePath["peakTablepath"])
        except FileNotFoundError:
            return {"reg":0, "msg":f"文件路径错误{FileNotFoundError}"}
    elif SampleType == "文库":
        try:
            qualityTable = pd.read_csv(DataFramePath["qualityTablepath"])
            smearTable = pd.read_csv(DataFramePath["smearTablepath"])
        except FileNotFoundError:
            return {"reg":0, "msg":f"文件路径错误{FileNotFoundError}"}
        except IOError:
            return {"reg":0, "msg":IOError}
        except Exception as e:
            return {"reg":0, "msg":e}
    else:
       return {"reg":0, "msg":"样本类型错误"}

def fomatResult(DataFrame:dict):
    '''格式化5400结果，并输出为dataframe
    : param DataFramePath: dict
    : return DataFrame
    '''
    pass


class MyQStandardItemModelModel(QStandardItemModel):
    """
    重写QStandardItemModel的data函数，使QTableView全部item居中
    """
    def data(self, index, role=None):
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        return QStandardItemModel.data(self, index, role)
    

class MessageBox(QMessageBox):
    resultReady = Signal(dict)

    def __init__(self, Icon, text):
        super().__init__()
        self.setWindowTitle("提示")
        self.setText(text)
        self.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        self.yes_button = self.button(QMessageBox.StandardButton.Yes)
        self.no_button = self.button(QMessageBox.StandardButton.No)
        self.yes_button.setText('是')  # 默认Yes按钮为“是”
        self.no_button.setText('否')  # 默认No按钮为“否”

        # 改进异常处理和验证Icon是否为有效枚举值
        if not hasattr(QMessageBox, Icon):
            raise ValueError(f"{Icon}不是有效的QMessageBox枚举值")
        iconValue = getattr(QMessageBox, Icon)
        self.setIcon(iconValue)
        self.show()

        # 绑定信号和槽
        self.buttonClicked.connect(self.handleButtonClicked)

    @Slot(QAbstractButton)
    def handleButtonClicked(self, button):
        # 根据点击的按钮提供相应的返回值
        if button.text() == "是":
            result = {"reg": 1, "msg": "用户点击了确定按钮"}
        elif button.text() == "否":
            result = {"reg": 0, "msg": "用户取消了操作"}
        else:
            result = {"reg": 0, "msg": "用户取消了操作"}
        self.resultReady.emit(result)  # 发出信号携带结果