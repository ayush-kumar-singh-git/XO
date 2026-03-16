import random

alpha = 0.1
gamma = 0.9   
epsilon = 0.1 

Q = {}

def getEmptySquares(B):
    squares = []
    for i in range(3):
        for j in range(3):
            if B[i][j] == 0:
                squares.append((i+1, j+1))
    return squares

def boardToState(B):
    return tuple(B[i][j] for i in range(3) for j in range(3))

def getQ(state, action) :
    return Q.get((state, action), 0.0)

def chooseAction(B) :
    moves = getEmptySquares(B)
    state = boardToState(B) 
    
    if random.random() < epsilon :
        return random.choice(moves)

    bestMove = None
    bestValue = -10000
    
    for move in moves:
        q = getQ(state, move)
        if q > bestValue :
            bestValue = q
            bestMove = move
    
    return bestMove

def updateQ(state, action, reward, nextState, nextMoves):
    old = getQ(state, action)
    if len(nextMoves) == 0:
        maxNext = 0
    else :
        maxNext = max(getQ(nextState, a) for a in nextMoves)
    Q[(state, action)] = old + alpha * (reward + gamma*maxNext - old)

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

def playGame() :
    B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    player = 1
    
    history = []
    
    while True:
        state = boardToState(B)
        move = chooseAction(B)
        B[move[0]-1][move[1]-1] = player
        history.append((state, move, player))
        result = check(B)
        moves = getEmptySquares(B)
        
        if result != 0 or len(moves) == 0:
            break
        player *= -1
    
    if result == 1:
        rewardX = 1
        rewardO = -1
    elif result == -1:
        rewardX = -1
        rewardO = 1
    else:
        rewardX = rewardO = 0
        
    for state, move, player in history:
        reward = rewardX if player == 1 else rewardO
        old = getQ(state, move)
        Q[(state, move)] = old + alpha * (reward - old)
            
for i in range(500):
    playGame()
    
def QEngine(B):

    state = boardToState(B)
    moves = getEmptySquares(B)

    bestMove = None
    bestVal = -1000

    for m in moves:
        val = getQ(state, m)
        if val > bestVal:
            bestVal = val
            bestMove = m

    return bestMove

def valid(B, i, j):
    res = 0
    if i >= 1 and i <= 3 and j >= 1 and j <= 3 and B[i-1][j-1] == 0:
        res = 1
    return res

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

def copyBoard(B):
    b = [[0,0,0],
                  [0,0,0],
                  [0,0,0]]
    for i in range(3):
        for j in range(3):
            b[i][j] = B[i][j]
    return b

def play():
    games = 10
    mmScore = 0
    mm = 1
    qScore = 0
    q = -1
    draws = 0
    for game in range(games) :
        moves = 0
        print("***********************************")
        B = [[0,0,0],[0,0,0],[0,0,0]]
        result = 0
        turn = 1
        while moves < 9 and result == 0:
            printBoard(B)
            print()
            if turn == mm :
                move, _ = minimax(B,9, mm == 1)
                B[move[0]-1][move[1]-1] = mm
            else :
                move = QEngine(B)
                B[move[0]-1][move[1]-1] = q
            result = check(B)
            turn *= -1
            moves+=1
        printBoard(B)
        print()
        if result == 0 :
            draws+=1
        elif result == mm :
            mmScore += 1
        elif result == q :
            qScore += 1
        
        mm*=-1
        q*=-1
        print("***************************************")
    print(f"Minimax Wins: {mmScore}")   
    print(f"Q Learning Wins: {qScore}")   
    print(f"Draws: {draws}")   
play()
