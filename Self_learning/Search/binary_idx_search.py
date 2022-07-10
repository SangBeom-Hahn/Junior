l = [1,3,5,7,9]
idxList = list()

def bs(l, k):
    if(len(l)==1 and l[0] != k):
        print("no")
        return

    n = len(l) // 2

    if(k == l[n]):
        idxList.extend(l[:n + 1])
        print(len(idxList)-1)
        return
    elif(k < l[n]):
        bs(l[:n], k)
    else:
        idxList.extend(l[:n])
        bs(l[n:], k)

bs(l, 8)