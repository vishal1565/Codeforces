n = int(input())
a = [int(i) for i in input().split()]
res = []
if n == 2 and a[0] == a[1]:
    print("-1")
elif n == 1:
    print("-1")
else:
    for i in range(n):
        if a[i] != sum(a)-a[i]:
            #print("1")
            res.append(i+1)
            break
if len(res)!=0:
    print("1")
    print(*res)