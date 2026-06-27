import copy


maze = [
    ["#","#","#","#","#","#","#","#","#","#"],
    ["E"," "," ","#","#"," "," "," "," ","#"],
    ["#","#"," ","#"," "," ","#","#"," ","#"],
    ["#"," "," "," "," ","#","#"," "," ","#"],
    ["#","#","#","#","#","#","#","#","#","#"]
]

x = 5
y = 2

def is_obstacle(x, y):
    if maze[y][x] == "#":
        return True
    
def is_exit(x, y):
    if maze[y][x] == "E":
        return True    

while True:
    # Making a copy of the maze so that it's not permanently changed when updating
    # the position of the robot
    maze_copy = copy.deepcopy(maze)
    maze_copy[y][x] = "R"
    for row in maze_copy:
        for cell in row:
            print(cell, end="")
        print()

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
        continue
    elif is_exit(new_x, new_y):
        print("Congratulations! You solved the maze")
        break

    x = new_x
    y = new_y