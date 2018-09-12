import time
import re
lists=[]
lists1=[]
def choose():
	while True:
		print('1、入住')
		print('2、离店')
		print('3、统计')
		print('4、退出')
		gongneng()
def gongneng():
	shuzi=int(input('请输入数字:'))
	if shuzi==1:
		add()
	elif shuzi==2:
		lidian()
	elif shuzi==3:
		tongji()
	elif shuzi==4:
		exit()
	else:
		print('输入有误')


def add():
	d={}
	name=input('请输入名字:')
	d['name']=name
	while True:
		sjh=input('输入手机号:')
		if len(sjh)==11:
			d['sjh']=sjh
			break
		else:
			print('输入错误 重新输入:')
	'''
	sjh=input('输入手机号:')
	re.match(r'1\d[3~9]{9}$'sjh)
	'''
	a=int(time.time())
	lists.append(d)

def lidian():
	name=input('请输入名字:')
	b=int(time.time())
	for i in lists:
		if i['name']==name:
			lists1.append(i)
	print('离店成功')

def tongji():
	print('总入店:',len(lists))
	print('离店:',len(lists1))
	print('今天赚了:')

choose()

