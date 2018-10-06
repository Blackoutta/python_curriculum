.keys()  .values()  .items() 的主要用途便是迭代字典。

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

print("\n打印所有键:")
for key in spiderman.keys():
    print("* " + key)

print("\n打印所有值:")
for value in spiderman.values():
    print("* " + value)

print("\n打印所有键值组:")
for key, value in spiderman.items(): # 这里在 for loop中用到了多重赋值技巧，分别将 key 和 value 设置成了 键 和 值
    print("{}: {}".format(key, value))
