for _ in range(int(input())):
    n = int(input())
    st = list(input())
    if st[0]=='>':
        print(0)
    elif st[-1]=='<':
        print(0)
    else:
        count1, count2 = 0, 0
        for i in range(n):
            if st[i]=='<':
                count1 += 1
            else:
                break
        for i in range(n-1,0,-1):
            if st[i]=='>':
                count2 += 1
            else:
                break
        print(min(count1,count2))