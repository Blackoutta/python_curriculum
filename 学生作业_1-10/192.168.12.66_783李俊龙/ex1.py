number = 100
price = 50
name = input('请输入您的姓名: ')
print(f'欢迎购买火车票,{name}！')
while number != 0:
    try:
        print(f'目前剩余票数:{number},票价为{price}/张 ')
        need = int(input('请输入你需要购买的票数,输入0退出!: '))
        if need == 0:
            break
        elif need > number:
            print('票数不足,请重新输入')

        elif need <=  number and need > 0:
            print(f'票数充足,总票价为:{need*price}')

            while True:
                confirm = input(f'订单确认,总票价为:{need*price}，需要购买吗?请输入yes选择购买,输入end选择退出：').lower()
                if confirm == 'yes':
                    number = number - need
                    print(f'{name},购票成功!')
                    break
                elif confirm == 'end':
                    break
                else:
                    print('请输入yes或end！')
        else:
            raise ValueError
    except ValueError:
        print('请输入正确票数!')

if number == 0:
    print('票卖完了，感谢购票!')

print('期待你的下次购票！')
