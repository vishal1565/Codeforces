def fun(n):
    count = 0
    while n%5==0:
        n = 4*n//5
        count += 1
    while n%3==0:
        n = 2*n//3
        count += 1
    while n%2==0:
        n = n//2
        count += 1
    if n==1:
        return count
    else:
        return -1
        
for _ in range(int(input())):
    n = int(input())
    print(fun(n))