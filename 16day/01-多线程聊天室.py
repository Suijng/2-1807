from threading import Thread
from socket import *
import time

s=socket(AF_INET,SOCK_DGRAM)
s.bind(('',7843))
def work():
	while True:
		m=input('请输入发送的数据:')
		s.sendto(m.encode('gb2312'),('192.168.43.247',5678))

def work1():
	while True:
		r=s.recvfrom(1024)
		print('接受内容:%s'%r[0].decode('gb2312'))
		print(r[1][0])
		print(r[1][1])

t=Thread(target=work)
t1=Thread(target=work1)
#s.close()
t.start()
t1.start()
t.join
t1.join
