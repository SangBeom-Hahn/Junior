import sys

su = int(sys.stdin.readline().rstrip())
l = []
for i in range(su):
    l.append(list(sys.stdin.readline().rstrip()))

for k in range(1, len(l[0])+1):
    result = []
    for i in range(su):
        result.append(l[i][   len(l[0])-k : len(l[0])   ])

    if(len(result) == len(set(list(map(tuple, result))))):
        print(k)
        break
