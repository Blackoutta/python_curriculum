新词：.join()

使用 .join()可以将一个列表中的'所有对象'合成为一个完整的'字符串'
.join()的使用格式比较'特殊'，请大家看仔细：
    '合并的依据(字符串)'.join(这里放入列表)

例子：
    video_games = ['刺客信条：奥德赛', '黄金之国伊拉', '漫威蜘蛛侠', '荒野大镖客2']

    favorite_games = '，'.join(video_games)  # 用 , 来将列表合并起来
    print("这个月我要买的游戏有：{}".format(favorite_games))
