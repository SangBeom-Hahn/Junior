l = [4,5,8,9,2,3]

def afterSort(l, k):
    n = len(l) // 2 #3

    if(k == l[n]):
        print("ok")
        return

    if(l[0] <= l[n-1]):
        if(l[n] < l[len(l)-1]):
            # ① 상태
            if(l[n] == k):
                print("ok")
                return
            elif(l[n] > k):
                bs(l[:n], k)
            else:
                bs(l[n:], k)

        else:
            # ② 상태
            if(l[n] > k and l[len(l)-1] < k):
                bs(l[:n], k)
            else:
                afterSort(l[n:], k)

    else:
        if(l[n] < l[len(l)-1]):
            # ③ 상태
            if (l[0] > k and l[len(l) - 1] < k):
                bs(l[n:], k)
            else:
                afterSort(l[:n], k)














def bs(l, k):
    if(len(l)==1 and l[0] != k):
        print("noop")
        return

    n = len(l) // 2

    if(l[n] == k):
        print("ok")
        return
    elif(l[n] < k):
        bs(l[n:], k)
    else:
        bs(l[:n], k)

afterSort(l, 9)