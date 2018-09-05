# TODO: 创建一个文件 ex4.py
# TODO: 抄写下方代码
# TODO: 该代码是教材 习题8 的练习题 的翻译版本
# TODO: 完成 习题8 的巩固练习

formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format('one','two','three','four'))
print(formatter.format('True','False','False','True'))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "尝试",
    "自己",
    "写点东西",
    "最好是一个关于恐惧的诗或者歌"
))
