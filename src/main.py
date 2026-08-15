from . import generator
from . import maze
from . import robot
from . import renderer


def get_player_move() -> str:
    """
    Get the input of a player and check if it is a valid command.
    """

    commands = {"north", "south", "east", "west", "quit"}
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

    height = 11
    width = 23
    grid = generator.generate_maze(height, width)
    y, x = robot.set_position(height, width)
    
    while True:
        renderer.display_maze(grid, (y, x))
        command = get_player_move()
        if command == "quit":
            return
        
        y, x = robot.move_robot(grid, command, (y, x))
        if maze.is_exit(grid, y, x):
            print("Congratulations! You solved the maze")
            return
        
if __name__ == "__main__":
    main()