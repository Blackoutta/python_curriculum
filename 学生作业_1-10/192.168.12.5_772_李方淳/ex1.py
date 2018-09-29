import os
def clear_screen():
    os.system('cls')
name = input("请输入你的名字：")
number = 50

while True:
    print(f"你好!{name}，当前剩余{number}张票")
    try:
        buy = int(input("请输入你想够票的数量："))
    except ValueError:
        print("请输入整数！")
    if buy <= number and buy > 0:
        ver = input(f"您需要购买{buy}张票,确定请输入yes,返回请输入no:")
        ver = ver.lower()
        clear_screen()
        if ver == "yes":
            print(f"您已成功购买{buy}张票，共花费{buy}元")
            input("按回车返回上一级")
            clear_screen()
            number = number - buy
            if number == 0:
                break
        elif ver == "no":
            clear_screen()
        else:
            print("请输入yes/no!")
    elif buy <= 0 :
        print("请输入正整数票数,按回车继续")
        input()
        clear_screen()
        continue
    else:
        print("我们没有这么多的票，按回车返回上一级")
        input()
        clear_screen()

print("票已卖完，欢迎下次光临！")
