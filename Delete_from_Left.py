a = list(input())
b = list(input())
a.reverse()
b.reverse()
count = 0
for i in range(min(len(a),len(b))):
    if a[i] == b[i]:
        count += 1
    else:
        break
res = len(a)-count+len(b)-count
print(res)