#!/usr/bin/env python
#coding:utf-8

import urllib

# urllib.urlencode
# 把字典数据转换为URL编码,用途：
# 对url参数进行编码
# 对post上去的form数据进行编码


def urlencode():
    params = {'score': 100, 'name': '爬虫基础', 'comment': 'very good'}
    qs = urllib.urlencode(params)
    print(qs)

if __name__ == '__main__':
    urlencode()
