def solveNQueens(n):
    def is_safe(board, row, col):
        # Check if a queen can be placed at board[row][col]
        # Check the left diagonal
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check the upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check the upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True

    def backtrack(row):
        if row == n:
            # All queens are placed, add the board configuration to solutions
            solutions.append(["".join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'  # Place a queen
                backtrack(row + 1)
                board[row][col] = '.'  # Backtrack
                
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    backtrack(0)
    return solutions

# Example usage
n = int(input("n value: "))
solutions = solveNQueens(n)
for solution in solutions:
    for row in solution:
        print(row)
    print()
 