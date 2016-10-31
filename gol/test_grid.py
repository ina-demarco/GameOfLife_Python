from unittest import TestCase

from gol import Grid as Grid


class TestGrid(TestCase):
    def setUp(self):
        self.grid = Grid.Grid(4, 6);

    def test_gridsize_x(self):
        self.assertEqual(self.grid.x, 4)

    def test_gridsize_x(self):
        self.assertEqual(self.grid.y, 6)

    def test_count_live_neighbors(self):
        self.grid.print_matrix()
        print("1,1 has neighbours: ", self.grid.count_neighbors(1, 1))
        print("1,3 has neigbors:", self.grid.count_neighbors(1, 3))

    def test_check_is_valid_position(self):
        self.assertTrue(self.grid.check_is_valid_position((self.grid.x - 1), (self.grid.y - 1)))
        self.assertTrue(self.grid.check_is_valid_position(0, 0))
        self.assertTrue(self.grid.check_is_valid_position(1, 3))
        self.assertFalse(self.grid.check_is_valid_position(self.grid.x, self.grid.y))
        self.assertFalse(self.grid.check_is_valid_position(10, 10))

    def test_check_is_alive(self):
        self.grid.print_matrix()
        print("0,0 is alive:", self.grid.check_is_alive(0, 0))
        print("4,6 is alive:", self.grid.check_is_alive(self.grid.x - 1, self.grid.y - 1))

    def test_next_generation(self):
        matrix = [[False, False, False, False, False, False, False, False],
                  [False, False, False, False, True, False, False, False],
                  [False, False, False, True, True, False, False, False],
                  [False, False, False, False, False, False, False, False]]
        self.grid.add_predefined_matrix(matrix)
        self.grid.print_matrix()

    def test_draw_matrix(self):
        self.grid.draw_matrix()

    def test_small_matrix(self):
        self.grid = Grid.Grid(5, 5)
        matrix = [[False, False, False, False, False],
                  [False, False, True, False, False],
                  [False, False, True, False, False],
                  [False, False, True, False, False],
                  [False, False, False, False, False]]
        self.grid.add_predefined_matrix(matrix)
        self.grid.draw_matrix()

    def test_other_dimension(self):
        self.grid = Grid.Grid(20, 20)
        self.grid.draw_matrix()
