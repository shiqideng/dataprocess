# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTabWidget, QTableView,
    QTextBrowser, QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 548)
        Form.setLayoutDirection(Qt.LeftToRight)
        Form.setStyleSheet(u"QMainWindow {\n"
"  border-radius: 200px;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(20, -1, 20, 20)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 15, 40, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(32)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Select5400label = QLabel(Form)
        self.Select5400label.setObjectName(u"Select5400label")
        font = QFont()
        font.setPointSize(9)
        self.Select5400label.setFont(font)

        self.horizontalLayout_3.addWidget(self.Select5400label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Import5400FilePathLineEdit = QLineEdit(Form)
        self.Import5400FilePathLineEdit.setObjectName(u"Import5400FilePathLineEdit")
        self.Import5400FilePathLineEdit.setFont(font)

        self.horizontalLayout_2.addWidget(self.Import5400FilePathLineEdit)

        self.Import5400FilePathToolButton = QToolButton(Form)
        self.Import5400FilePathToolButton.setObjectName(u"Import5400FilePathToolButton")

        self.horizontalLayout_2.addWidget(self.Import5400FilePathToolButton)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Export5400Label = QLabel(Form)
        self.Export5400Label.setObjectName(u"Export5400Label")
        self.Export5400Label.setFont(font)

        self.horizontalLayout_5.addWidget(self.Export5400Label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Export5400FilePathLineEdit = QLineEdit(Form)
        self.Export5400FilePathLineEdit.setObjectName(u"Export5400FilePathLineEdit")
        self.Export5400FilePathLineEdit.setFont(font)

        self.horizontalLayout_4.addWidget(self.Export5400FilePathLineEdit)

        self.Export5400FilePathToolButton = QToolButton(Form)
        self.Export5400FilePathToolButton.setObjectName(u"Export5400FilePathToolButton")

        self.horizontalLayout_4.addWidget(self.Export5400FilePathToolButton)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_7.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 15, -1, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 10, -1)
        self.SampleType5400label = QLabel(Form)
        self.SampleType5400label.setObjectName(u"SampleType5400label")
        self.SampleType5400label.setFont(font)

        self.horizontalLayout_6.addWidget(self.SampleType5400label)

        self.SampleType5400ComboBox = QComboBox(Form)
        self.SampleType5400ComboBox.addItem("")
        self.SampleType5400ComboBox.addItem("")
        self.SampleType5400ComboBox.setObjectName(u"SampleType5400ComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SampleType5400ComboBox.sizePolicy().hasHeightForWidth())
        self.SampleType5400ComboBox.setSizePolicy(sizePolicy)
        self.SampleType5400ComboBox.setMinimumSize(QSize(80, 0))
        self.SampleType5400ComboBox.setMaximumSize(QSize(16777215, 16777215))
        self.SampleType5400ComboBox.setFont(font)
        self.SampleType5400ComboBox.setStyleSheet(u"")
        self.SampleType5400ComboBox.setEditable(False)
        self.SampleType5400ComboBox.setDuplicatesEnabled(False)

        self.horizontalLayout_6.addWidget(self.SampleType5400ComboBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.ReName5400CheckBox = QCheckBox(Form)
        self.ReName5400CheckBox.setObjectName(u"ReName5400CheckBox")
        self.ReName5400CheckBox.setLayoutDirection(Qt.LeftToRight)
        self.ReName5400CheckBox.setAutoFillBackground(True)
        self.ReName5400CheckBox.setInputMethodHints(Qt.ImhHiddenText)
        self.ReName5400CheckBox.setChecked(True)
        self.ReName5400CheckBox.setTristate(False)

        self.verticalLayout_2.addWidget(self.ReName5400CheckBox)

        self.Waring5400Label = QLabel(Form)
        self.Waring5400Label.setObjectName(u"Waring5400Label")
        font1 = QFont()
        font1.setBold(True)
        font1.setUnderline(True)
        self.Waring5400Label.setFont(font1)
        self.Waring5400Label.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_2.addWidget(self.Waring5400Label)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(40, -1, 40, 20)
        self.Preview5400PushButton = QPushButton(Form)
        self.Preview5400PushButton.setObjectName(u"Preview5400PushButton")

        self.horizontalLayout.addWidget(self.Preview5400PushButton)

        self.Start5400PushButton = QPushButton(Form)
        self.Start5400PushButton.setObjectName(u"Start5400PushButton")

        self.horizontalLayout.addWidget(self.Start5400PushButton)

        self.Export5400PushButton = QPushButton(Form)
        self.Export5400PushButton.setObjectName(u"Export5400PushButton")

        self.horizontalLayout.addWidget(self.Export5400PushButton)

        self.Clear5400PushButton = QPushButton(Form)
        self.Clear5400PushButton.setObjectName(u"Clear5400PushButton")

        self.horizontalLayout.addWidget(self.Clear5400PushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.QTabWidget5400 = QTabWidget(Form)
        self.QTabWidget5400.setObjectName(u"QTabWidget5400")
        font2 = QFont()
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.QTabWidget5400.setFont(font2)
        self.QTabWidget5400.setStyleSheet(u"\u3001")
        self.QTabWidget5400.setTabBarAutoHide(False)
        self.SmearTable5400tab = QWidget()
        self.SmearTable5400tab.setObjectName(u"SmearTable5400tab")
        self.gridLayout_3 = QGridLayout(self.SmearTable5400tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.SmearTable5400TableView = QTableView(self.SmearTable5400tab)
        self.SmearTable5400TableView.setObjectName(u"SmearTable5400TableView")
        self.SmearTable5400TableView.setStyleSheet(u"QTableView {\n"
"	border-radius: 10px;  /* \u8bbe\u7f6e\u5706\u89d2\u7684\u50cf\u7d20\u503c*/\n"
"	background-color: white; /* \u80cc\u666f\u8272*/\n"
"	\n"
"}\n"
"QHeaderView::section {\n"
"	border: 1px solid #D8D8D8;  /* \u5206\u533a\u7ebf\u7684\u989c\u8272\u548c\u5bbd\u5ea6*/\n"
"	background-color: #F8F8F8; /* \u8868\u5934\u80cc\u666f\u8272	*/\n"
"	border: 1px solid #D8D8D8; /* \u5206\u533a\u7ebf\u7684\u989c\u8272\u548c\u5bbd\u5ea6*/\n"
"	padding-left: 5px; /* \u5185\u8fb9\u8ddd*/\n"
"	/* border-radius: 10px; /* \u8bbe\u7f6e\u5706\u89d2\u7684\u50cf\u7d20\u503c*/\n"
"	text-align: center;\n"
"}")

        self.gridLayout_3.addWidget(self.SmearTable5400TableView, 0, 0, 1, 1)

        self.QTabWidget5400.addTab(self.SmearTable5400tab, "")
        self.QualityTabletab = QWidget()
        self.QualityTabletab.setObjectName(u"QualityTabletab")
        self.gridLayout_5 = QGridLayout(self.QualityTabletab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.QualityTable5400TableView = QTableView(self.QualityTabletab)
        self.QualityTable5400TableView.setObjectName(u"QualityTable5400TableView")
        self.QualityTable5400TableView.setStyleSheet(u"QTableView {\n"
"	border-radius: 10px;  /* \u8bbe\u7f6e\u5706\u89d2\u7684\u50cf\u7d20\u503c*/\n"
"	background-color: white; /* \u80cc\u666f\u8272*/\n"
"}\n"
"QHeaderView::section {\n"
"	border: 1px solid #D8D8D8;  /* \u5206\u533a\u7ebf\u7684\u989c\u8272\u548c\u5bbd\u5ea6*/\n"
"	background-color: #F8F8F8; /* \u8868\u5934\u80cc\u666f\u8272	*/\n"
"	border: 1px solid #D8D8D8; /* \u5206\u533a\u7ebf\u7684\u989c\u8272\u548c\u5bbd\u5ea6*/\n"
"	padding-left: 5px; /* \u5185\u8fb9\u8ddd*/\n"
"}")

        self.gridLayout_5.addWidget(self.QualityTable5400TableView, 0, 0, 1, 1)

        self.QTabWidget5400.addTab(self.QualityTabletab, "")
        self.PeakTable5400tab = QWidget()
        self.PeakTable5400tab.setObjectName(u"PeakTable5400tab")
        self.gridLayout_2 = QGridLayout(self.PeakTable5400tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.PeakTable5400TableView = QTableView(self.PeakTable5400tab)
        self.PeakTable5400TableView.setObjectName(u"PeakTable5400TableView")
        self.PeakTable5400TableView.setStyleSheet(u"QTableView {\n"
"	border-radius: 10px;  /* \u8bbe\u7f6e\u5706\u89d2\u7684\u50cf\u7d20\u503c*/\n"
"	background-color: white; /* \u80cc\u666f\u8272*/\n"
"}\n"
"QHeaderView::section {\n"
"	border: 1px solid #D8D8D8;  /* \u5206\u533a\u7ebf\u7684\u989c\u8272\u548c\u5bbd\u5ea6*/\n"
"	background-color: #F8F8F8; /* \u8868\u5934\u80cc\u666f\u8272	*/\n"
"	border: 1px solid #D8D8D8; /* \u5206\u533a\u7ebf\u7684\u989c\u8272\u548c\u5bbd\u5ea6*/\n"
"	padding-left: 5px; /* \u5185\u8fb9\u8ddd*/\n"
"}")

        self.gridLayout_2.addWidget(self.PeakTable5400TableView, 0, 0, 1, 1)

        self.QTabWidget5400.addTab(self.PeakTable5400tab, "")
        self.ResultTable5400tab = QWidget()
        self.ResultTable5400tab.setObjectName(u"ResultTable5400tab")
        self.gridLayout = QGridLayout(self.ResultTable5400tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ResultTable5400TableView = QTableView(self.ResultTable5400tab)
        self.ResultTable5400TableView.setObjectName(u"ResultTable5400TableView")
        self.ResultTable5400TableView.setStyleSheet(u"QTableView {\n"
"	border-radius: 10px;  /* \u8bbe\u7f6e\u5706\u89d2\u7684\u50cf\u7d20\u503c*/\n"
"	background-color: white; /* \u80cc\u666f\u8272*/\n"
"}\n"
"QHeaderView::section {\n"
"	border: 1px solid #D8D8D8;  /* \u5206\u533a\u7ebf\u7684\u989c\u8272\u548c\u5bbd\u5ea6*/\n"
"	background-color: #F8F8F8; /* \u8868\u5934\u80cc\u666f\u8272	*/\n"
"	border: 1px solid #D8D8D8; /* \u5206\u533a\u7ebf\u7684\u989c\u8272\u548c\u5bbd\u5ea6*/\n"
"	padding-left: 5px; /* \u5185\u8fb9\u8ddd*/\n"
"	border-radius: 10px; /* \u8bbe\u7f6e\u5706\u89d2\u7684\u50cf\u7d20\u503c*/\n"
"}")

        self.gridLayout.addWidget(self.ResultTable5400TableView, 0, 0, 1, 1)

        self.QTabWidget5400.addTab(self.ResultTable5400tab, "")
        self.logTab = QWidget()
        self.logTab.setObjectName(u"logTab")
        self.gridLayout_4 = QGridLayout(self.logTab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.logTextBrowser = QTextBrowser(self.logTab)
        self.logTextBrowser.setObjectName(u"logTextBrowser")

        self.gridLayout_4.addWidget(self.logTextBrowser, 0, 0, 1, 1)

        self.QTabWidget5400.addTab(self.logTab, "")

        self.verticalLayout_4.addWidget(self.QTabWidget5400)


        self.retranslateUi(Form)
        self.ReName5400CheckBox.clicked["bool"].connect(self.Waring5400Label.setVisible)

        self.QTabWidget5400.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"DataProcess", None))
        self.Select5400label.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u5939\u8def\u5f84\uff1a", None))
        self.Import5400FilePathToolButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.Export5400Label.setText(QCoreApplication.translate("Form", u"\u7ed3\u679c\u4fdd\u5b58\u8def\u5f84\uff1a", None))
        self.Export5400FilePathToolButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.SampleType5400label.setText(QCoreApplication.translate("Form", u"\u6837\u672c\u7c7b\u578b\uff1a", None))
        self.SampleType5400ComboBox.setItemText(0, QCoreApplication.translate("Form", u"\u6587\u5e93", None))
        self.SampleType5400ComboBox.setItemText(1, QCoreApplication.translate("Form", u"\u6838\u9178", None))

        self.ReName5400CheckBox.setText(QCoreApplication.translate("Form", u"\u56fe\u7247\u91cd\u547d\u540d", None))
        self.Waring5400Label.setText(QCoreApplication.translate("Form", u"\u63d0\u793a\uff1a\u52fe\u9009\u540e\u5c06\u91cd\u547d\u540d\u56fe\u7247", None))
        self.Preview5400PushButton.setText(QCoreApplication.translate("Form", u"\u9884\u89c8", None))
        self.Start5400PushButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u5904\u7406", None))
        self.Export5400PushButton.setText(QCoreApplication.translate("Form", u"\u5bfc\u51fa\u7ed3\u679c", None))
        self.Clear5400PushButton.setText(QCoreApplication.translate("Form", u"\u6e05\u9664", None))
        self.QTabWidget5400.setTabText(self.QTabWidget5400.indexOf(self.SmearTable5400tab), QCoreApplication.translate("Form", u"Smear Table", None))
        self.QTabWidget5400.setTabText(self.QTabWidget5400.indexOf(self.QualityTabletab), QCoreApplication.translate("Form", u"Quality Table", None))
        self.QTabWidget5400.setTabText(self.QTabWidget5400.indexOf(self.PeakTable5400tab), QCoreApplication.translate("Form", u"Peak Table", None))
        self.QTabWidget5400.setTabText(self.QTabWidget5400.indexOf(self.ResultTable5400tab), QCoreApplication.translate("Form", u"\u7ed3\u679c\u9884\u89c8", None))
        self.logTextBrowser.setMarkdown("")
        self.logTextBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.QTabWidget5400.setTabText(self.QTabWidget5400.indexOf(self.logTab), QCoreApplication.translate("Form", u"\u65e5\u5fd7", None))
    # retranslateUi

