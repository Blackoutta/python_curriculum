number = 100
price = 488
name = input('��������������: ')
print(f'��ӭ�����Ʊ,{name}!')
while True:
    try:
        print(f'Ŀǰʣ��Ʊ��:{number},Ʊ��Ϊ{price}/�� ')
        need = int(input('����������Ҫ�����Ʊ��: '))
        if need > number:
            print('Ʊ�����������,�����¹���')
            continue
        elif need < number and need >= 0:
            print(f'Ʊ������,��Ʊ��Ϊ:{need*price}')

            while True:
                confirm = input(f'����ȷ��,��Ʊ��Ϊ:{need*price}����Ҫ������?������confirm����,����exit�˳���')
                if confirm == 'confirm':
                    number = number - need
                    print(f'{name},��Ʊ�ɹ�!')
                    break
                elif confirm == 'exit':
                    break
                else:
                    print('������confirm��exit!')
                    continue
        else:
        raise ValueError
except ValueError:
        print('��������ȷƱ��!')
