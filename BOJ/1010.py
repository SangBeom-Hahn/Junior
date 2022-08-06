import math

n = int(input())
sight = []

for i in range(n):
    sight.append(list(map(int, input().split())))

for west, east in sight:
    print(math.comb(east, west))
