import sys
sys.stdin = open('mowing.in', 'r')
sys.stdout = open('mowing.out', 'w')

cells = []
for i in range(3000):
    cells.append([0]*3000)

x = 1500
y = 1500
count = 0
ans = float('inf')

d = {'N':(-1,0), 'S':(1,0), 'W':(0,-1), 'E':(0,1)}

n = int(input())
for i in range(n):
    direction, step = input().split()
    step = int(step)
    dx,dy = d[direction]
    # move
    for i in range(step):
        count += 1
        x += dx
        y += dy
        if cells[x][y] != 0:
            ans = min(ans, count - cells[x][y])
        cells[x][y] = count

if ans == float('inf'):
    print(-1)
else:
    print(ans)