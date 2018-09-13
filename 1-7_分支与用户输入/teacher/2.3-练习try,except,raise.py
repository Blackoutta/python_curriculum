# TODO: 创建一个新文件 ex2.py
# TODO: 将下列代码复制进 ex2.py
# TODO: 用 try except raise 来堵住用户在该脚本中可能进行的误操作。

# 学生的总分为 100分
score = int(input("请输入学生的成绩： "))

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
