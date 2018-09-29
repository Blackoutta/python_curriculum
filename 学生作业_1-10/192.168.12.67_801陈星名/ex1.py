import os
def clear_screen():
    os.system('cls')
num=100
name=input("请输入你的名字")
print("欢迎,{}".format(name))

while True:
    print("剩余的票数：{}".format(num))
    try:
        aa= int(input("请输入你要购买的票数:"))
    except ValueError:
        clear_screen()
        print("请输入正确的票数！")
        continue

    if  aa<num:
        clear_screen()
        bb=aa*20
        print("你要购买的票数为{},价格为{}".format(aa,bb))
        print("确认yes订单:{}，{}".format(aa,bb))
        cc=input("")
        if cc=="yes":
            print("购买成功,继续购买请输入continue,输入其他任意退出")
            dd=input("")
            if dd=="continue":
                num=num-aa
                clear_screen()
                continue
            else:
                print("拜拜")
                break
        else:
            clear_screen()
            print("请重新选票")
            continue


    else:
        clear_screen()
        print("票数不足,无法继续买票")
        continue
