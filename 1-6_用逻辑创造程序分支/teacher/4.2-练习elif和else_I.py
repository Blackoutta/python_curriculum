# TODO: 创建一个文件 ex2.py
# TODO: 抄写以下代码，该脚本是教材上 习题30 的翻(mo)译(gai)版本
# TODO: 修改变量，尝试操纵打印结果。

money = 648
gotcha = 648

print("我手头有{}元。".format(money))
print("氪金一单手游需要{}元。".format(gotcha))


if money > gotcha:
    print("氪金一单还有剩，安心氪金。")
elif money < gotcha:
    print("我好像氪不起一单。")
else:
    print("能氪，但是氪了只能喝西北风了。")



if money * 10 > gotcha * 10:
    print("要是我有10倍工资，我就可以氪10单。")
else:
    print("洗洗睡吧。")
