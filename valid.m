function [res] = valid(B,i,j)
    res = 0;
    if i>=1 && i<=3 && j>=1 && j<=3 && B(i,j) == 0
        res = 1;
    end
end
