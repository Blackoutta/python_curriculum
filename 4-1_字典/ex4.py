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

    get_english = dictionary.get(query, "没有找到关键词,你可以手动将它的英语单词添加到字典中。")
    print("{}: {}".format(query, get_english))
    if get_english == "没有找到关键词,你可以手动将它的英语单词添加到字典中。":
        query_add_to_dict = input("请输入 {} 的英语单词: ".format(query))
        dictionary[query] = query_add_to_dict
        print("添加成功！")
    else:
        continue
