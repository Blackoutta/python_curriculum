现在我们来制作一个可以快速打开高德地图并搜索地址的脚本。我会提供一些代码，而你需要完成所有 #TODO

代码
--------------------------------------------------------------------------------
import webbrowser, sys, pyperclip

# TODO： 创建文件 ex1.py
# TODO： 设定一个变量 address (意为地址)
# TODO： 如果用户在运行脚本时有输入一个或多个命令行参数，将所有命令行参数拼合起来(文件名除外)，并赋值给 address
# TODO： 如果用户在运行脚本时没有输入任何命令行参数，则将当前剪贴板上的内容赋值给 address
# TODO： 使用 webbrowser.open()运行高德地图的网站，并搜索 address 中的内容
# TODO： 使用 webbrowser.open()运行高德地图的网站，并搜索 address 中的内容
# TODO:  高德地图URL格式例子：
        # https://www.amap.com/search?query=重庆
        # https://www.amap.com/search?query=重庆机电职业技术学院
        # https://www.amap.com/search?query=尖顶坡 U城天街 汉堡王
