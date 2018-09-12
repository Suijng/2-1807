def w1(fun):
	def inner():
		print('正在验证')
	return inner
@w1
def text():
	print('哈哈')

text()


