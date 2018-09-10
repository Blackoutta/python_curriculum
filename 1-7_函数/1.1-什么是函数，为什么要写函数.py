函数(function)就是由一系列语句构成的'迷你脚本'。
当你的脚本中，存在着大量'被重复使用的语句'时，你就可以将'重复的语句'做成函数来'反复调用'。

请看这个例子：
假设老师每天都会随机让一名同学去帮忙买午饭，如果我们把这个做成一个程序的话...

# 设置固定的变量
left = "左边"
right = "右边"


#星期一
student_name = ""
lunch = "红烧肉套饭"
restaurant = "老麻抄手"


print("{}，帮我去{}买一份{}!".format(student_name, lunch, restaurant))
print("从学校后门出去，在街道{}可以找到".format(right))

#星期二
student_name = ""
lunch = "番茄烫饭"
restaurant = "莱得快"
print("{}，帮我去{}买一份{}!".format(student_name, lunch, restaurant))
print("从学校后门出去，在街道{}可以找到".format(left))

#星期三
student_name = ""
lunch = "三鲜米线"
restaurant = "嘿六米线"
print("{}，帮我去{}买一份{}!".format(student_name, lunch, restaurant))
print("从学校后门出去，在街道{}可以找到".format(right))

# 以此类推......

这样的代码太冗长了，而且重复的地方太多。而将他们做成函数便可以大大底简化代码。
在改造这段代码之前，我们先来看看一些基础操作。
