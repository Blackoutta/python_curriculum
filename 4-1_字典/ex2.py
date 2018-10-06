dictionary = {
    "苹果": "apple",  #冒号左侧是键(key)，右侧是值(value)
    "梨子": "pear",  # 每队键值以逗号隔开
    "桃子": "peach",
    "橘子": "orange",
}

while True:
    query = input("请输入你要查询的词(中文): ")
    if query == '':
        input("输入的词不能为空！")
        continue
    elif query.isnumeric() == True:
        input("请输入一个中文词而不是数字!")
        continue
    elif " " in query:
        input("输入的词不能含有空格!")
        continue
    if query in dictionary:
        print("{}: {}".format(query, dictionary[query]))
    else:
        print("找不到相关词条: {}，请手动输入它的英文单词。".format(query))
        dictionary[query] = input("*{}* 的英文单词是:  ".format(query))
        print("词条: {} 的英文单词已更新为: {}!".format(query, dictionary[query]))
