import random

random_number = random.randint(1,4)
guess = int(input("现在有一个1-5之间的整数，猜猜看是几： "))

if guess == random_number:
    print("恭喜你，猜对了！")
else:
    print("很可惜，猜错了！")
