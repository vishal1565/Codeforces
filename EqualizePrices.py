for _ in range(int(input())):
    n, k = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    maxi,mini = max(a),min(a)
    if mini+k>=maxi:
        print(mini+k)
    else:
        if mini+k>=maxi-k:
            print(mini+k)
        else:
            print(-1)