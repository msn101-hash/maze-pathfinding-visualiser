from . import maze


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
    
    new_y, new_x = position[0], position[1]

    dy, dx = MOVES[command]
    new_y += dy
    new_x += dx

    if maze.is_obstacle(grid, new_y, new_x):
        print("obstacle! try again")
        return position

    position = (new_y, new_x)
    return position