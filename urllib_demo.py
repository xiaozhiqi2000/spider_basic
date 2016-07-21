#/usr/bin/env python
#coding:utf8


import urllib

def print_list(list):
    for i in list:
        print(i)


def demo():
    s = urllib.urlopen('http://blog.kamidox.com')
    msg = s.info()

    #获取url的请求首部
    print_list(msg.headers)

    #解析过的首部元祖
    print_list(msg.items())

    #单独获取某个首部
    print(msg.getheader('Content-Type'))

    #获取msg对象所有的方法属性
    print_list(dir(msg))

if __name__ == '__main__':
    demo()