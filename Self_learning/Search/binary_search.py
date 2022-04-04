def binarySearch(l, a):
    if(l[len(l) // 2] == a):
        return len(l) // 2

    elif(l[len(l) // 2] > a):
        l = l[:len(l)//2]
        return binarySearch(l, a)
    else:
        l = l[len(l)//2:]
        return binarySearch(l, a)


l = [1,2,3,4,5,6]
print(binarySearch(l, 4))

