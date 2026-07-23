import constants


def is_obstacle(maze, y, x):
    return maze[y][x] == constants.WALL
    
def is_exit(maze, y, x):
    return maze[y][x] == constants.EXIT