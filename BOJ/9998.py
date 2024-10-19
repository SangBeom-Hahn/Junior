max_r = 0

def back(st):
    global max_r
    
    if(len(alphas) == k):
        al = set(alphas)
        cnt = 0
        for word in words:
            for digit in word:
                if(digit not in al):
                    break
            else:
                cnt += 1
        
        if(max_r < cnt):
            max_r = cnt
        return

    for i in range(st, 26):
        if(not used[i]):
            alphas.append(chr(97+i))
            used[i] = True
            back(i+1)
            alphas.pop()
            used[i] = False

alphas = ["a", "n", "t", "i", "c"]
used = [False] * 26
for ele in alphas:
    used[int(ord(ele)) - int(ord("a"))] = True

if(k < 5):
    print(0)
else:
    back(0)
    print(max_r)