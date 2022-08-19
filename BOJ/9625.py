k = int(input())
dpA = [0] * (k+1)
dpB = [0] * (k+1)

dpA[0] = 1


for i in range(1, k+1):
    dpB[i] = dpA[i-1] + dpB[i-1]
    dpA[i] = dpB[i-1]

print(dpA[k], dpB[k])

print(dpA)
print(dpB)


# 1. A의 개수, B의 개수를 따로 세서 내 방식으로 풀기
# 2. DP 배열에 문자열을 넣었는데 그렇게 하지말고 DP[k]가 정답이도록 정수가 들어가게 하자(메모리 적게)
# 2-2. A와 B의 개수를 잘 세어보면 피보나치 모양이 나옴