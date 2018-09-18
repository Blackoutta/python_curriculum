import os

def clear_screen():
    os.system('cls')


clear_screen()
user_name = input("请输入您的姓名：  ")
tickets_remaining = 100
ticket_price = 15

clear_screen()
print("{}，欢迎来到胡老师购票系统！".format(user_name))

while True:
    clear_screen()
    try:
        print("当前剩余票数：{}".format(tickets_remaining))

        if tickets_remaining > 0:
            purchase_amount = int(input("请输入购买数量： "))
            if tickets_remaining < purchase_amount:
                clear_screen()
                input("\n**对不起，您的购买数量({})超出了剩余票数({})，购买失败。**\n".format(purchase_amount, tickets_remaining))
                continue
            elif purchase_amount == 0:
                clear_screen()
                input("\n**对不起，购票数量不能为0。**\n")
                continue
            elif purchase_amount < 0:
                clear_screen()
                input("\n**对不起，购票数量不能为负数。**\n")
                continue
            total = purchase_amount * 15
            clear_screen()
            print("你想购买{}张票，总价为{}元。".format(purchase_amount, total))
            confirm = input("确认订单请输入'CONFIRM'并按回车键。取消请输入任意其他键并按回车键。  >> ")
            if confirm.lower() == 'confirm':
                tickets_remaining -= purchase_amount
                clear_screen()
                input("您成功支付了{}元！祝您玩得开心！".format(total))
            else:
                continue
        else:
            clear_screen()
            input("\n**所有的票都已售罄。欢迎下次光顾。**\n")
            break
    except ValueError:
        clear_screen()
        input("\n**票数必须是整数且不能为空！**\n")
        continue
