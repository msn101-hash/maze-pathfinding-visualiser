class Robot:
    MOVES = {
            "north": (-1, 0),
            "south": (1, 0),
            "east": (0, 1),
            "west": (0, -1),
        }

    # directions = ["north", "east", "south", "west"]

    def __init__(self, position):
        self.position = position

    def move_robot(self, command, maze):
        global position
        new_y, new_x = self.position[0], self.position[1]

        dy, dx = self.MOVES[command]
        new_y += dy
        new_x += dx

        if maze.is_obstacle(new_y, new_x):
            print("obstacle! try again")
            return

        self.position = (new_y, new_x)

    def get_position(self):
        return self.position