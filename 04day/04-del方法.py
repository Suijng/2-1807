class gou():
	def __init__(self):
		self.name='二哈'
		print('init')
	def __str__(self):
		return '我是str'
	def __del__(self):
		print('我是del')

eh=gou()
print(eh)
er1=eh
del eh
print('哈哈')










