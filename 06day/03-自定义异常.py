class showerror(Exception):
	def __init__(self,name):
		name=name

class baocuo():
	def mingzi(self):
		name=input('请输入名字')
		try:
			if name=='laowang':
				raise showerror(name)
		except showerror as ret:
			print('laowang有毒')
im=baocuo()
im.mingzi()










