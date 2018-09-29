tickets_remaining = 100
ticket_price = 20

user_name = input("请输入您的名字：")
print("欢迎来到康哥购票系统，{}！".format(user_name))

while tickets_remaining !=0:
    print("当前剩余票数：{}".format(tickets_remaining))
    try:
        tickets_to_buy = int(input("请输入购票数量："))
        if tickets_to_buy <= 0:
            print("请输入一个大于0的整数！")
            continue

        elif tickets_to_buy <= tickets_remaining:
            print("您正在购买{}张票，总价格为{}".format(tickets_to_buy,tickets_to_buy * ticket_price))
            confirm = input("确认购买输入 CONFIRM 并按回车，取消请输入任意字符并按回车。")
            if confirm.upper() == 'CONFIRM':
                print("购买成功！")
                tickets_remaining -= tickets_to_buy
                continue
        elif tickets_to_buy > tickets_remaining:
            print("您正在购买{}张票，剩余票数有{},剩余票数不足，请重新输入购买数量。".format(tickets_to_buy,tickets_remaining))
            continue
    except ValueError:
        print("请输入一个整数！")
    else:
        print("对不起，卖完了，欢迎下次光临！")
