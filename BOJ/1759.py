'''
49개 수 중에서 k개를 골라서 집합 s를 만들고 그 수만 가지고 6개를 선택한다.

ex) s = 1, 2, 3, 5, 8, 13, 21, 24인 경우/ 6개를 고르는 수는 28가지다.
* k, s
출 : 수를 고르는 모든 방법을 출력하라

'''

def back(chose, start):
    if(len(chose) == 6):
        print(chose)
        return
    
    for i in range(start, k):
        chose.append(arr[i])
        back(chose, i+1)
        chose.pop()

nums = list(map(int, input().split()))
k = nums[0]
arr = nums[1:]

back([], 0)