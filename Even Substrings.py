n = int(input())
a = [int(i) for i in list(input())]
res = 0
for i in range(n):
    if a[i]%2==0:res += i+1
print(res)