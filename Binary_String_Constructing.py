a, b, x = [int(i) for i in input().split()]
ans = [1]
for i in range(x):
    if ans[-1]==1:
        ans.append(0)
    else:ans.append(1)
one = sum(ans)
zero = len(ans)-one
if one < b:
    for i in range(b-one):
        ans.insert(0,1)
if zero < a:
    if ans[-1]==0:
        while zero != a:
            ans.append(0)
            zero+=1
    else:
        ind = ans.index(0)
        for i in range(a-zero):
            ans.insert(ind,0)
#print(ans)
if sum(ans) != b:
    while sum(ans)!= b:
        del ans[0]
if ans[0]!=1:
    ans.append(0)
    del ans[0]
#print(ans)
zero = len(ans)-b
while zero!=a:
    del ans[ans.index(0)]
print(*ans,sep="")