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

