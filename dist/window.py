from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(810, 400)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 810, 360))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Название', 'Cорт', 'Ожарка', 'Молотый/в зернах',
                                                    'Вкус', 'Цена', 'Объем'])
        self.tableWidget.setRowCount(0)

        self.btn = QtWidgets.QPushButton(Dialog)
        self.btn.move(700, 370)
        self.btn.resize(100, 20)

        self.btn1 = QtWidgets.QPushButton(Dialog)
        self.btn1.move(590, 370)
        self.btn1.resize(100, 20)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn.setText(_translate("Dialog", "Изменить"))
        self.btn1.setText(_translate("Dialog", "Добавить"))