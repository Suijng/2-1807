class syster():
	def __init__(self):
		self.name='老师管理系统'
		self.lists=[]

	def add(self,tc):
		self.lists.append(tc)

	def find(self):
		pass

	def delete(self):
		pass

	def change(self):
		pass

class Techer():
	def __init__(self,name,age,sex):
		self.name=name
		self.age=age
		self.sex=sex

t=syster()
while True:
	num=int(input('请选择功能1、\n请选择功能2、\n请选择功能3、\n'))
	if num==1:
		name=input('请输入姓名')
		age=input('请输入年龄')
		sex=input('请输入性别')
		print('')
		tc=Techer(name,age,sex)
		t.add(tc)

