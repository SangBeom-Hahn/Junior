# 버블 반복문
l = [1,-4,2,5,3]

for i in range(len(l)):
    for j in range(len(l)-(i)):
        if(l[j] > l[j+1]):
            l[j], l[j+1] = l[j+1], l[j]

print(l)
"""
버블 재귀
lst = [-2, 1, 4, -3, 5]
lst2 = list()

def bubble(l):
    maxi = max(l)
    rec = 0

    if(len(l) == 1):
        lst2.append(maxi)
        return
    else:
        l.remove(maxi)
        bubble(l)
        lst2.append(maxi)
        return maxi

bubble(lst)
print(lst2)
"""

#선택 : 작은걸 앞으로
#삽입 : 이미 정렬된 애들이랑 비교해서 들어갈 곳 쏙
#버블 : 큰거