lists=[]
class guanli():
	def add(self):
		while True:
			name=input('输入名字:')
			age=int(input('输入年龄:'))
			lists.append(name,age)
			lists.append(age)
			f=open('1.txt','w')
			f.write(str(lists))
			f.close()
mingpian=guanli()
mingpian.add()























