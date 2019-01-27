n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = []
for i in a:
    b.append(i)
b.sort(reverse= True)
res = []
last = 0
count = []
for i in range(k):
    res.append(b[i])
print(sum(res))

for i in range(n):
    if a[i] in res:
        count.append(i+1-last)
        res.remove(a[i])
        last = i+1

if sum(count)<n:
    count[-1] += n-sum(count)
print(*count,sep=' ')