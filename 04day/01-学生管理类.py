class guanli():
	def __init__(self):
		self.naem='学生管理大师v1.0'
		self.list=[]

	def add(self,stu):
		self.list.append(stu)

	def find(self):
		pass

	def delete(self):
		pass

	def change(self):
		pass

class student():
	def __init__(self,name,age):
		self.name=name
		self.age=age

m=guanli()
for i in range(2):
	name=input('输入学生姓名:')
	age=int(input('输入学生年龄:'))
	stu=student(name,age)
	m.add(stu)
print(m.list)


















