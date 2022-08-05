N , k = input().split()
N = int(N)
k = int(k)

l = []
su = 0


for i in range(N):
    kinds = int(input())
    l.append(kinds)

for j in range(N-1,-1,-1):
    mok = k // l[j]
    if(mok != 0):
        su += mok
    k = k % l[j]
    if(k == 0):
        break

print(su)