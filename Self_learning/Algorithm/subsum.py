def subSum(X, i, T):
    if(T == 0):
        return True
    elif(T<0 or i==-1):
        return False
    else:
        wIn = subSum(X, i-1, T-X[i])
        wOut = subSum(X, i-1, T)
        return wIn or wOut

print(subSum([11,6,5,1,7,13,12], 6, 15))