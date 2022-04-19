l = [8,9,1,2,3]

def maxE(l):
    mid = len(l) // 2 # 2
    maxL, maxR = 0, 0
    if(mid == 1):
        return l[0]

    subL = l[:mid] #81
    subR = l[mid:] #23

    if(subL[0] > subL[len(subL) - 1]):
        maxL = maxE(subL)
    else:
        maxL = subL[len(subL) - 1]

    if (subR[0] > subR[len(subR) - 1]):
        maxR = maxE(subR)
    else:
        maxR = subR[len(subR) - 1]

    return maxL if maxL > maxR else maxR

print(maxE(l))