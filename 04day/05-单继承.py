class sj():
	def __init__(self,name,xh):
		self.name=name
		self.xh=xh
	def cd(self):
		print('能充电')


class sx(sj):
	pass	

class hw(sj):
	pass

class oppo(sj):
	pass

sanxing=sx('三星','not3')
print(sanxing.name,sanxing.xh)
sanxing.cd

huawei=hw('华为','x7')
print(huawei.name,huawei.xh)
huawei.cd

oppo=oppo('oppo','R9s')
print(oppo.name,oppo.xh)
oppo.cd









