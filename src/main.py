import maze
import robot
import renderer

def get_player_move():
    commands = ["north", "south", "east", "west", "quit"]
    while True:
        command = input("Enter a command: ").lower()
        if command not in commands:
            print("Invalid command! Try again")
            continue
        return command

def main():
    while True:
        renderer.display_maze(maze.get_maze(), robot.get_position())
        command = get_player_move()
        if command == "quit":
            return
        
        robot.move_robot(command)
        y, x = robot.get_position()
        if maze.is_exit(y, x):
            print("Congratulations! You solved the maze")
            return
        

if __name__ == "__main__":
    main()