import random
random_number = random.randint(1,5)

try:
    guess = int(input("现在有一个1-5之间的整数，猜猜看是几： "))
    if guess < 1 or guess > 5:  # 如果用户猜的数小于1 或者 大于5
        raise ValueError  # 就引发一个 值错误

    if guess == random_number:
        print("恭喜你，答对了!")
    elif guess > random_number:
        guess = int(input("你的数比我想的数要大，再给你一次机会： "))
        if guess < 1 or guess > 5:  # 如果用户猜的数小于1 或者 大于5
            raise ValueError  # 就引发一个 值错误

        if guess == random_number:
            print("恭喜你，答对了！")
        else:
            print("答错了！")
    elif guess < random_number:
        guess = int(input("你的数比我想的数要小，再给你一次机会： "))
        if guess < 1 or guess > 5:  # 如果用户猜的数小于1 或者 大于5
            raise ValueError  # 就引发一个 值错误

        if guess == random_number:
            print("恭喜你，答对了！")
        else:
            print("答错了！")
    else:
        print("答错了！")
except ValueError:
    print("哦豁！程序出错。你必须输入一个1-5之间的整数！")
