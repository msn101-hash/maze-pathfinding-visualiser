import constants


class Maze:
    def __init__(self, height, width, maze):
        self.height = height
        self.width = width
        self.maze = maze

    def is_obstacle(self, y, x):
        return self.maze[y][x] == constants.WALL
        
    def is_exit(self, y, x):
        return self.maze[y][x] == constants.EXIT

    def get_maze(self):
        return self.maze