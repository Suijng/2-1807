class youxi():
	def go(self):
		import random
		for i in range(10):
			dn=random.randint(1,3)
			wj=int(input('请出拳:'))
			if (dn==1 and wj==2) or (dn==2 and wj==3) or (dn==3 and wj==1):
				print('玩家赢')
			elif dn==wj:
				print('平局')
			else:
				print('电脑赢')
caiquan=youxi()
caiquan.go()




















