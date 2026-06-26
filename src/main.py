import copy


maze = [
    [1,1,1,1,1],
    [9,0,1,0,1],
    [1,0,0,1,1],
    [1,1,0,0,1],
    [1,1,1,1,1]
]

x = 2
y = 2

def is_obstacle(x, y):
    if maze[y][x] == 1:
        return True
    
def is_exit(x, y):
    if maze[y][x] == 9:
        return True    

while True:
    maze_copy = copy.deepcopy(maze)
    maze_copy[y][x] = 5
    for row in maze_copy:
        print(row)

    new_x = x
    new_y = y

    prompt = input("move: ").lower()
    if prompt == "north":
        new_y -= 1
    elif prompt == "south":
        new_y += 1
    elif prompt == "east":
        new_x += 1
    elif prompt == "west":
        new_x -= 1
    elif prompt == "quit":
        break

    if is_obstacle(new_x, new_y):
        print("obstacle! try again")
    elif is_exit(new_x, new_y):
        x = new_x
        y = new_y
        print("Congratulations! You solved the maze")
    else:
        x = new_x
        y = new_y