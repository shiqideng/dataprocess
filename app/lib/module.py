# 第三方库
from PySide6.QtGui import QStandardItemModel
from PySide6.QtWidgets import QMessageBox, QAbstractButton, QStyledItemDelegate, QComboBox
from PySide6.QtCore import Qt, Signal, Slot


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
