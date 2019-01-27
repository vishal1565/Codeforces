n = int(input())
a = [int(i) for i in input().split()]
avg = sum(a)/n
a.sort()
count = 0
if avg < 4.5 :
    for i in range(n):
        if avg < 4.5 :
            avg = (sum(a)+(5-a[i]))/n
            a[i] = 5
            count += 1
        else:
            break
print(count)