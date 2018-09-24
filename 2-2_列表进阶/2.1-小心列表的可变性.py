列表也是'可变对象'(mutable)，意思是我们可以自由自在地'改变'列表内的内容
但是同时，这也会引发一个问题：在迭代列表时，我们可能会遇到一些意想不到的情况。

例子：
    video_games = ['刺客信条：奥德赛', '黄金之国伊拉', '漫威蜘蛛侠', '荒野大镖客2']

    # 我们写一个函数，它会在一个列表中推荐一个随机游戏，然后打印出剩下的游戏
    def recommendation(list):
        list_len = len(video_games)
        random_number = random.randint(0, list_len - 1)
        print("\n====> 今日推荐游戏为：{} <====".format(list.pop(random_number)))
        print("\n近期热点：")
        for game in list:
            print(" * " + game)

    recommendation(video_games)

# 用 python -i 运行这个脚本，然后反复调用 recommendation(video_games)，看看会发生什么?

--------------------------------------------------------------------------------
# 没错，随着每次pop()，列表中的值会越来越少。在多次调用该函数后，列表被清空，从而导致程序错误。
# 解决方法很简单，那就是用 .copy()这个方法

    def recommendation(list):
        list_copy = list.copy()  # 这里我们将传递进来的列表用 .copy()复制出一份镜像，并存储在新的变量中
        list_len = len(video_games)
        random_number = random.randint(0, list_len - 1)
        print("\n====> 今日推荐游戏为：{} <====".format(list_copy.pop(random_number)))  # 这里我们在pop()的时候是对着列表的镜像进行pop()，故原列表不会受到任何影响
        print("\n近期热点：")
        for game in list_copy:  # 这里我们将迭代的列表变成列表的镜像
            print(" * " + game)

    recommendation(video_games)

# 用 python -i 运行这个脚本，然后反复调用 recommendation(video_games)，看看问题是不是解决了？
