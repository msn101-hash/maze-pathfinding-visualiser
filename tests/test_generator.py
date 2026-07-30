import unittest
import src.generator as generator
import src.constants as constants

class TestGenerator(unittest.TestCase):

    def setUp(self):
        self.maze = []    
        for i in range(7):
            row = []
            for j in range(7):
                if i % 2 == 0:
                    row.append(constants.WALL)
                elif j % 2 == 0:
                    row.append(constants.WALL)
                else:
                    row.append(constants.EMPTY)
            self.maze.append(row)

    def test_remove_wall_north(self):
        generator.remove_wall((3, 3), (1, 3), self.maze)
        self.assertEqual(self.maze[2][3], constants.EMPTY)
        self.assertEqual(self.maze[1][3], constants.EMPTY)
        self.assertEqual(self.maze[3][3], constants.EMPTY)
        self.assertEqual(self.maze[2][2], constants.WALL)
        self.assertEqual(self.maze[2][4], constants.WALL)

    def test_remove_wall_south(self):
        generator.remove_wall((3, 3), (5, 3), self.maze)
        self.assertEqual(self.maze[4][3], constants.EMPTY)
        self.assertEqual(self.maze[3][3], constants.EMPTY)
        self.assertEqual(self.maze[5][3], constants.EMPTY)
        self.assertEqual(self.maze[4][2], constants.WALL)
        self.assertEqual(self.maze[4][4], constants.WALL)

    def test_remove_wall_west(self):
        generator.remove_wall((3, 3), (3, 1), self.maze)
        self.assertEqual(self.maze[3][2], constants.EMPTY)
        self.assertEqual(self.maze[2][2], constants.WALL)
        self.assertEqual(self.maze[4][2], constants.WALL)
        self.assertEqual(self.maze[3][1], constants.EMPTY)
        self.assertEqual(self.maze[3][3], constants.EMPTY)

    def test_remove_wall_east(self):
        generator.remove_wall((3, 3), (3, 5), self.maze)
        self.assertEqual(self.maze[3][4], constants.EMPTY)
        self.assertEqual(self.maze[3][3], constants.WALL)
        self.assertEqual(self.maze[3][5], constants.WALL)
        self.assertEqual(self.maze[2][4], constants.EMPTY)
        self.assertEqual(self.maze[4][4], constants.EMPTY)

    def test_find_unvisited_all_neighbours(self):
        unvisited = generator.find_unvisited(3, 3, self.maze, [])
        self.assertEqual(4, len(unvisited))
        self.assertEqual({(1, 3), (3, 5), (5, 3), (3, 1)}, set(unvisited))

    def test_find_unvisited_one_visited(self):
        unvisited = generator.find_unvisited(3, 3, self.maze, [(1, 3)])
        self.assertEqual(3, len(unvisited))
        self.assertEqual({(3, 5), (5, 3), (3, 1)}, set(unvisited))

    def test_find_unvisited_edge(self):
        unvisited = generator.find_unvisited(3, 1, self.maze, [(3, 3)])
        self.assertEqual(2, len(unvisited))
        self.assertEqual({(1, 1), (5, 1)}, set(unvisited))

    def test_find_unvisited_corner(self):
        unvisited = generator.find_unvisited(5, 5, self.maze, [(5, 3)])
        self.assertEqual(1, len(unvisited))
        self.assertEqual({(3, 5)}, set(unvisited))

    def test_find_unvisited_none(self):
        unvisited = generator.find_unvisited(3, 3, self.maze, [(1, 3), (3, 5), (5, 3), (3, 1)])
        self.assertEqual(0, len(unvisited))

    def test_maze_dimensions(self):
        maze = generator.generate_maze(11, 23)
        self.assertEqual(11, len(maze))
        self.assertEqual(23, len(maze[0]))

    def test_maze_exit(self):
        height = 7
        width = 7
        maze = generator.generate_maze(height, width)
        exits = [
            (i, j)
            for i, row in enumerate(maze)
            for j, cell in enumerate(row)
            if cell == constants.EXIT
        ]

        self.assertEqual(1, len(exits))

        exit_pos = exits[0]
        top = exit_pos[0] == 0
        bottom = exit_pos[0] == height - 1
        left = exit_pos[1] == 0
        right = exit_pos[1] == width - 1

        self.assertEqual(1, top + bottom + left + right)
    

if __name__ == "__main__":
    unittest.main()