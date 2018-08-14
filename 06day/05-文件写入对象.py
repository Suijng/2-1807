import sys,shelve

file=shelve.open('D:\\test.dat')


data={}
data['key1']='123456'
data['key2']='eeeeee'
data['key3']='ABCDEF'
datakey='mydata'
file[datakey]=data
file.close()



file=shelve.open('D\\test.dat')
datakey='mydata'
print file[datakey]
{'key3':'ABCDEF','key2':'eeeeee','key1':'123456'}
file.close()

