#coding:utf-8

import requests
import urllib
import os


def _download_image(url, foler='image'):
    if not os.path.isdir(foler):
        os.mkdir(foler)
    print('downloading %s' % url)

    def _fname(s):
        return os.path.join(foler, os.path.split(url)[1])
    urllib.urlretrieve(url,_fname(url))


def download_wallpaper():
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
    print('totally %d images' % len(imgs))
    for i in imgs:
        if 'downloadUrl' in i:
            _download_image(i['downloadUrl'])


if __name__ == '__main__':
    download_wallpaper()