import os

def clear_screen():
    os.system('cls')

my_name = input("请输入你的姓名： ")
print("欢迎{}来到买票网站！".format(my_name))
wz_ps = 20
p_j = 338
while True:
    try:
        print("本网站还剩余票数为{}张！如有需要请尽快购买。当前票价为{}元一张".format(wz_ps,p_j))
        my_sl = int(input("请输入购买数量："))
    except ValueError:
        print("请输入一个正整数！")
        continue
    if my_sl > wz_ps:
        print("你购买的数量过多，请重新输入！")
        continue
    elif my_sl <= 0:
        print("请输入一个正整数！")
    else:
        print("您购买的数量为{}张，总价为{}元".format(my_sl,p_j * my_sl))
        my_cf = input("请输入1按回车键确认购买或输入任意键按回车离开：")
        if my_cf == "1":
            print("购买成功！")
            wz_ps - my_sl
            break
        else:
            continue
