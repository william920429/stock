# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph
from AskText import *
from AskBool import *
from Ui.Ui_MainWindow import *
import os, sys

#print(os.path.dirname(sys.argv[0]))

debug = False

def sell_formula(n):
	return 10 + 5*( (n - 1)//10 )

def buy_formula(n):
	return 10 + 5*(n//10)
	

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, app, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		#uic.loadUi("MainWindow.ui", self)

		self.graph_init()
		self.event_init()

		self.ui.buy_sell_tableWidget.setRowCount(10)
		self.ui.buy_sell_tableWidget.setColumnCount(2)
		self.ui.buy_sell_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		
		if not debug:
			self.ui.label.hide()

		self.buy_list = []	#for plotting
		self.sell_list = []
		self.times = []	#for plotting 0 to current
		self.now = -1 #record current time
		self.n = None 
		self.log = self.ui.log_listWidget
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
				self.buy()
				return True
		if obj is self.ui.sell_input and event.type() == QtCore.QEvent.KeyPress:
			if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
				self.sell()
				return True
		return super().eventFilter(obj, event)
	
	def event_handle(self):
		sender = self.sender()
		if sender is self.ui.buy_btn:
			self.buy()
		elif sender is self.ui.sell_btn:
			self.sell()

	def text_changed(self):
		sender = self.sender()
		if sender is self.ui.buy_input:
			text = self.ui.buy_input.toPlainText()
			formula = buy_formula
			label = self.ui.buy_price_label
			sign = 1

		elif sender is self.ui.sell_input:
			text = self.ui.sell_input.toPlainText()
			formula = sell_formula
			label = self.ui.sell_price_label
			sign = -1

		else: return
		if text == "":
			label.setText("0")
		elif not str.isdigit(text): return
		else:
			n = self.n
			price = 0
			for i in range(int(text)):
				price += formula(n + sign*i)
			label.setText(str(price))

	def buy(self):
		n = self.n
		price = 0
		text = self.ui.buy_input.toPlainText()
		if text == "": return False
		if not str.isdigit(text):
			self.log.addItem("Invalid Buy Input!")
			return False
		num = int(text)
		self.add(n + num)
		self.ui.buy_input.setPlainText("")
		for i in range(num):
			price += buy_formula(n + i)
		self.log.addItem("成功購買 {} 張股票，共 {} 元".format(num, price))

	def sell(self):
		n = self.n
		price = 0
		text = self.ui.sell_input.toPlainText()
		if text == "": return False
		if not str.isdigit(text):
			self.log.addItem("Invalid Sell Input!")
			return False
		num = int(text)
		self.add(n - num)
		self.ui.sell_input.setPlainText("")
		for i in range(num):
			price += sell_formula(n - i)
		self.log.addItem("成功賣出 {} 張股票，共 {} 元".format(num, price))

	def graph_init(self):
		self.ui.graphWidget.setBackground("#ffffff")
		self.ui.graphWidget.setTitle("股票價格", color = "#0000ff")#, size = 30
		self.ui.graphWidget.showGrid(x = True, y = True)
		self.buy_pen  = pyqtgraph.mkPen(width = 3, style = QtCore.Qt.SolidLine,  symbol='o', color = "#ff0000")
		#self.sell_pen = pyqtgraph.mkPen(width = 2, style = QtCore.Qt.SolidLine,  symbol='o', color = "#00ff00")
		#self.ui.graphWidget.plot([1,2,3,4,5], [1,2,3,4,5], pen = pen)
		#self.ui.graphWidget.plot([8,7,8,7,8], [0,4,5,8,1], pen = pen)
	
	def add(self, n, flush_and_update = True):
		self.buy_list.append( buy_formula(n) )
		self.sell_list.append( sell_formula(n) )
		self.n = n
		self.now += 1
		self.times.append(self.now)
		self.ui.label.setText(str(n))
		if flush_and_update:
			self.data.write(str(n) + '\n')
			self.data.flush()
			self.draw()
			self.UpdateTable()

	def draw(self):
		self.ui.graphWidget.clear()
		self.ui.graphWidget.plot(self.times, self.buy_list, pen = self.buy_pen)
		#self.ui.graphWidget.plot(self.times, self.sell_list, pen = self.sell_pen)
		self.UpdatePrice()

	def UpdatePrice(self):
		self.ui.buy_current_label.setText(str(buy_formula(self.n)))
		self.ui.sell_current_label.setText(str(sell_formula(self.n)))

	def UpdateTable(self):
		self.ui.buy_sell_tableWidget.clearContents()
		n = self.n
		buy_price = 0
		sell_price = 0
		for i in range(10):
			buy_price += buy_formula(n + i)
			sell_price += sell_formula(n - i)
			self.ui.buy_sell_tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(buy_price)))
			self.ui.buy_sell_tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(sell_price)))
	
	def main(self):
		filename = os.path.dirname(sys.argv[0]) + "/data.txt"
		self.n = 100
		self.data = None
		react = False
		
		if os.path.isfile(filename) and os.stat(filename).st_size > 0:
			#react = input("偵測到存檔，是否讀入？ (y/n)：")
			react = AskBool(self, "偵測到存檔，是否讀入？").get()
			if react == None:
				sys.exit(-1)

		if react:
			self.data = open(filename, mode="r+", encoding="utf8")
			for line in map(int, self.data.read().split()):
				self.n = line
				self.add(self.n, flush_and_update = False)
				self.log.addItem("Reading: " + str(line))

		else:
			self.data = open(filename, mode="w", encoding="utf8")
			a = AskText(self, "請輸入起始流通量 (預設：{})".format(self.n)).get()
			if a is None:
				sys.exit(-1)
			#print(a)
			#a = input("請輸入起始流通量 n (預設：10)：")
			if str.isdecimal(a):
				self.log.addItem( a )
				self.n = int(a)
			else:
				self.log.addItem("使用預設值")
				#print("使用預設值")
			self.add(self.n)

		self.draw()
		self.UpdateTable()
		
	
			


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	mainWindow = MainWindow(app)
	mainWindow.show()
	#timer = QtCore.QTimer()
	#timer.timeout.connect(mainWindow.aaa)
	#timer.start(1000)
	sys.exit(app.exec_())
