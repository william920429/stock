# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph
from MainWindow import *
from AskBool import *
from AskText import *
import os, sys

app = None
log = None
#print(os.path.dirname(sys.argv[0]))


def sell(n):
	return 10 + 5*(n//10)

def buy(n):
	return 10 + 5*( (n - 1)//10 )

class AskText(QtWidgets.QMainWindow):
	def __init__(self, str):
		super().__init__()
		self.ui = Ui_AskText()
		self.ui.setupUi(self)
		self.setWindowTitle(str)
		self.ui.question_label.setText(str)
		self.ui.confirm_btn.clicked.connect(self.react)
		self.ans = ""
		self.ui.input.installEventFilter(self)
		log.addItem(str)
	
	def eventFilter(self, obj, event):
		if obj is self.ui.input and event.type() == QtCore.QEvent.KeyPress:
			if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
				self.react()
				return True
		return super().eventFilter(obj, event)

	def react(self):
		self.ans = self.ui.input.toPlainText()
		self.close()

	def keyPressEvent(self, e):
		if e.key() == QtCore.Qt.Key_Return:
			self.react()

	def get(self):
		self.show()
		app.exec_()
		return self.ans

class AskBool(QtWidgets.QMainWindow):
	def __init__(self, str):
		super().__init__()
		self.ui = Ui_AskBool()
		self.ui.setupUi(self)
		self.setWindowTitle(str)
		self.ui.question_label.setText(str)
		self.ui.confirm_btn.clicked.connect(self.react)
		self.ui.cancel_btn.clicked.connect(self.react)
		self.ans = False
		log.addItem(str)
		
	def react(self):
		sender = self.sender()
		if sender is self.ui.confirm_btn: self.ans = True
		else: self.ans = False
		log.addItem(sender.text())
		self.close()
	
	def get(self):
		self.show()
		app.exec_()
		return self.ans

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		#uic.loadUi("MainWindow.ui", self)

		self.ui.graphWidget.setBackground("#ffffff")
		self.ui.graphWidget.setTitle("股票價格", color = "#0000ff")#, size = 30
		self.ui.graphWidget.showGrid(x = True, y = True)
		self.buy_pen  = pyqtgraph.mkPen(width = 2, style = QtCore.Qt.SolidLine,  symbol='o', color = "#ff0000")
		self.sell_pen = pyqtgraph.mkPen(width = 2, style = QtCore.Qt.SolidLine,  symbol='o', color = "#00ff00")
		#self.ui.graphWidget.plot([1,2,3,4,5], [1,2,3,4,5], pen = pen)
		#self.ui.graphWidget.plot([8,7,8,7,8], [0,4,5,8,1], pen = pen)

		self.buy = []
		self.sell = []
		self.times = []
		self.now = -1
		global log
		log = self.ui.log_listWidget
		self.main()
	
	def add(self, n):
		self.buy.append( buy(n) )
		self.sell.append( sell(n) )
		self.now += 1
		self.times.append( self.now )

	def draw(self):
		self.ui.graphWidget.plot(self.times, self.buy, pen = self.buy_pen)
		self.ui.graphWidget.plot(self.times, self.sell, pen = self.sell_pen)
	
	def main(self):
		filename = os.path.dirname(sys.argv[0]) + "/data.txt"
		n = 10
		data = None
		react = False
		
		if os.path.isfile(filename) and os.stat(filename).st_size > 0:
			#react = input("偵測到存檔，是否讀入？ (y/n)：")
			react = AskBool("偵測到存檔，是否讀入？").get()
		
		if react:
			data = open(filename, mode="r+", encoding="utf8")
			for line in data:
				self.add(int(line))

		else:
			data = open(filename, mode="w", encoding="utf8")
			a = AskText("請輸入起始流通量 (預設：10)").get()
			print(a)
			#a = input("請輸入起始流通量 n (預設：10)：")
			if str.isdecimal(a):
				log.addItem( a )
				n = int(a)
			else:
				log.addItem("使用預設值")
				#print("使用預設值")
			data.write(str(n) + '\n')
			data.flush()
			self.add(n)
		
		self.draw()
	



if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWindow = MainWindow()
	mainWindow.show()
	#timer = QtCore.QTimer()
	#timer.timeout.connect(mainWindow.aaa)
	#timer.start(1000)
	sys.exit(app.exec_())
