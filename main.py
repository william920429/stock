#import numpy
import os, sys

#print(os.path.dirname(sys.argv[0]))


def sale(n):
	return 10 + 5*(n//10)

def buy(n):
	return 10 + 5*( (n - 1)//10 )

def draw(prev, cur):
	print("Draw", prev, cur)
	pass

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
	
	a = True
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
	main()
