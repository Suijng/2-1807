import random
lists=[]
while True:
	i=random.randint(1,101)
	if i not in lists:
		lists.append(i)
		if len(lists)==10:
			break
print(lists)

a=lists[7]
print(a)

lists.sort()
print(lists)

b=lists.index(a)
print(b)

