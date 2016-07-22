#/usr/bin/env python
#coding:utf8

#参考文档 http://blog.csdn.net/pfm685757/article/details/46047655

import urllib2
import cookielib

# cookielib.CookieJar()用来获取服务器发送给客户端的cookies
def handle_cookie():
    # 提供解析并保存 cookie 的接口
    cookiejar = cookielib.CookieJar()
    # 提供自动处理 cookie的功能
    handler = urllib2.HTTPCookieProcessor(cookiejar=cookiejar)
    opener = urllib2.build_opener(handler, urllib2.HTTPHandler(debuglevel=1),
                                  urllib2.HTTPSHandler(debuglevel=1))
    s = opener.open('http://www.douban.com')
    print(s.read(100))
    s.close()

    print('=' * 80)

    # 获取服务器发来的cookies
    print(cookiejar._cookies)
    print('=' * 80)

    s = opener.open('http://www.douban.com')
    s.close()


if __name__ == '__main__':
    handle_cookie()








