import os

def clear_screen():
    os.system('cls')
name = input("请输入你的名字:")

print("欢迎你{},来到天价购票网站".format(name))


ticket = 1000
remainder = 666
price = 666

print("今天还有{}张票。".format(ticket))
print("截止到目前还有{}张票，还要不要？".format(remainder))

while True:
    try:
        buy = int(input("买几张？:"))
        if  remainder < buy  or buy < 0:
            raise ValueError
    except ValueError:
            print("票数不够了！ 或者你输入了不存在的票，你，{}再输一遍!要么买要么走。".format(name))
            continue
    else:
            print("运气不错{}，票数还够，买吧，一共要支付{}元。".format(name,price*buy))

            while True:
                b=input("你买了{}张票，一共要支付{}元，买吗？    yes/no ".format(buy,price*buy))
                if b == "yes":
                    remainder -= buy
                    print("哎哟{}，购票成功，神豪啊！还剩票数{}张！，壕，要不一起买了呗！".format(name,remainder))
                    break
                elif b =="no":
                    print("在看看吧！{}，不买吗？那滚吧！".format(name))
                    break
                else:
                    print("输错了，再输一遍，还输错就不要买了")
                    continue

    zmp=input("{}，你还要买票不？  yes/no(任意键退出)" .format(name))
    if zmp == "yes":
        continue
    else:
        zmp == "no"
        print("{}，走你！下次不要再来了！".format(name))
        break

prompt = input("是否清屏? y/n")
if prompt == 'y':
            clear_screen()
