import os
import random

def clear_screen():
    os.system('cls')

price = 89
ticket = 900
z_price = price * ticket
name = input("请输入您的姓名，并以回车键结束：")

try:
    while True:
        num = input(f"{name}您好！现在有{ticket}张票！")
        
            buy = int(input("请输入您想购买的票数："))
            buy2 = input(f"您确定购买{buy}张票？yes or no")
                if buy2 == "yes":
                    print(f"您已支付{z_price}元，购买成功！")
                    ticket = ticket-buy
                    print(f"现在剩余{ticket}张票！")
                elif buy2 == "no":
                    print("您已取消订单！")
                    continue
                else:
                    raise ValueError
                break

except ValueError:
    print("输入错误，请重新登录！")
