n = int(input())
a = [int(i) for i in input().split()]
if n%2 ==1:
    for i in range(n):
        if a[i]%2 == 0:
            a[i] -= 1
else:
    for i in range(n):
        if a[i]%2 == 0:
            a[i] -= 1
print(*a,sep=' ')