字典是python中的一种数据类型，它使用 键-值(key-value)对应的方式来存储数据，就像我们日常生活中的字典一样。


如何创建一个字典：

    dictionary = {
        "苹果": "apple",  #冒号左侧是键(key)，右侧是值(value)
        "梨子": "pear",  # 每队键值以逗号隔开
        "桃子": "peach",
        "橘子": "orange",
    }

如何从字典中取值：

    dicitonary["苹果"]  # 没错，字典的索引不是数字，而是键(key)
    dicitonary["梨子"]   # 在REPL中试试看会不会返回与这个键配套的值
    dicitonary["桃子"]
    dicitonary["橘子"]

检测一个键是否在字典中：
    "苹果" in dicitonary  # 返回 True
    "梨子" in dictionary  # 返回 True
    "apple" in dicitonary # 返回 False, 因为 "apple" 不是键
