class Student():
	def __init__(self):
		self.lists=[]
	def __str__(self):
		self.stat='一共有%d'%len(self.lists)
		return stat
		print('一共有%d'%self.stat)

	def jishu(self):
		self.name=input('请输入学生姓名:')
		self.lists.append(self.name)
student=Student()
student.jishu


