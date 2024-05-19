from PySide6.QtWidgets import QApplication, QMessageBox, QPushButton
from PySide6.QtCore import Slot
 
def show_message_box_and_get_button_click():
    app = QApplication([])
 
    # 创建一个消息框
    message_box = QMessageBox(QMessageBox.Information, "Message Box Title", "Message Box Text")
    message_box.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
 
    # 连接按钮点击信号到槽函数
    message_box.buttonClicked.connect(handle_button_click)
 
    # 显示消息框
    message_box.exec()
 
    # 应用运行
    app.exec()
 
@Slot(QPushButton)
def handle_button_click(button):
    if button.text() == "Yes":
        print("Ok button clicked")
    elif button.text() == "Cancel":
        print("Cancel button clicked")
 
if __name__ == "__main__":
    show_message_box_and_get_button_click()
