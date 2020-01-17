# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph
from AskText import *
from AskBool import *
from Ui.Ui_MainWindow import *
import os, sys

#print(os.path.dirname(sys.argv[0]))

def sell_formula(n):
	return 10 + 5*(n//10)

def buy_formula(n):
	return 10 + 5*( (n - 1)//10 )

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, app, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		#uic.loadUi("MainWindow.ui", self)

		self.graph_init()
		self.event_init()

		self.ui.buy_tableWidget.setRowCount(10)
		self.ui.buy_tableWidget.setColumnCount(2)
		
		self.buy = []
		self.sell = []
		self.times = []
		self.now = -1
		global log
		log = self.ui.log_listWidget
		#self.ui.log_listWidget.rowsInserted
		self.app = app
		self.main()

	def event_init(self):
		self.ui.buy_input.installEventFilter(self)
		self.ui.sell_input.installEventFilter(self)

		self.ui.buy_btn.clicked.connect(self.event_handle)
		self.ui.sell_btn.clicked.connect(self.event_handle)

		self.ui.buy_input.textChanged.connect(self.text_changed)
		self.ui.sell_input.textChanged.connect(self.text_changed)

		self.ui.log_clear.clicked.connect(self.ui.log_listWidget.clear)

	
	def eventFilter(self, obj, event):
		if obj is self.ui.buy_input and event.type() == QtCore.QEvent.KeyPress:
			if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
				log.addItem("log: buy " + self.ui.buy_input.toPlainText())
				self.ui.buy_input.setPlainText("")
				return True
		if obj is self.ui.sell_input and event.type() == QtCore.QEvent.KeyPress:
			if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
				log.addItem("log: sell " + self.ui.sell_input.toPlainText())
				self.ui.sell_input.setPlainText("")
				return True
		return super().eventFilter(obj, event)
	
	def event_handle(self):
		sender = self.sender()
		if sender is self.ui.buy_btn:
			log.addItem("log: buy " + self.ui.buy_input.toPlainText())
			self.ui.buy_input.setPlainText("")
		elif sender is self.ui.sell_btn:
			log.addItem("log: sell " + self.ui.sell_input.toPlainText())
			self.ui.sell_input.setPlainText("")

		pass

	def text_changed(self):
		sender = self.sender()
		if sender is self.ui.buy_input:
			log.addItem(self.ui.buy_input.toPlainText())
		elif sender is self.ui.sell_input:
			log.addItem(self.ui.sell_input.toPlainText())

	def graph_init(self):
		self.ui.graphWidget.setBackground("#ffffff")
		self.ui.graphWidget.setTitle("股票價格", color = "#0000ff")#, size = 30
		self.ui.graphWidget.showGrid(x = True, y = True)
		self.buy_pen  = pyqtgraph.mkPen(width = 2, style = QtCore.Qt.SolidLine,  symbol='o', color = "#ff0000")
		self.sell_pen = pyqtgraph.mkPen(width = 2, style = QtCore.Qt.SolidLine,  symbol='o', color = "#00ff00")
		#self.ui.graphWidget.plot([1,2,3,4,5], [1,2,3,4,5], pen = pen)
		#self.ui.graphWidget.plot([8,7,8,7,8], [0,4,5,8,1], pen = pen)
	
	def add(self, n, flush = True):
		self.buy.append( buy_formula(n) )
		self.sell.append( sell_formula(n) )
		self.now += 1
		self.times.append( self.now )
		self.data.write(str(n) + '\n')
		if flush:
			self.data.flush()

	def draw(self):
		self.ui.graphWidget.clear()
		self.ui.graphWidget.plot(self.times, self.buy, pen = self.buy_pen)
		self.ui.graphWidget.plot(self.times, self.sell, pen = self.sell_pen)
	
	def main(self):
		filename = os.path.dirname(sys.argv[0]) + "/data.txt"
		n = 10
		self.data = None
		react = False
		
		if os.path.isfile(filename) and os.stat(filename).st_size > 0:
			#react = input("偵測到存檔，是否讀入？ (y/n)：")
			react = AskBool(self, "偵測到存檔，是否讀入？").get()
			if react == None:
				sys.exit(-1)
		
		if react:
			self.data = open(filename, mode="r+", encoding="utf8")
			for line in self.data:
				self.add(int(line), flush = False)
				log.addItem(line.strip('\n'))

		else:
			self.data = open(filename, mode="w", encoding="utf8")
			a = AskText(self, "請輸入起始流通量 (預設：10)").get()
			if a is None:
				sys.exit(-1)
			#print(a)
			#a = input("請輸入起始流通量 n (預設：10)：")
			if str.isdecimal(a):
				log.addItem( a )
				n = int(a)
			else:
				log.addItem("使用預設值")
				#print("使用預設值")
			self.add(n)

		self.draw()
		self.UpdateTable()
		
	def UpdateTable(self):
		self.ui.buy_tableWidget.clearContents()
		self.ui.sell_tableWidget.clearContents()
		n = self.times[-1]
		sell_price = sell_formula(n)
		buy_price = buy_formula(n)
		for i in range(10):
			self.ui.buy_tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i)))
			print(i)
			pass


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWindow = MainWindow(app)
	mainWindow.show()
	#timer = QtCore.QTimer()
	#timer.timeout.connect(mainWindow.aaa)
	#timer.start(1000)
	sys.exit(app.exec_())
