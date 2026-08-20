from . import constants


def is_obstacle(
    grid: list[list[str]],
    y: int,
    x: int
) -> bool:
    """
    Return True if the specified position is a wall.
    """
    
    return grid[y][x] == constants.WALL
    
def is_exit(
    grid: list[list[str]],
    y: int,
    x: int
) -> bool:
    """
    Return True if the specified position is an exit.
    """
    
    return grid[y][x] == constants.EXIT