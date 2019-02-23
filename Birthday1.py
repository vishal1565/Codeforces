n = int(input())
arr = [int(i) for i in input().split()]
arr1, arr2 = [], []
arr.sort(reverse = True)
for i in range(n):
    if i%2==0:
        arr1.append(arr[i])
    else:
        arr2.append(arr[i])
arr2.reverse()
for i in arr2:
    arr1.append(i)
print(*arr1)