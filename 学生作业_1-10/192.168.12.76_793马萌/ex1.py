tickets = 100
price = 53

user_name = input("请输出你的名字:")
print("欢迎来到购票系统,{}!".format(user_name))

while tickets !=0:
    print("当前剩余张{}票".format(tickets))
    try:
        tickets_by = int(input("请输出你购买的数量:"))
        if tickets_by <=0 :
            print("请输出一个大于0的整数")
            continue
        elif tickets_by <= tickets :
            print("你购买了{}张票,价格为{}".format(tickets_by,tickets_by*price))
            confirm =input("确认购买请输出YES并按回车,取消请输出NO并按回车")
            if confirm.upper() =='YES':
                print("购买成功")
                tickets -= tickets_by
                continue
        elif tickets_by > tickets:
            print("还剩有{}张票,请再次确认购买".format(tickets))
            continue
    except ValueError:
            print("请输出一个整数！")
    else:
        print("本次车票已售罄完，欢迎下次购买")
