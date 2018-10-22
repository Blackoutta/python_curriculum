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

    # 找漫画图片的url
    comic_elems = soup.select('#comic img')
    if comic_elems == []:
        print("找不到漫画图片。")
    else:
        comic_url = "http:" + comic_elems[0].get('src')
    # 下载漫画图片
        print("正在下载漫画{}".format(comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()

    # 将图片保存到 ./XKCD
    image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    # 抓取前一张图片的url
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')
