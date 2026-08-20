import unittest
from src import maze


class TestMaze(unittest.TestCase):

    def setUp(self):
        self.maze = [
            ["#", "#", "#"],
            ["#", " ", "E"],
            ["#", "#", "#"]
        ]

    def test_is_obstacle(self):
        self.assertTrue(maze.is_obstacle(self.maze, 0, 0))
        self.assertFalse(maze.is_obstacle(self.maze, 1, 1))
        self.assertFalse(maze.is_obstacle(self.maze, 1, 2))

    def test_is_exit(self):
        self.assertTrue(maze.is_exit(self.maze, 1, 2))
        self.assertFalse(maze.is_exit(self.maze, 0, 0))
        self.assertFalse(maze.is_exit(self.maze, 1, 1))