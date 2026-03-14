function [] = printBoard(B)
    for i = 1 : 3
        for j = 1 : 3
            if B(i,j) == 0
                fprintf(".  ");
            elseif B(i,j) == 1
                fprintf("X  ");
            else
                fprintf("O  ");
            end
        end
        fprintf('\n')
    end
end
