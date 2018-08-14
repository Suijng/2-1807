class shouji():
	print('哈哈哈')
	def __init__(self,color):
		self.color=color#实力属性
		self.__age=10

	def getgn(self):
		return self.__age





xiaomi=shouji('蓝色')
print(xiaomi.color)
print(xiaomi.getgn())











