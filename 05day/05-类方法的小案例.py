class detel():
	def __init__(self,y,m,d):
		self.y=y
		self.m=m
		self.d=d

	def show(slef):
		print('今年是%s年%s月%s日'%(self.y,self.m,self.d))

	@classmethod
	def del_date(cls,date):
		'''
		y,m,d=str.split('')
		return y,m,d  #相当于date(y,m,d)
		'''

'''
str1='2018-8-10'
str2='2018-08-02'
str4='2018-08-2'
'''

str='2018-08-10'
y,m,d=str.split('-')
dt=datel(y,m,d)
dt.show()

'''
str='2018-08-10'
dt=datle.del_date(str)
dt.show()
'''


'''
str='2018-08-10'
dt.datel.del_date(str)
dt.print_show()
'''

str='2018-08-10'
datel.del_date(str)




