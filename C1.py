n,m =  [int(i) for i in input().split()]
t = [int(i) for i in input().split()] 
s = 0
for i in range(n):
    s += t[i]
    count = 0
    if s>m:
        curr = s
        for j in sorted(t[:i],reverse=True):
            if curr>m:
                count += 1
                curr -= j
            else:break
    print(count,end=" ")