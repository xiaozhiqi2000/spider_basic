#/usr/bin/env python
#coding:utf8

#参考文档 http://blog.csdn.net/pfm685757/article/details/46047655

import urllib2

def request():
    # 定制 HTTP头
    headers = {'User-Agent': 'Mozilla/5.0', 'x-my-header': 'my value'}
    req = urllib2.Request('http://blog.kamidox.com', headers=headers)
    s = urllib2.urlopen(req)
    print(s.read(100))
    print(req.headers)
    s.close()

# 安装不同的opener对象作为urlopen()使用的全局opener。
def install_debug_handler():
    opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1),
                                  urllib2.HTTPSHandler(debuglevel=1))
    urllib2.install_opener(opener)


if __name__ == '__main__':
    install_debug_handler()
    request()








