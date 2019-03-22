n = int(input())
a = [int(i) for i in input().split()]
days, maxi = 0,0
for i in range(n):
    if maxi<a[i]:maxi=a[i]
    if a[i]==i+1:
        if a[i]==maxi:
            days += 1
print(days)