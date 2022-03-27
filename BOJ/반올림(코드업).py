a, b = map(long , input().split())

c = a/b
d = c//0.0001
e = d%10

if(e >= 5 and e<9):
    c = c+0.001
    f = int((c//0.001))
else:
    f = int((c//0.001))
g = f*0.001

print(f)
print("%.3f"%g)
