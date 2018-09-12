def greeting(*args):  # 这里的 * 号是通配符，后面的args意为参数。你也可以用别的单词，但是 * 必须保留
    name, day, weather = args  # 用多个变量来将可传递参数进行解包，简单来说就是用一句话同时设置了两个变量
    print("你好啊，{}！今天是{}！今天天气: {}".format(name, day, weather))
greeting("hyy", "星期二", "晴")
