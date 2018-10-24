首先确保你安装了火狐浏览器，并且把火狐浏览器的安装路径添加到PATH
然后我们输入以下代码：
--------------------------------------------------------------------------------
from selenium import webdriver # 不要直接 import selenium，这样之后的代码会过于冗长
browser = webdriver.Firefox()
# 使用webdriver启动机电校的智慧校园登陆界面，你会在浏览器地址栏看到：当前网页受远程控制
browser.get('http://i.cqevi.net.cn/zfca/login')
