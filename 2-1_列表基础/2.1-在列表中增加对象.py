列表是一种'可变对象'(mutable), 意思就是说我们可以'增加'，'删除'，或'改变'列表中的内容。

现在我们来学习如何在列表中增加内容

# 创建一个空列表 和 一个有内容的列表
projects = []
other_projects = ['静态网页', '动态网页', 'UI设计']

# 在 REPL 中尝试下列命令：

    # 使用 .append来向列表中添加一个对象，这个对象会出现在列表的最后
    projects.append("双十一电商海报")


    # 使用.extend来向列表中添加另一个列表
    projects.extend(other_projects)


    # 使用 + 来将两个列表合并，并生成一个新列表
    all_projeccts = projects + other_projects
