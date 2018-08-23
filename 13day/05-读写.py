from multiprocessing import Pool,Manager
import time
def writer(q):
	for i in 'laownag':
		q.put(i)
		print('写入队列成功')
		time.sleep(0.5)
def reader(q):
	while True:
		if not q.empty():
			msg=q.get()
			print(msg)
			if msg=='g':
				break
			time.sleep(0.5)
p=Pool(5)
q=Manager().Queue()#创建一个无限大小的队列
p.apply_async(writer,(q,))  #边写边读
p.apply_async(reader,(q,))  
p.apply(writer,(q,))  #写完 一起读
p.apply(reader,(q,))
p.close()
p.join()
