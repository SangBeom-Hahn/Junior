def Lis(a, l):
    if(len(l) == 0):
        return 0
    elif(a > l[0]): # 작으면 포함 안하고 재귀하고
        return Lis(a, l[1:]) 
    else: #크면 포함 안하기도 하고 해보기도 해서 재귀한다 -> 백트랙의 개념
        skip = Lis(a, l[1:])
        take = Lis(l[0], l[1:])+1
        return max(skip, take)

l = [1,4,5,3,2,8]
print(Lis(l[0], l)) #len(l[6:]) == 0