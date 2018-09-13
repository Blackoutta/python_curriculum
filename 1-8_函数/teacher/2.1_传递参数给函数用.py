在设定函数时，你可以在括号中设置'可传递的参数'，在'调用函数'时，在括号中'放入参数'，然后这些参数就可以被'传递到函数中的相关语句里'。


# 不传递参数
def greeting():
    print("你好啊，hyy!")
greeting()

# 传递一个参数
def greeting(name):
    print("你好啊，{}".format(name))
greeting("hyy")

# 传递两个参数
def greeting(name, day):
    print("你好啊，{}！今天是{}！".format(name, day))
my_name = "hyy"
today = "星期五"
greeting(my_name, today) #调用函数之前，也可以先设置变量，再直接调用变量

# 传递任意数量的参数 (这个不常用，了解一下即可)
def greeting(*args):  # 这里的 * 号是通配符，后面的args意为参数。你也可以用别的单词，但是 * 必须保留
    name, day, weather = args  # 用多个变量来将可传递参数进行解包，简单来说就是用一句话同时设置了三个变量
    print("你好啊，{}！今天是{}！今天天气: {}".format(name, day, weather))
greeting("hyy", "星期二", "晴")
