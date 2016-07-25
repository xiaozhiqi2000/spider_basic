#/usr/bin/env python
#coding:utf8

# 正则表达式默认以单行开始匹配的
import re

def re_pattern_syntax_meta_char():
    # \number反向引用
    print(re.search(r'(\d)(\d)(\d)\1\2\3', '135135').groups())
    print(re.search(r'(\d{3}) \1', '135 135').groups())
    print('*' * 80)

def re_pattern_syntax_meta_char1():
    # \d\D,\d表示一个数字，\D表示一个非数字,\b表示单词边界
    print(re.search(r'(\d{3}-\d{4}-\d{4})', 'The Phone Number is 1380-2231-2998').groups())
    print(re.search(r'\b(\d{3}-\d{4}-\d{4})\b','The Phone Number is 138-2231-2998').groups())
    print(re.search(r'\b(\d{3}\D\d{4}\D\d{4})\b', 'The Phone Number is 138=2231@2998').groups())
    print('*' * 80)

def re_pattern_syntax_meta_char2():
    # \s\S: [空格\t\n\r\f\v] \t:制表 \f:换页,\v:垂直制表, \S非前面那些符号
    print(re.match(r'Name\s*:\s*([a-zA-Z]+)','Name: \t Joey').groups())
    print(re.search(r'Name\s*:\s*([a-zA-Z]+)', 'FirstName: \t  Joey').groups())
    print(re.search(r'\S+:\s*([a-zA-Z]+)', 'FirstName: \t  Joey').groups())
    print('*' * 80)

def re_pattern_syntax_meta_char3():
    # \w\W: \w表示这些[a-zA-Z0-9_], \W是非前面那些字符
    print(re.match(r'(\w+)\s*:\s*(\w+)','Name  : Joey').groups())
    print('*' * 80)

def re_pattern_flags():
    # re.I/re.IGNORECASE
    print(re.match(r'(Name)\s*:\s*(\w+)','NAME  : Joey',re.IGNORECASE).groups())
    print('*' * 80)

def re_pattern_flags1():
    # re.VERBOSE此标识位可以添加注释/re.compile
    s = 'the number is 20.5'
    r = re.compile(r'''
                    \d+   # 整数部分
                    \.?   # 小数点，可能包含也可能不包含
                    \d*   # 小数部分,可选
                    ''',re.VERBOSE)
    print(re.search(r,s).group())
    print(r.search(s).group())
    print('*' * 80)

if __name__ == '__main__':
    re_pattern_syntax_meta_char()
    re_pattern_syntax_meta_char1()
    re_pattern_syntax_meta_char2()
    re_pattern_syntax_meta_char3()
    re_pattern_flags()
    re_pattern_flags1()
