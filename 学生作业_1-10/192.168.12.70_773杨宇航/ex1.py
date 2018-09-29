number = 100
price = 488
name = input('请输入您的姓名: ')
print(f'欢迎购买火车票,{name}!')
while True:
    try:
        print(f'目前剩余票数:{number},票价为{price}/张 ')
        need = int(input('请输入你需要够买的票数: '))
        if need > number:
            print('票数不足或售罄,请重新购买')
            continue
        elif need < number and need >= 0:
            print(f'票数充足,总票价为:{need*price}')

            while True:
                confirm = input(f'订单确认,总票价为:{need*price}，需要购买吗?请输入confirm购买,输入exit退出：')
                if confirm == 'confirm':
                    number = number - need
                    print(f'{name},购票成功!')
                    break
                elif confirm == 'exit':
                    break
                else:
                    print('请输入confirm或exit!')
                    continue
        else:
        raise ValueError
except ValueError:
        print('请输入正确票数!')
