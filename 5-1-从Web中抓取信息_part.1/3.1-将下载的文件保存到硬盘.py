如要将下载的文件保存到硬盘，你需要：
1. 调用 requests.get()下载该文件
2. 用 .open('需要创建的文件名', 'wb')来以二进制的方式打开一个新文件
3. 利用 Response对象的iter_content()方法做循环
4. 在每次迭代中调用 write()，将内容写入文件
5. 调用 close() 关闭该文件

代码：
--------------------------------------------------------------------------------
import requests
# get文件及排错
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
try:
    res.raise_for_status()
except Exception as err:
    print("哦豁！出错了！错误是：{}".format(err))

# open write close文件
playFile = open('罗密欧与朱丽叶.txt', 'wb')
for chunk in res.iter_content(100000):  # 以100000字节为单位进写文件写入
    playFile.write(chunk)
playFile.close()
