# TODO: 创建一个文件 ex1.py
# TODO: 抄写下方代码
# TODO: 该代码是教材 习题6 的练习题 的翻译版本
# TODO: 完成  习题6 的巩固练习

types_of_people = 10
first_sentence = f"世界上只有 {types_of_people} 种人."

binary = "二进制"
do_not = "不懂"
second_sentence = f"懂{binary}的人和{do_not}{binary}的人。 "

print(first_sentence)
print(second_sentence)

print(f"刚才我说了：{first_sentence}")
print(f"刚才我还说了：'{second_sentence}'")

hilarious = False
joke_evaluation = "这个笑话好笑吗？{}"

print(joke_evaluation.format(hilarious))

left = "我来组成字符串的左边"
right = "我来组成字符串的右边"

print(left + right)
