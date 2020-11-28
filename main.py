from ui import Ui_Dialog
import sqlite3
import sys
from PyQt5 import QtWidgets


class MyWidget(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fill_table()

    def add_elem(self):
        self.openWin()

    def fill_table(self):
        with sqlite3.connect('coffee.sqlite') as con:
            cur = con.cursor()
            res = cur.execute(f"""SELECT * FROM coffee order by id""").fetchall()
            self.tableWidget.setRowCount(len(res))
            for i, row in enumerate(res):
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())