import maze as Maze


MOVES = {
        "north": (-1, 0),
        "south": (1, 0),
        "east": (0, 1),
        "west": (0, -1),
    }
def set_position(height, width):
    y = height // 2
    x = width // 2

    return y, x

def move_robot(maze, command, position):
    new_y, new_x = position[0], position[1]

    dy, dx = MOVES[command]
    new_y += dy
    new_x += dx

    if Maze.is_obstacle(maze, new_y, new_x):
        print("obstacle! try again")
        return position

    position = (new_y, new_x)
    return position