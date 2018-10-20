要使用 BeautifulSoup4 (以下简称bs4) 来拆解 HTML，你需要先把抓取的 HTML 做成一个 bs4 对象。

如果想从互联网抓取网页，并制作bs4对象：
--------------------------------------------------------------------------------
import requests, bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)  # 返回 'bs4.BeautifulSoup'表示成功
--------------------------------------------------------------------------------



如果想从本地文件夹抓取网页，并制作bs4对象：
--------------------------------------------------------------------------------
import bs4
example_file = open('example.html')
example_soup = bs4.BeautifulSoup(example_file)
type(example_file)  # 返回 'bs4.BeautifulSoup'表示成功
--------------------------------------------------------------------------------
