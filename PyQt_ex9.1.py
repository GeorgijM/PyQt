from PyQt5.QtCore import (QCoreApplication, QMetaObject,
                          QRect, Qt, QDate)
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import json
import sys
import os

# PyQt options for window's dispaly
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(978, 694)
        MainWindow.setToolTipDuration(-1)
        self.action1 = QAction(MainWindow)
        self.action1.setObjectName(u"action1")
        self.actionShow_all = QAction(MainWindow)
        self.actionShow_all.setObjectName(u"actionShow_all")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 2)

        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")

        self.gridLayout.addWidget(self.toolButton, 0, 3, 1, 1)

        self.toolButton_2 = QToolButton(self.centralwidget)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.gridLayout.addWidget(self.toolButton_2, 0, 4, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 4, 0, 1, 2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(300)
        self.spinBox.setValue(300)

        self.gridLayout.addWidget(self.spinBox, 6, 0, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.gridLayout.addWidget(self.spinBox_2, 8, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout.addWidget(self.checkBox_4, 9, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 10, 0, 1, 2)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 11, 0, 1, 2)

        self.checkBox_2 = QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 12, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout.addWidget(self.checkBox_3, 13, 0, 1, 2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 14, 0, 1, 2)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 14, 2, 1, 2)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        # self.lineEdit.setFocusPolicy(Qt.NoFocus)
        # self.lineEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit.setMaxLength(32774)
        # self.lineEdit.setEchoMode(QLineEdit.NoEcho)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 4)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(6)

        self.gridLayout.addWidget(self.tableWidget, 0, 5, 15, 1)

        self.horizontalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 978, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.pushButton, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.checkBox_2)
        QWidget.setTabOrder(self.checkBox_2, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.checkBox_3)
        QWidget.setTabOrder(self.checkBox_3, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.toolButton)
        QWidget.setTabOrder(self.toolButton, self.checkBox_4)
        QWidget.setTabOrder(self.checkBox_4, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.dateEdit)
        QWidget.setTabOrder(self.dateEdit, self.pushButton_2)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionShow_all)
        self.menu.addSeparator()
        self.menu.addAction(self.action1)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action1.setText(QCoreApplication.translate("MainWindow", u"Reset data to default", None))
        self.actionShow_all.setText(QCoreApplication.translate("MainWindow", u"Show all", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Birthday", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Weight", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Car", None))
        self.checkBox_4.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Languages", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Python", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"C#", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Java", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Birtday", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Height", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Weight", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Car", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Languages", None));
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi


# person's charackteristics
data = [
    {
        "name": "John Smith",
        "birthday": "02.10.1990",
        "height": 175,
        "weight": 76.5,
        "car": True,
        "languages": ["C#", "Python"]
    },
    {
        "name": "Alexey Alexeev",
        "birthday": "05.06.1986",
        "height": 197,
        "weight": 101.2,
        "car": False,
        "languages": ["Java", "Python"]
    },
    {
        "name": "Maria Ivanova",
        "birthday": "28.08.1998",
        "height": 165,
        "weight": 56.1,
        "car": True,
        "languages": ["C#", "Java", "Python"]
    }
]
# for usage when restoring from menu button
default_data = data.copy()

#creating data.json file for the first launch
if os.path.exists('data.json') == False:
    with open('data.json', 'w') as file_json:
        json.dump(data, file_json, indent=1)



