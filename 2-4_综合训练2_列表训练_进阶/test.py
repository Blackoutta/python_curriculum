BOARD = [
        [0,0], [1,0], [2,0],
        [0,1], [1,1], [2,1],
        [0,2], [1,2], [2,2]
        ]

print(" _" * 3)
tile = "|{}"

for slot in BOARD:
    x, y = slot
    if x < 2:
        print(tile.format("_"), end = '')
    else:
        print(tile.format("_|"), end = '\n')
