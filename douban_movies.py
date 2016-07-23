#/usr/bin/env python
#coding:utf8

'''
 HTMLParser参考 http://www.cnblogs.com/rollenholt/archive/2011/12/01/2271058.html
 http://www.oschina.net/code/snippet_16840_1809
 HTMLParser()返回的对象具有feed()方法: 向解析器喂数据，可以分段提供

 HTMLParser是python用来解 析html的模块。它可以分析出html里面的标签、数据等等，是一种处理html的简便途径。 HTMLParser采用的是一种事件驱动的模式，当HTMLParser找到一个特定的标记时，它会去调用一个用户定义的函数，以此来通知程序处理。它主要的用户回调函数的命名都是以handler_开头的，都是HTMLParser的成员函数。当我们使用时，就从HTMLParser派生出新的类，然后重新定义这几个以handler_开头的函数即可。这几个函数包括：
 handle_startendtag 处理开始标签和结束标签
 handle_starttag 处理开始标签，比如<xx>
 handle_endtag 处理结束标签，比如</xx>
 handle_charref 处理特殊字符串，就是以&#开头的，一般是内码表示的字符
 handle_entityref 处理一些特殊字符，以&开头的，比如
 handle_data 处理数据，就是<xx>data</xx>中间的那些数据
 handle_comment 处理注释
 handle_decl 处理<!开头的，比如<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
 handle_pi 处理形如<?instruction>的东西
 '''

import urllib2
from HTMLParser import HTMLParser

class MovieParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []

    def handle_starttag(self, tag ,attrs):
        '''handle_startag这个方式是继承HTMLParser而来的，这里是重写，原来的这个方法是空的。
        tag为html中标签名称，attrs标签中的属性和值是字典类型，如data-title="绝地逃亡"'''

        # 定一个内部函数将html中属性的值取出如data-title="绝地逃亡"可以取出"绝地逃亡"
        def _attr(attrlist, attrname):  # 传入属性列表和要获取属性值的属性名
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None

        # 判断tag标签等于li,能获取属性的值，data-catetory的属性的值=nowplaying
        if tag == 'li' and _attr(attrs,'data-title') and _attr(attrs,'data-category') == 'nowplaying':
            movie = {}
            movie['title'] = _attr(attrs, 'data-title')
            movie['score'] = _attr(attrs, 'data-score')
            movie['director'] = _attr(attrs, 'data-director')
            movie['actors'] = _attr(attrs, 'data-actors')
            self.movies.append(movie)
            print('%(title)s|%(score)s|%(director)s|%(actors)s' % movie)

def nowplaying_movies(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454.101 Chrome/45.0.2454.101 Safari/537.36'}
    req = urllib2.Request(url, headers=headers)
    s = urllib2.urlopen(req)
    parser = MovieParser()
    parser.feed(s.read())
    s.close()
    return parser.movies


if __name__ == '__main__':
    url = 'https://movie.douban.com/nowplaying/shenzhen/'
    movies = nowplaying_movies(url)

    import json
    print('%s' % json.dumps(movies, sort_keys=True, indent=4, separators=(',',': ')))





