import constants
import random


visited = []
height = 11
width = 23

EXITS = {
    "north": (0, random.randint(1, width - 2)),
    "south": (height - 1, random.randint(1, width - 2)),
    "east": (random.randint(1, height - 2), width - 1),
    "west": (random.randint(1, height - 2), 0)
}

MOVES = {
    "north": (-2, 0),
    "south": (2, 0),
    "east": (0, 2),
    "west": (0, -2)
}

def generate_grid():
    grid = []
    for i in range(height):
        row = []
        for j in range(width):
            if i % 2 == 0:
                row.append(constants.WALL)
            elif j % 2 == 0:
                row.append(constants.WALL)
            else:
                row.append(constants.EMPTY)
        grid.append(row)

    generate_exits(grid)

    return grid

def generate_exits(grid):
    for exit in EXITS.keys():
        y = EXITS[exit][0]
        x = EXITS[exit][1]
        grid[y][x] = constants.EXIT

def generate_maze(y, x, grid):
    while True:
        visited.append((y, x))
        unvisited = find_unvisited(y, x)
        if len(unvisited) == 0:
            return grid
        
        neighbour = random.choice(unvisited)
        remove_wall((y, x), neighbour, grid)
        new_y, new_x = neighbour
        generate_maze(new_y, new_x, grid)

def find_unvisited(y, x):
    unvisited = []
    for move in MOVES.keys():
        new_y, new_x = y, x
        dy, dx = MOVES[move]
        new_y += dy
        new_x += dx

        if new_y in range(height) and new_x in range(width):
            if (new_y, new_x) not in visited:
                unvisited.append((new_y, new_x))

    return unvisited

def remove_wall(cell, neighbour, grid):
    if cell[0] == neighbour[0]:
        if cell[1] > neighbour[1]:
            grid[cell[0]][cell[1]-1] = constants.EMPTY
        else:
            grid[cell[0]][neighbour[1]-1] = constants.EMPTY
    elif cell[1] == neighbour[1]:
        if cell[0] > neighbour[0]:
            grid[cell[0]-1][cell[1]] = constants.EMPTY
        else:
            grid[neighbour[0]-1][cell[1]] = constants.EMPTY