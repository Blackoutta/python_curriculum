# name = input("你好，你叫什么名字： ")
# understand = input("{}，while循环的作用你理解了吗？ yes/no  ".format(name))
# while understand.lower() != "yes":
#     print("没有关系, {}, 现在听好了：只要 while 关键词右边的'布尔条件'处于 True 状态, while loop 就可以让其代码块中的语句循环运行。".format(name))
#     understand = input("{}，现在while循环的作用你理解了吗？ yes/no  ".format(name))
#
# print("恭喜你掌握了while循环的用法，{}！我们下节课再会！".format(name))


name = input("你好，你叫什么名字：  ")
while True:
    understand = input("{}，while循环的作用你理解了吗? yes/no  ".format(name))
    if understand.lower() != 'yes':
        print("没有关系, {}, 现在听好了：只要 while 关键词右边的'布尔条件'处于 True 状态, while loop 就可以让其代码块中的语句循环运行。".format(name))
        continue
    else:
        print("恭喜你掌握了while循环的用法，{}！我们下节课再会！".format(name))
        break
