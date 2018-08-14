class mao():
	def __init__(self,name):
		self.name=name

	def eat(self):
		print('吃')

	def sleep(self):
		print('谁')

class Cat(mao):
	pass

class Dog(mao):
	pass

class pig(mao):
	pass

bsm=Cat('波斯猫')
bsm.eat()
bsm.sleep()
print(bsm.name)

wc=Dog('旺财')
wc.eat()
wc.sleep()
print(wc.name)

pq=pig('佩奇')
pq.eat()
pq.sleep()
print(pq.name)













