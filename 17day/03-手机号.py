import re
def dh(a):
	ret=re.match(r'1[3456789]\d{9}$',a)
	if ret:
		print('合法')
	else:
		print('不合法')
dh(15712341234)
