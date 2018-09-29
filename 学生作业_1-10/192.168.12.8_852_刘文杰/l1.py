
import os

def clear_screen():
    os.system('cls')
name = input("请输入你的姓名：")
clear_screen()
number = 200
price = 20


while True:
    try:
        print(f"当前剩余票数：{number}")
        print(name + ",欢迎进入")

        gmsl = int(input("请输入你要购买的数量："))
        clear_screen()
    except ValueError:
        print("请输入整数的购买数量")
        input("输入任意键继续")
        clear_screen()
        continue

    if gmsl < 0:
         print(f"你的购买数为{gmsl},购买数量不能为负数")
         input()
         clear_screen()
    elif gmsl > number:
         print(f"你的购买数为{gmsl},超出了剩余票数")
         input()
         clear_screen()
    elif gmsl == 0:
        print(f"购买数量不能为0，输入任意键返回")
        input()
        clear_screen()
    else:
         price_number = price * gmsl
         pay = input(f"你的购买数量为{gmsl},需要支付{price_number}元（输入pay确认支付，输入其他任意键取消支付）:").lower()
         clear_screen()
         if pay == "pay":
             number = number - gmsl
             print("购买成功，祝你旅途愉快！")
             input("输入任意键返回")
             clear_screen()
             if number == 0:
                 print("票已售完，输入任意键退出售票")
                 input()
                 break
         else:
             print("你取消了购买，输入任意键返回")
             input("输入任意键返回")
             clear_screen()
