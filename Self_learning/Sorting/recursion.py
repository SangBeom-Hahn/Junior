lst = [3, 5, 2, 1, 7, 6, 4]
lst3 = []

def pan(l):
    for i in range(len(l)):
        lst2 = []

        for j in range(len(l)): #이 for문은 다시 들어오는데 l의 길이가 줄어들어서 len이 줄어 들지 않을까? 맞음
            maxi = max(l)

            if(l[j] != maxi):
                lst2.append(l[j])
            else:
                lst2.append(l[j])
                lst2.reverse()

        lst2.reverse()
        a = lst2.pop()
        lst3.append(a)
        l.remove(a)

    lst3.reverse()

pan(lst)
print(lst3)

# 최악의 경우에 얼마나 뒤집냐
# 코드로 짜라
"""
1번
lst = [-2, 1, 4, 3, 5]

def min(l):
    mini = l.pop()

    if(l == []):
        return mini
    else:
        com = min(l)
        if(mini > com):
            mini = com
        return mini

print(min(lst))
"""

"""
2번
lst = [2, 1, 4, 3, 5, 7, 6, 8, 9, 10]

def sum(l):
    if(l == []):
        return 0
    else:
        return (l.pop() + sum(l))

print(sum(lst))
"""


# 3번
lst = [2, -1, -4, 3, 5]
lst2 = list()

def select(l):
    mini = min(lst)
    rec = 0

    if(len(l) == 1):
        lst2.append(mini)
        return mini
    else:
        lst2.append(mini)
        l.remove(mini)
        rec = select(l)
        return mini

select(lst)
print(lst2)

