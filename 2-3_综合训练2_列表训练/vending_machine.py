import random
import os

sodas = ["百事可乐", "可口可乐", "美年达"]
chips = ["乐事原味", "妙脆角"]
candy = ["大白兔", "花生酥", "软糖"]

def clear_screen():
    os.system('cls')

def random_item(list):
    output = random.randint(0, len(list) - 1)
    return output


while True:
    clear_screen()
    choice = input("你需要 苏打,  薯片, 还是 糖果?  ").lower()
    try:
        if choice == "苏打":
            snack = sodas.pop(random_item(sodas))
        elif choice == "薯片":
            snack = chips.pop(random_item(chips))
        elif choice == "糖果":
            snack = candy.pop(random_item(candy))
        else:
            input("对不起，我没有听懂你的请求。")
            clear_screen()
            continue
    except IndexError:
        input("{} 已经全部卖完啦！".format(choice))
        clear_screen()
        continue
    except ValueError:
        input("{} 已经全部卖完啦！".format(choice))
        clear_screen()
        continue
    input("购买成功！你购买了 {}: {}!".format(choice, snack))
