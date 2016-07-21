#!/usr/bin/env python
#coding:utf-8

import urllib
import urlparse

# urllib.urlencode
# 把字典数据转换为URL编码,用途：
# 对url参数进行编码
# 对post上去的form数据进行编码

# urlparse.parse_qs
# 把URL编码转换为字典数据

def urlencode():
    params = {'score': 100, 'name': '爬虫基础', 'comment': 'very good'}
    qs = urllib.urlencode(params)
    print(qs)
    print urlparse.parse_qs(qs)

# 把URL编码成请求参数
def parse_qs():
    url = 'https://www.baidu.com/s?wd=url%20%E7%BC%96%E7%A0%81%E8%A7%84%E5%88%99&rsv_spt=1&rsv_iqid=0x928cf1380000a436&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=16&rsv_sug1=15&rsv_t=1699JwFmhB8a5kfErU33lHHt8KRbsMzqMwqlJ00%2F9fusUM%2Bmx3gc8GLs5In0kVh7s3zU&rsv_sug2=0&inputT=5565&rsv_sug4=6174'
    result = urlparse.urlparse(url)
    print(result)
    params = urlparse.parse_qs(result.query)
    print(params)

if __name__ == '__main__':
    urlencode()
    parse_qs()