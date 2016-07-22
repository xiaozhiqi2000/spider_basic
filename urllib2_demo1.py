#/usr/bin/env python
#coding:utf8

# urllib2.Request(url,data,headers)
# headers - 字典
# 使用 Request 添加或修改 http 请求首部
# Accept: application/json
# Content-Type: application/json
# User-Agent: Chorme


import urllib2

def request():
    # 定制 HTTP头
    headers = {'User-Agent': 'Mozilla/5.0', 'x-my-header': 'my value'}
    req = urllib2.Request('http://blog.kamidox.com', headers=headers)
    s = urllib2.urlopen(req)
    print(s.read(100))
    print(req.headers)
    s.close()

if __name__ == '__main__':
    request()








