class B():
	def __init__(self,name):
		self.name=name
		print('我是 爸爸')
	def handle(self):
		print('看我多强大')

class A(B):
	def __init__(self,name):
		self.name=name
		print('我是 儿子')

a=A('叫爸爸')
a.handle()


