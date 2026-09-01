import time
from . import constants


def display_maze(grid: list[list[str]], robot_pos: tuple[int, int]) -> None:
    """
    Render the maze and the current position of the robot.
    """

    print()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == robot_pos[0] and j == robot_pos[1]:
                print(constants.ROBOT, end="")
                continue
            print(grid[i][j], end="")
        print()

def solve_maze(
        grid: list[list[str]],
        path: list[tuple[int, int]]
) -> str:
    """
    Render the path the robot takes to solve the maze.
    """

    if path:
        for robot_pos in path:
            time.sleep(.5)
            display_maze(grid, robot_pos)

            if robot_pos == path[-1]:
                return "solved"
    else:
        return "unsolved"