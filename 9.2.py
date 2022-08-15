from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                          QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                         QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                         QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1060, 780)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(266, 82, 256, 192))
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(12, 486, 93, 28))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(12, 82, 73, 22))
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(12, 408, 65, 20))
        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(12, 434, 44, 20))
        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(12, 460, 52, 20))
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(12, 334, 95, 20))
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(12, 360, 95, 20))
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(237, 82, 23, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(12, 386, 61, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(12, 110, 33, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(12, 209, 46, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(12, 308, 20, 16))
        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(51, 308, 81, 20))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(12, 181, 137, 22))
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(12, 280, 86, 22))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(138, 486, 93, 28))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1060, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Python", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"C#", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Java", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Languages", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Birthday", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Car", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)




data =   [
        {
            "name": "John Smith",
            "birthday": "02.10.1990",
            "height": 175,
            "weight": 76.5,
            "car": True,
            "languages": ["C++", "Python"]
        },
        {
            "name": "Alexey Alexeev",
            "birthday": "05.06.1986",
            "height": 197,
            "weight": 101.2,
            "car": False,
            "languages": ["Pascal", "Delphi"]
        },
        {
            "name": "Maria Ivanova",
            "birthday": "28.08.1998",
            "height": 165,
            "weight": 56.1,
            "car": True,
            "languages": ["C#", "C++", "C"]
        }
    ]

# for i in data:
#     print(i)
# print(data[1]['name'])
#
# data2 = ['asd','safd']
# row = 0
# col = 0
#
# for item in data2:
#     cellinfo = QTableWidgetItem(item)
#     Ui_MainWindow.tableWidget.setItem(row, col, cellinfo)
#     col += 1
#
# row += 1


# def print_data_to_table():
#     row = 0
#     for i in data:
#         col = 0
#
#         for item in data:
#             cellinfo = QTableWidgetItem(item)
#             self.ui.tableWidget.setItem(row, col, cellinfo)
#             col += 1
#
#         row += 1





app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
