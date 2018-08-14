class car():
	def __init__(self,color,xh):
		self.color=color
		self.xh=xh
	def __str__(self):
		dy='颜色:%s,型号:%s'%(self.color,self.xh)
		return dy
	def yd(self):
		print('移动')
	def yy(self):
		print('音乐')

bm=car('黑','x5')
bm.yd()
bm.yy()
#print('颜色:%s'%(bm.color))
#print('型号:%s'%(bm.xh))
print(bm)


















