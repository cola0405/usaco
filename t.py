n, m = map(int, input().strip().split())

cells = []
for i in range(n):
    cells.append(input())

ans = 0
lst = []



for i in range(n):
    for j in range(m):
        if cells[i][j] == "#":
            continue
        if ((j-1>=0 and cells[i][j-1] == "#") or j == 0)\
                 and j+2<m and cells[i][j+1] == "." and cells[i][j+2] == ".":
            ans += 1
            lst.append([i+1,j+1])

        elif ((i-1>=0 and cells[i-1][j] == "#") or i == 0)\
                 and i+2<n and cells[i+1][j] == "." and cells[i+2][j] == ".":
            ans += 1
            lst.append([i+1,j+1])

print(ans)
for i in lst:
    print(i[0],i[1])





