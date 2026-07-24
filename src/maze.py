import constants


def is_obstacle(
    maze: list[list[str]],
    y: int,
    x: int
) -> bool:
    """
    Return True if the specified position is a wall.
    """
    
    return maze[y][x] == constants.WALL
    
def is_exit(
    maze: list[list[str]],
    y: int,
    x: int
) -> bool:
    """
    Return True if the specified position is an exit.
    """
    
    return maze[y][x] == constants.EXIT