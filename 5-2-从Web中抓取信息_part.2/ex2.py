#! python3
# ex2.py 在命令行输入需要搜索的内容，脚本会自动打开若干个搜索到的网页
import requests, sys, webbrowser, bs4
from random import randint

if len(sys.argv) < 2:
    print("本脚本使用格式：python ex3.py <搜索内容>")
    sys.exit()

print("正在下载网页...")
# 用requests下载百度搜索的网页，搜索关键词为所有的命令行参数(文件名除外)
res = requests.get('http://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:]))
# 如果网址无效就报错并终止程序，每次必加
res.raise_for_status()

# 将网页变成bs4对象
baiduSoup = bs4.BeautifulSoup(res.text, features='html.parser')

# 用.select()提取所有跟搜索结果相关的<a>标签
search_results = baiduSoup.select('.t a')

# 这里只是告知我自己有多少个搜索结果被找到
num_of_results = len(search_results)
print("找到{}个链接。".format(num_of_results))

# 挑战模式：打开随机三个搜索到的网页
url_1 = search_results.pop(randint(0, len(search_results) - 1)).get('href')
url_2 = search_results.pop(randint(0, len(search_results) - 1)).get('href')
url_3 = search_results.pop(randint(0, len(search_results) - 1)).get('href')

webbrowser.open(url_1)
webbrowser.open(url_2)
webbrowser.open(url_3)




# 普通模式：打开前三个搜索到的网页
# url_1 = search_results[0].get('href')
# url_2 = search_results[1].get('href')
# url_3 = search_results[2].get('href')
#
# webbrowser.open(url_1)
# webbrowser.open(url_2)
# webbrowser.open(url_3)
