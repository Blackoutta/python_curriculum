import random
video_games = ['漫威蜘蛛侠', '刺客信条:奥德赛', '黄金之国伊拉']

def recommendation(list):
    list_len = len(video_games)
    random_number = random.randint(0, list_len - 1)
    print("今日推荐游戏为：{}".format(list.pop(random_number)))

recommendation(video_games)
