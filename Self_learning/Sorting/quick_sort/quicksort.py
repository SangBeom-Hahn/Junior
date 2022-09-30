def quick_Sort(l):
    if(len(l) <= 1):
        return l

    l_L, l_R, l_P = [], [], []
    p = len(l) // 2
    n = len(l) - 1

    l[p], l[n] = l[n], l[p]

    L = -1
    for i in range(n):
        if (l[i] < l[n]):
            L+=1
            l[i], l[L] = l[L], l[i]

    l[L+1], l[n] = l[n], l[L+1]


    l_L = quick_Sort(l[:L+1])
    l_R = quick_Sort(l[L+2:])
    l_P = list(map(int, str(l[L + 1])))

    print(l_L)
    print(l_P)
    print(l_R)

    return l_L+l_P+l_R


'''
test.py

from main import quick_Sort

print(quick_Sort([2, 1, 3, 5, 4]))

'''

