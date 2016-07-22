#/usr/bin/env python
#coding:utf8

#参考文档 http://blog.csdn.net/pfm685757/article/details/46047655
# build_opener(handler1,handler2,...)
# 参数handler是Handler实例,build_opener()返回的对象具有open()方法，与urlopen()函数的功能相同。
# 默认有这些 Handler 链
# ProxyHandler (如果设置了代理)
# UnknownHandler
# HTTPHandler
# HTTPDefaultErrorHandler
# HTTPRedirectHandler
# FTPHandler
# FileHandler
# HTTPErrorProcessor
# HTTPSHandler (如果安装了 ssl 模块)

import urllib2
import urllib

def request():
    # 定制 HTTP头
    headers = {'User-Agent': 'Mozilla/5.0', 'x-my-header': 'my value'}
    req = urllib2.Request('http://blog.kamidox.com', headers=headers)
    s = urllib2.urlopen(req)
    print(s.read(100))
    print(req.headers)
    s.close()

# urllib2.urlopen()函数不支持验证、cookie或者其它HTTP高级功能。要支持这些功能，必须使用build_opener()
def request_post_debug():
    # POST 提交
    data = {'username': 'kamidox', 'password': 'xxxxxxxxx'}
    headers = {'User-Agent': 'Mozilla/5.0'}
    req =  urllib2.Request('http://www.douban.com', data=urllib.urlencode(data), headers=headers)

    # 如果build_opener()没有填写Handler默认上面的全部Handler都会有
    opener = urllib2.build_opener(urllib2.HTTPHandler(debuglevel=1),
                                  urllib2.HTTPSHandler(debuglevel=1))

    # 返回的对象具有open()方法和urlopen()是功能相同的
    s = opener.open(req)
    print(s.read(100))
    s.close()


if __name__ == '__main__':
    request_post_debug()









