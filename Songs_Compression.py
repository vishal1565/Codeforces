n, m = [int(i) for i in input().split()]
a = []
un, comp = 0, 0
for _ in range(n):
    temp = [int(i) for i in input().split()]
    tmp = temp[0]-temp[1]
    temp.append(tmp)
    a.append(temp)
    un += temp[0]
    comp += temp[1]
if un <= m:
    print("0")
elif comp>m:
    print("-1")
else:
    a.sort(key=lambda a: (-a[2],-a[1]))
    count = 0
    for i in range(n):
        un = un - a[i][0] +a[i][1]
        count += 1
        if un<= m:
            break
    print(count)