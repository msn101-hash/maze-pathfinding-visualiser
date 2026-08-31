from . import constants


def find_path(
    y: int,
    x: int,
    grid: list[list[str]],
    visited: set[tuple[int, int]]
) -> list[tuple[int, int]]:
    """
    Find a path from the starting position to the exit using DFS.

    Returns a list of coordinates representing the path. Returns an
    empty list if no path exists.
    """

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
                    path = find_path(cell_y, cell_x, grid, visited)
                    if len(path) > 0:
                        return [(y, x)] + path

    return []