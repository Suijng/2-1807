year=int(input('请输入哪年:\n'))
month=int(input('请输入月:\n'))
day=int(input('请输入日:\n'))
sum=day
days=[31,28,31,30,31,30,31,31,30,31,30,31]
i=0
if (year%4==0 and year%100!=0) or (year%400==0):
	days[1]=29
while i<month-1:
	sum=sum+days[i]
	i+=1
print('这一天是该年的第%d天'%(sum))





