#! python3
# xkcd.py - 下载所有的 XKCD 漫画

import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    # 下载页面
    print("正在下载页面{}".format(url))
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, features="html.parser")

    # **找漫画图片的url**
    comic_elems = soup.select('#comic img')
    if comic_elems == []:
        print("找不到漫画图片。")
    else:
        comic_url = "http:" + comic_elems[0].get('src')

    # TODO: 下载漫画图片

    # TODO: 将图片保存到 ./XKCD

    # TODO: 抓取前一张图片的url
