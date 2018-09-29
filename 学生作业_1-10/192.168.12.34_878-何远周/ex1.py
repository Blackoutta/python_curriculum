import os
import string
import random
num=100
temp=""
temp2=""
error=""
name=""
price=35
n=0
num2=0
max=0
loop=""
rd=0
cj=""
def clear_screen():  # 这个函数一旦被调用会对控制台进行清屏
    os.system('cls')

def try_(z):
    clear_screen()
    temp=z.isdigit()
    error=1
    loop=z
    while True:
        if z==True and int(temp)>0 and  int(temp)<=100:
            if int(z)>0 and int(z)<=100:
                return int(temp)
                break
        elif temp ==True and int(temp)>0 and  int(temp)<=100:
            if int(loop)>0 and int(loop)<=100:
                return int(z)
                break
            else:
                if temp==True:
                    loop=z
                    error=0
                else:
                    loop=temp
                temp=str(input("输入有误，请输入1~100之间的数字！您输入的信息为：{}\n请您重新输入要购票的数量:".format(loop)))
                z=temp.isdigit()
                clear_screen()

        else:
            if error==1:
                temp=str(input("输入有误，请输入1~100之间的数字！您输入的信息为：{}\n请您重新输入要购票的数量:".format(z)))
                z=temp.isdigit()
                clear_screen()
                error=0
            else:
                temp=str(input("输入有误，请输入1~100之间的数字！您输入的信息为：{}\n请您重新输入要购票的数量:".format(temp)))
                z=temp.isdigit()
                clear_screen()

name=input("请输入您的姓名:")
while True:

    if num == 0:
        print("抱歉！系统已经没有票可购买！")
        exit()
    print("欢迎{}使用买票系统!\n当前系统剩余票数为{}张".format(name,num))
    temp=str(input("请输入您想要购票的数量："))
    num2=int(try_(temp))

    if num<=0:
        print("票数售罄，无法继续购票！")
    elif num<num2:
        print("票数不足，请输入有效的票数！")
    else:
        print("你购买的数量为{}张!总票价为{}元".format(num2,num2*price))
        temp2=input("是否确认购买该票！YES/NO：")
        clear_screen()
        while True:
            if temp2.upper()=="YES"  or temp2.lower()=="yes" or temp2.upper() == "NO"or temp2.lower() == "no":
                if temp2.upper()=="YES"  or temp2.lower()=="yes":
                    num-=num2
                    clear_screen()
                    break
                else:
                    break
            else:
                temp2=input("是否确认购买该票！\n请输入正确指令！YSE/NO：")
                clear_screen()

        rd=random.randint(1,3)
        rdtemp=random.randint(0,1)
        if rdtemp==0:
            if temp2.upper()=="YES"  or temp2.lower()=="yes":
                cj=input("购票成功！您有一次免票机会，输入任意键进行抽奖。")
                if rd == 1:
                    print("恭喜您中奖了！获得一张票")
                    num-=1
                else:
                    print("很可惜，您没有抽中。")
        else:
             if temp2.upper()=="YES"  or temp2.lower()=="yes":
                 cj=input("购票成功！您有一次抽取红包的机会，输入任意键进行抽奖。")
                 if rd == 1:
                     print("恭喜您中奖了！获得{}元红包。".format(rd))
                 else:
                     print("很可惜，您没有抽中。")


        temp2=input("是否继续购票！YES/NO：")
        while True:
            if temp2.upper()=="YES"  or temp2.lower()=="yes" or temp2.upper() == "NO"or temp2.lower() == "no":
                if temp2.upper()=="YES"  or temp2.lower()=="yes":
                    break
                else:
                    print("欢迎下次使用，再见！")
                    exit()
            else:
                clear_screen()
                temp2=(input("请输入正确指令！\n是否继续购票！YES/NO："))
                clear_screen()
