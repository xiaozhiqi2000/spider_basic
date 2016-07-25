#/usr/bin/env python
#coding:utf8

# 正则表达式默认以单行开始匹配的
import re

def re_pattern_syntax():
    # .表示任意单一字符
    # *表示前一个字符出现>=0次
    # re.DOTALL就可以匹配换行符\n,默认是以行来匹配的
    print(re.match(r'.*', 'abc\nedf').group())
    print('*' * 80)
    print(re.match(r'.*', 'abc\nedf',re.DOTALL).group())

def re_pattern_syntax1():
    # ^表示字符串开头(单行)
    # re.MULTILINE多行匹配字符串开头
    print(re.findall(r'^abc', 'abc\nedf'))
    print('*' * 80)
    print(re.findall(r'^abc', 'abc\nabc',re.MULTILINE))

def re_pattern_syntax2():
    # $表示字符串结尾
    # re.MULTILINE表示行的结束
    print(re.findall(r'abc\d$', 'abc1\nabc2'))
    print('*' * 80)
    print(re.findall(r'abc\d$', 'abc1\nabc2',re.MULTILINE))

def re_pattern_syntax3():
    # ×/+/？
    print(re.match(r'ab*', 'a'))
    print(re.match(r'ab+', 'abb'))
    print(re.match(r'ab?', 'ab'))
    print('*' * 80)

def re_pattern_syntax4():
    # greedy贪婪/non-greedy非贪婪,默认的是贪婪的匹配
    s = '<H1>title</H1>'
    print(re.match(r'<.+>', s).group())  #贪婪模式会匹配尽量多的匹配
    print(re.match(r'<.+?>', s).group()) #非贪婪模式匹配尽量少的匹配
    print(re.match(r'<(.+)>', s).group(1))
    print(re.match(r'<(.+?)>', s).group(1))

def re_pattern_syntax5():
    # {m}/{m,}/{m,n}
    print(re.match(r'ab{2,4}', 'abbbbbbb').group())  #贪婪模式尽量匹配多
    print(re.match(r'ab{2,4}?', 'abbbbbbb').group()) #非贪婪模式尽量匹配少
    print('*' * 80)

def re_pattern_syntax6():
    # 转义字符 \ 用来匹配特殊字符
    print(re.search(r'\$','The price is $9.00').group())
    print(re.search(r'\\', 'The \\ price is $9.00').group())
    print('*' * 80)

def re_pattern_syntax7():
    # []集合中的任意单一字符
    print(re.search(r'0[xX]([0-9A-Fa-f]{6})','The hex value is 0xFF03D6').group())

if __name__ == '__main__':
    re_pattern_syntax()
    re_pattern_syntax1()
    re_pattern_syntax2()
    re_pattern_syntax3()
    re_pattern_syntax4()
    re_pattern_syntax5()
    re_pattern_syntax6()
    re_pattern_syntax7()

