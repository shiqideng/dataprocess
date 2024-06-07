# 标准库
import datetime
from configparser import ConfigParser

# 第三方库
import pandas as pd
from openpyxl import load_workbook
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMessageBox, QAbstractButton
from PySide6.QtCore import Qt, Signal, Slot, QObject

# 本地库
import re


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
    
def getConfig(configPath: str, section: str, option: str) -> str:

    config = ConfigParser()
    try:
        config.read(configPath, encoding="utf-8")
        return {"reg": 1, "msg":config.get(section, option)}
    except Exception as e:
        return {"reg": 0, "msg": str(e)}

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
        data = detectEncoding(variable["path"])
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

def fomatResult(DataFrame:dict):
    '''格式化5400结果，并输出为dataframe
    : param DataFramePath: dict
    : return DataFrame
    '''
    pass

def caculateResult(DataFramePath:dict):
    '''判断5400结果，并输出为dataframe
    : param DataFramePath: dict
    : return dict {"reg": 0, "msg": {"DataFrame": DataFrame}}
    '''
    # progress_changed.emit(10)
    
    SampleType = DataFramePath["SampleType"]

    if SampleType == "核酸":
        try:
            qualityTable = detectEncoding(DataFramePath["qualityTablepath"])
            smearTable = detectEncoding(DataFramePath["smearTablepath"])
        except FileNotFoundError:
            return {"reg":0, "msg":f"文件路径错误{FileNotFoundError}"}
    elif SampleType == "文库":
        try:
            smearTable = detectEncoding(DataFramePath["smearTablepath"])
            column = ["Well","Sample ID","Range","ng/uL", "nmole/L", "Avg. Size"]
            SMEARADAPTOR="100 bp to 150 bp"
            SMWAESMALLFRAG = "150 bp to 260 bp"
            SMEARAVERAGWFRAG = "200 bp to 4000 bp"
            SMEARDETERMINEFRAG = "200 bp to 6000 bp"
            # 格式化样本数据，去除无SmearPeak的样本
            smearTable = smearTable.dropna(subset=["Range"])
            smearTable = smearTable.dropna(subset=["Sample ID"])
            smearTable = smearTable.loc[:,column]
            smearTable.fillna(0, inplace=True)

            # 获取样本名称输出一个列表
            newSmearTable = smearTable.duplicated(subset=["Sample ID"])
            newSmearTableIndex = newSmearTable[newSmearTable==False].index

            sampleIDList = smearTable.loc[newSmearTableIndex]["Sample ID"].to_list()

            # 去除列表中的空字符串
            dupSampleIDList = list(filter(lambda x: x == x, sampleIDList))
            # 设置表头
            resultDataFrameColumn = ["文库号","片段大小","质量浓度","摩尔浓度","结果","判定","片段描述","备注","空列","原始质量浓度","原始摩尔浓度","稀释倍数"]

            resultDataFrame = pd.DataFrame(columns=resultDataFrameColumn)

            for sampleID in dupSampleIDList:
                sampleDataFrame = smearTable[smearTable["Sample ID"] == sampleID]
                adaptorMolarity = sampleDataFrame.loc[smearTable["Range"]==SMEARADAPTOR,"nmole/L"].to_list()[0]
                smallFragMolarity = sampleDataFrame.loc[smearTable["Range"]==SMWAESMALLFRAG,"nmole/L"].to_list()[0]
                averageFragMolarity = sampleDataFrame.loc[smearTable["Range"]==SMEARAVERAGWFRAG,"nmole/L"].to_list()[0]
                averageFragConc = sampleDataFrame.loc[smearTable["Range"]==SMEARAVERAGWFRAG,"ng/uL"].to_list()[0]
                averageFragment = sampleDataFrame.loc[smearTable["Range"]==SMEARAVERAGWFRAG,"Avg. Size"].to_list()[0]
                determineFragment = sampleDataFrame.loc[smearTable["Range"]==SMEARDETERMINEFRAG,"Avg. Size"].to_list()[0]
                # 计算占比情况
                totalMolarity = adaptorMolarity + smallFragMolarity + averageFragMolarity
                adaptorPercentage = safeDivide(adaptorMolarity,totalMolarity)
                smallFrafPercentage = safeDivide(smallFragMolarity,totalMolarity)
                # 判断样品是否合格
                result = ""
                judge = ""
                # 接头二聚体情况判断
                if adaptorPercentage >= 0.03:
                    if len(result) >0:
                        result += ";接头二聚体污染"
                    else:
                        result += "接头二聚体污染"
                elif adaptorPercentage < 0.03:
                    pass
                # 小片段情况判断
                if smallFrafPercentage >= 0.1:
                    if len(result) >0:
                        result += ";小片段污染"
                    else:
                        result += "小片段污染"
                elif smallFrafPercentage < 0.1:
                    pass
                # 文库大小判断
                if determineFragment <260:
                    if len(result) >0:
                        result += ";文库偏小"
                    else:
                        result += "文库偏小"
                elif determineFragment > 650:
                    if len(result) >0:
                        result += ";文库偏大"
                    else:
                        result += "文库偏大"
                # 综合判断
                if len(result) == 0:
                    result += "无"
                    judge += "成功"
                elif len(result) > 0:
                    # 判断文库类型
                    pattern = re.compile('^W')
                    if pattern.match(sampleID):
                        judge += "风险上机"
                    else:
                        judge += "待反馈"
                # 汇总结果，插入到新Dataframe中
                excelDict = {"文库号":sampleID,
                            "片段大小":averageFragment,
                            "质量浓度":averageFragConc,
                            "摩尔浓度":averageFragMolarity,
                            "结果":result,
                            "判定":judge,
                            "片段描述":0,
                            "备注":0,
                            "空列":0,
                            "原始质量浓度":averageFragConc,
                            "原始摩尔浓度":averageFragMolarity,
                            "稀释倍数":1
                            }
                newPD = pd.DataFrame(excelDict, index=[0])
                newPD.fillna(0, inplace=True)
                resultDataFrame = pd.concat([resultDataFrame, newPD], ignore_index=True)
            return {"reg":1, "msg":resultDataFrame}
        except FileNotFoundError:
            return {"reg":0, "msg":f"文件路径错误{FileNotFoundError}"}
        except IOError:
            return {"reg":0, "msg":IOError}
        except Exception as e:
            return {"reg":0, "msg":e}

def safeDivide(numerator, denominator):  
    if denominator == 0:  
        return numerator / 1
    else:  
        return numerator / denominator

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