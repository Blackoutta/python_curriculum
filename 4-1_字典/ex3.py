quiz_1 = {
    "问题": "以下哪个方法会返回一个字典中所有的 键值组?",
    "1": ".keys()",
    "2": ".values()",
    "3": ".items()",
    "答案": ".items()"
}

quiz_2 = {
    "问题": "对字典使用.keys(), .values(), .items()会返回什么?",
    "1": "列表",
    "2": "特殊的数据类型 dict_keys, dict_values, dict_items",
    "3": "字符串",
    "答案": "特殊的数据类型 dict_keys, dict_values, dict_items"
}

quiz_3 = {
    "问题": "本课的授课老师的名字是?",
    "1": "彭光彬",
    "2": "张永志",
    "3": "郑殿君",
    "4": "胡阳译",
    "答案": "胡阳译"
}

def quiz_launcher(dict):
    print()
    for key, value in dict.items():
        if key != "答案":
            print("{}: {}".format(key, value))
    user_answer = input("请输入选项的编号并按回车确定: ")
    if dict[user_answer] == dict["答案"]:
        print("回答正确！")
    else:
        print("回答错误！")


quiz_launcher(quiz_1)
quiz_launcher(quiz_2)
quiz_launcher(quiz_3)
