from math import ceil,floor
n = int(input())
nos,res = [],[]
for i in range(n):      
    nos.append(float(input()))
for i in nos:
    res.append(floor(i))
s = sum(res)
if s==0:
    print(*res,sep="\n")
else:
    for i in range(n):
        if s==0:break
        if nos[i]!=res[i]:
            res[i] += 1
            s += 1
    print(*res,sep="\n")