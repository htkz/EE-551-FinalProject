# The main purpose of our program is to test whether an input sudoku is valid or not
# The input should be an 9 * 9 matrix

valid_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def check_num_range(mat):
    for i in range(9):
        for j in range(9):
            if mat[i][j] not in valid_nums:
                return False
    return True


def check_sudoku(mat):
    # check if there are duplicate value in the same row
    for row in mat:
        row_set = set()
        for val in row:
            if val in row_set:
                return False
            row_set.add(val)

    # check if there are duplicate value in the same column
    for col in range(9):
        col_set = set()
        for row in range(9):
            val = mat[row][col]
            if val in col_set:
                return False
            col_set.add(val)

    # check if there are duplicate in each 3 * 3 square area
    for row in [0, 3, 6]:
        for col in [0, 3, 6]:
            square_set = set()
            for offset_row in range(3):
                for offset_col in range(3):
                    curr_row = row + offset_row
                    curr_col = col + offset_col
                    if mat[curr_row][curr_col] in square_set:
                        return False
                    square_set.add(mat[curr_row][curr_col])

    return True

def test_sudoku(mat):
    if not mat or not mat[0] or len(mat) != 9 or any(len(row) != 9 for row in mat):
        print('Error: The sudoku is not a 9 * 9 sudoku!')
        return
    if not check_num_range(mat):
        print('Error: There are values that is not in range 1 - 9 in the input!')
        return

    if not  check_sudoku(mat):
        print('The answer of this sudoku is not correct!')
        return

    print('Congratulations, this answer of this sudoku is correct!')


test_sudoku0 = [
    [1, 2, 3]
]

test_sudoku1 = [
    [9, 7, 4, 2, 3, 6, 1, 5, 8],
    [6, 3, 8, 5, 9, 1, 7, 4, 2],
    [1, 2, 5, 4, 8, 7, 9, 3, 6],
    [3, 1, 6, 7, 5, 4, 2, 8, 9],
    [7, 4, 2, 9, 1, 8, 5, 6, 3],
    [5, 8, 9, 3, 6, 2, 4, 1, 7],
    [8, 6, 7, 1, 2, 5, 3, 9, 4],
    [2, 5, 3, 6, 4, 9, 8, 7, 1],
    [4, 9, 1, 8, 7, 3, 6, 2, 5],
]

test_sudoku2 = [
    [9, 7, 2, 4, 3, 6, 1, 5, 8],
    [6, 3, 8, 5, 9, 1, 7, 4, 2],
    [1, 2, 5, 4, 8, 7, 9, 3, 6],
    [3, 1, 6, 7, 5, 4, 2, 8, 9],
    [7, 4, 2, 9, 1, 8, 5, 6, 3],
    [5, 8, 9, 3, 6, 2, 4, 1, 7],
    [8, 6, 7, 1, 2, 5, 3, 9, 4],
    [2, 5, 3, 6, 4, 9, 8, 7, 1],
    [4, 9, 1, 8, 7, 3, 6, 2, 5],
]

test_sudoku3 = [
    [9, 7, 2, 4, 3, 6, 1, 5, 8],
    [7, 3, 8, 5, 9, 1, 6, 4, 2],
    [1, 2, 5, 4, 8, 7, 9, 3, 6],
    [3, 1, 6, 7, 5, 4, 2, 8, 9],
    [7, 4, 2, 9, 1, 8, 5, 6, 3],
    [5, 8, 9, 3, 6, 2, 4, 1, 7],
    [8, 6, 7, 1, 2, 5, 3, 9, 4],
    [2, 5, 3, 6, 4, 9, 8, 7, 1],
    [4, 9, 1, 8, 7, 3, 6, 2, 5],
]

if __name__ == "__main__":
    for sudoku in [test_sudoku0, test_sudoku1, test_sudoku2, test_sudoku3]:
        test_sudoku(sudoku)




