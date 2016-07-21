#/usr/bin/env python
#coding:utf8

import urllib

#urllib.urlretrieve比urlopen相比urlretrieve可以将内容下载到本地
# url: 远程地址
# filename: 要保存都本地的文件
# reporthook: 下载状态报告
# data: POST 的application/x-www-form-urlencoded 格式的数据
# 返回(filename, HTTPMessage),本地存入的文件名和HTTPMessage对象

# reporthook:(包含了body内容,而没有包含首部的大小,所以得出的进度会超过100%)
# 参数1：当前传输的块数
# 参数2：块大小
# 参数3：数据总大小
# 需要注意：content-length 不是必需的

def print_list(list):
    for i in list:
        print(i)

#可以打印当前的进度
def progress(blk,blk_size,total_size):
    print('%d/%d - %.02f%%' %(blk * blk_size, total_size, (float)(blk * blk_size) * 100 / total_size))

def retrieve():
    urllib.urlretrieve('http://blog.kamidox.com','index.html',reporthook=progress)

if __name__ == '__main__':
    retrieve()