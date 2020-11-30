from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton, QTableWidget, QTableWidgetItem, QDialog, QComboBox, QStatusBar
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui
import sqlite3
from dist.addEditCoffeeForm import Ui_Dialog
import sys


class SecondWindow(QDialog, Ui_Dialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.setupUi(self)
        self.main = root
        self.build()


    def build(self):
        self.pushButton.clicked.connect(self.clos)
        if self.main.set:
            self.lineEdit.setText(self.main.tableWidget.item(self.main.tableWidget.currentRow(), 1).text())
            self.lineEdit_2.setText(self.main.tableWidget.item(self.main.tableWidget.currentRow(), 2).text())
            self.lineEdit_8.setText(self.main.tableWidget.item(self.main.tableWidget.currentRow(), 3).text())
            self.lineEdit_7.setText(self.main.tableWidget.item(self.main.tableWidget.currentRow(), 5).text())
            self.lineEdit_4.setText(self.main.tableWidget.item(self.main.tableWidget.currentRow(), 6).text())
            self.lineEdit_5.setText(self.main.tableWidget.item(self.main.tableWidget.currentRow(), 7).text())

    def clos(self):
        try:
            if not self.main.set:
                if self.lineEdit_4.text().isdigit() and self.lineEdit_5.text().isdigit():
                    with sqlite3.connect('coffee.sqlite') as con:
                        cur = con.cursor()
                        cur.execute("""INSERT INTO coffee (
                                                          name,
                                                          grade,
                                                          roast,
                                                          type,
                                                          taste,
                                                          price,
                                                          size
                                                          )
                                                          VALUES (?,?,?,?,?,?,?)""", [self.lineEdit.text(),
                                                                                      self.lineEdit_2.text(),
                                                                                      self.lineEdit_8.text(),
                                                                                      self.comboBox.currentText(),
                                                                                      self.lineEdit_7.text(),
                                                                                      self.lineEdit_4.text(),
                                                                                      self.lineEdit_5.text()])
                        con.commit()
                    self.main.fill_table()

                    self.main.tableWidget.setCurrentCell(self.main.tableWidget.rowCount() - 1, 0)
                    self.close()
                else:
                    valid = QMessageBox.question(self.pushButton, '',
                                                 'Заполните все значения',
                                                 QMessageBox.Ok)
            else:
                for j, elem in enumerate([self.lineEdit.text(),
                                          self.lineEdit_2.text(),
                                          self.lineEdit_8.text(),
                                          self.comboBox.currentText(),
                                          self.lineEdit_7.text(),
                                          self.lineEdit_4.text(),
                                          self.lineEdit_5.text()]):
                    self.main.tableWidget.setItem(
                        self.main.tableWidget.currentRow(), j + 1, QTableWidgetItem(str(elem)))
                    self.main.fill_bd()
                self.close()

        except ValueError:
            valid = QMessageBox.question(self.pushButton, '',
                                         'Неверные значения в числовых полях',
                                         QMessageBox.Ok)
