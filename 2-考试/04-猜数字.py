import random
a=random.randint(1,100)
for i in range(10):
	b=int(input('请输入数字'))
	if b>a:
		print('猜的太大了')
	elif b<a:
		print('猜的太小了')
	else:
		print('恭喜你答对了')
		break



