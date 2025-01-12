n,q = map(int, input().split())
xy = [[0]*n for _ in range(n)]
xz = [[0]*n for _ in range(n)]
yz = [[0]*n for _ in range(n)]

ans = 0
for _ in range(q):
    x,y,z = map(int, input().split())
    xy[x][y] += 1
    xz[x][z] += 1
    yz[y][z] += 1
    if xy[x][y] == n:
        ans += 1
    if xz[x][z] == n:
        ans += 1
    if yz[y][z] == n:
        ans += 1
    print(ans)