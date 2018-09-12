# 练习一： 无传递参数的函数
# TODO: 定义一个函数，名称为 poem
# TODO: 在函数中，分行打印一首诗。
# TODO: 在脚本中调用这个函数
# TODO: 结果应该类似如下：
#       输入：poem()
#       输出：窗前明月光，
#            疑似地上霜.
#            举头望明月,
#            低头思故乡.


# 练习二： 有传递参数的函数
# TODO: 定义一个函数，名称为 who_wrote_what
# TODO: 给这个函数传递两个参数： 作品， 作者 (英文参数名自定)
# TODO: 使用传递的参数，在函数中打印哪个作者写了什么作品。
# TODO: 调用函数的同时传递两个参数，结果应该类似这样：
#       输入：who_wrote_what("李白", "静夜思")
#       输出："李白是静夜思的作者"

#       输入：who_wrote_what("小畑健", "死亡笔记")
#       输出："小畑健是死亡笔记的作者"

#       输入：who_wrote_what("马伯庸", "长安十二时辰")
#       输出："马伯庸是长安十二时辰的作者"


# 练习三： *args 的妙用 I
# TODO: 调用 who_wrote_what 函数，在调用时故意多传递一个额外的参数，看看会发生什么
# TODO: 改造 who_wrote_what 函数，增加一个传递参数: *args
# TODO: 调用 who_wrote_what 函数，在调用时故意多传递一个额外的参数，看看会发生什么

# 练习四： *args 的妙用 II
# TODO: 还是刚才的 who_wrote_what 函数
# TODO: 在刚才的打印下面新增一条打印，这里打印出作者的其他作品，数量不限
# TODO: 调用函数，照常传递进作者和一个作品，但是这次在后面追加数个其他作品
# TODO: 结果应该类似如下：
#       输入： who_wrote_what("渡边信一郎", "星际牛仔", "混沌武士", “攻壳机动队”)
#       输出： 渡边信一郎是攻壳机动队的作者
#             TA的其他作品有：('混沌武士', '攻壳机动队')
