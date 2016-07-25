#/usr/bin/env python
#coding:utf8

'''
金库取钱: 经典的生产者消费者模型
采购需要进入金库拿钱买东西
销售会把卖东西得来的前放到金库里
进门需要带一把钥匙
'''

import threading
import time
import random

# 开始讲解经典的线程问题：生产者消费者模型
gPool = 1000
gCondition = threading.Condition()

# 生产者
class Producer(threading.Thread):
    # 重写父类的run方法
    def run(self):
        # 打印初始的钱
        print('%s started' % threading.current_thread())
        while True:
            # 引用全局变量
            global gPool
            global gCondition
            # 为关键资源操作上锁
            gCondition.acquire()
            random.seed()
            p = random.randint(100, 200)
            gPool += p  # 金库存钱是关键操作，要确保为原子操作
            print('%s: Produced %d. Left %d' % (threading.current_thread(), p, gPool))
            # 随机睡眠一下，为了方便查看打印信息
            time.sleep(random.random())
            gCondition.notify_all()
            # 先通知，再释放
            gCondition.release()


# 消费者类：不停拿钱
class Consumer(threading.Thread):
    def run(self):
        print('%s started' % threading.current_thread())
        while True:
            global gPool
            global gCondition
            # 还是先上锁
            gCondition.acquire()
            # 改变随机数生成器种子
            random.seed()
            # 随机一个消费者要取的金额数
            c = random.randint(500, 1000)
            print('%s: Trying to consume %d. Left %d' % (threading.current_thread(), c, gPool))
            # 如果钱不够就等待生产者存入
            while gPool < c:
                gCondition.wait()
            # 如果钱够就直接扣除
            gPool -= c
            # 随机睡眠一下，为了方便查看打印信息
            time.sleep(random.random())
            print('%s: Consumed %d. Left %d' % (threading.current_thread(), c, gPool))
            gCondition.release()


# 生产者-消费者问题
def consumer_producer_demo():
    for i in range(10):
        Consumer().start()

    for i in range(1):
        Producer().start()

if __name__ == '__main__':
    consumer_producer_demo()