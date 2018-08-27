from socket import *

s=socket(AF_INET,SOCK_STREAM)#创建ctp
s.bind(('',4577))

s.listen(5)#监听

s1.info=s.accept()#等着接电话
print('有新连接了')

print(s1.recv(1024).decode('gb2312'))
s1.send(('哈哈'.encode))

s1.close()
s.close()

