# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1396, 882)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphWidget = PlotWidget(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(29, 30, 741, 561))
        self.graphWidget.setObjectName("graphWidget")
        self.buy_sell_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.buy_sell_tableWidget.setGeometry(QtCore.QRect(790, 30, 261, 561))
        self.buy_sell_tableWidget.setObjectName("buy_sell_tableWidget")
        self.buy_sell_tableWidget.setColumnCount(2)
        self.buy_sell_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.buy_sell_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.buy_sell_tableWidget.setHorizontalHeaderItem(1, item)
        self.buy_btn = QtWidgets.QPushButton(self.centralwidget)
        self.buy_btn.setGeometry(QtCore.QRect(200, 730, 91, 41))
        self.buy_btn.setObjectName("buy_btn")
        self.buy_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.buy_input.setGeometry(QtCore.QRect(40, 730, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.buy_input.setFont(font)
        self.buy_input.setObjectName("buy_input")
        self.buy_label = QtWidgets.QLabel(self.centralwidget)
        self.buy_label.setGeometry(QtCore.QRect(40, 680, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.buy_label.setFont(font)
        self.buy_label.setObjectName("buy_label")
        self.sell_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.sell_input.setGeometry(QtCore.QRect(490, 730, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.sell_input.setFont(font)
        self.sell_input.setObjectName("sell_input")
        self.sell_label = QtWidgets.QLabel(self.centralwidget)
        self.sell_label.setGeometry(QtCore.QRect(490, 680, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.sell_label.setFont(font)
        self.sell_label.setObjectName("sell_label")
        self.sell_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sell_btn.setGeometry(QtCore.QRect(650, 730, 91, 41))
        self.sell_btn.setObjectName("sell_btn")
        self.log_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.log_listWidget.setGeometry(QtCore.QRect(850, 660, 401, 141))
        self.log_listWidget.setObjectName("log_listWidget")
        self.log_label = QtWidgets.QLabel(self.centralwidget)
        self.log_label.setGeometry(QtCore.QRect(850, 610, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.log_label.setFont(font)
        self.log_label.setObjectName("log_label")
        self.buy_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.buy_label_3.setGeometry(QtCore.QRect(40, 790, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.buy_label_3.setFont(font)
        self.buy_label_3.setObjectName("buy_label_3")
        self.sell_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.sell_label_3.setGeometry(QtCore.QRect(490, 790, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.sell_label_3.setFont(font)
        self.sell_label_3.setObjectName("sell_label_3")
        self.buy_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.buy_label_2.setGeometry(QtCore.QRect(40, 610, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.buy_label_2.setFont(font)
        self.buy_label_2.setObjectName("buy_label_2")
        self.sell_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.sell_label_2.setGeometry(QtCore.QRect(490, 610, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.sell_label_2.setFont(font)
        self.sell_label_2.setObjectName("sell_label_2")
        self.buy_current_label = QtWidgets.QLabel(self.centralwidget)
        self.buy_current_label.setGeometry(QtCore.QRect(220, 610, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.buy_current_label.setFont(font)
        self.buy_current_label.setObjectName("buy_current_label")
        self.sell_current_label = QtWidgets.QLabel(self.centralwidget)
        self.sell_current_label.setGeometry(QtCore.QRect(660, 610, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.sell_current_label.setFont(font)
        self.sell_current_label.setObjectName("sell_current_label")
        self.buy_price_label = QtWidgets.QLabel(self.centralwidget)
        self.buy_price_label.setGeometry(QtCore.QRect(210, 790, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.buy_price_label.setFont(font)
        self.buy_price_label.setObjectName("buy_price_label")
        self.sell_price_label = QtWidgets.QLabel(self.centralwidget)
        self.sell_price_label.setGeometry(QtCore.QRect(660, 790, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.sell_price_label.setFont(font)
        self.sell_price_label.setObjectName("sell_price_label")
        self.log_clear = QtWidgets.QPushButton(self.centralwidget)
        self.log_clear.setGeometry(QtCore.QRect(1280, 710, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.log_clear.setFont(font)
        self.log_clear.setObjectName("log_clear")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1110, 380, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1396, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stock"))
        item = self.buy_sell_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "買價"))
        item = self.buy_sell_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "賣價"))
        self.buy_btn.setText(_translate("MainWindow", "確定"))
        self.buy_label.setText(_translate("MainWindow", "我要買"))
        self.sell_label.setText(_translate("MainWindow", "我要賣"))
        self.sell_btn.setText(_translate("MainWindow", "確定"))
        self.log_label.setText(_translate("MainWindow", "訊息"))
        self.buy_label_3.setText(_translate("MainWindow", "本次購買金額："))
        self.sell_label_3.setText(_translate("MainWindow", "本次售出金額："))
        self.buy_label_2.setText(_translate("MainWindow", "※目前買入價："))
        self.sell_label_2.setText(_translate("MainWindow", "※目前賣出價："))
        self.buy_current_label.setText(_translate("MainWindow", "0"))
        self.sell_current_label.setText(_translate("MainWindow", "0"))
        self.buy_price_label.setText(_translate("MainWindow", "0"))
        self.sell_price_label.setText(_translate("MainWindow", "0"))
        self.log_clear.setText(_translate("MainWindow", "clear"))
        self.label.setText(_translate("MainWindow", "0"))
from pyqtgraph import PlotWidget
