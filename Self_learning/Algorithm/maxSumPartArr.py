l = [31, -41, 59, 26, -53, 58, 97, -93]

def right(l):
    rightMaxTotal = 0
    rightSumCurr = 0

    for i in range(0, len(l)):
        rightSumCurr += l[i]

        if (rightMaxTotal < rightSumCurr):
            rightMaxTotal = rightSumCurr

    return rightMaxTotal

def left(l):
    leftMaxTotal = 0
    letfSumCurr = 0

    for i in range(len(l)-1, -1, -1):
        letfSumCurr += l[i]

        if(leftMaxTotal < letfSumCurr):
            leftMaxTotal = letfSumCurr

    return(leftMaxTotal)

def mid(l):
    n = len(l) // 2 #2
    leftMaxTotal = 0
    letfSumCurr = 0
    rightMaxTotal = 0
    rightSumCurr = 0


    for i in range(n-1, -1, -1):
        letfSumCurr += l[i]

        if(leftMaxTotal < letfSumCurr):
            leftMaxTotal = letfSumCurr

    for i in range(n, len(l)):
        rightSumCurr += l[i]

        if (rightMaxTotal < rightSumCurr):
            rightMaxTotal = rightSumCurr

    return rightMaxTotal+leftMaxTotal

def maxSumPartArr(l):
    n = len(l) // 2

    if(n == 1):
        m = mid(l)
        r = right(l[n:])
        l = left(l[:n])
        return max(m, r, l)

    m = mid(l)
    r = maxSumPartArr(l[:n])
    l = maxSumPartArr(l[n:])
    return(max(m, r, l))

print(maxSumPartArr(l))