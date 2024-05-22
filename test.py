import sys
from PySide6.QtWidgets import QApplication, QTabWidget, QPushButton, QWidget, QVBoxLayout, QTabBar
 
class TabWidgetExample(QTabWidget):
    def __init__(self):
        super().__init__()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        
        self.tab1.setObjectName('Tab1')
        self.tab2.setObjectName('Tab2')
        
        self.addTab(self.tab1, 'Tab 1')
        self.addTab(self.tab2, 'Tab 2')
        
        self.button = QPushButton('Hide Tab 2')
        self.button.clicked.connect(self.toggle_tab)
        
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)
    
    def toggle_tab(self):
        tab_bar = self.tabBar()
        if tab_bar.isTabEnabled(1):
            tab_bar.setTabEnabled(1, False)
            self.tab2.hide()
            self.button.setText('Show Tab 2')
            self.button.clicked.disconnect()
            self.button.clicked.connect(self.toggle_tab)
        else:
            tab_bar.setTabEnabled(1, True)
            self.tab2.show()
            self.button.setText('Hide Tab 2')
            self.button.clicked.disconnect()
            self.button.clicked.connect(self.toggle_tab)
 
app = QApplication(sys.argv)
window = TabWidgetExample()
window.show()
sys.exit(app.exec_())