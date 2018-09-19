#                                 I
# TODO: 使用 del 和 索引 删除以下列表中的 数字, 并运行脚本查看效果
string_list = ['1', 2, '3', 4]
# TODO: 你的代码写在下一行：
#-------------------------------------------------------------------------------
del string_list[1]
del string_list[2]


#-------------------------------------------------------------------------------
print(string_list)



#                                 II
# TODO: 使用 .remove 删除以下列表中的 字符串, 并运行脚本查看效果
number_list = [1, '贰', 3, 4, '伍', '陆', 7, '捌', 9, '拾']

# TODO: 你的代码写在下一行：
#-------------------------------------------------------------------------------
number_list.remove('贰')
number_list.remove('伍')
number_list.remove('陆')
number_list.remove('捌')
number_list.remove('拾')


#-------------------------------------------------------------------------------
print(number_list)




#                                 III
learning_list = ['列表', '添加', '索引', '.remove', 'del', '.pop()']

# TODO: 用 .pop()，结合上方老师给出的列表，来完成下面的 '完形填空'

print(
    """
    1. 今天我们学习了{}。
    2. 通过.append()和.extend()，我们可以向列表中{}对象。
    3. 通过{}，我们可以查询或修改列表中特定位置的对象。也可以在特定对象的前方插入新的对象。
    4. 通过{}, 我们可以删除列表中特定位置上的对象。
    5. 通过{}, 我们可以根据列表中对象的值来删除该对象。
    6. 通过{}, 我们可以删除列表中特定位置上的对象，并且同时返回该对象的值。
    """.format(
    # 在这个format()中，使用 learning_list.pop(#索引自己想) 来完成这个打印
    # learning_list.pop(0),
    # learning_list.pop(0),
    # learning_list.pop(0),
    # learning_list.pop(1),
    # learning_list.pop(0),
    # learning_list.pop(),
    learning_list.copy().pop(0),
    learning_list.copy().pop(1),
    learning_list.copy().pop(2),
    learning_list.copy().pop(4),
    learning_list.copy().pop(3),
    learning_list.copy().pop()
    ))
