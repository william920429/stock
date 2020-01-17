# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_AskBool.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AskBool(object):
    def setupUi(self, AskBool):
        AskBool.setObjectName("AskBool")
        AskBool.resize(412, 172)
        AskBool.setMinimumSize(QtCore.QSize(412, 172))
        AskBool.setMaximumSize(QtCore.QSize(412, 172))
        self.centralwidget = QtWidgets.QWidget(AskBool)
        self.centralwidget.setObjectName("centralwidget")
        self.confirm_btn = QtWidgets.QPushButton(self.centralwidget)
        self.confirm_btn.setGeometry(QtCore.QRect(70, 110, 93, 28))
        self.confirm_btn.setObjectName("confirm_btn")
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(260, 110, 93, 28))
        self.cancel_btn.setObjectName("cancel_btn")
        self.question_label = QtWidgets.QLabel(self.centralwidget)
        self.question_label.setGeometry(QtCore.QRect(60, 20, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.question_label.setFont(font)
        self.question_label.setAlignment(QtCore.Qt.AlignCenter)
        self.question_label.setObjectName("question_label")
        AskBool.setCentralWidget(self.centralwidget)

        self.retranslateUi(AskBool)
        QtCore.QMetaObject.connectSlotsByName(AskBool)

    def retranslateUi(self, AskBool):
        _translate = QtCore.QCoreApplication.translate
        AskBool.setWindowTitle(_translate("AskBool", "MainWindow"))
        self.confirm_btn.setText(_translate("AskBool", "確定"))
        self.cancel_btn.setText(_translate("AskBool", "取消"))
        self.question_label.setText(_translate("AskBool", "TextLabel"))
