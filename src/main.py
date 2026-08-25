import time
from . import generator
from . import maze
from . import robot
from . import renderer


def get_player_move() -> str:
    """
    Get the input of a player and check if it is a valid command.
    """

    commands = {"north", "south", "east", "west", "solve", "quit"}
    while True:
        command = input("Enter a command: ").lower()
        if command not in commands:
            print("Invalid command! Try again")
            continue
        return command

def main() -> None:
    """
    Run the program.
    """

    # Make sure that when height and width are divided by 2 and rounded up,
    # the result is even
    height = 11
    width = 23
    grid = generator.generate_maze(height, width)
    y, x = robot.set_position(height, width)

    renderer.display_maze(grid, (y, x))
    
    while True:
        command = get_player_move()
        if command == "quit":
            return
        
        elif command == "solve":
            path = robot.solve_maze(y, x, grid, set())
            for robot_pos in path:
                time.sleep(.5)
                renderer.display_maze(grid, robot_pos)

                if robot_pos == path[-1]:
                    print("Maze solved!")

            y, x = path[-1]
            continue
        
        position, status = robot.move_robot(grid, command, (y, x))
        y, x = position

        if status == "obstacle":
            print("Obstacle! Try again")
            continue
        elif maze.is_exit(grid, y, x):
            print("Congratulations! You solved the maze")
            return

        renderer.display_maze(grid, (y, x))
        
if __name__ == "__main__":
    main()