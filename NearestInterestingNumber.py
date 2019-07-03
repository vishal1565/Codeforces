a = int(input())
while True:
    b = [int(i) for i in str(a)]
    if sum(b)%4==0:
        print(a)
        break
    else:
        a += 1