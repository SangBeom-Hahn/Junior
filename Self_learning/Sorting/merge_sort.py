l = [5,4,3,2,1, 7, 8, 9,6]


def mergeSort(l):
    lst = list()

    if(len(l) == 1):
        return l

    mid = len(l) // 2
    m1 = mergeSort(l[:mid])
    m2 = mergeSort(l[mid:])


    i, j = 0, 0
    while(i < len(m1) and j < len(m2)):
        if (m1[i]>m2[j]):
            lst.append(m2[j])
            j += 1
        else:
            lst.append(m1[i])
            i += 1
    lst.extend(m1[i:])
    lst.extend(m2[j:])
    return lst

print(mergeSort(l))