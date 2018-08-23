from threading import Thread
import time

def sing():
	for i in range(5):
		print('唱歌')
		time.sleep(0.5)

def dance():
	for i in range(5):
		print('跳舞')
		time.sleep(0.5)

t1=Thread(target=sing)
t2=Thread(target=dance)
t1.start()
t2.start()
#t1.join(3)
#t2.join(3)
print('哈哈哈哈')
