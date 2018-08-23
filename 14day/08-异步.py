from multiprocessing import Pool
import time

def download():
	for i in range(10):
		print('下载%d%%'%(i*5))
		time.sleep(0.5)
	return '下载完了'

def noti(arg):
	print(arg)
p=Pool()
p.apply_async(download,callback=noti)
p.close()
for i in range(20):
	print('看电影中')
	time.sleep(0.5)


