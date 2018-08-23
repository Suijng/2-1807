from threading import Thread
import time

def whork(i):
	num=0
	time.sleep(i)
	num+=1
	print(num)
'''
def whork1(i):
	num=0
	time.sleep(i)
	num+=2
	print(num)
'''
t=Thread(target=whork,args=(1,))
t1=Thread(target=whork,args=(3,))
t.start()
t1.start()



