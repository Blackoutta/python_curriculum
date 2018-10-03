spam = ['apples', 'bananas', 'tofu', 'cats']

def sentence(list):
    list[-1] = "and " + list[-1]
    output = ', '.join(list)
    return "I like {}!".format(output)


test = sentence(spam)
print(test)
