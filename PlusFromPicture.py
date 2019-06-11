def checkPlus(h,w,i,j,grid):
    for r1 in range(i-1,-1,-1):
        if grid[r1][j]=='*':
            grid[r1][j]='.'
        else:
            break
    for r1 in range(i+1,h):
        if grid[r1][j]=='*':
            grid[r1][j]='.'
        else:
            break
    for c1 in range(j-1,-1,-1):
        if grid[i][c1]=='*':
            grid[i][c1]='.'
        else:
            break
    for c1 in range(j+1,w):
        if grid[i][c1]=='*':
            grid[i][c1]='.'
        else:
            break
    grid[i][j]='.'
    for x in range(h):
        for y in range(w):
            if grid[x][y]=='*':
                return 'NO'
    return 'YES'

h,w = [int(i) for i in input().split()]
grid = []
for _ in range(h):
    temp = list(input())
    grid.append(temp)
ans,flag = 'NO', False
for i in range(1,h-1):
    for j in range(1,w-1):
        if grid[i][j]=='*':
            if grid[i-1][j]=='*' and grid[i+1][j]=='*' and grid[i][j-1]=='*' and grid[i][j+1]=='*':
                print(i,j)
                ans = checkPlus(h,w,i,j,grid)
                flag = True
                break
    if flag:break
print(ans)