class ren:
	#作用:初始化属性
	def pao(self):#实例化方法　默认被调用
		print('跑')
	def tiao(self):
		print('跳')
	def ddm(self):
		print('打代码')
	def gz(self):
		print('为爱情鼓掌')
	def sx(self):
		print('我的年龄是%d,身高是%d'%(nv.age,nv.height))



nv=ren()#创建对象或实力
nv.pao()
nv.tiao()
nv.ddm()
nv.gz()

nv.age=24#添加属性
nv.height=178
nv.sx()
#print(nv.age)
#print(nv.height)

sj=ren()
sj.pao()
sj.tiao()
sj.ddm()
sj.gz()
sj.sx()








