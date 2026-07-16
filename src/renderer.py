import constants


def display_maze(maze, robot_pos):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if i == robot_pos[0] and j == robot_pos[1]:
                print(constants.ROBOT, end="")
                continue
            print(maze[i][j], end="")
        print()