class dl(object):
	__sy=None
	def __new__(cls,*a,**b):
		if cls.__sy==None:
			cls.__sy==object.__new__(cls,*a,**b)
		return cls.__sy
a=dl()
b=dl()
print(a)
print(b)
