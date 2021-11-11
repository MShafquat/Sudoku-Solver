import unittest
from sudoku import Sudoku
from main import convert_input_to_int_list


class ValidationTest(unittest.TestCase):
    def setUp(self):
        self.grid = '''
            9 0 4 0 1 2 0 3 0
            0 7 1 0 0 0 0 0 0
            8 3 0 0 0 4 5 6 0
            0 0 6 2 5 0 0 0 0
            0 8 5 9 0 3 6 4 0
            0 0 0 0 4 6 1 0 0
            0 9 7 1 0 0 0 8 6
            0 0 0 0 0 0 9 2 0
            0 5 0 4 2 0 3 0 7
        '''
        self.sudoku = Sudoku(convert_input_to_int_list(self.grid))

    def test_grid_converted_to_int_list(self):
        self.assertTrue(convert_input_to_int_list(self.grid))

    def test_input_grid_valid(self):
        self.assertTrue(self.sudoku.is_grid_valid())

    def test_duplicate_num_in_row_invalid(self):
        self.assertFalse(self.sudoku.is_valid(9, 0, 1))

    def test_duplicate_num_in_column_invalid(self):
        self.assertFalse(self.sudoku.is_valid(5, 0, 1))

    def test_duplicate_num_in_subgrid_invalid(self):
        self.assertFalse(self.sudoku.is_valid(9, 2, 2))

    def test_valid_num_valid(self):
        self.assertTrue(self.sudoku.is_valid(6, 0, 1))


class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        self.expected_solution = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        self.sudoku = Sudoku(self.grid)

    def test_is_solution_correct(self):
        result = self.sudoku.get_solution()
        self.assertTrue(result)
        self.assertEqual(result, self.expected_solution)
