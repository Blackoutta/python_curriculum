#! python3
# xkcd.py - 下载所有的 XKCD 漫画

import requests, os, bs4

url = 'http://xkcd.com'  # 原始url
os.makedirs('xkcd', exist_ok=True)  # 创建一个文件夹 xkcd，用来存储漫画

# 只要url的末尾不是#号，就一直循环下载漫画图片
while not url.endswith('#'):
    # TODO: 下载页面

    # TODO: 寻找漫画图片的url

    # TODO: 下载漫画图片

    # TODO: 将图片保存到 ./XKCD

    # TODO: 抓取前一张图片的url
