n, k =[int(i) for i in input().split()]
rocket = [(ord(i)-96) for i in list(input())]
rocket.sort()
sum, i = 0, 1
prev = rocket[0]
sum += rocket[0]
k -=1
while k>0 and i<n:
    if rocket[i] - prev > 1:
        sum += rocket[i]
        prev = rocket[i]
        k -= 1
    i += 1
if k == 0:
    print(sum)
else:
    print("-1") 