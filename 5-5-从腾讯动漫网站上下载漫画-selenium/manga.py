#! python3
# 从腾讯动漫网站上下载所有漫画

import requests, os, bs4, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

episode = 1  # 设定初始话数
os.makedirs('航海王', exist_ok=True)  # 创建一个来装漫画的总文件夹
url = 'http://ac.qq.com/ComicView/index/id/505430/cid/1'  # 获取第一话的url
# browser = webdriver.Chrome()  想用谷歌浏览器的话就用这个
browser = webdriver.Firefox()

while episode < 903:  # 目前一共902话，所以以下代码要循环902次
    browser.get(url)  # 让 selenium打开设定的url
    os.makedirs('航海王//航海王第{}话'.format(episode), exist_ok=True)  # 建立一个子文件夹，该文件夹以话数命名
    html_element = browser.find_element_by_css_selector("html")  # 获取页面中的html元素，我们会在下面对它发送向下滚动网页的指令。
    # 腾讯使用了JS来让用户边浏览边加载图片，如果不让网页滚动到最下面，则无法获取所有的图片元素

    print("正在通过滚动页面获取图片...")
    for i in range(130):  # 对于60+页的某些话，需要向下滚动130下才能到达最底
        html_element.send_keys(Keys.PAGE_DOWN)  # 让页面向下滚动一下，等同于你自己在浏览器中按一下page down按钮
        time.sleep(0.1) # 按下按钮后等待 0.1秒，防止图片加载
    image_elements = browser.find_elements_by_css_selector("#comicContain li img")  # 获取所有的图片元素
    image_quantity = len(image_elements)  # 获取图片的数量

    for i in range(image_quantity):  # 以图片数量来做下载循环
        comic_url = image_elements[i].get_attribute('src')  # 获取当前图片的url
        res = requests.get(comic_url)  # 有了url，就可以用requests将图片做成res对象，从而让我们可以通过iter_content进行下载
        res.raise_for_status() # 排错保险，没啥好说的
        image_file = open("航海王//航海王第{}话//{}-{}.jpg".format(episode, episode, i), 'wb')  # 创建.jpg文件，准备以二进制方式写入
        print("正在下载图片{}...".format(i))
        for chunk in res.iter_content(100000): # 写入图片
            image_file.write(chunk)
        image_file.close()
        print("图片{}下载完成!".format(i))

    next_page_element = browser.find_element_by_css_selector("#mainControlNext")  # 找到下一话按钮的<a>标签
    url = next_page_element.get_attribute("href")  # 从按钮的<a>标签中提取href，即下一话的url地址
    episode += 1 # 话数 + 1
