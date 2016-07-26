#coding:utf-8

import requests
import urllib
import os
import threading

# 图片中转站就像金库
gImageList = []
# 线程条件,当图片中转站有图片的时候通知线程过来取
gCondition = threading.Condition()

# 生产者把图片放入中转站
class Producer(threading.Thread):
    def run(self):
        global gImageList
        global gCondition
        print('%s: started' % threading.current_thread())

        imgs = download_wallpaper_list()
        # 上锁
        gCondition.acquire()
        # 生产者将图片不断发给图片中转站
        for i in imgs:
            if 'downloadUrl' in i:
                gImageList.append(i['downloadUrl'])
        print('%s: produce finished. Left: %s' % (threading.current_thread(),len(gImageList)))
        # 发送完通知线程
        gCondition.notify_all()
        # 释放锁
        gCondition.release()

# 消费者不断的从图片中转站拿图片
class Consumer(threading.Thread):
    def run(self):
        print('%s: started' % threading.current_thread())

        # 消费者就不断的从图片中转站中拿图片
        while True:
            global gImageList
            global gCondition

            gCondition.acquire()
            print('%s: trying to download from pool.pool size is %d' % (threading.current_thread(),len(gImageList)))
            while len(gImageList) == 0:
                gCondition.wait()
                print('%s: waken up.pool size is %d' % (threading.current_thread(), len(gImageList)))
            url = gImageList.pop()
            gCondition.release()
            _download_image(url)

def _download_image(url, foler='image'):
    if not os.path.isdir(foler):
        os.mkdir(foler)
    print('downloading %s' % url)

    def _fname(s):
        return os.path.join(foler, os.path.split(url)[1])
    urllib.urlretrieve(url,_fname(url))

def download_wallpaper_list():
    # 数据分析
    # http://image.baidu.com/channel/wallpaper#%E7%83%AD%E9%97%A8%E6%8E%A8%E8%8D%90&%E5%85%A8%E9%83%A8&6&0
    # 分析得知只要往这个url发送带数据的请求，就会返回一个json文件
    url = 'http://image.baidu.com/data/imgs'
    # 用chrome分析得出需要发送的数据
    params = {
        'pn': 41,
        'rn': 100,
        'col': '壁纸',
        'tag': '国家地理',
        'tag3': '',
        'width': 1600,
        'height': 900,
        'ic': 0,
        'ie': 'utf8',
        'oe': 'utf-8',
        'image_id': '',
        'fr': 'channel',
        'p': 'channel',
        'from': 1,
        'app': 'img.browse.channel.wallpaper',
        't': '0.016929891658946872'
    }
    s = requests.get(url, params=params)
    # 用json解析
    imgs = s.json()['imgs']
    print('%s: totally %d images' % (threading.current_thread(),len(imgs)))
    return imgs


if __name__ == '__main__':
    Producer().start()

    for i in range(20):
        Consumer().start()