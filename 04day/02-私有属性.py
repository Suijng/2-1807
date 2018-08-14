class gou():
	def __init__(self,name):
		self.name=name
		self.__age=0

	def setage(self,age):
		if age>15 or age<1:
			print('不符合')
		else:
			self.__age=age

	def getage(self):
		return self.__age





'''	
za=gou('藏獒',100)
hsq=gou('哈士奇',18)
print(za.name,za.age)
print(hsq.name,hsq.age)
'''

#za.setage('藏獒')
#za.getage(100)

za=gou('藏獒')
za.setage(13)
print(za.getage())
print(za.name)
