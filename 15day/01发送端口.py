#udp接口
from socket import *
s=socket(AF_INET,SOCK_DGRAM)
m=input('请输入发送的数据:')
s.sendto(m.encode('gb2312'),('192.168.43.131',8080))

while True:
	r=s.recvfrom(1024)#,s.decode('gb2312')
	print(r[0].decode('gb2312'))
	print(r[1][0])
	print(r[1][1])

s.close()




