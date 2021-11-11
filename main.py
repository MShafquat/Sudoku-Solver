import re
import sys

from sudoku import Sudoku


def convert_input_to_int_list(text):
    """
    converts text input for grid to a 2d list of integers
    :param text: a string input for sudoku grid
    :return: 2d list of integers
    """
    regex = r"(\d\s){9}"  # a pattern of 9 (digit + whitespace)
    matches = re.finditer(regex, text, re.MULTILINE)
    return [list(map(int, line.group().split())) for line in matches]


if __name__ == '__main__':
    # check if a file name is provided
    n = len(sys.argv)
    if n < 3:
        print(f"Usage: {sys.argv[0]} <input file> <output file>")
        sys.exit(1)

    # open input file or throw exception if not found
    try:
        in_file = open(sys.argv[1], 'r')
        in_file.close()
    except FileNotFoundError:
        print("Input file not found")
        sys.exit(1)

    # open output file or throw exception if not found
    try:
        out_file = open(sys.argv[2], 'w')
        out_file.close()
    except FileExistsError:
        print("File already exists")
        sys.exit(1)

    try:
        grid = convert_input_to_int_list(in_file.readlines())
    except ValueError:
        print('Invalid input file')
        sys.exit(1)

    sudoku = Sudoku(grid)
    if sudoku.is_grid_valid():
        solution = sudoku.get_solution()
        if not solution:
            print("Solution not possible")
        else:
            print(solution)
