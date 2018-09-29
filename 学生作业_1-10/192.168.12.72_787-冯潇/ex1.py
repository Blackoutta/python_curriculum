import os

def clear_screen():  # 这个函数一旦被调用会对控制台进行清屏
    os.system('cls')


number = 100
price = 399
name = input('请输入您的姓名: ')
print(f'欢迎购买火车票,{name}！')
while number != 0:
    try:
        clear_screen()
        print(f'目前剩余票数:{number},票价为{price}/张 ')
        need = int(input('请输入你需要购买的票数,或者输入-1退出购票: '))
        if need == -1:
            break
        elif need > number:
            print('票数不足,请重新输入')

        elif need <=  number and need > 0:
            print(f'票数充足,总票价为:{need*price}')

            while True:
                clear_screen()
                confirm = input(f'订单确认,总票价为:{need*price}，需要购买吗?请输入confirm选择购买,输入exit选择退出：').lower()
                if confirm == 'confirm':
                    number = number - need
                    print(f'{name},购票成功!')
                    break
                elif confirm == 'exit':
                    break
                else:
                    clear_screen()
                    print('请输入confirm或exit！')
        else:
            raise ValueError
    except ValueError:
        print('请输入正确票数!')
if number == 0:
    print('票已售罄，感谢购票!')

print('欢迎下次光临!')
