class choose(object):
	def __init__(self,name):
		self.name=name
	def run(self):
		print('握手爸爸')

class Dog(choose):
	def __init__(self,name):
		choose.__init__(self.name)
	def dayin(self):
		print('%s'%(self.name))

hsq=Dog('儿子')
hsq.dayin()
hsq.run()


