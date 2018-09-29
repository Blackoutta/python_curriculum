
tickets_remaining = 80
ticket_price = 30

user_name = input("请输入您的名字: ")
print("欢迎来到购票系统, {}!" .format(user_name))

while tickets_remaining !=0:
    print("当前剩余票数: {}" .format(tickets_remaining))
    try:
        ticket_to_buy = int(input("请您输入购买票数: "))
        if ticket_to_buy <=0:
            print("请输入一个大于0的有效票数！")
            continue

        elif ticket_to_buy <= tickets_remaining:
            print("你正在购买{}张票,总价为{}" .format(ticket_to_buy,ticket_to_buy * ticket_price))
            confirm = input("确认购买请输入CONFIRM并按回车，取消按任意键。")
            if confirm.upper() =='CONFIRM':
                print("购买成功!")
                tickets_remaining -= ticket_to_buy
                continue
        elif ticket_to_buy > tickets_remaining:
            print("你正在买{}张票,剩余{}张,票数不足,请重新输入.".format(ticket_to_buy,tickets_remaining))
    except ValueError:
        print("请输入整数!")
else:
    print("对不起，已卖完。欢迎下次使用。")