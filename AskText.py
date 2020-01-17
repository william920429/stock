# -*- coding: utf-8 -*-
from Ui.Ui_AskText import *

class AskText(QtWidgets.QMainWindow):
	def __init__(self, mainWindow, str):
		super().__init__()
		self.ui = Ui_AskText()
		self.ui.setupUi(self)
		self.setWindowTitle(str)
		self.ui.question_label.setText(str)
		
		self.mainWindow = mainWindow
		self.log = self.mainWindow.ui.log_listWidget
		self.log.addItem(str)

		self.event_init()

	def event_init(self):
		self.ans = None
		self.ui.confirm_btn.clicked.connect(self.event_handle)
		self.ui.input.installEventFilter(self)

	def event_handle(self):
		self.ans = self.ui.input.toPlainText()
		# self.log.addItem(self.ans)
		self.close()

	def eventFilter(self, obj, event):
		if obj is self.ui.input and event.type() == QtCore.QEvent.KeyPress:
			if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
				self.event_handle()
				return True
		return super().eventFilter(obj, event)

	# def keyPressEvent(self, e):
	# 	if e.key() == QtCore.Qt.Key_Return:
	# 		self.react()

	def get(self):
		self.show()
		self.mainWindow.app.exec_()
		return self.ans
