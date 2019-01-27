n = int(input())
ch = str(input())
divisors = []
a = list(ch)
temp = []
for i in range(1,(n//2)+1):
    if n%i == 0:
        divisors.append(i)
for i in divisors:
    temp = a[0:i]
    for j in temp:
        a.remove(j)
    for j in range(i):
        a.insert(0,temp[j])
a.reverse()
print(*a,sep='')