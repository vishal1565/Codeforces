for _ in range(int(input())):
    n, s, t = [int(i) for i in input().split()]
    if s==n and t==n:print(1)
    elif s==n or t==n:
        print(n-min(s,t)+1)
    else:
        comm = s+t-n
        a,b = s-comm, t-comm
        print(max(a,b)+1)