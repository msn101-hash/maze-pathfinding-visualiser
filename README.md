Toy Robot Maze Solver

Toy Robot Maze Solver is a Python application that generates a random maze using recursive backtracking. Players can solve the maze by manually navigating a robot to the exit.


Features

- Procedurally generated random mazes
- Maze generation using recursive backtracking
- Manual robot navigation
- Random exit generation
- Modular project structure
- Unit tests


# Demo


Installation

# git clone
# cd maze-pathfinding-visualiser
# python -m src.main


Usage

Use the following commands to move the robot:
- north
- east
- south
- west

Use "quit" to end the program


Algorithms
Maze generation

The maze is generated using recursive backtracking. First the algorithm is given the position of a random cell to explore in a grid of cells and walls. It explores the cell by checking for neighbouring cells that have not been visited yet, and randomly picking one to explore. It then removes the wall between itself and the neighbouring cell before exploring it. A cell is considered explored once all neighbouring cells have been visited.

The program continues with this process until it reaches an explored cell. It then backtracks to a cell that hasn't been explored, and continues exploring it and the rest of the grid until every cell has been visited.


Project Structure

src/
    constants.py
    generator.py
    main.py
    maze.py
    rendered.py
    robot.py

tests/
    test_generator.py