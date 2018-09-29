import os
os.system('cls')
name = input("您好！请输入您的名字：")
number = 100 #票数为100张
Price = 50   #票价为50元
print(f"欢迎 {name} 来到电影城购票系统！当前票数为{number}张,票价为50元一张！")
while True:
    purchase = input("购票请输入 :“YES”;退出请输入：“exit”！\n" )
    if purchase == 'yes':
        print("正在为您下单！")
    elif purchase == 'exit':
        print("您已经退出购票系统，期待您的下次光临！")
        break
    else:
        print("您输入的格式不正确，请您重新输入!!! ")
        continue
    try:
        ticke = int(input(f"请您选择票数："))
        number1 = input("确认订单请输入 :“YES”;取消订单请输入：“NO”！\n ")
        number2 = int(number-ticke)
        money = Price*ticke
        if ticke > number:
            print("票数不足或售罄，请重新输入！")
        elif number1 == 'yes':
            number = number-ticke
            print(f"订单已成功！您购买了{ticke}张票，您一共消费了{money}元！当前票数还剩{number2}")
            print(f"谢谢您的观看，欢迎 {name} 再次光临！")
            continue
        elif number1 == 'no':
            print("订单已取消，感谢您的光临！")
            break
        elif purchase == 'exit':
            print("您已经退出购票系统，期待您的下次光临！")
            break
        else:
            raise  ValueError
    except ValueError:
        print("您输入的格式不正确，请您重新输入!!! ")
