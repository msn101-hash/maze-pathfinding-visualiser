import copy


maze = [
    [1,1,1,1,1],
    [0,0,1,0,1],
    [1,0,0,1,1],
    [1,1,0,0,1],
    [1,1,1,1,1]
]

x = 2
y = 2

while True:
    maze_copy = copy.deepcopy(maze)
    maze_copy[y][x] = 5
    for row in maze_copy:
        print(row)

    prompt = input("move: ").lower()
    if prompt == "north":
        y -= 1
    elif prompt == "south":
        y += 1
    elif prompt == "east":
        x += 1
    elif prompt == "west":
        x -= 1
    elif prompt == "quit":
        break