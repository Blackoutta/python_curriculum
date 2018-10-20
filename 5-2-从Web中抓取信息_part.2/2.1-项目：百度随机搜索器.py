#! python3
# ex2.py 在命令行输入需要搜索的内容，脚本会自动打开若干个搜索到的网页
import requests, sys, webbrowser, bs4

# requests正在下载网页时，用户也许会等待，我们用一个print()来告知
print("正在下载网页...")
# 用requests下载百度搜索的网页，搜索关键词为所有的命令行参数(文件名除外)
res = requests.get('http://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:]))
# 如果网址无效就报错并终止程序，每次必加
res.raise_for_status()

# TODO: 创建文件 ex2.py，将上方代码复制进去
# TODO: 普通模式：用bs4抓取前三个搜索结果的URL，它们被存储在<a>标签中的 href属性中
# TODO: 挑战模式：用bs4抓取随机三个搜索结果的URL，它们被存储在<a>标签中的 href属性中

# TODO: 用webbrowser.open()打开上述3个URL
