from dist.window import Ui_Dialog
import sqlite3
import sys
from PyQt5 import QtWidgets
from dist.editer import SecondWindow


class MyWidget(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fill_table()
        self.btn1.clicked.connect(self.openWin)
        self.btn.clicked.connect(self.set_coffee)
        self.secondWin = None
        self.set = False

    def set_coffee(self):
        self.set = True
        self.openWin()

    def openWin(self):
        if not self.secondWin:
            self.secondWin = SecondWindow(self)
        self.secondWin.show()

    def fill_table(self):
        with sqlite3.connect('coffee.sqlite') as con:
            cur = con.cursor()
            res = cur.execute(f"""SELECT * FROM coffee order by id""").fetchall()
            self.tableWidget.setRowCount(len(res))
            for i, row in enumerate(res):
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(str(elem)))

    def change_films(self):
        if self.tableWidget.currentRow() < 0:
            valid = QtWidgets.QMessageBox.question(self.set_film, '',
                                                   'Вы забыли выделить поле в таблице',
                                                   QtWidgets.QMessageBox.Ok)
            return
        self.set = True
        self.openWin()

    def fill_bd(self):
        with sqlite3.connect('coffee.sqlite') as con:
            rows = self.tableWidget.rowCount()
            cols = self.tableWidget.columnCount()
            data = []
            cur = con.cursor()
            for row in range(rows):
                tmp = []
                for col in range(1, cols):
                    tmp.append(self.tableWidget.item(row, col).text())
                data.append(tmp)

            cur.execute("DELETE FROM coffee")
            con.commit()
            for i in data:
                cur.execute("""INSERT INTO coffee (
                                                      name,
                                                      grade,
                                                      roast,
                                                      type,
                                                      taste,
                                                      price,
                                                      size
                                                  )
                                              VALUES (?,?,?,?,?,?,?)""", i)
            con.commit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())