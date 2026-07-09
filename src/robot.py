import maze


position = (2, 5)
MOVES = {
        "north": (-1, 0),
        "south": (1, 0),
        "east": (0, 1),
        "west": (0, -1),
    }
# direction = "north"
# directions = ["north", "east", "south", "west"]

def move_robot(command):
    global position
    new_y, new_x = position[0], position[1]

    dy, dx = MOVES[command]
    new_x += dx
    new_y += dy

    if maze.is_obstacle(new_y, new_x):
        print("obstacle! try again")
        return

    position = (new_y, new_x)

def get_position():
    return position