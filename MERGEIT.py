def fun(n,a):
    a.sort()
    count,t1,t2 = 0, [],[]
    for i in a:
        if i%3==0:
            count += 1
        elif i%3==1:
            t1.append(i)
        else:
            t2.append(i)
    l1,l2 = len(t1), len(t2)
    m = min(l1,l2)
    count += m
    l1,l2 = l1-m,l2-m
    if l1==0:
        count += l2//3
    else:
        count += l1//3
    return count
 
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    print(fun(n,a))