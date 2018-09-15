while True:
    try:
        number = int(input("请输入一个数字： "))
    except ValueError:
        print("Oh no, please input a number!")
        continue
    is_fizz = number%3 == 0
    is_buzz = number%5 == 0

    print("你输入的数字是 {}...".format(number))

    if is_fizz and is_buzz:
        print("它是 FizzBuzz!")
        continue
    elif is_buzz:
        print("它是 Buzz!")
        continue
    elif is_fizz:
        print("它是 Fizz!")
        continue
    else:
        print("它不是 Fizz 也不是 Buzz!")
        continue
