import os
poll = 100    #票数
price = 98    #票的价格
user_name = input("请输入你的名字：")
def clear_screen():  # 这个函数一旦被调用会对控制台进行清屏
    os.system('cls')

flag = True
while flag:
    try:
        print("当前票数为{}张".format(poll))
        user_buy = int(input("你好，{}，请问你需要购买几张票：".format(user_name)))
        if user_buy < poll and user_buy > 0:
            clear_screen()
            buy_price = user_buy * price
            print("你需要支付{}元".format(buy_price))
            verify = input("请确认你的票数{}并输入confirm确认，取消请按任意键:".format(user_buy))
            clear_screen()
            if verify.lower() == "confirm":
                print("购票成功！")
                poll = poll - user_buy
                while True:
                    try:
                        user_buy1 = input("你是否还需要购票，请输入yes/no：")
                        if user_buy1.lower() == "yes":
                            clear_screen()
                            break
                        elif user_buy1.lower() == "no":
                            clear_screen()
                            print("欢迎下次光临！")
                            flag = False
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        clear_screen()
                        print("请输入yes/no")
            elif verify.lower() != "confirm":
                print("你已经取消购票！")
                while True:
                    try:
                        user_buy1 = input("你是否还需要购票，请输入yes/no：")
                        if user_buy1.lower() == "yes":
                            clear_screen()
                            break
                        elif user_buy1.lower() == "no":
                            clear_screen()
                            print("欢迎下次光临！")
                            flag = False
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        clear_screen()
                        print("请输入yes/no")
        elif user_buy > poll:
            clear_screen()
            print("你正在购买{}张票，剩余票数有{}，剩余票数不足，请重新输入购买数量。".format(user_buy,poll))
            continue
        elif user_buy < 0:
            clear_screen()
            print("请输入一个大于0的整数！")
            continue
        elif user_buy == poll:
            clear_screen()
            buy_price = user_buy * price
            print("你需要支付{}元".format(buy_price))
            verify = input("请确认你的票数{}并输入confirm确认，取消请按任意键:".format(user_buy))
            clear_screen()
            if verify.lower() == "confirm":
                print("购票成功！")
                print("当前票价已售完，欢迎下次光临！")
                break
        else:
            raise ValueError
    except:
        clear_screen()
        print("请输入一个整数。")
