# 标准库
import sys
import glob


# 第三方库
from PySide6.QtWidgets import QApplication,  QWidget, QFileDialog, QTableWidget, QTableWidgetItem
from PySide6.QtCore import QStandardPaths, Slot
from PySide6.QtGui import QStandardItemModel, QStandardItem
import pandas as pd

# 本地包
from UI.Ui_MainWindow import Ui_Form
from DataOperation import Module
import test

class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # self.tabWidget.setTabEnabled(2, False)
        self.Import5400FilePathLineEdit.setText(r"C:\Users\shiqideng\OneDrive\桌面\test\5400\RNA\20240321")
        self.run()

    def run(self):
        # 使用lambda函数来传递参数
        self.Import5400FilePathToolButton.clicked.connect(lambda: self.selectFile("Import5400FilePathLineEdit"))
        self.Export5400FilePathToolButton.clicked.connect(lambda: self.selectFile("Export5400FilePathLineEdit"))
        self.Preview5400PushButton.clicked.connect(self.preview5400)
        self.Start5400PushButton.clicked.connect(self.start5400)
        self.Export5400PushButton.clicked.connect(self.export5400)
        self.Clear5400PushButton.clicked.connect(self.clear5400)

    @Slot(str)
    def selectFile(self, lineEditName):
        defaultPath = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        filePath = QFileDialog.getExistingDirectory(self, "选取文件夹", defaultPath)
        if filePath:
            getattr(self, lineEditName).setText(filePath)
        else:
            self.logTextBrowser.append(Module.logFormat("INFO" ,"用户取消了文件夹选择操作或出现了错误。"))

    def start5400(self):
        pass

    def export5400(self):
        pass

    def clear5400(self):
        self.Export5400FilePathLineEdit.clear()
        self.Import5400FilePathLineEdit.clear()

    def preview5400(self):
        if self.Import5400FilePathLineEdit.text():
            try:
                filePath = CreateModule({"path": self.Import5400FilePathLineEdit.text(), "SampleType":self.SampleType5400ComboBox.currentText()})
                filePath = filePath.getFilePath()
                if filePath["reg"] == 1:
                    if self.SampleType5400ComboBox.currentText() == "核酸":
                        self.logTextBrowser.append(Module.logFormat("INFO", "qualityTablePath:" + str(filePath["msg"]["qualityTable"])))
                        self.logTextBrowser.append(Module.logFormat("INFO", "smearTablePath:" + str(filePath["msg"]["smearTable"])))
                        self.logTextBrowser.append(Module.logFormat("INFO", "peakTablePath:" + str(filePath["msg"]["peakTable"])))

                        qualityTablePath = filePath["msg"]["qualityTable"]
                        quality = self.createModel(qualityTablePath)
                        self.QualityTable5400TableView.setModel(quality)

                        smearTablePath = filePath["msg"]["smearTable"]
                        smear = self.createModel(smearTablePath)
                        self.SmearTable5400TableView.setModel(smear)

                        peakTablePath = filePath["msg"]["qualityTable"]
                        peak =self.createModel(peakTablePath)
                        self.PeakTable5400TableView.setModel(peak)

                    elif self.SampleType5400ComboBox.currentText() == "文库":
                        self.logTextBrowser.append(Module.logFormat("INFO", "qualityTablePath:" + str(filePath["msg"]["qualityTable"])))
                        self.logTextBrowser.append(Module.logFormat("INFO", "smearTablePath:" + str(filePath["msg"]["smearTable"])))

                        qualityTablepath = filePath["msg"]["qualityTable"]
                        quality = self.createModel(qualityTablepath)
                        self.QualityTable5400TableView.setModel(quality)

                        smearTablepath = filePath["msg"]["smearTable"]
                        smear = self.createModel(smearTablepath)
                        self.SmearTable5400TableView.setModel(smear)
                else:
                    self.logTextBrowser.append(Module.logFormat("ERROR", str(filePath["msg"])))
            except IOError:
                self.logTextBrowser.append(Module.logFormat("ERROR", "部分文件存在异常"+ str(IOError)))
            except ValueError:
                self.logTextBrowser.append(Module.logFormat("ERROR", "发生意外错误"+ str(ValueError)))
        else:
            self.logTextBrowser.append(Module.logFormat("ERROR", "请选择导入文件路径。"))

    def createModel(self, path: str) -> QStandardItemModel:
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

class CreateModule:
    def __init__(self, filePath: dict) -> None:
        self.filePath = filePath["path"]
        self.sampleType = filePath["SampleType"]

    def getFilePath(self) -> dict:
        """从文件夹中筛选出需要分析的文件。

        :return: 分析所需的文件信息
        """
        # 输入校验
        if not self.valiDateSampleType():
            print("无效的样本类型。")
            return {"reg": 0, "msg": "无效的样本类型"}

        # 定义文件名常量
        PEAKTABLEFILE = "Peak Table.csv"
        SMEARTABLEFILE = "Smear Analysis Result.csv"
        QUALITYTABLEFILE = "Quality Table.csv"

        peakTable = ""

        try:
            # 搜索文件并进行异常处理
            smearTable = self.findFileInPath(self.filePath, SMEARTABLEFILE)[0]
            if not smearTable:
                print(f"未找到 {SMEARTABLEFILE}。")
                return {"reg": 0, "msg": f"未找到 {SMEARTABLEFILE}"}

            qualityTable = self.findFileInPath(self.filePath, QUALITYTABLEFILE)[0]
            if not qualityTable:
                print(f"未找到 {QUALITYTABLEFILE}。")
                return {"reg": 0, "msg": f"未找到 {QUALITYTABLEFILE}"}

            if self.sampleType == "核酸":
                peakTable = self.findFileInPath(self.filePath, PEAKTABLEFILE)[0]
                if not peakTable:
                    print(f"未找到 {PEAKTABLEFILE}。")
                    return {"reg": 0, "msg": f"未找到 {PEAKTABLEFILE}"}
            if self.sampleType == "文库":
                return {"reg": 1, "msg": {"smearTable": smearTable, "qualityTable": qualityTable}}
            elif self.sampleType == "核酸":
                return {"reg": 1, "msg": {"smearTable": smearTable, "qualityTable": qualityTable, "peakTable": peakTable}}
        except Exception as e:
            # 对潜在的异常进行处理
            print(f"处理文件时发生错误：{e}")
            return {"reg": 0, "msg": e}

    def valiDateSampleType(self):
        """验证样本类型是否有效。

        :param sampletype: 样本类型
        :return: True 如果样本类型有效，否则 False
        """
        validTypes = {"核酸", "文库"}  # 定义有效样本类型集合
        return self.sampleType in validTypes

    def findFileInPath(self, path: str, filename: str) -> list[str]:
        """搜索指定路径下的文件。

        :param path: 文件夹路径
        :param filename: 文件名
        :return: 文件的完整路径列表
        """
        folderPath = path
        partialFileName = filename
        filePath = []
        a = f'{folderPath}/*{partialFileName}'
        for file in glob.iglob(f'{folderPath}/*{partialFileName}'):
            filePath.append(file)
        return filePath


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())