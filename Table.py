from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.QtGui import QColor
from TableInterface import Ui_Dialog


class Table(QDialog, Ui_Dialog):
    def __init__(self, parent, data):
        super().__init__(parent)
        self.setupUi(self)

        self.COLORS = [
            [215, 215, 0],
            [192, 192, 192],
            [255, 140, 0]
        ]
        self.set_data(data)
        self.btn__close.clicked.connect(self.close)

    def set_data(self, data):
        self.tableWidget.setColumnCount(len(data['headers']))
        self.tableWidget.setHorizontalHeaderLabels(data['headers'])
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data['players']):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(elem))
            if i in range(3):
                self.color_row(i, QColor(*self.COLORS[i]))
        self.tableWidget.resizeColumnsToContents()

    def color_row(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)
