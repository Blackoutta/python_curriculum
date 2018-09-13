只要有input()的地方，就'必然'有用户会输入一些你不想让他输入的内容，从而导致'程序出错'。
所幸，python提供了简单的'堵错'方法，现在我们来学习两个词：try 和 except


import random
random_number = random.randint(1,5)

# 在控制台找到 出错的语句，将它变成 try 的代码块
try:
    guess = int(input("现在有一个1-5之间的整数，猜猜看是几： "))
# 在控制带找到 错误类型， 然后将错误类型写在 except 后面。代码块中的语句写上出错后程序的应对语句
except ValueError:
    print("请输入一个1-5之间的整数！")
# try 也允许使用 else， else 中的语句只有在 try代码块中的语句 不出错 的情况下才会运行
else:
    if guess == random_number:
        print("恭喜你，猜对了！")
    else:
        print("很可惜，猜错了！")
