import copy


maze = [
    ["#","#","#","#","#","#","#","#","#","#"],
    ["E"," "," ","#","#"," "," "," "," ","#"],
    ["#","#"," ","#"," "," ","#","#"," ","#"],
    ["#"," "," "," "," ","#","#"," "," ","#"],
    ["#","#","#","#","#","#","#","#","#","#"]
]

def is_obstacle(x, y):
    return maze[y][x] == "#"
    
def is_exit(x, y):
    return maze[y][x] == "E"

def get_player_move():
    commands = ["north", "south", "east", "west", "quit"]
    while True:
        command = input("Enter a command: ").lower()
        if command not in commands:
            print("Invalid command! Try again")
            continue
        return command
    
def move_robot(x, y, command):
    new_x, new_y = x, y

    MOVES = {
        "north": (0, -1),
        "south": (0, 1),
        "east": (1, 0),
        "west": (-1, 0),
    }

    dx, dy = MOVES[command]
    new_x += dx
    new_y += dy

    if is_obstacle(new_x, new_y):
        print("obstacle! try again")
        return x, y

    return new_x, new_y

def display_maze(x, y):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if i == y and j == x:
                print("R", end="")
                continue
            print(maze[i][j], end="")
        print()

def main():
    x, y = 5, 2
    while True:
        display_maze(x, y)
        command = get_player_move()
        if command == "quit":
            return
        
        x, y = move_robot(x, y, command)
        if is_exit(x, y):
            print("Congratulations! You solved the maze")
            return
        

if __name__ == "__main__":
    main()