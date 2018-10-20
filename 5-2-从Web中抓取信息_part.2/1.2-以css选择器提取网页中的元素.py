import bs4
example_file = open('example.html')
example_soup = bs4.BeautifulSoup(example_file)
elems = example_soup.select('#author')  # 以css选择器选中html中的元素

# TODO: 以 python -i 模式运行该脚本，并在REPL中依次输入以下命令：
    # type(elems)                    # 查看 elems的数据类型
    # len(elems)                     # 查看 elmes的长度
    # type(elems[0])                 # 查看 elems列表中对象的类型
    # elem[0].getText()              # 获取 elems 0号索引对象的文本
    # str(elems[0])                  # 将 elems 0号索引对象转换为字符串
    # elems[0].attrs                 # 提取 elems 0号索引对象的属性
