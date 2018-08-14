def cfkj(a,b,x):
	if x=='+':
		return a+b
	elif x=='-':
		return a-b
	elif x=='*':
		return a*b
	elif x=='/':
		if b!=0:
			return a/b
		else:
			print('你傻啊 0能被除么')



