# 标准库
import re
import os
import shutil
import datetime
from configparser import ConfigParser

# 第三方库
import numpy
import pandas as pd
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QMessageBox, QAbstractButton, QStyledItemDelegate, QComboBox, QListView
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
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "<span style='color:#ffff00;'> [DEBUG] </span>" + message
    elif Type == "INFO":
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "<span style='color:#00aa00;'> [Info] </span>" + message
    elif Type == "WARRING":
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "<span style='color:#ffaa00;'> [Waring] </span>" + message
    elif Type == "ERROR":
        return  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "<span style='color:#aa00ff;'> [Error] </span>" + message
    elif Type == "FATAL":
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "<span style='color:#ff0000;'> [Fatal] </span>" + message
    
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
    data.fillna(0, inplace=True)
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

def reNameImage(params):
    """
    批量将输入文件夹路径下的图片复制到输出路径并重命名。
    
    :param params: 字典，包含两个键：
                  'input_folder': 输入文件夹路径（str）
                  'output_folder': 输出图片路径（str）
    :return: 字典, 包含两个键:
              'reg': 成功标志，1表示成功，0表示失败（int）
              'msg': 错误信息，成功为空字符串，失败为错误提示（str）
    """
    IMAGEFORMAT = ['jpg', 'JPEG', 'png', 'gif', 'bmp']
    patternGel = r"\bGel\b"
    pattern_2 = r'\d{4}\s\d{2}\s\d{2}\s\d{2}H\s\d{2}M\s[A-H][0-9]*\s[.]'

    input_folder = params.get('input_folder')
    output_folder = params.get('output_folder')

    if not os.path.isdir(input_folder):
        return {'reg': 0, 'msg': f"输入路径 '{input_folder}' 不存在或不是文件夹"}

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        for filename in os.listdir(input_folder):
            if not re.search(pattern=pattern_2,string=filename):
                if not re.search(pattern=patternGel, string=filename.split(".")[0]):
                    if filename.split(".")[-1] in IMAGEFORMAT:  # 示例图片扩展名，可按需调整
                        # 获取原文件名中最后一个空格之后的内容作为新文件名
                        new_name = filename.split(' ')[-1]
                        src_path = os.path.join(input_folder, filename)
                        dest_path = os.path.join(output_folder, new_name)
                        
                        shutil.copy2(src_path, dest_path)  # 复制并保留元数据
        return {'reg': 1, 'msg': ""}
    except Exception as e:
        return {'reg': 0, 'msg': str(e)}
    

