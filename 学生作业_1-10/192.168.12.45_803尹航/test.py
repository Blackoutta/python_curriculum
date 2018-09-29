import os
import random

def clear_screen():
    os.system('cls')



tickets = 100
remainder = random.randint(1,100)
price = 8

name = input("\n请输入您的用户名称：")


while True:
    print("\n尊敬的 {} ，欢迎进入永辉yh售票网站\n   你需要的票数总共有 {} 张\n   目前票数还有 {} 张\n".format(name,tickets,remainder))
    try:
        a = int(input("\n请输入您想购买的票数："))
        if a <= 0:
            print("\n   请检查票数是否为大于0的整数。")
            continue
        elif a > remainder:
            print("\n   请检查票数是否超出了规定购买票数。\n")
            continue
    except ValueError:
        print("\n   请检查票数是否是纯数字。\n")
        continue
    else:
        print("\n   恭喜您 {} ，您抢票成功。\n".format(name))


    while True:
        b = input("\n您抢到了 {} 张票，总共 {} 元。请问您确定付款吗？ (yes/no)     ".format(a,a*price))
        if b == "yes":
            remainder -= a
            print("\n   好吧，您成功订购了 {} 张票。".format(a))
            print("   现在剩票为 {} 张\n".format(remainder))
            break
        elif b == "no":
            print("\n   没关系，再看看吧。\n")
            break
        else:
            print("\n输入错误，请重新输入！")
            continue


    xiao = input("是否继续操作？   (yes/no)      ")
    if xiao == "yes":
        clear_screen()
        continue
    elif xiao == "no":
        break
    else:
        print("\n输入错误！")
        break
