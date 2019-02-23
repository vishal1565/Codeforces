w1, h1, w2, h2 = [int(i) for i in input().split()]
area = w1+2+2*h1+1
area += w2+2+2*h2
if w1>w2:
    area += w1-w2 -1
else:
    area -= 1
print(area)