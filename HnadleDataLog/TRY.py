import os
from multiprocessing import Process
import time
def foo(x):
    print('Process start')
    time.sleep(x)
    print('Process end')

if __name__ == '__main__':
    p1 = Process(target=foo, args=(1,)) #进程传参的固定模式
    print(os.getpid())
    p2 = Process(target=foo, args=(2,))
    print(os.getpid())
    p3 = Process(target=foo, args=(3,))
    print(os.getpid())
    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    end = time.time()
    print(end-start)
    print('主进程')

