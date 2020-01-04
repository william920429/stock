import numpy

class stock:
	sale = 0
	buy = 0
	'''
	def __init__(self, sale, buy):
		self.sale = sale
		self.buy = buy
	'''

def main():
	stocks = []
	start = stock()
	
	n = int(input("請輸入起始流通量 n ："))
	start.sale = 10 + 5*(n//10)
	start.buy = 10 + 5*( (n - 1)//10 )
	stocks.push(start)
	pass


if __name__ == "__main__":
	main()
