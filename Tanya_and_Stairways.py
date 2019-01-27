n = int(input())
arr = [int(i) for i in input().split()]
count = 1
res = []
if n != 1:
    for i in range(1,n-1):
        if arr[i] == 1:
            count += 1
            res.append(arr[i-1])
    if arr[-1] == 1:
        count += 1
        res.append(arr[-2])
        res.append(1)
    else:
        res.append(arr[-1])

print(count)
if n != 1:
    print(*res,sep=' ')
else:
    print(1)