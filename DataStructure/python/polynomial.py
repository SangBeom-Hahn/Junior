def addPoly():
    a = [3, [4,3,5,0]]
    b = [4, [3,1,0,2,1]]

    aDegree = a[0]
    bDegree = b[0]
    cDegree = max(aDegree, bDegree)
    cCoef = [0 for i in range(cDegree+1)]
    aIndex = 0
    bIndex = 0
    cIndex = 0

    while(aIndex <= aDegree or bIndex <= bDegree):
        if(aDegree > bDegree):
            cCoef[cIndex] = a[1][aIndex]
            cIndex+=1
            aIndex+=1
            aDegree-=1

        elif(aDegree < bDegree):
            cCoef[cIndex] = b[1][bIndex]
            cIndex += 1
            bIndex += 1
            bDegree -= 1

        else:
            cCoef[cIndex] = a[1][aIndex] + b[1][bIndex]
            cIndex += 1
            aIndex += 1
            bIndex += 1

    c = [cDegree, cCoef]
    return c

def printPoly():
    c = addPoly()
    for i in range(c[0]+1):
        print(f"{c[1][i]}X^{c[0]-i} +", end="")

if(__name__ == '__main__'):
    printPoly()

