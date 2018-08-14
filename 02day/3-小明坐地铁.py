'''
i=31
a=i*2*6
if a>=100 and a<150:
	c=a*0.8
	print('1月12月打八折各',c)
elif a>=150 and a<400:
	d=a*0.5
	print('1月12月打五折各',d)
else:
	print('1月12月各',a)
i=28
a=i*2*5
if a>=100 and a<150:
	c=a*0.8
	print('2月打8折后')
elif 
'''
money=0
d=float(input('输入公里数:'))#公里
for i in range(1,31):
	#print('%d天'%i,end='')
	for j in range(1,3):
		#print('%d次'%j)
		if d<=6:
			p=3
		elif d>6 and d<=12:
			p=4
		elif d>12 and d<=22:
			p=5
		elif d>22 and d<=32:
			p=6
		elif d>32:
			if(d-32)%20==0:
				p=6+(d-32)/20
			else:
				p=6+int((d-32)/20)+1

		if money>100 and money<=150:
			p=p*0.8
		elif money>150 and money<400:
			p=p*0.5
		money = money+p

print('一共花了%.2f元'%money)





















	
