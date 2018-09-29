video_games = ['刺客信条：奥德赛', '黄金之国伊拉', '漫威蜘蛛侠', '荒野大镖客2']

# TODO: 创建一个文件 ex1.py
# TODO: 写一个函数，用它来清空上面列表中的所有对象，并将列表打印出来
# TODO: 如果打印出来的列表为空，表示成功；如果还有值残留在里面，表示未成功；
# TODO: 你会用到 for loop, .remove(), .copy()


for i in video_games.copy():
    video_games.remove(i)

print(video_games)
