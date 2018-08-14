class shouji():
	print('哈哈哈')
	count=10#类属性
	__count1=20#私有类属性
	def __init__(self,color):
		self.color=color#实力属性
		self.__age=10#私有属性

	def getgn(self):
		return self.__age

	'''
	def getCount1(self):
		return shouji.count
	'''
	@classmethod
	def getCount(cls):
		print('我是类方法')
		return cls.count

	@classmethod
	def getCount1(cls):
		return cls.__count1




xiaomi=shouji('蓝色')
print(xiaomi.color)
print(xiaomi.getgn())

#print(shouji.count)#通过类访问类属性

shouji.getCount()#通过类访问类对象
#tom.getCount()#通过对象访问类方法

#print(tom.getCount1())

#print(shouji.__count1())
print(shouji.getCount1())#通过类访问类属性








