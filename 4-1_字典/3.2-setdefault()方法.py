dict.setdefault() 方法和 dict.get()方法类似。
不同之处在于: dict.setdefault()如果没有找到指定的键，会为这个键直接设置一个默认值(get方法只会返回一个设置的值)

dictionary = {
    "苹果": "apple",  #冒号左侧是键(key)，右侧是值(value)
    "梨子": "pear",  # 每队键值以逗号隔开
    "桃子": "peach",
    "橘子": "orange",
}

dictionary.setdefault("菠萝", "pineapple")
