def generate_maze(width, height):
    maze = []
    for i in range(height):
        row = []
        for j in range(width):
            if i % 2 == 0:
                row.append("#")
            elif j % 2 == 0:
                row.append("#")
            else:
                row.append(" ")
        maze.append(row)

    return maze