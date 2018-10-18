Python的 requests模块可以让你轻松从网页下载文件

首先，安装requests:
--------------------------------------------------------------------------------
联网： pip install requests
无网： pip install requests-2.19.1.tar.gz   # 确保控制台在文件所在路径
在REPL中输入 import requests, 如无错误出现，证明安装成功
--------------------------------------------------------------------------------





用requests.get()下载一个网页:
--------------------------------------------------------------------------------
import requests
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# 用 python -i 运行这个脚本，然后在REPL中输入以下命令：
    # type(res)   检查res对象的类型
    # resource.status_code == requests.codes.ok    检查res的HTTP协议状态，200为通过，404为没找到
    # len(res.text)    计算res对象中文本的长度
    # print(resource.text[:250])    打印res文本的前250个字符
-----------------------------------------
