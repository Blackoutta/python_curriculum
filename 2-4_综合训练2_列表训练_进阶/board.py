import os
# CELLS = [(0,0), (1,0),(2,0),(3,0),(4,0),
#          (0,1), (1,1),(2,1),(3,1),(4,1),
#          (0,2), (1,2),(2,2),(3,2),(4,2),
#          (0,3), (1,3),(2,3),(3,3),(4,3),
#          (0,4), (1,4),(2,4),(3,4),(4,4)]

def clear_screen():
    os.system('cls')

def create_map(column, row):
    # create list
    CELLS = []
    y = 0
    while y < row:
        for i in range(column):
            list = [i, y]
            CELLS.append(list)
        y += 1

    # draw map
    print(" _" * column)
    tile = "|{}"
    for cell in CELLS:
        x, y = cell
        if x < column - 1:
            print(tile.format("_"), end = '')
        else:
            print(tile.format("_|"), end = '\n')

while True:
    clear_screen()
    try:
        column = int(input("请输入地图的 *列数*: "))
        if column < 1:
            raise ValueError
        row = int(input("请输入地图的 *行数*: "))
        if column < 1:
            raise ValueError
    except ValueError:
        clear_screen()
        input("请确保你输入的是整数，且不小于1！")
        continue
    else:
        break

create_map(column, row)
