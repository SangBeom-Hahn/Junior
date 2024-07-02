'''
n개의 정수의 수열에서 크기가 양수인 부분 수열 중에서 그 수열이 원소를 다 더한 값이 
s가 되는 경우의 수를 구하라

1.모경수(prt, n=1)
1) 백으로 탐색(start)

* n, s : 정수의 개수, 합
n개의 정수
출 : 합이 s가 되는 부분 수열의 개수
2. 시복 : n^3
'''
from itertools import permutations

def solution(n, weak, dist):
    leng = len(weak)
    for x in range(leng):
        weak.append(weak[x]+n)
    answer = len(dist)+1
    
    for start in range(leng):
        for fr in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + fr[0]
            
            for i in range(start, start+leng):
                if(position < weak[i]):
                    count += 1
                    if(count > len(dist)):
                        break
                    position = weak[i] + fr[count-1]
            answer = min(answer, count)
    return answer 
    
            
print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))