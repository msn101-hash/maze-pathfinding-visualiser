# Toy Robot Maze Solver

Toy Robot Maze Solver is a Python application that procedurally generates random mazes using recursive backtracking. Players can navigate a robot through the maze using directional commands and attempt to reach the exit.

## Features

- Procedurally generated random mazes
- Maze generation using recursive backtracking
- Manual robot navigation
- Randomly generated exits
- Modular project structure
- Unit tests for maze generation and functionality

## Demo

Coming soon.

## Installation

Clone the repository:

```bash
git clone https://github.com/msn101-hash/maze-pathfinding-visualiser.git
cd maze-pathfinding-visualiser
```

Run the application:

```bash
python -m src.main
```

## Usage

Use the following commands to move the robot:
- `north`
- `east`
- `south`
- `west`

Use `quit` to end the program

## Algorithms

### Maze generation

The maze is generated using recursive backtracking. The algorithm begins at a starting cell in a grid of cells separated by walls. It checks the current cell for unvisited neighbouring cells and randomly selects one to explore.

When an unvisited neighbour is selected, the wall between the two cells is removed and the algorithm moves to the neighbouring cell. This process continues until a cell that has no unvisited neighbours is reached.

The algorithm then backtracks through previously visited cells until it finds a cell with an unvisited neighbour. It continues exploring and backtracking until every cell in the grid has been visited.

The result is a randomly generated maze in which every room is reachable from every other room.

## Project Structure

```text
src/
    constants.py - stores constant variables
    generator.py - procedurally generates a random maze
    main.py      - executes the program
    maze.py      - determines whether a position is a wall or exit
    renderer.py  - displays the maze
    robot.py     - handles robot movement

tests/
    test_generator.py - tests maze generation and related functionality
```

## Testing

Run all unit tests with:

```bash
python -m unittest discover
```

The test suite currently covers:
- wall removal
- exit generation
- maze connectivity
- helper functions

## Requirements

- Python 3.x