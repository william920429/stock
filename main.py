# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
import pyqtgraph
from MainWindow import *
import os, sys

#print(os.path.dirname(sys.argv[0]))


def sale(n):
	return 10 + 5*(n//10)

def buy(n):
	return 10 + 5*( (n - 1)//10 )

def draw(prev, cur):

	print("Draw", prev, cur)
	pass

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		#uic.loadUi("MainWindow.ui", self)
		self.ui.graphWidget.enableMouse(b = False)
		self.ui.graphWidget.setBackground("#ffffff")
		self.ui.graphWidget.setTitle("股票價格", color = "#0000ff")#, size = 30
		self.ui.graphWidget.showGrid(x = True, y = True)
		pen = pyqtgraph.mkPen(width = 1.5, style = QtCore.Qt.SolidLine)
		self.ui.graphWidget.plot([1,2,3,4,5], [1,2,3,4,5], pen = pen)
		self.ui.graphWidget.plot([8,7,8,7,8], [0,4,5,8,1], pen = pen)
	

	def draw(self, prev, cur):
		pass


def GUI():
	app = QtWidgets.QApplication(sys.argv)
	mainWindow = MainWindow()
	mainWindow.show()
	return app.exec_()

def main():
	
	#stock_num = []
	filename = os.path.dirname(sys.argv[0]) + "/data.txt"
	current_n = 10
	prev_n = current_n


	data = None
	react = 'n'
	if os.path.isfile(filename) and os.stat(filename).st_size > 0:
		react = input("偵測到存檔，是否讀入？ (y/n)：\n")
	
	if str.lower(react) == 'y':
		data = open(filename, mode="r+", encoding="utf8")
		first = True
		for line in data:
			#stock_num.append(int(line))
			if first:
				prev_n = current_n = int(line)
				first = False
			else:
				prev_n = current_n
				current_n = int(line)

			draw(prev_n, current_n)

	else:
		data = open(filename, mode="w", encoding="utf8")
		a = input("請輸入起始流通量 n (預設：10)：\n")
		if str.isdecimal(a):
			current_n = prev_n = int(a)
		else:
			print("使用預設值")
		#stock_num.append(n)
		data.write(str(current_n) + '\n')
		data.flush()
		draw(prev_n, current_n)
	
	a = False
	while a:
		a = False
		get_buy = 10
		pass
		if get_buy:
			prev_n = current_n
			current_n += get_buy
			data.write(str(current_n) + '\n')
			data.flush()
			draw(prev_n, current_n)
		
		pass
	
	


if __name__ == "__main__":
	#main()
	sys.exit(GUI())
