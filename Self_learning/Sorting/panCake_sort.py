res = []
cnt = 0

def pan(l):
    global cnt
    if(len(l) == 1):
        res.append(l[0])
        return

    M = max(l)
    idx = l.index(M)
    subList = l[:idx+1]
    subList.reverse()
    if(idx != 0):
        cnt = cnt + 1
    l[:idx+1] = subList[:idx+1]
    l.reverse()
    cnt = cnt + 1

    part = l.pop()
    pan(l)
    res.append(part)

pan([2,4,3,1])
print(res)
print(cnt)