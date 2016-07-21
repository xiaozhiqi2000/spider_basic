#/usr/bin/env python
#coding:utf8

# 雅虎财经股票数据接口介绍
# 股票数据：
# 深市数据链接： http://table.finance.yahoo.com/table.csv?s=000001.sz
# 上市数据链接： http://table.finance.yahoo.com/table.csv?s=600000.ss

# 例子:获取所有上市的数据

import urllib

def download_stock_data(stock_list):
    for sid in stock_list:
        url = 'http://table.finance.yahoo.com/table.csv?s=' + sid
        fname = sid + '.csv'
        print('downloading %s form %s' % (fname, url))
        urllib.urlretrieve(url, fname)

if __name__ == '__main__':
    stock_list = ['300001.sz', '300002.sz']
    download_stock_data(stock_list)




