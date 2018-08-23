class Student():
	count=0
	def __init__(self,name):
		self.name=name
		Student.count+=1
	def good(self):
		print('好学生')

student=Student('小明')
student1=Student('红红')
student2=Student('萱萱')
student3=Student('娇娇')
student4=Student('瑶瑶')

student.good()

print('一共有%d'%student.count)



