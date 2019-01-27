q = int(input())
for _ in range(q):
    n = int(input())
    seq = list(input())
    n1 = int(seq[0])
    n2 = ""
    n2 = n2.join(i for i in seq[1:])
    n2 = int(n2)
    if n2>n1:
        print("YES")
        print(2)
        print(n1,n2)
    else:
        print("NO")