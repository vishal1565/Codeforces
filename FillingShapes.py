def solve(n):
    if n%2==1:
        return 0
    else:
        return pow(2,n//2)

n = int(input())
print(solve(n))