class digua():
	def __init__(self):
		self.status='生的'
		self.times=0

	def __str__(self):
		msg='烤的程度是:%s,烤的时间是:%d'%(self.status,self.times)
		return msg

	def pr(self,time):
		times=time+times
		if self.times>=1 and times<=2:
			self.status='生的'
		elif self.times>=3 and times<=5:
			self.ststus='半生不熟'
		elif self.times>=6 and times<=8:
			self.status='8分熟'
		elif self.times>=9 and times<=12:
			sekf.status='正好'
		elif selif.times>12:
			selif.status='烤焦了'

def addzl(self,name):
	self.zl.append(name)


list=['盐','糖','辣椒','淀粉','孜然','辣椒面']
dg=digua()
for i in range(5):
	dg.pr(random.randint(1,4))
	zl=random.choice(list)
	list.remove(zl)
	dg.addzl(zl)
	print(dg)






