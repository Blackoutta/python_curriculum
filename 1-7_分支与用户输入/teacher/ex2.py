try:
    score = int(input("请输入学生的成绩： "))
    if score < 0 or score > 100:
        raise ValueError
except ValueError:
    print("\n出错啦。学生成绩应为 1-100 之间的整数。")
else:
    if 60 <= score <= 69:
        print("你的成绩是：及格")
    elif 70 <= score <= 79:
        print("你的成绩是：还行")
    elif 80 <= score <= 89:
        print("你的成绩是：良好")
    elif 90 <= score <= 99:
        print("你的成绩是：陈独秀")
    elif score == 100:
        print("你的成绩是：天秀")
    else:
        print("你怕是不及格。")
