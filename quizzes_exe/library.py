# quiz_x = {
# 'question': '在这里写下问题',
# 'answer_ls': ('选项1', '选项2', '选项3', '选项4'),
# 'real_answer': '正确答案'
# }

quiz_1 = {
'question': '使用单个字母命名变量是不是一个好习惯',
'answer_ls': ('是，我打字更快了，一口气打5页不费劲', '不是，在程序越来越复杂后，我就很难分清各个变量的作用了'),
'real_answer': '不是，在程序越来越复杂后，我就很难分清各个变量的作用了'
}

quiz_2 = {
'question': '在python中，对于一般的变量，我应该用哪种风格来命名',
'answer_ls': ('snake_case', 'camelCase'),
'real_answer': 'snake_case'
}

quiz_3 = {
'question': '下列哪个是正确的常量书写方式',
'answer_ls': ('MYNAME', 'my_name', 'MyName', 'myName'),
'real_answer': 'MYNAME'
}

quiz_4 = {
'question': '下列哪行代码正确地使用了 f-string 风格的格式化字符串',
'answer_ls': ('print("我的名字是 name, 我今年 age 岁")',
f'print("我的名字是{{name}}, 我今年{{age}}岁")',
f'print(f"我的名字是{{name}}, 我今年{{age}}岁")'),
'real_answer': f'print(f"我的名字是{{name}}, 我今年{{age}}岁")'
}

quiz_5 = {
'question': '下列哪行代码正确地使用了 str.format 风格的格式化字符串',
'answer_ls': ('print("我的名字是 name, 我今年 age 岁".format(name, age))',
f'print("我的名字是{{}}, 我今年{{}} 岁".format(name, age))',
f'print("我的名字是{{name}}, 我今年{{age}} 岁".format(name, age))'),
'real_answer': f'print("我的名字是{{}}, 我今年{{}} 岁".format(name, age))'
}

quiz_6 = {
'question': '变量名称能不能以数字命名',
'answer_ls': ('能', '不能'),
'real_answer': '不能'
}
