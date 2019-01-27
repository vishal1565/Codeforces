n = int(input())
a = []
temp = pow(10,9)+1
for i in range(n):
    t = [int(i) for i in input().split()]
    a.append(t)
c = False
for i in a:
    if temp>=max(i):
        temp = max(i)
        continue
    elif temp>= min(i):
        temp = min(i)
        continue
    else:
        print("NO")
        c = True
        break
if not c:
    print("YES")