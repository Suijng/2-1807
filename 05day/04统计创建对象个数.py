class phone():
	count=0#类属性
	def __init__(self,color):
		self.cplor=color
		phone.count+=1

	def call(self):
		print('打电话')


xiaomi=phone('白色')
xiaomi1=phone('黑色')
xiaomi2=phone('灰色')

print(phone.count)















