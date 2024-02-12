'''

'''

arr = [0, 7, 3, 5, 8, 2, 1, 4, 6, 9]

def q(arr):
    if(len(arr) <= 1):
        return arr
    
    p = arr[0]
    tail = arr[1:]
    
    left = [i for i in tail if(i < p)]
    right = [i for i in tail if(i >= p)]
    
    return q(left) + [p] + q(right)

print(q(arr))