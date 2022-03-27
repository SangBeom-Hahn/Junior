l = [2, 1, 4, 6, 7, 3, 5]

for i in range(1, len(l)):
    for j in range(i):
        if(l[i] > l[j]):
            pass
        else:
            l[i], l[j] = l[j], l[i]

print(l)