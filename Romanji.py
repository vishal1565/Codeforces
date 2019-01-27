s = list(input())
a = ['a','e','i','o','u']
c = False
for i in range(len(s)-1):
    if not s[i] in a and s[i] != 'n':
        if s[i+1] in a:
            continue
        else:
            c = True
            print("NO")
            break
    elif s[i] in a or s[i] == 'n':
        continue
if not c and len(s)>1:
    if not s[-2] in a and s[-1] in a:
        print("YES")
    elif s[-2] in a:
        if s[-1] in a or s[-1] == 'n':
            print("YES")
        else:
            print("NO")
    elif s[-2] == 'n' and s[-1] == 'n':
        print("YES")
    else:
        print("NO") 
elif not c and len(s)==1:
    if s[0] in a :
        print("YES")
    elif s[0] == 'n':
        print("YES")
    else:
        print("NO")