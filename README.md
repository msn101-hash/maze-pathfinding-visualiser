# Toy Robot Maze Solver

Toy Robot Maze Solver is a Python application that procedurally generates random mazes using recursive backtracking. Players can navigate a robot through the maze using directional commands and attempt to reach the exit, or have the robot solve the maze automatically using the DFS algorithm.

## Features

- Procedurally generated random mazes
- Maze generation using recursive backtracking
- Manual robot navigation
- Pathfinding
- Randomly generated exits
- Modular project structure
- Unit tests for maze generation and functionality

## Demo

Coming soon.

## Installation

Clone the repository:

```bash
git clone ...
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

Use `solve` to automatically solve the maze, and `quit` to end the program.

## Algorithms

### Maze generation

The maze is generated using recursive backtracking. The algorithm begins in a room in a grid of rooms separated by walls. It checks the current room for unvisited neighbouring rooms and randomly selects one to explore.

When an unvisited neighbour is selected, the wall between the two rooms is removed and the algorithm moves to the neighbouring room. This process continues until a room that has no unvisited neighbours is reached.

The algorithm then backtracks through previously visited rooms until it finds a room with an unvisited neighbour. It continues exploring and backtracking until every room in the grid has been visited.

The result is a randomly generated maze in which every room is reachable from every other room.

### Pathfinding

The pathfinding algorithm uses DFS to solve the maze. It is given a starting position in the maze and searches for the exit.

From the starting position, it looks for empty, unvisited neighbouring cells and recursively explores them. If a route reaches a dead end, the algorithm backtracks and explores another unvisited route. When the exit is found, the recursive calls return the successful path back to the starting position.

The result is the only path from the starting position to the exit.

## Design / Architecture

The project is divided into separate modules, with each module responsible for a specific part of the application:

- `generator.py` handles procedural maze generation using recursive backtracking.
- `robot.py` handles the robot's position and movement.
- `maze.py` contains functions for checking properties of the maze, such as whether a position is an exit.
- `renderer.py` handles displaying the maze and robot.
- `pathfinding.py` handles finding a path from the starting position to the exit.
- `constants.py` stores values shared across the project.
- `main.py` coordinates the different components and controls the game loop.

This separation keeps individual components focused on a single responsibility and makes the code easier to test and maintain.

## Project Structure

```text
src/
    generator.py
    robot.py
    maze.py
    renderer.py
    pathfinding.py
    constants.py
    main.py

tests/
    test_generator.py
    test_maze.py
    test_robot.py
    test_pathfinding.py
```

## Testing

Run all unit tests with:

```bash
python -m unittest discover
```

The test suite currently covers:
- Wall removal
- Exit generation
- Maze connectivity
- Robot movement
- Pathfinding
- Wall collision
- Obstacle and exit detection
- Helper functions

## Requirements

- Python 3.x