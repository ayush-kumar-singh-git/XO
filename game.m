result = 0;
moves = 0;
board = zeros(3,3);
printBoard(board)
while moves < 9 && result == 0
    move = input(' ');
    i = move(1);
    j = move(2);
    if ~valid(board, i, j)
        fprintf("Invalid Move. Please Re-enter Your Move\n")
        continue
    end
    moves = moves + 1;
    if mod(moves, 2) == 1
        board(i,j) = 1;
    else 
        board(i,j) = -1;
    end
    printBoard(board)
    result = check(board);
end

if result == 1
    fprintf("X Wins\n")
elseif result == -1
    fprintf("O Wins\n")
else
    fprintf("Draw\n")
end
