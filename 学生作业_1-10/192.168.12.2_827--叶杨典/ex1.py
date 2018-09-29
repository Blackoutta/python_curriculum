import os
def clear_screen():
    os.system('cls')

user_name = input("请输入你的名字：")
buy_ticket = 100
price = 50

print("欢迎您{}，进入阿典售票系统".format(user_name))
print("当前剩余票数为{},每张票价格为{}".format(buy_ticket,price))

while True:
    try:
        question_1 =int(input("你需要买多少张票，目前剩余{}张票".format(buy_ticket)))
    except ValueError:
        clear_screen()
        print("你很皮呢！*******************请不要什么都不输入好吧！！！")
        continue
    if question_1 != "":
        if question_1 > buy_ticket:
            clear_screen()
            print("错误！***********************请输入正确的购票数量")
            continue
        elif question_1 <= buy_ticket and question_1 > 0:
            total_price = question_1 * price
            remaining_quantity = buy_ticket - question_1
            print("你购买了{}张票，总价为{}，输入666确认购票，否则取消购票！！！".format(question_1,total_price))
            try:
                sr = int(input("请确定"))
            except ValueError:
                clear_screen()
                print("你很皮呢！*******************请不要什么都不输入好吧！！！")
                continue
            if sr == 666:
                print("您用了{}元，购买了{}张票！感谢你的光临！祝你生活愉快！再见!如果还想买就重新运行脚本！对我就是怎么任性！怎样咯！！！！！！！！！！！！！".format(total_price,question_1))
                break
            else:
                clear_screen()
                print("购票失败，还剩余{}张票，请重新购票".format(buy_ticket))
                continue
        else:
            clear_screen()
            print("输入错误请重新输入需要购买的票的数量！！！！！！！！！！！！！！！")
            continue
    else:
        print("你很皮呢！*******************请不要什么都不输入好吧！！！")
        continue
