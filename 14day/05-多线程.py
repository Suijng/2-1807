from threading import Thread
import time
num=0

def whork1():
	global num
		for i in range(10000000):
			num+=1
		print(num)

def whork2():
	global num
		for i in range(10000000):
			num+=1
		print(num)

t1=Thread(target=whork1)
t1.start()
t2=Thread(target=whork2)
t2.start()
