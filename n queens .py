def solve_n_queens(N):
    def is_safe(board, row, col):
        # Check if no queen can attack this position
        for i in range(col):
            if board[row][i] == 'Q':
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True

    def backtrack(board, col):
        if col == N:
            solutions.append(["".join(row) for row in board])
            return

        for i in range(N):
            if is_safe(board, i, col):
                board[i][col] = 'Q'
                backtrack(board, col + 1)
                board[i][col] = '.'

    solutions = []
    empty_board = [['.' for _ in range(N)] for _ in range(N)]
    backtrack(empty_board, 0)

    return solutions

def print_solutions(solutions):
    for i, solution in enumerate(solutions):
        print(f"Solution {i + 1}:")
        for row in solution:
            print(row)
        print()

# Example usage for N = 4
N = 4 ''' To get input from user use => int(input()) '''
solutions = solve_n_queens(N)
print_solutions(solutions)
'''

Explanation of the Backtracking Approach:

The is_safe function checks if it's safe to place a queen at a given position (row, col) on the chessboard.
It checks for conflicts in the same row, left diagonal, and right diagonal.

The backtrack function recursively explores all possible queen placements for a given column col.
It starts from the first column (column 0) and progresses column by column.
When it reaches the last column (col == N), a valid solution is found and added to the solutions list.

In the backtrack function, if a safe position for a queen is found in a column,
the queen is placed ('Q' is placed on the chessboard), and the function proceeds to the next column.

If a solution is found or the algorithm reaches an invalid configuration,
it backtracks by undoing the queen placement ('.' is placed on the chessboard), and the exploration continues.

The solve_n_queens function initializes an empty chessboard and starts the backtracking process from column 0.

All valid solutions are collected in the solutions list and returned.

Time Complexity Analysis:

The time complexity of the backtracking algorithm for the N-Queens problem can be quite high,
especially for larger values of N.
It depends on the number of recursive calls and the time it takes to validate each queen placement.

In the worst case, the algorithm explores all possible combinations of queen placements,
resulting in a time complexity of approximately O(N!), where N is the size of the chessboard.
In practice, the algorithm prunes many branches early when it finds conflicts,
which can significantly reduce the number of recursive calls.
The actual time complexity may vary depending on the specific problem instance and the efficiency of the implementation.
For small to moderate values of N, the algorithm can efficiently find solutions. However, for very large values of N,
the time required to find all solutions may become prohibitive due to the factorial nature of the time complexity.

It's important to note that there are more efficient algorithms and optimizations for solving the N-Queens problem for very large N,
such as using bitwise operations or symmetry reduction techniques.
''' 

