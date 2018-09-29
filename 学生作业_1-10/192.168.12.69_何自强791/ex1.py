number = 100
price = 399
name = input('请输入您的姓名: ')
print(f'欢迎购买火车票,{name}！')
while True:
    try:
        print(f'目前剩余票数:{number},票价为{price}/张 ')
        need = int(input('请输入你需要购买的票数: '))
        if need > number:
            print('票数不足,请重新输入')

        elif need <=  number and need >= 0:
            print(f'票数充足,总票价为:{need*price}')

            while True:
                confirm = input(f'订单确认,总票价为:{need*price}，需要购买吗?请输入1选择购买,输入0选择退出：')
                if confirm == '1':
                    number = number - need
                    print(f'{name},购票成功!')
                    break
                elif confirm == '0':
                    break
        else:
            raise ValueError
    except ValueError:
        print('请输入正确票数!')