def caculateResult(DataFramePath:dict):
    '''
    判断5400结果，并输出为dataframe
    param: dict(DataFramePath)
    return: dict {"reg": 0, "msg": {"DataFrame": DataFrame}}
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
            SMEARTRAILING = "650 bp to 4000 bp"
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
            resultDataFrameColumn = getConfig("conf/config.ini", "Export Sheet Head", "Agilent")["msg"].split(",")

            resultDataFrame = pd.DataFrame(columns=resultDataFrameColumn)
            for sampleID in dupSampleIDList:
                sampleDataFrame = smearTable[smearTable["Sample ID"] == sampleID]
                wellID = sampleDataFrame.iloc[0]["Well"]
                mask1 = sampleDataFrame['Range'].str.contains(SMEARADAPTOR, na=False)
                mask2 = sampleDataFrame['Range'].str.contains(SMWAESMALLFRAG, na=False)
                mask3 = sampleDataFrame['Range'].str.contains(SMEARAVERAGWFRAG, na=False)
                mask4 = sampleDataFrame['Range'].str.contains(SMEARTRAILING, na=False)
                size = len(sampleDataFrame)
                # 检查需要做判断的SmearPeak是否存在
                if mask1.any() and mask2.any() and mask3.any() and mask4.any():
                    adaptorMolarity = sampleDataFrame.loc[sampleDataFrame["Range"]==SMEARADAPTOR,"nmole/L"].to_list()[0]*1000 # 从nmole/L转换为pmole/L
                    smallFragMolarity = sampleDataFrame.loc[sampleDataFrame["Range"]==SMWAESMALLFRAG,"nmole/L"].to_list()[0]*1000 # 从nmole/L转换为pmole/L
                    averageFragMolarity = sampleDataFrame.loc[sampleDataFrame["Range"]==SMEARAVERAGWFRAG,"nmole/L"].to_list()[0]*1000 # 从nmole/L转换为pmole/L
                    averageFragConc = sampleDataFrame.loc[sampleDataFrame["Range"]==SMEARAVERAGWFRAG,"ng/uL"].to_list()[0]*1000 # 从ng/uL转换为pg/uL
                    averageFragment = sampleDataFrame.loc[sampleDataFrame["Range"]==SMEARAVERAGWFRAG,"Avg. Size"].to_list()[0]
                    determineFragment = sampleDataFrame.loc[sampleDataFrame["Range"]==SMEARAVERAGWFRAG,"Avg. Size"].to_list()[0]
                    trailingFragment = sampleDataFrame.loc[sampleDataFrame["Range"]==SMEARTRAILING,"nmole/L"].to_list()[0]*1000 # 从nmole/L转换为pmole/L
                    # 计算占比情况
                    totalMolarity = int(adaptorMolarity + smallFragMolarity + averageFragMolarity)
                    adaptorPercentage = int(safeDivide(adaptorMolarity,totalMolarity))
                    smallFrafPercentage = int(safeDivide(smallFragMolarity,totalMolarity))
                    trailingPercentage = int(safeDivide(trailingFragment,totalMolarity))
                    # 判断样品是否合格
                    result = ""
                    judge = ""
                    # 摩尔浓度小于500pmol/L，判断无明显目的峰
                    if averageFragMolarity >= 500:
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
                        # 拖尾判定
                        if trailingPercentage >= 0.1:
                            if len(result) >0:
                                result += ";拖尾"
                            else:
                                result += "拖尾"
                        elif trailingPercentage < 0.1:
                            pass
                        # 综合判断
                        patternW = re.compile('^W')
                        patternCT = re.compile('^C|^T')
                        if len(result) == 0:
                            result += "无"
                            if patternW.match(sampleID):
                                judge += "成功"
                            elif patternCT.match(sampleID):
                                judge += "待反馈"
                            else:
                                judge += "成功"
                        elif len(result) > 0:
                            # 判断文库类型
                            if patternW.match(sampleID):
                                judge += "风险上机"
                            elif patternCT.match(sampleID):
                                judge += "待反馈"
                            else:
                                judge += "待反馈"
                        # 判定是否需要人工判定（Smear区间大于默认的4个）
                        if size > 4:
                            judge = "需要人工判定"
                            if len(result) >0:
                                result += ";多峰"
                            else:
                                result += "多峰"
                    else:
                        result = "无明显目的峰"
                        # 判断文库类型
                        patternW = re.compile('^W')
                        if patternW.match(sampleID):
                            judge += "风险上机"
                        else:
                            judge += "待反馈"
                    # 汇总结果，插入到新Dataframe中
                    excelDict = {"孔号":wellID,
                                "文库号":sampleID,
                                "片段大小":averageFragment,
                                "质量浓度":averageFragConc, 
                                "摩尔浓度":averageFragMolarity,
                                "结果":result,
                                "判定":judge,
                                "片段描述":numpy.nan,
                                "备注":numpy.nan,
                                "空列":numpy.nan,
                                "原始质量浓度":numpy.nan,
                                "原始摩尔浓度":numpy.nan,
                                "稀释倍数":numpy.nan
                                }
                    resultDataFrame = pd.concat([resultDataFrame,pd.DataFrame(excelDict,index=[0])])
                else:
                    # 汇总结果，插入到新Dataframe中
                    excelDict = {"孔号":wellID,
                                "文库号":sampleID,
                                "片段大小":"ERROR",
                                "质量浓度":"ERROR", 
                                "摩尔浓度":"ERROR",
                                "结果":"ERROR",
                                "判定":"ERROR",
                                "片段描述":numpy.nan,
                                "备注":numpy.nan,
                                "空列":numpy.nan,
                                "原始质量浓度":numpy.nan,
                                "原始摩尔浓度":numpy.nan,
                                "稀释倍数":numpy.nan
                                }
                    resultDataFrame = pd.concat([resultDataFrame,pd.DataFrame(excelDict,index=[0])])
            return {"reg":1, "msg":resultDataFrame}
        except FileNotFoundError:
            return {"reg":0, "msg":f"文件路径错误{FileNotFoundError}"}
        except IOError:
            return {"reg":0, "msg":IOError}

# 避免直接使用除法报错
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

# 配置下拉列表单选
class MyComboBoxDelegate(QStyledItemDelegate):  
    def __init__(self, item_list, parent=None):  
        super().__init__(parent)  
        self.item_list = item_list
  
    def createEditor(self, parent, option, index):  
        if index.column() == 1:  # 假设我们想要在第2列显示下拉列表  
            comboBox = QComboBox(parent)
            comboBox.addItems(self.item_list)  # 使用初始化时传入的item_list
            comboBox.setEditable(False)  # 禁止编辑框编辑
            return comboBox  
  
    def setEditorData(self, editor, index):  
        value = index.model().data(index, Qt.EditRole)  
        if isinstance(editor, QComboBox):  
            editor.setCurrentText(value)  
  
    def setModelData(self, editor, model, index):  
        if isinstance(editor, QComboBox):  
            model.setData(index, editor.currentText(), Qt.EditRole)  
  
    def updateEditorGeometry(self, editor, option, index):  
        editor.setGeometry(option.rect)  