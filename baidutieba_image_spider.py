#coding:utf-8
'''
爬取python贴吧里面用户名及头像图片信息.爬取网页链接:http://tieba.baidu.com/p/4622665804，只需要爬取该贴吧链接里面的头像即可,用户名作为头像图片的名称。
'''

import requests
from HTMLParser import HTMLParser

# ugly code to fix UnicodeDecodeError
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def _attr(attrs, attrname):
    for attr in attrs:
        if attr[0] == attrname:
            return attr[1]
    return None

class ImageParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.image = []
        self.in_a = False

    def handle_starttag(self, tag ,attrs):
        if tag == 'img' and _attr(attrs,'username') and _attr(attrs,'src'):
            image = {}
            image['username'] = _attr(attrs, 'username')
            image['url'] = _attr(attrs, 'src')
            self.image.append(image)

            _download_poster_image(image)

def _download_poster_image(image):
    src = image['url']         # 获取到图片的URL
    r = requests.get(src)      # 请求图片的URL
    fname = '/tmp/' + image['username']
    with open(fname,'wb') as f:
        f.write(r.content)
        image['poster-path'] = fname

def image_req(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/45.0.2454.101 Chrome/45.0.2454.101 Safari/537.36'}
    r = requests.get(url, headers=headers)
    parser = ImageParser()
    parser.feed(r.content)
    return parser.image

if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/4622665804'
    userinfo = image_req(url)

    import json

    print('%s' % json.dumps(userinfo, sort_keys=True, indent=4, separators=(',', ': ')))





