#/usr/bin/env python
#coding:utf8
# 从雅虎财经获取股票数据

import urllib
import datetime

def download_stock_data_in_period(stock_list, start , end):
    for sid in stock_list:
        params = {'a': start.month - 1, 'b': start.day, 'c': start.year,
              'd': end.month - 1, 'e': end.day, 'f': end.year, 's': sid}

        url = 'http://table.finance.yahoo.com/table.csv?'
        qs = urllib.urlencode(params)
        url = url + qs
        fname = '%s_%d%d%d_%d%d%d.csv' % (sid,start.year,start.month,start.day,
                                            end.year, end.month, end.day)
        if int(urllib.urlopen(url).getcode()) != 404:
            print('downloading %s from %s' % (fname, url))
            urllib.urlretrieve(url, fname)


if __name__ == '__main__':
    stock_list = ['300001.sz','300002.sz', '304002.sz']
    start = datetime.date(year=2016, month=6, day=17)
    end = datetime.date(year=2016, month=7, day=17)
    download_stock_data_in_period(stock_list,start,end)




