n = int(input())
if n==1:print(1)
elif n==2:print(5)
else:
    res = (2*n-1)+(1+(2*(n-1)-1))*(n-1)
    print(res)