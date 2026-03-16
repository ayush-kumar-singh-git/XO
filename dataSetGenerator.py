import random

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
    

def generate(number) :
    for game in range(number) :
        moves = random.randint(0, 9)
        result = 0
        move = 0
        board = [[0,0,0],[0,0,0],[0,0,0]]
        player = 1
        while move < moves and result == 0 :
            move += 1
            sq = getEmptySquares(board)
            r,c = random.choice(sq)
            board[r-1][c-1] = player
            player *= -1
            result = check(board)
        
        for i in range(3) :
            for j in range(3) :
                print(board[i][j], end=",")
        currMove = (move%2==0)
        if result != 0:
            value = result
        else:
            depth = len(getEmptySquares(board))
            ans = minimax(board,depth, currMove)
            value = ans[1]
        print(value)

generate(40000)