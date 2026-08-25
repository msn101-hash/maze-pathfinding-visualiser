from . import maze
from . import constants


MOVES = {
        "north": (-1, 0),
        "south": (1, 0),
        "east": (0, 1),
        "west": (0, -1),
    }
def set_position(height: int, width: int) -> tuple[int, int]:
    """
    Set the position of the robot to be at the centre of the maze.
    """
    
    y = height // 2
    x = width // 2

    return y, x

def move_robot(
    grid: list[list[str]],
    command: str,
    position: tuple[int, int]
) -> tuple[int, int]:
    """
    Move the robot from one position to the next.
    """

    status = "normal"
    new_y, new_x = position[0], position[1]

    dy, dx = MOVES[command]
    new_y += dy
    new_x += dx

    if maze.is_obstacle(grid, new_y, new_x):
        status = "obstacle"
        return position, status

    position = (new_y, new_x)
    return position, status

def solve_maze(
    y: int,
    x: int,
    grid: list[list[str]],
    visited: set[tuple[int, int]]
) -> list:

    MOVES = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited.add((y, x))
    
    for cell_dy, cell_dx in MOVES:
        cell_y = y + cell_dy
        cell_x = x + cell_dx

        if 0 <= cell_y < len(grid) and 0 <= cell_x < len(grid[0]):
            if grid[cell_y][cell_x] == constants.EXIT:
                return [(y, x), (cell_y, cell_x)]
            
            elif grid[cell_y][cell_x] == constants.EMPTY:
                if (cell_y, cell_x) not in visited:
                    path = solve_maze(cell_y, cell_x, grid, visited)
                    if len(path) > 0:
                        return [(y, x)] + path

    return []