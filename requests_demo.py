#/usr/bin/env python
#coding:utf8

'''
可以阅读官方文档获得更多信息：http://requests.readthedocs.io/en/latest/
requests是第三方库,pip install requests
请求requests.request(method,url,params,data,json,headers,cookies,verify)
应答requests.Response(status_code,headers,json,text,content,cookies
'''


import requests

def get_json():
    r = requests.get('https://api.github.com/events')
    print(r.status_code)
    print(r.headers)
    print(r.content)
    print(r.text)
    print(r.json())

def get_querystring():
    url = 'http://httpbin.org/get'
    params = {'qs1':'value1' ,'qs2':'value2'}  #自定义参数
    headers = {'x-headre1': 'header1','x-header2':'header2'} #自定义首部
    r = requests.get(url,params=params, headers=headers)
    print(r.status_code)
    print(r.content)

def get_cookie():
    headers = {'User-Agent':'Chrome'}
    url = 'http://www.douban.com'
    r = requests.get(url,headers=headers)
    print(r.status_code)
    print(r.cookies)
    print(r.cookies['bid'])

if __name__ == '__main__':
    get_json()
    print('=' * 80)
    get_querystring()
    print('=' * 80)
    get_cookie()









