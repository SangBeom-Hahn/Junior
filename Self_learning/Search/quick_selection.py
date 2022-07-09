'''
질문 : 아니 이진탐색은 정렬된 상태만 되는 거 아님? 이것도 중간에서 나누는 것만 아니지 2진이라고 볼 수 있잖아
답변 : 퀵 정렬의 특징이 피봇을 기준으로 양 옆에 크고 작은 값이 나뉜다는 거잖아 이진 탐색이
정렬된 상태에서만 되는 이유는 중간 값을 잡았는데 왼쪽에 크고 작은 값이 섞여있으면 대소비교를 못하니 그래
근데 퀵셀렉은 파티션 과정에서 완벽하게 나뉘니 대소비교가 되어서 탐색이 가능한 거다
+ 파티션으로 언젠가는 다 정렬이 되네
'''

l = [1,2,7,5,4,8,3,9]

def part(l):
    p = len(l)//2 #파티션의 인덱스
    checkL = -1
    n = len(l) - 1

    l[p], l[n] = l[n], l[p]

    for i in range(len(l)):
        if(l[i]<l[n]):
            checkL+=1
            l[checkL], l[i] = l[i], l[checkL]

    l[checkL+1], l[n] = l[n], l[checkL+1]

    return l, checkL+1

def QS(l, k):
    if(len(l) == 1 and l[0] != k):
        print("noop")
        return

    l, p = part(l)

    if(l[p] == k):
        print("find")
        return
    elif(l[p] > k):
        QS(l[:p], k)
    else:
        QS(l[p+1:], k)

QS(l, 111)