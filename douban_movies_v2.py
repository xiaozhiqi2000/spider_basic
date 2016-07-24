#/usr/bin/env python
#coding:utf8

import requests
from HTMLParser import HTMLParser

class MovieParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []
        self.in_movies = False

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
            self.in_movies = True  # 给当前的电影打上标记

        # 判断tag标签等于img并且self.in_movies这个标记等于true的时候
        if tag == 'img' and self.in_movies:
            self.in_movies = False   # 这个标记等于false就不会继续爬取下一个电影
            src = _attr(attrs, 'src')
            movie = self.movies[len(self.movies) - 1]  # 获取当前的电影
            movie['poster-url'] = src
            _download_poster_image(movie)

def _download_poster_image(movie):
    src = movie['poster-url']  # 获取到图片的URL
    r = requests.get(src)      # 请求图片的URL
    fname = '/tmp/' + src.split('/')[-1]  #将URL以/进行分割取最后一个字符串
    with open(fname,'wb') as f:
        f.write(r.content)
        movie['poster-path'] = fname

def nowplaying_movies(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454.101 Chrome/45.0.2454.101 Safari/537.36'}
    r = requests.get(url, headers=headers)
    parser = MovieParser()
    parser.feed(r.content)
    return parser.movies


if __name__ == '__main__':
    url = 'https://movie.douban.com/nowplaying/shenzhen/'
    movies = nowplaying_movies(url)

    import json
    print('%s' % json.dumps(movies, sort_keys=True, indent=4, separators=(',',': ')))





