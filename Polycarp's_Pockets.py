from itertools import groupby
n = int(input())
a = [int(i) for i in input().split()]
s=sorted(a)
keys=[]
groups=[]
length= []
for k,g in groupby(s):
    keys.append(k)
    groups.append(list(g))
for i in groups:
    length.append(len(i))
print(max(length))