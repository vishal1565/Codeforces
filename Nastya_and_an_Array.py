n = int(input())
a = [int(i) for i in input().split()]
list1 = set(a)
unique = list(list1)
flag = True
for i in unique:
    if i == 0:
        print(len(unique)-1)
        flag = False
        break
if flag:
    print(len(unique))