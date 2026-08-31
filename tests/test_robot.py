import unittest
from src import robot


class TestRobot(unittest.TestCase):

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

    def test_move_north(self):
        new_position, status = robot.move_robot(self.maze, "north", (5, 5))
        self.assertEqual((4, 5), new_position)
        self.assertEqual("normal", status)

    def test_move_north_into_wall(self):
        new_position, status = robot.move_robot(self.maze, "north", (1, 1))
        self.assertEqual((1, 1), new_position)
        self.assertEqual("obstacle", status)

    def test_move_east(self):
        new_position, status = robot.move_robot(self.maze, "east", (1, 1))
        self.assertEqual((1, 2), new_position)
        self.assertEqual("normal", status)

    def test_move_east_into_wall(self):
        new_position, status = robot.move_robot(self.maze, "east", (5, 5))
        self.assertEqual((5, 5), new_position)
        self.assertEqual("obstacle", status)

    def test_move_south(self):
        new_position, status = robot.move_robot(self.maze, "south", (1, 1))
        self.assertEqual((2, 1), new_position)
        self.assertEqual("normal", status)

    def test_move_south_into_wall(self):
        new_position, status = robot.move_robot(self.maze, "south", (5, 5))
        self.assertEqual((5, 5), new_position)
        self.assertEqual("obstacle", status)

    def test_move_west(self):
        new_position, status = robot.move_robot(self.maze, "west", (5, 5))
        self.assertEqual((5, 4), new_position)
        self.assertEqual("normal", status)

    def test_move_west_into_wall(self):
        new_position, status = robot.move_robot(self.maze, "west", (1, 1))
        self.assertEqual((1, 1), new_position)
        self.assertEqual("obstacle", status)