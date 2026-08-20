from . import constants


def display_maze(grid: list[list[str]], robot_pos: tuple[int, int]) -> None:
    """
    Render the maze and the current position of the robot.
    """
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == robot_pos[0] and j == robot_pos[1]:
                print(constants.ROBOT, end="")
                continue
            print(grid[i][j], end="")
        print()