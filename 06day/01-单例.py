class dag():
	__instance=None
	__mingzi=False

	def __init__(self,name):
		if dag.__mingzi==False:
			self.name=name
			dag.mingzi=True

	def __new__(cls):
		if cls.__instance==None:
			cls.__instance=super().__new__(cls)
			return cls.__instance
		else:
			return cls.__instance

dog2=dag('小红')
print(id(dog2))
dog1=dag('小明')
print(id(dog1))









