temp = [int(i) for i in input().split()]
pos, d = temp[:3], temp[-1]
pos.sort()
count = 0
if pos[1]-pos[0]<d:
    count += d-(pos[1]-pos[0])
if pos[2]-pos[1]<d:
    count += d-(pos[2]-pos[1])
print(count)