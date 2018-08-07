lists=[]
d={}

def menu():#菜单声明
	while True:
		print('《欢迎来到练习生管理信息》'.center(50,' '))
		print('1、添加实习生信息')
		print('2、查找实习生信息')
		print('3、修改实习生信息')
		print('4、删除练习生信息')
		print('5、打印练习生信息')
		print('6、退出练习生系统')
		info()#调用选择功能的函数


def info():#选择功能的声明
	choose=input('选择所需选项:')
	if choose.isdigit():
		choose=int(choose)
		if choose==1:
			add()#调用添加函数
		elif choose==2:
			find()#调用查找函数
		elif choose==3:
			change()#调用修改函数
		elif choose==4:
			pop()#调用删除函数
		elif choose==5:
			print_list()#调用打印函数
		elif choose==6:
			ext()
			exit()
		else:
			print('输入错误,请重新输入')
	else:
		print('请重新输入')




def add():#添加的声明
	while True:
		name=input('请输入名字:')
		if len(name)>=2 and len(name)<=4:	
			d['name']=name
			break
		else:
			print('\n姓名必须大于2小于4\n')
	while True:
		phone=input('请输入手机号:')
		if phone.startswith('1') and len(phone)==11:
			d['phone']=phone
			break
		else:
			print('输入有误，请重新输入')
	while True:
		ID=input('请输入身份证号:')
		if len(ID)==18:
			d['ID']=ID
			break
		else:
			print('输入有误')
	lists.append(d)
	print(lists)
	print('')

	f=open('4.txt','w')
	f.write(str(lists))
	f.close()
	for i in lists():
		print(lists)


def find():#查找的声明
	find=input('请输入查找人的姓名:')
	for i in lists:
		if find==i['name']:
			print('实习生姓名:%s\n实习生手机号:%s\n实习生身份证号:%s\n'%(i['name'],i['phone'],i['ID']))
			break


def change():#修改的声明
	find=input('请输入实习生的名字:')
	for i in lists:
		if find==i['name']:
			print('实习生姓名:%s\n实习生手机号:%s\n实习生身份证号:%s\n'%(i['name'],i['phone'],i['ID']))	
			print('1、修改名字')
			print('2、修改手机号')
			print('3、修改身份证号')
			c=int(input('请选择修改的序号:'))
			if c==1:
				while True:
					name=input('请输入新的名字:')
					if len(name)>=2 and len(name)<=4:	
						i['name']=name
						break
					else:
						print('\n姓名必须大于2小于4\n')
			elif c==2:
				while True:
					phone=input('请输入新的手机号:')
					if phone.startswith('1') and len(phone)==11:
						i['phone']=phone
						break
					else:
						print('输入有误，请重新输入')
			elif c==3:
				while True:
					ID=input('请输入新的身份证号:')
					if len(ID)==18:
						i['ID']=ID
						break
					else:
						print('输入有误,请重新输入')
		for k,v in i.items():
			print(k,v)
	print('')


def pop():#删除的声明
	dell=input('输入要删除的姓名:')
	for j in lists:
		if dell==j['name']:
			lists.remove(j)
			print(lists)
		else:
			print('没有此人')
	print('')


def print_list():#打印的声明
	for i in lists:
		print(i)
	print('')


def ext():
	print('　　　　　　　　欢迎下次使用^_^')


menu()

'''
def save():
	f=open('3.txt','w')
	f.write(str(lists))
	f.close()

def read():
	f1=open('3.txt','r')
	content=f1.read()
	if len(content)!=0:
		lists=eval(content)
		for i in lists:
			print(lists)
	f1.close()


save()
read()
'''








