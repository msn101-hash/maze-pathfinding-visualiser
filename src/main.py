import generator
import maze
import robot
import renderer


def get_player_move():
    commands = {"north", "south", "east", "west", "quit"}
    while True:
        command = input("Enter a command: ").lower()
        if command not in commands:
            print("Invalid command! Try again")
            continue
        return command

def main():
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