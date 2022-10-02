def a():
    arr = [[8, 7, 10], [0, 2, 2], [0, 6, 12], [1, 4, 7], [2, 0, 23], [3, 3, 31], [4, 1, 14], [4, 5, 25], [5, 6, 6], [6, 0, 52], [7, 4, 11]]
    return arr

def b():
    arr = [[0]*len(a()[0]) for i in range(len(a()))]
    print(arr)
    return arr

