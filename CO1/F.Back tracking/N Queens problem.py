#N-Queens Problem using Backtracking

def is_safe(board, row, col, N):
    # Check the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper-left diagonal
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve_n_queens(board, row, N):
    # If all queens are placed
    if row == N:
        return True

    # Try placing queen in every column
    for col in range(N):

        if is_safe(board, row, col, N):
            # Place queen
            board[row] = col

            # Recursively place remaining queens
            if solve_n_queens(board, row + 1, N):
                return True

            # Backtrack: remove queen
            board[row] = -1

    return False


# Input
N = int(input("Enter the value of N: "))

# Board representation
board = [-1] * N

# Solve the problem
if solve_n_queens(board, 0, N):
    print("\nSolution:")

    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution exists.")