# updating data if it was changed in previously session
with open('data.json', 'r') as file_add_json:
    data = json.load(file_add_json)


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.row = 0

    # running when press 'Show all button' in menu
    # display current data in tablewidget
    def print_data_to_table(self):
        for i in range(self.row):
            self.ui.tableWidget.removeRow(0)
            self.row -= 1

        for person in data:
            self.ui.tableWidget.setRowCount(self.row + 1)
            col = 0
            print('print_data_to_table')
            print(id(data))
            print(person)
            for key, value in person.items():
                value = str(value)
                cellinfo = QTableWidgetItem(value)
                self.ui.tableWidget.setItem(self.row, col, cellinfo)
                col += 1
            self.row += 1

    def add_data_to_combobox(self):
        self.ui.comboBox.clear()
        for person in data:
            person_name = person.get('name')
            self.ui.comboBox.addItem(person_name)
        print('add_data_to_combobox was run')

    # using after menu 'Reset to default' pressed, because 'data'not updated
    def add_default_data_to_combobox(self):
        self.ui.comboBox.clear()
        for person in default_data:
            person_name = person.get('name')
            self.ui.comboBox.addItem(person_name)
        print('add_default_data_to_combobox was run')

    def delete_data_from_combobox(self):
        current_index = self.ui.comboBox.currentIndex()
        self.ui.comboBox.removeItem(current_index)

    # for 'save' button
    def add_new_person_to_data(self):
        global new_person

        name = self.ui.lineEdit.text()
        birthday = self.ui.dateEdit.text()
        height = self.ui.spinBox.text()
        weight = self.ui.spinBox_2.text()
        car = self.ui.checkBox_4.isChecked()

        languages_check_box = []
        if self.ui.checkBox.isChecked():
            languages_check_box.append('Python')
        if self.ui.checkBox_2.isChecked():
            languages_check_box.extend(['C#'])
        if self.ui.checkBox_3.isChecked():
            languages_check_box += ['Java']
        languages = languages_check_box

        new_person = {
            "name": name,
            "birthday": birthday,
            "height": height,
            "weight": weight,
            "car": car,
            "languages": languages
        }

        data.append(new_person)
        print(data)
        return (new_person)

    def print_new_person_to_table(self):
        self.ui.tableWidget.setRowCount(self.row + 1)
        col = 0
        for key, value in new_person.items():
            value = str(value)
            cellinfo = QTableWidgetItem(value)
            self.ui.tableWidget.setItem(self.row, col, cellinfo)
            col += 1
        self.row += 1

    def print_current_combobox_person_to_table(self):
        name_combo = self.ui.comboBox.currentText()
        self.ui.tableWidget.setRowCount(self.row + 1)

        col = 0
        for person in data:
            if person['name'] == name_combo:
                for key, value in person.items():
                    value = str(value)
                    cellinfo = QTableWidgetItem(value)
                    self.ui.tableWidget.setItem(self.row, col, cellinfo)
                    col += 1
        self.row += 1

    # save data to the json file
    def save_delete_data_buttons(self):
        self.ui.pushButton.clicked.connect(self.add_new_person_to_data)
        self.ui.pushButton.clicked.connect(self.add_data_to_combobox)
        self.ui.pushButton.clicked.connect(self.create_current_data_json_file)
        self.ui.pushButton_2.clicked.connect(self.delete_person_from_data)
        self.ui.pushButton_2.clicked.connect(self.delete_data_from_combobox)
        self.ui.pushButton_2.clicked.connect(self.create_current_data_json_file)

    # adding and removing selected person  in combobox from the table
    def plus_minus_buttons_to_table(self):

        # name_combo = self.ui.comboBox.currentText()
        # element_index_combobox = self.ui.comboBox.currentIndex()
        self.ui.comboBox.currentTextChanged.connect(self.show_selected_person_characteristics_in_widgets)
        self.ui.toolButton.clicked.connect(self.print_current_combobox_person_to_table)
        self.ui.toolButton_2.clicked.connect(self.delete_selected_person_from_table)

    def show_selected_person_characteristics_in_widgets(self, selected_name_in_combobox):
        for person in data:
            if person['name'] == selected_name_in_combobox:
                birthday_combobox = person['birthday']
                year = int(birthday_combobox[6:])
                month = int(birthday_combobox[3:5])
                day = int(birthday_combobox[0:2])
                height_combobox = int(person['height'])
                weight_combobox = int(person['weight'])
                car_combobox = person['car']
                languages_combobox = person['languages']

                self.ui.lineEdit.setText(selected_name_in_combobox)

                self.ui.dateEdit.setDate(QDate(year, month, day))

                self.ui.spinBox.setValue(height_combobox)
                self.ui.spinBox_2.setValue(weight_combobox)

                self.ui.checkBox_4.setChecked(car_combobox)

                self.ui.checkBox.setChecked(False)
                self.ui.checkBox_2.setChecked(False)
                self.ui.checkBox_3.setChecked(False)

                if 'Python' in languages_combobox:
                    self.ui.checkBox.setChecked(True)
                if 'C#' in languages_combobox:
                    self.ui.checkBox_2.setChecked(True)
                if 'Java' in languages_combobox:
                    self.ui.checkBox_3.setChecked(True)

    def delete_selected_person_from_table(self):
        #
        # ints = [1, 3, 7, 5, 4, 3]
        # item = 3
        #
        # indexes = [i for i, j in enumerate(ints) if j == item]
        # print(f"Item {item} is found at index {indexes}")
        name_combo = self.ui.comboBox.currentText()
        names_list = []
        row_quantity = self.ui.tableWidget.rowCount()
        for i in range(row_quantity):
            name_in_table = self.ui.tableWidget.item(i, 0).text()
            names_list.append(name_in_table)
        name_indexes = [i for i, j in enumerate(names_list) if j == name_combo]

        count = 0
        for i in name_indexes:
            if i == name_indexes[0] == 0:
                self.ui.tableWidget.removeRow(0)
                self.row -= 1
                # print('removeRow(0')
            elif i == name_indexes[0]:
                self.ui.tableWidget.removeRow(i)
                self.row -= 1
                # print('removeRow(i)', i)
            else:
                self.ui.tableWidget.removeRow(i - count)
                self.row -= 1
                # print('removeRow(i-1-count)', i - count)
            count += 1

    # when 'delete' button was pressed
    def delete_person_from_data(self):
        print(data)
        name_combo = self.ui.comboBox.currentText()
        for person in data:
            if person['name'] == name_combo:
                del data[data.index(person)]
        print(data)

    # menu actions 'Show all' and 'Reset data to default'
    def menu(self):
        self.ui.action1.triggered.connect(self.create_default_json_file)
        self.ui.action1.triggered.connect(self.add_default_data_to_combobox)
        self.ui.action1.triggered.connect(self.restore_data_to_default)
        self.ui.actionShow_all.triggered.connect(self.print_data_to_table)

    def restore_data_to_default(self):
        global data
        data = default_data.copy()
        print('Data has been restored to default')
        print(data)

    # creating json with default data (three persons)
    def create_default_json_file(self):
        with open('data.json', 'w') as file_json:
            json.dump(default_data, file_json, indent=1)

    def create_current_data_json_file(self):
        with open('data.json', 'w') as file_json:
            json.dump(data, file_json, indent=1)
            print('File with updated data has been created.')


app = QtWidgets.QApplication([])
application = mywindow()

application.add_data_to_combobox()
application.save_delete_data_buttons()
application.plus_minus_buttons_to_table()
application.print_data_to_table()
application.menu()

application.show()
sys.exit(app.exec())
