from . import generator
from . import maze
from . import robot
from . import renderer
from . import pathfinding


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
            path = pathfinding.find_path(y, x, grid, set())
            status = renderer.solve_maze(grid, path)

            if status == "solved":
                print("Maze solved!")
                return
            elif status == "unsolved":
                print("Can't solve maze!")
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