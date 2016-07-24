#/usr/bin/env python
#coding:utf8

import re

def re_demo():
    # 解析价格
    txt = 'If you puchase more than 100 sets, the price of product A is $9.90.'
    # 解析数量和价格: pattern/string/MatchObject
    m = re.search(r'(\d+).*\$(\d+\.?\d*)',txt)
    print(m.groups())

def re_method():
    # search vs match
    s = 'abcdc'
    print(re.search(r'c',s))  #search是从开头到结尾的匹配到第一个匹配的
    print(re.search(r'^c', s))
    print(re.match(r'c',s))   #match是开头开始匹配
    print(re.match(r'.*c', s))

def re_method1():
    # split
    s = 'This is Joey Huang'
    print(re.split(r'\W', s))

def re_method2():
    # findall
    s1 = 'Hello, this is Joey'
    s2 = 'The first price is $9.90 and the second price is $100'
    print(re.findall(r'\w+',s1))
    print(re.findall(r'\d+\.?\d*',s2))

def re_method3():
    # finditer
    s2 = 'The first price is $9.90 and the second price is $100'
    i = re.finditer(r'\d+\.?\d*',s2)
    for m in i:
        print(m.group())

def re_method4():
    # sub
    s2 = 'The first price is $9.90 and the second price is $100'
    print(re.sub(r'\d+\.?\d*','<number>',s2))

def re_method5():
    # subn
    s2 = 'The first price is $9.90 and the second price is $100'
    print(re.subn(r'\d+\.?\d*','<price>',s2))

def re_match_object():
    # match对象
    s1 = 'Joey Huang'
    m = re.match(r'(\w+) (\w+)',s1)
    print(m.group(0,1,2))
    print(m.groups())

    m1 = re.match(r'\w+ (\w+)', s1)
    print(m1.group(1))
    print(m1.groups())


if __name__ == '__main__':
    re_demo()
    re_method()
    re_method1()
    re_method2()
    re_method3()
    re_method4()
    re_method5()
    re_match_object()



