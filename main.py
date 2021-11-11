import argparse
from pprint import pprint
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
    parser = argparse.ArgumentParser(description="Solves a valid sudoku puzzle")
    parser.add_argument('input_file', help="Input text file containing 9x9 grid of spaced separated "
                                           "integers 0 - 9, where 0 represents an empty cell")
    parser.add_argument('-o', '--output_file', help="Output text file with the solution of the puzzle. "
                                                    "If not provided, the output is shown to the console")
    args = parser.parse_args()
    input_file_name = args.input_file
    output_file_name = args.output_file

    # open input file or throw exception if not found
    try:
        input_file_handle = open(input_file_name, 'r')
    except FileNotFoundError:
        print("Input file not found")
        sys.exit(1)

    if output_file_name:
        # open output file or throw exception if not found
        try:
            output_file_handle = open(output_file_name, 'w')
        except FileExistsError:
            print("File already exists")
            sys.exit(1)

    try:
        grid = convert_input_to_int_list(input_file_handle.read())
    except ValueError:
        print('Invalid input file')
        sys.exit(1)

    sudoku = Sudoku(grid)
    if sudoku.is_grid_valid():
        solution = sudoku.get_solution()
        if not solution:
            print("Solution not possible")
        else:
            if output_file_name:
                for row in solution:
                    row = list(map(str, row))
                    output_file_handle.writelines(' '.join(row))
                    output_file_handle.writelines('\n')
            else:
                print("Solution of the puzzle:")
                pprint(solution)
    input_file_handle.close()
    if output_file_name:
        output_file_handle.close()
