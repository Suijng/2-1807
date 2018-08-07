import os
name=input('请输入文件名字:')
lists=os.listdir(name)
os.chdir(name)
for i in lists:
	name1=i.rfind('.')
	name2=i[:name1]+'-腾讯'+i[name1:]
	os.rename(i,name2)



























