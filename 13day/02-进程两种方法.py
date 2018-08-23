from multiprocessing import Process
import time

def show(name):
    for i in range(5):
        time.sleep(1)
        print(name)


p=Process(target=show,args=('干活',))
p.start()#启动进程
p.join()#等待子进程结束，再往下运行
p.join(3)#最多等三秒

#time.sleep(3)
#p.terminate()#不管子进程结没结束，立马让子进程停止
print('吃喝玩乐')





