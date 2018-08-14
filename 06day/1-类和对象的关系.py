class tool(object):
	zhi=None
	cai=False
	
	def __init__(self,name):
		if tool.cai==False:
			self.name=name
		else:
			tool.cai=True

	def __new__(cls,*a,**b):
		if cls.zhi==None:
			cls.zhi=object.__new__(cls)
			return cls.zhi
		else:
			return cls.zhi


gaoba=tool('搞吧   执行')
print(gaoba.name)
print(id(gaoba))
gaoba1=tool('执行么')
print(id(gaoba))






'''
	def __str__(self):
		return '能看家     str方法'

	def __del__(self):
		print('打不过我吧,哈哈哈     del方法')

	def __new__(cls,*a,**b):
		if cls.zhi==None:
			cls.zhi=object.__new__(cls)
			return cls.zhi
		else:
			return cls.zhi
'''

gaoba=tool('搞吧   执行init')
print(gaoba.name)
gaoba1=tool('执行么')

