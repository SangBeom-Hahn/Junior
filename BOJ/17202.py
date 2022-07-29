n1 = input()
n2 = input()

l = list()
for i in range(len(n1)):
    l.append(int(n1[i]))
    l.append(int(n2[i]))

while(1):
    if(len(l) == 2):
        print(str(l[0]) + str(l[1]))
        break

    arr = list()
    for i in range(len(l)-1):
        arr.append((l[i]+l[i+1]) % 10)
    l = arr


