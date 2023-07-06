def is_safe(puzzle, row, col, num):
    # Check if the number already exists in the row
    if num in puzzle[row]:
        return False

    # Check if the number already exists in the column
    for i in range(len(puzzle)):
        if puzzle[i][col] == num:
            return False

    # Check if the number already exists in the 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if puzzle[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(puzzle):
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            if puzzle[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(puzzle, row, col, num):
                        puzzle[row][col] = num
                        if solve_sudoku(puzzle):
                            return True
                        puzzle[row][col] = 0  # backtrack if no solution found
                return False
    return True


def print_sudoku(puzzle):
    for i in range(len(puzzle)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(puzzle[i])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(puzzle[i][j], end=" ")
        print()


# Get user input for the Sudoku puzzle
print("""Enter your sudoku problem using format given below:
x x x x x x x x x  |  Eg: 0 0 0 3 9 0 0 0 5
x x x x x x x x x  |      0 2 8 0 0 6 1 0 0
x x x x x x x x x  |      4 0 0 0 0 0 0 0 0
x x x x x x x x x  |      0 6 3 0 0 8 2 0 0
x x x x x x x x x  |      0 7 0 0 0 0 0 0 0
x x x x x x x x x  |      0 0 0 2 0 0 0 1 0
x x x x x x x x x  |      7 0 0 0 0 0 3 0 0
x x x x x x x x x  |      1 0 0 0 0 4 0 0 0
x x x x x x x x x  |      0 3 4 0 6 0 0 9 0
  """)
print("Enter the Sudoku puzzle (use spaces, 0 for empty cells):")
puzzle = []
for _ in range(9):
    row = list(map(int, input().split()))
    puzzle.append(row)

print("\nSudoku puzzle:")
print_sudoku(puzzle)

if solve_sudoku(puzzle):
    print("\nSolution:")
    print_sudoku(puzzle)
else:
    print("\nNo solution exists.")

    