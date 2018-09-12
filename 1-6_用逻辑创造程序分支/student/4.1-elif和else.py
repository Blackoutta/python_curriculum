概念:
    刚才我们用 if 创造了一个单分支，程序要么会运行这个分支，要么就跳过它。
    现在我们用 elif 和 else 创建更复杂的分支。
    elif 是 else if 的简写，如果 if 的条件没有被满足，则脚本中的下一个 elif 判断会被触发
    else 你可以理解成否则，else 代码块中的代码会在上面所有 if 和 elif 的条件都不为 True 的情况下触发。

例子：

if False:
    print("这行会被跳过，程序会进入下一个elif")
elif False:
    print("因为是False，这行也会被跳过，进入下一个elif")
elif True:
    print("这个elif是True，所以你可以看到本行被打印出来")




if False:
    print("这行会被跳过，程序会进入下一个elif")
elif False:
    print("因为是False，这行也会被跳过，进入下一个elif")
elif False:
    print("因为是False，这行也会被跳过")
else:
    print("上面已经没有任何elif了，并且所有的elif判定都是False，故本else中的语句会被执行。")
