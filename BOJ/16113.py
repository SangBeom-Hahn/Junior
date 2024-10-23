def back(chose, start):
    if(len(chose) > 0):
        combs.append(chose[:])
    
    for i in range(start, n):
        chose.append(nums[i])
        back(chose, i+1)
        chose.pop()

n = int(input())
nums = list(map(int, input().split()))
combs = []

back([], 0)

comb_sum = set()
for comb in combs:
    comb_sum.add(sum(comb))

m = sum(nums)

print(m - len(comb_sum))