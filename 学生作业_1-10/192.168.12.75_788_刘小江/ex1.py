import os
def clear_screen():
      s.system('cls')

ticke = 100
price_one = 20
while True:
    print("\n\t\t\t\t\t\t买票系统\t\t\t\t\n")
    name = input("请输入你的姓名： ")
    print("——————————————————————————————————————————————————————————")
    number = input("你好！欢迎{}来到购票商城，当前的余票是{},请按任意键进入购票 ".format(name,ticke))
    try:
        aa = int(input("输入你购买的票数为整数，一张票20元: "))
        if aa > ticke :
            print("你买的票数过多超过了总票数{}张,请输入名字重新购票： ".format(aa))
        elif aa < 0:
            print("你买的票数低于了不符合购票规则{}张 ，请输入名字重新购票：".format(aa))
        elif aa < ticke and aa > 0:
            bb = input("你购买{}张票  yes  or  no(大小写即可) ？ ".format(aa))
            if bb == "no".lower() or bb =="no".upper:
                print("你好 订单已取消！返回购票页面，重新输入名字")
                print("-----------------------------------------------------------------------")
                print("-----------------------------------------------------------------------")
                continue
            elif bb == "yes".lower() or bb =="yes".upper:
                print(f"你买得票共{aa}张，你共支付了{price_one * aa}，当前的余票是{ticke-aa}张")
                print("-----------------------------------------------------------------------")
                print("-----------------------------------------------------------------------")
                continue
            else:
                print("错误：输入有误！")
                bb = input(" 请正确输入yes or no ,按任意键进入购票登陆系统 ")
        else:
            ValueError
    except ValueError:
        print("请输入一个整数")
