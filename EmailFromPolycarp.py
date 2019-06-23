from itertools import groupby
for _ in range(int(input())):
    str1 = list(input())
    str2 = list(input())
    g1 = [(k,sum(1 for i in g)) for k,g in groupby(str1)]
    g2 = [(k,sum(1 for i in g)) for k,g in groupby(str2)]
    flag = True
    if len(g1)!=len(g2):
        flag==False
        print("NO")
        continue
    else:
        for i in range(len(g1)):
            if g1[i][0]!=g2[i][0]:
                flag = False
                break
            else:
                if g1[i][1]>g2[i][1]:
                    flag = False
                    break
    if flag:print("YES")
    else:print("NO")