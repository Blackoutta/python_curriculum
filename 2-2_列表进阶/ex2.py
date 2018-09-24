import random

persona = ['任性的', '傲娇的', '勇敢的', '腹黑的', '跋扈的', '粉切黑的', '病娇的']
kanji = '玛德哈尔桑胡索毕牛顿艾因斯坦哥白尼华兹拉夏洛克'



def random_name():
    kanji_list = list(kanji)
    name = []
    for i in range(random.randint(2, 4)):
        letter = kanji_list.copy().pop(random.randint(0, len(kanji_list) - 1))
        name.append(letter)
    output = ''.join(name)
    return output

def random_persona():
    return persona.copy().pop(random.randint(0, len(persona) - 1))

print('你的随机名字是：{}{}'.format(random_persona(),random_name()))
