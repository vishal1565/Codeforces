import heapq

def f(start,k,hits):
    s, count = hits[start][1],0
    for i in range(start,len(hits)):
        if hits[i][1]==s:
            count += 1
        else:
            break
    if count<=k:
        return False,sum(hits[start:start+count]),start+count
    else:
        h = []
        for i in hits[start:start+count]:
            heapq.heappush(h,i)
        t = heapq.nlargest(k,h)
        val= 0
        for i in t:
            val+=i[0]
        return True, val, start+count


n, k = [int(i) for i in input().split()]
s = [int(i) for i in input().split()]
seq = list(input())
hits, dmg, t1,t2 = [], s[0], "",""
for i in range(n):
    hits.append([s[i],seq[i]])
if k>=n:
    print(sum(s))
else:
    i = 1
    while i<n:
        if seq[i]==seq[i-1]:
            flag, tmp, newIndex =f(i-1,k,hits)
            
            dmg += tmp-s[i-1]
            i = newIndex
            if i<n:dmg+=s[i]
        else:
            dmg += s[i]
        i+=1 
    print(dmg)