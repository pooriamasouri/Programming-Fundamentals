import copy

def getValue(board, position):
    return board[(position - 1) // 3][(position - 1) % 3]

def is_winner(board, player):
    # Check rows, columns, diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    if all([board[i][i] == player for i in range(3)]): return True
    if all([board[i][2 - i] == player for i in range(3)]): return True
    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def minimax(board, depth, is_maximizing):
    if is_winner(board, "O"): return 10 - depth
    if is_winner(board, "X"): return depth - 10
    if is_full(board): return 0

    if is_maximizing:
        best = -float("inf")
        for i in range(1, 10):
            if getValue(board, i) == " ":
                new_board = copy.deepcopy(board)
                new_board[(i - 1) // 3][(i - 1) % 3] = "O"
                val = minimax(new_board, depth + 1, False)
                best = max(best, val)
        return best
    else:
        best = float("inf")
        for i in range(1, 10):
            if getValue(board, i) == " ":
                new_board = copy.deepcopy(board)
                new_board[(i - 1) // 3][(i - 1) % 3] = "X"
                val = minimax(new_board, depth + 1, True)
                best = min(best, val)
        return best

def getMove(board):
    best_score = -float("inf")
    best_move = None
    for i in range(1, 10):
        if getValue(board, i) == " ":
            new_board = copy.deepcopy(board)
            new_board[(i - 1) // 3][(i - 1) % 3] = "O"
            score = minimax(new_board, 0, False)
            if score > best_score:
                best_score = score
                best_move = i
    return best_move
