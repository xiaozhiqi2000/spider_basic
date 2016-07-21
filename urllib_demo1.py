#/usr/bin/env python
#coding:utf8

import urllib

#urllib.urlretrieve比urlopen相比urlretrieve可以将内容下载到本地
# url: 远程地址
# filename: 要保存都本地的文件
# reporthook: 下载状态报告
# data: POST 的application/x-www-form-urlencoded 格式的数据
# 返回(filename, HTTPMessage),本地存入的文件名和HTTPMessage对象

# reporthook:
# 参数1：当前传输的块数
# 参数2：块大小
# 参数3：数据总大小
# 需要注意：content-length 不是必需的

def print_list(list):
    for i in list:
        print(i)

def retrieve():
    fname, msg = urllib.urlretrieve('http://blog.kamidox.com','index.html')
    print(fname)
    print_list(msg.items())

if __name__ == '__main__':
    retrieve()