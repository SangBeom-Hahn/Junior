li = [4, 2, 3, 1, 5, 7, 6, 10, 9, 8]
min_Index = 0

for i in range(len(li) - 1):
    m = max(li)

    for j in range(i, len(li)):
        if(li[j] < m):
            m = li[j]
            min_Index = j

    li[i], li[min_Index] = li[min_Index], li[i]

print(li)

# 재귀 버전
l = [2,3,5,1,4]
l2 = list()

def select(l):
    if(len(l) == 1):
        return l[0]

    big = max(l)
    idx = l.index(big)
    l[0], l[idx] = l[idx], l[0]

    l2.append(select(l[1:]))
    return l[0]

l2.append(select(l))
print(l2)

