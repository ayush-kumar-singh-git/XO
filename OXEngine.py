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

def valid(B, i, j):
    res = 0
    if i >= 1 and i <= 3 and j >= 1 and j <= 3 and B[i-1][j-1] == 0:
        res = 1
    return res


def copyBoard(B):
    b = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
    for i in range(3):
        for j in range(3):
            b[i][j] = B[i][j]
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
    if move == None :
        print("The Game Is Already Finished")
        return
    print()
    if evaluation == 1 :
        print("X is Winning")
    elif evaluation == -1 :
        print("O is Winning")
    else :
        print("Position is Drawn")
    print()
    print("Best move in the position is: ")
    print()
    if XtoMove :
        B[move[0]-1][move[1]-1] = 1
    else :
        B[move[0]-1][move[1]-1] = -1
    printBoard(B)

# B = [[1, 0, 1], [0, -1, 0], [-1, 0, 0]]
# B = [[1, -1, 1], [0, 0, 0], [-1, 0, 0]]
B = [[-1, 1, 0], [0, 0, 0], [-1, 0, 1]]
# B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# B = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
OXEngine(B, 10, False)