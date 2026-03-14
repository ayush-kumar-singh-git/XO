import random

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

def move(B) :
    squares = getEmptySquares(B)
    x = random.choice(squares)
    return x

def start():
    result = 0
    moves = 0
    B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    while moves < 9 and result == 0 :
        moves+=1

        curr = move(B);
        if moves % 2 == 1:
            B[curr[0]-1][curr[1]-1] = 1
        else :
            B[curr[0]-1][curr[1]-1] = -1

        result = check(B)

    printBoard(B)
    print()
    return result

def simulate(number):
    X = 0
    O = 0
    D = 0
    for i in range(number):
        print(i+1)
        x = start()
        if x == 1:
            X+=1
        elif x == -1:
            O += 1
        else :
            D += 1
    print("Final Stats: ")
    print(f"Number of X wins {X}")
    print(f"Number of O wins {O}")
    print(f"Number of Draws {D}")

simulate(10000)
