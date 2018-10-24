#! python3
# xkcd.py - 下载所有的 XKCD 漫画

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # **下载页面**
    print("正在下载页面{}".format(url))
    # 日常三板斧:
    res = requests.get(url)  # 用requests下载网页
    res.raise_for_status()  # 如果下载url有误，直接报错，终止程序
    soup = bs4.BeautifulSoup(res.text, features="html.parser") # 把 requests下载的网页的文本做成bs4对象

    # TODO: 寻找漫画图片的url

    # TODO: 下载漫画图片

    # TODO: 将图片保存到 ./XKCD

    # TODO: 抓取前一张图片的url
