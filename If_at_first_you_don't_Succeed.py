a ,b ,c ,n = [int(i) for i in input().split()]
res = n-(a+b-c) 
if res > 0 and c <= min(a,b) :
    print(res)
else:
    print("-1")