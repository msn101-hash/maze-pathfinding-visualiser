import constants
import random


MOVES = {
    "north": (-2, 0),
    "south": (2, 0),
    "east": (0, 2),
    "west": (0, -2)
}

def generate_maze(height, width):
    maze = []
    visited = []

    for i in range(height):
        row = []
        for j in range(width):
            if i % 2 == 0:
                row.append(constants.WALL)
            elif j % 2 == 0:
                row.append(constants.WALL)
            else:
                row.append(constants.EMPTY)
        maze.append(row)

    y = height // 2
    x = width // 2
    carve_maze(y, x, maze, visited)
    generate_exits(maze)

    return maze

def generate_exits(maze):
    height = len(maze)
    width = len(maze[0])

    EXITS = {
        "north": (0, random.randint(1, width - 2)),
        "south": (height - 1, random.randint(1, width - 2)),
        "east": (random.randint(1, height - 2), width - 1),
        "west": (random.randint(1, height - 2), 0)
    }

    for exit in EXITS.keys():
        y = EXITS[exit][0]
        x = EXITS[exit][1]
        maze[y][x] = constants.EXIT

def carve_maze(y, x, maze, visited):
    visited.append((y, x))
    unvisited = find_unvisited(y, x, maze, visited)

    while unvisited:
        neighbour = random.choice(unvisited)
        remove_wall((y, x), neighbour, maze)
        new_y, new_x = neighbour
        carve_maze(new_y, new_x, maze, visited)
        unvisited = find_unvisited(y, x, maze, visited)

def find_unvisited(y, x, maze, visited):
    height = len(maze)
    width = len(maze[0])
    unvisited = []

    for dy, dx in MOVES.values():
        new_y, new_x = y, x
        new_y += dy
        new_x += dx

        if 0 <= new_y < height and 0 <= new_x < width:
            if (new_y, new_x) not in visited:
                unvisited.append((new_y, new_x))

    return unvisited

def remove_wall(cell, neighbour, maze):
    wall_y = int((cell[0] + neighbour[0]) / 2)
    wall_x = int((cell[1] + neighbour[1]) / 2)
    maze[wall_y][wall_x] = constants.EMPTY