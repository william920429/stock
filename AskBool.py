# -*- coding: utf-8 -*-
from Ui.Ui_AskBool import *

class AskBool(QtWidgets.QMainWindow):
	def __init__(self, mainWindow, str):
		super().__init__()
		self.ui = Ui_AskBool()
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
		self.ui.cancel_btn.clicked.connect(self.event_handle)

	def event_handle(self):
		sender = self.sender()
		if sender is self.ui.confirm_btn:
			self.ans = True
		elif sender is self.ui.cancel_btn:
			self.ans = False
		else:
			self.log.addItem("Error Asking Bool!")

		self.log.addItem(sender.text())
		self.close()
	
	def get(self):
		self.show()
		self.mainWindow.app.exec_()
		return self.ans
