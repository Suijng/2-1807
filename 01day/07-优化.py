lists=[]
name=input('请输入名字:')
age=int(input('请输入年龄:'))
lists.append(name)
lists.append(age)



def save():
	f=open('3.txt','w')
	f.write(str(lists))
	f.close()

def read():
	f1=open('3.txt','r')
	content=f1.read()
	if len(content)!=0:
		lists=eval(content)
		for i in lists:
			for k,v in i.items():
				print(k,v)
		print(lists)
	f1.close()


save()
read()

