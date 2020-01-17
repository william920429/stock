# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_AskText.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AskText(object):
    def setupUi(self, AskText):
        AskText.setObjectName("AskText")
        AskText.resize(412, 172)
        AskText.setMinimumSize(QtCore.QSize(412, 172))
        AskText.setMaximumSize(QtCore.QSize(412, 172))
        self.centralwidget = QtWidgets.QWidget(AskText)
        self.centralwidget.setObjectName("centralwidget")
        self.confirm_btn = QtWidgets.QPushButton(self.centralwidget)
        self.confirm_btn.setGeometry(QtCore.QRect(260, 100, 93, 41))
        self.confirm_btn.setObjectName("confirm_btn")
        self.question_label = QtWidgets.QLabel(self.centralwidget)
        self.question_label.setGeometry(QtCore.QRect(60, 20, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.question_label.setFont(font)
        self.question_label.setAlignment(QtCore.Qt.AlignCenter)
        self.question_label.setObjectName("question_label")
        self.input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(70, 100, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.input.setFont(font)
        self.input.setObjectName("input")
        AskText.setCentralWidget(self.centralwidget)

        self.retranslateUi(AskText)
        QtCore.QMetaObject.connectSlotsByName(AskText)

    def retranslateUi(self, AskText):
        _translate = QtCore.QCoreApplication.translate
        AskText.setWindowTitle(_translate("AskText", "MainWindow"))
        self.confirm_btn.setText(_translate("AskText", "確定"))
        self.question_label.setText(_translate("AskText", "TextLabel"))
