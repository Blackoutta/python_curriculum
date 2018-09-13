现在用户输入字符串导致程序错误这个'硬漏洞'是补上了，但是还有个'软漏洞'—— 用户会输入 1-5 之外的数
别怕，我们可以通过 raise 这个词来'手动引发错误'


import random
random_number = random.randint(1,5)

try:
    guess = int(input("现在有一个1-5之间的整数，猜猜看是几： "))
    if guess < 1 or guess > 5:  # 如果用户猜的数小于1 或者 大于5
        raise ValueError  # 就引发一个 值错误，这个值错误会被下面的 except截取到
except ValueError:
    print("错误：请输入一个1-5之间的整数！")
else:
    if guess == random_number:
        print("恭喜你，猜对了！")
    else:
        print("很可惜，猜错了！")
