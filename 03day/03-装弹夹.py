class ren():
	def __init__(self,name):
		self.name=name
	def zhangdan(self,dj,zd):
		dj.adddan(zd)
	def zhangjia(self,qiang,dj):
		qiang.zhangjia(dj)

class qiang():
	def __init__(self,name):
		self.name=name
	def zhangjia(self,dj):
		self.dj=dj

class danjia():
	def __init__(self,rl):
		self.rl=rl
		self.zds=[]
	def adddan(self,zd):
		self.zds.append(zd)
		

class zidan():
	def __init__(self,xh,sh):
		self.xh=xh
		self.sh=sh

nr=ren('老王')
AKM=qiang('AK')
dj=danjia(40)
for i in range(40):
	zd=zidan('7.62',10)
	nr.zhangdan(dj,zd)
nr.zhangjia(dj)
























