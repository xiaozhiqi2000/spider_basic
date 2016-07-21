#/usr/bin/env python
#coding:utf8


import urllib

def print_list(list):
    for i in list:
        print(i)


def demo():
    s = urllib.urlopen('http://blog.kamidox.com')
    # readline()读取一行
    # for i in range(10):
    #     print('line %d: %s' %(i+1 , s.readline()))

    # readlines()读取全部,返回的是一个列表
    # lines = s.readlines()
    # print_list(lines)

    # getcode()是获取请求url的状态码
    print(s.getcode())

if __name__ == '__main__':
    demo()