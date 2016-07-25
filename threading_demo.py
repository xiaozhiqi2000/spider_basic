#/usr/bin/env python
#coding:utf8

'''
1.锁：aquire,release,threading.Lock,threading.RLock
2.信号量：threading.Semaphore,init_value
3.条件：threading.Condition,wait,notify,notify_all
4.事件：和条件类似
'''


import threading
import time
import random

def worker_func():
    print('worker thread is started at %s' % threading.current_thread())
    # 变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
    random.seed()
    # 让线程随机睡眠0-1秒之间
    time.sleep(random.random())
    print('worker thread is finished at %s' % threading.current_thread())


def simple_thread_demo():
    # 通过for循环生成10个线程
    for i in range(10):
        # 每个线程都执行worker_func这个方法，注意这里不需要带括号
        threading.Thread(target=worker_func).start()

# 给每个线程加锁：一个时间只会有一个线程在运行
def worker_func_lock(lock):
    lock.acquire()  # 请求上锁
    worker_func()   # 执行
    lock.release()  # 释放锁

# 创建一个锁
gLock = threading.Lock()

# 创建线程信号量，设置设置多少线程同时开锁,这里是同时3个线程一起工作
gSem = threading.Semaphore(3)


def thread_demo_lock():
    for i in range(10):
        threading.Thread(target=worker_func_lock,args=[gLock]).start()

def thread_demo_lock1():
    for i in range(10):
        threading.Thread(target=worker_func_lock,args=[gSem]).start()

if __name__ == '__main__':
    #simple_thread_demo()
    #thread_demo_lock()
    thread_demo_lock1()