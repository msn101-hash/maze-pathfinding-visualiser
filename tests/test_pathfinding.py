import unittest
from src import pathfinding
from src import generator
from src import constants


class TestPathfinding(unittest.TestCase):

    def setUp(self):
        self.maze = [
            ["#", "#", "#", "#", "#", "#", "#"],
            ["#", " ", " ", " ", " ", " ", "#"],
            ["#", " ", "#", "#", "#", "#", "#"],
            ["#", " ", "#", " ", " ", " ", "#"],
            ["#", " ", "#", "#", "#", " ", "#"],
            ["#", " ", " ", " ", " ", " ", "#"],
            ["#", "#", "#", "E", "#", "#", "#"]
        ]

    def test_solve_maze_finds_exit(self):
        maze = generator.generate_maze(7, 7)
        path = pathfinding.find_path(3, 3, maze, set())

        self.assertTrue(path)
        start = path[0]
        exit = path[-1]

        self.assertEqual((3, 3), start)
        self.assertTrue(maze[exit[0]][exit[1]] == constants.EXIT)

    def test_pathfinding(self):
        path = pathfinding.find_path(3, 3, self.maze, set())
        expected = [(3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (6, 3)]
        self.assertEqual(expected, path)