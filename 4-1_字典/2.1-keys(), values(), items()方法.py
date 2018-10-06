现在我们来学习三个字典方法，它们是: .keys()  .values()  .items()

例子：
spiderman = {
    '中文名': '彼得·本杰明·帕克',
    '外文名': 'Peter Benjamin Parker',
    '别名': 'Spider-Man',
    '身高': '178cm',
    '体重': '76kg',
    '武器装备': '蛛网发射器',
    '主要能力': '蜘蛛力量、蜘蛛吸附、蜘蛛感应'
}

在'REPL'中试试:
spiderman.keys() 会返回所有字典中的 键
spiderman.values() 会返回所有字典中的 值
spiderman.items() 会返回所有字典中的 键值组
注意，这三个方法所返回的列表'不是真正的列表'，而是三种特殊的数据类型：dict_keys, dict_values, dict_items
想要把这三种特殊的数据类型转换成列表，用list()即可。如： list(spiderman.keys())
