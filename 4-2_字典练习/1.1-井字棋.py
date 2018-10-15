import os

board = {'TOP-L':' ', 'TOP-M':' ', 'TOP-R':' ',
         'MID-L':' ', 'MID-M':' ', 'MID-R':' ',
         'LOW-L':' ', 'LOW-M':' ', 'LOW-R':' ',
}

def clear_screen():
    os.system('cls')

def print_board(board):
    print(f"{board['TOP-L']}|{board['TOP-M']}|{board['TOP-R']}")
    print("-+-+-")
    print(f"{board['MID-L']}|{board['MID-M']}|{board['MID-R']}")
    print("-+-+-")
    print(f"{board['LOW-L']}|{board['LOW-M']}|{board['LOW-R']}")


clear_screen()
turn = 'X'
for i in range(9):
    print_board(board)
    print("现在是玩家 {} 的回合。您想将棋子放置在哪一格？".format(turn))
    move = input(">> ")
    board[move.upper()] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    clear_screen()

# TODO: 创建文件 ex1.py, 抄写以上代码
# TODO: 上面的代码能做出一个不完整的井字棋游戏，它暂时没无法判断玩家之间的胜负
# TODO: 你能想一个办法来判断胜负吗？
