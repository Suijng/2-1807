def fid():
	a=0
	b=1
	for i in range(10):
		yield b
		a,b=b,a+b


print('')
g=fid()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
for i in g:
	print(i)

#生成器一定是迭代器
#迭代器不一定都是生成器







