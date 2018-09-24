列表也是'可变对象'(mutable)，意思是我们可以自由自在地'改变'列表内的内容
但是同时，这也会引发一个问题：在迭代列表时，我们可能会遇到一些意想不到的情况。

例子：
    # 我们写一个函数，它可以在列表中随机推荐一款游戏
    import random
    video_games = ['漫威蜘蛛侠', '刺客信条:奥德赛', '黄金之国伊拉']

    def recommendation():
        list_len = len(video_games)
        random_number = random.randint(0, list_len)
        print("今日推荐游戏为：{}".format(video_games.pop(random_number)))
