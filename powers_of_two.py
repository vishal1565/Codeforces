n, k = [int(i) for i in input().split()]
if n == k:
    res = [1]*k
    print(*res)
else:
    res = list(int(i) for i in bin(n)[2:])
    if sum(res) == k:
        print("YES")
        res.reverse()
        for i in range(len(res)):
            if res[i]!=0:
                print(pow(2,i),end=" ")
    else:
        res.reverse()
        a = []
        for i in range(len(res)):a.append(res[i])
        res.pop()
        a[len(res)], a[len(res)-1] = 0, a[len(res)-1]+2
        while len(res)!=0 and sum(a)!=k and len(res)>=2: 
            if a[len(res)-1]!=0:
                a[len(res)-2],a[len(res)-1] = a[len(res)-2]+2, a[len(res)-1]-1
            else:
                res.pop()
        if sum(a)==k:
            print("YES")
            #final = []
            for i in range(len(a)):
                if a[i]!=0:
                    for _ in range(a[i]):
                        print(pow(2,i),end=" ")
                        #final.append(pow(2,i))
            #print(*final)

        else:
            print("NO")