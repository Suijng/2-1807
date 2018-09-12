class Xs():
	def __init__(self):
		self.list=[]
		self.read()
		print(self.list)
	def save(self):
		d={}
		name=input('请输入名字')
		age=input('请输入年龄')
		d['name']=name
		d['age']=age
		self.list.append(d)
		self.writelocation()
	def writelocation(self):
		f=open('1.data','w')
		f.write(str(self.list))
		f.close()

	def read(self):
		f=open('1.data','r')
		self.list=eval(f.read)
		f.close()

sm=Xs()
sm.save()



