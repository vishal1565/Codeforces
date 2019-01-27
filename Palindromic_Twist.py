def checkpalin(n,str):
    palin = True
    for i in range(n//2):
        if str[i] != str[n-1-i]:
            palin = False
    if palin:
        return True
    else:
        return False

def func(n,str):
    res = True
    for i in range(n//2):
        if abs(ord(str[i])-ord(str[n-1-i])) == 1 or abs(ord(str[i])-ord(str[n-1-i])) > 2:
            return False
    return res


t = int(input())
while t>0:
    n = int(input())
    str = list(input())
    if checkpalin(n,str):
        print("YES")
    else:
        if func(n,str):
            print("YES")
        else:
            print("NO")


    t -= 1