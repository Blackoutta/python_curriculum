graduation_project_students = [
    '唐宇',
    '王馨',
    '凡安顺',
    '向港',
    '袁悦',
    '李青松',
    '谭定坤',
    '黎永明',
    '龙燕',
    '谭旭滟',
    '邹雨辰'
    ]

graduation_project_students.append('刘江')
other_students = ['王杰', '梁桥']
graduation_project_students.extend(other_students)

print("今天我请以下同学吃火锅: {}, 共计{}位同学。".format(graduation_project_students, len(graduation_project_students)))
