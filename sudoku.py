class Sudoku:
    def __init__(self, grid):
        self.grid = grid

    def __is_array_unique(self, array):
        """checks if all numbers in array are unique"""
        return len(set(array)) == len(array)

    def is_grid_valid(self):
        """checks if the grid is valid"""
        # test if the grid is of size 9x9
        row_size = len(self.grid)
        column_size = len(self.grid[0])
        if row_size != column_size or row_size != 9:
            return False

        # test if all numbers in a row are unique
        for i in range(9):
            row = [num for num in self.grid[i] if num > 0]
            if not self.__is_array_unique(row):
                return False

        # test if all numbers in a column are unique
        for j in range(9):  # for jth column
            column = []
            for i in range(9):
                if self.grid[i][j] > 0:
                    column.append(self.grid[i][j])
            if not self.__is_array_unique(column):
                return False

        # test if all numbers in a subgrid are unique
        for i in range(9):
            x = (i // 3) * 3
            y = (i % 3) * 3
            subgrid = []
            for j in range(x, x+3):
                for k in range(y, y+3):
                    if self.grid[j][k] > 0:
                        subgrid.append(self.grid[j][k])
            if not self.__is_array_unique(subgrid):
                return False
        return True

    def is_valid(self, num, x, y):
        """
        checks if inserting num in grid's (x, y) position is valid
        :param num: the number to be inserted
        :param x: row number
        :param y: column number
        :return: True if the num can be inserted in (x, y) position, False otherwise
        """
        # check in current row
        if num in self.grid[x]:
            return False
        # check in current column
        for i in range(9):
            if num == self.grid[i][y]:
                return False

        # check in current subgrid
        subgrid_start_x = (x // 3) * 3
        subgrid_start_y = (y // 3) * 3
        subgrid_end_x = subgrid_start_x + 3
        subgrid_end_y = subgrid_start_y + 3
        for i in range(subgrid_start_x, subgrid_end_x):
            for j in range(subgrid_start_y, subgrid_end_y):
                if self.grid[i][j] == num:
                    return False

        return True

    def get_next_empty_cell(self):
        """
        returns next empty cell in the grid starting from 0, 0
        :return: a tuple of int if an empty cell is found, else a tuple of None
        """
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return None, None

    def solve(self):
        """
        recursively solves the grid using backtracking
        :return: True if a solution is possible, False otherwise
        """
        i, j = self.get_next_empty_cell()
        if i is None:  # all empty cells are filled
            return True
        for num in range(1, 10):
            if self.is_valid(num, i, j):
                self.grid[i][j] = num  # guess a number
                if self.solve():  # if the guess leads to a correct solution
                    return True
                else:  # undo the change in grid if the guess doesn't lead to a solution
                    self.grid[i][j] = 0
        return False

    def get_solution(self):
        """
        returns the solved grid if a solution is possible
        :return: 2d list of size 9x9 if a correct solution is possible, None otherwise
        """
        is_solved = self.solve()
        if is_solved:
            return self.grid
        return None
