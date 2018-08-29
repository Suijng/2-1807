class car():
	def __init__(self,color):
		self.color=color
	def ren(self):
		print('------ren------')

class Bm(car):
	def __init__(self,color):
		self.color=6
		super().__init__(color)
	def ren(self):
		print('Bm---跑---ren')

class Bc(car):
	def ren(self):
		print('Bm---跑---ren')

class Bk(car):
	def ren(self):
		print('Bk---跑---ren')

class Gc():
	def create(self,type):
		if type==1:
			return Bm('红色')
		elif type==2:
			return Bc('银色')
		elif type==3:
			return Bk('白色')
bm=Gc.create(1)
bc=GC.create(2)



