from threading import Thread,Lock
import time
num=0

def whork1():
	global num
	m.acquire(True)#加锁  堵塞
	for i in range(1000000):
		num+=1
	m.release()#释放锁
	print('wo')
	print(num)

def whork2():
	global num
	m.acquire(True)
	for i in range(1000000):
		num+=1
	m.release()
	print(num)

m=Lock()
t1=Thread(target=whork1)
t1.start()
t2=Thread(target=whork2)
t2.start()
