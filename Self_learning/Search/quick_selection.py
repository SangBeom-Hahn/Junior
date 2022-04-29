l = [1,10,9,19,20,2,12,5,15,3,13,4,14,7,17,8,18,16,6,11]
# l = [5, 2, 1, 7, 4, 3, 9, 6, 8, 12, 11, 10]
# l = [5, 2, 1, 7, 4, 3, 6]

def part(l, p):
    p = l.index(p)
    l[len(l)-1], l[p] = l[p], l[len(l)-1]
    L = -1

    for i in range(len(l)-1):
        if(l[i] < l[len(l)-1]):
            L+=1
            l[i], l[L] = l[L], l[i]
    l[len(l)-1], l[L+1] = l[L+1], l[len(l)-1]

    return L+1

def quick(l, k):
    m = mom(l) # 피봇 13으로 함
    p = part(l, m) # p는 피봇 인덱스임 12

    if(k < p): #
        return quick(l[:p], k)
    elif(k > p):
        return quick(l[p+1:], k-p-1)
    else:
        return l[p]

def mom(l):
    l3 = []
    sort_List = sorted(l)
    if(len(sort_List) <= 5):
        return sort_List[len(sort_List) // 2]
    for i in sort_List:
        if(sort_List.index(i) % 5 == 2):
            l3.append(i)

    return mom(l3)

print(quick(l, 3))















# def quick(l, k):
#     p = part(l, k)
#
#     if(k < p):
#         return quick(l[:p], 5)
#     elif(k > p):
#         return quick(l[p:], 5)
#     else:
#         return l[p]
