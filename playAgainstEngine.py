def printBoard(B):
    for i in range(3):
        for j in range(3):
            if B[i][j] == 0:
                print(". ", end=" ")
            elif B[i][j] == 1:
                print("X ", end=" ")
            else:
                print("O ", end=" ")
        print()

def check(B):
    r = 0

    if B[0][0] == B[0][1] and B[0][1] == B[0][2]:
        r = B[0][0]

    elif B[1][0] == B[1][1] and B[1][1] == B[1][2]:
        r = B[1][0]

    elif B[2][0] == B[2][1] and B[2][1] == B[2][2]:
        r = B[2][0]

    elif B[0][0] == B[1][0] and B[1][0] == B[2][0]:
        r = B[0][0]

    elif B[0][1] == B[1][1] and B[1][1] == B[2][1]:
        r = B[0][1]

    elif B[0][2] == B[1][2] and B[1][2] == B[2][2]:
        r = B[0][2]

    elif B[0][0] == B[1][1] and B[1][1] == B[2][2]:
        r = B[0][0]

    elif B[0][2] == B[1][1] and B[1][1] == B[2][0]:
        r = B[0][2]

    return r

def valid(board, row, col):
    res = 0
    if row >= 1 and row <= 3 and col >= 1 and col <= 3 and board[row-1][col-1] == 0:
        res = 1
    return res


def copyBoard(board):
    b = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
    for i in range(3):
        for j in range(3):
            b[i][j] = board[i][j]
    return b

def getEmptySquares(B):
    squares = []
    for i in range(3):
        for j in range(3):
            if B[i][j] == 0:
                squares.append((i+1, j+1))
    return squares

def minimax(B, depth, XtoMove):
    result = check(B)
    squares = getEmptySquares(B)
    if depth == 0 or result != 0 or len(squares) == 0:
        return None, result
    inf = 10000
    if XtoMove == True :
        bestEval = -1*inf
        bestMove = None
        for sq in squares:
            b = copyBoard(B)
            b[sq[0]-1][sq[1]-1] = 1
            _, val = minimax(b, depth-1, False)
            if val > bestEval :
                bestEval = val
                bestMove = sq
        return bestMove, bestEval
    else :
        bestEval = inf
        bestMove = None
        for sq in squares:
            b = copyBoard(B)
            b[sq[0]-1][sq[1]-1] = -1
            _, val = minimax(b, depth-1, True)
            if val < bestEval :
                bestEval = val
                bestMove = sq
        return bestMove, bestEval
    

def OXEngine(B, maxDepth, XtoMove) :
    printBoard(B)
    move, evaluation = minimax(B, maxDepth, XtoMove)
    if XtoMove :
        B[move[0]-1][move[1]-1] = 1
    else :
        B[move[0]-1][move[1]-1] = -1
    return B

def play():
    print("Choose your side (X/O): ", end="")
    playerSide = input().strip().upper()
    board = [[0,0,0],[0,0,0],[0,0,0]]
    moves = 0
    result = 0
    playerIsX = (playerSide == 'X')
    while moves < 9 and result == 0:
        print("\nCurrent Board:")
        printBoard(board)
        if (moves % 2 == 0 and playerIsX) or (moves % 2 == 1 and not playerIsX):
            while True:
                print("Your move (row col): ", end="")
                r, c = map(int, input().split())

                if valid(board, r, c):
                    break
                else:
                    print("Invalid move. Try again.")

            board[r-1][c-1] = 1 if playerIsX else -1
        else:
            print("Engine thinking...")
            move, _ = minimax(board, 10, moves % 2 == 0)

            r, c = move
            board[r-1][c-1] = 1 if moves % 2 == 0 else -1

            print(f"Engine plays: {r} {c}")
        moves += 1
        result = check(board)
    print("\nFinal Position:")
    printBoard(board)

    if result == 1:
        print("X wins!")
    elif result == -1:
        print("O wins!")
    else:
        print("Draw!")
play()
