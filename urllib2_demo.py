#/usr/bin/env python
#coding:utf8

# urllib2提供了urllib更丰富的功能：
# urllib2.Request - 提供http header定制能力
# 提供更强大的功能，包括cookie处理，鉴权，可定制化等
# urllib2不能完全代替urllib,一般都是混合使用
# urllib.urlencode是urllib2没有的
# urlopen(url,data,timeout)
# 错误处理 HTTPError, e

import urllib2

def urlopen():
    url = 'http://blog.kamidox.com/no-exists'
    try:
        s = urllib2.urlopen(url, timeout=3)
    except urllib2.HTTPError, e:
        print(e)
    else:
        print(s.read(100))

if __name__ == '__main__':
    urlopen()








