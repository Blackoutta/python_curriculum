每次我们上B站，都需要：
打开浏览器 - 打开B站 - 找到搜索栏 - 在搜索栏搜索需要看的番剧 - 显示搜索结果

我们可以利用python让这个流程简化点：
运行python脚本 - 输入想要看的番剧 - 显示搜索结果

--------------------------------------------------------------------------------
import webbrowser

address = input("请输入想看的番剧: ")
webbrowser.open('https://search.bilibili.com/all?keyword=' + address)
