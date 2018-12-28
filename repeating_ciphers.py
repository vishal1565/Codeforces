n = int(input())
s = list(input())
s.reverse()
res,count = [],1
while(len(s)!=0):
    res.append(s[-1])
    for i in range(count):
        s.pop()
    count += 1
print(*res,sep="")
