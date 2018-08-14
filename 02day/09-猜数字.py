class youxi():
	def cai(self):
		import random
		a=random.randint(0,100)
		for i in range(10):
			yh=int(input('请猜数字:'))
			if yh<a:
				print('猜小了')
			elif yh>a:
				print('猜大了')
			else:
				print('猜对了')
				break
caizi=youxi()
caizi.cai()
























