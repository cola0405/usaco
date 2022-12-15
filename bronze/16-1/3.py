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

n = int(input())
for i in range(n):
    direction, step = input().split()
    step = int(step)
    on_x = 0
    on_y = 0

    if direction == 'N':
        on_x = -1
    elif direction == 'S':
        on_x = 1
    elif direction == 'W':
        on_y = -1
    else:
        on_y = 1

    # move
    for i in range(step):
        count += 1
        x += 1 * on_x
        y += 1 * on_y
        if cells[x][y] != 0:
            ans = min(ans, count - cells[x][y])
        cells[x][y] = count

if ans == float('inf'):
    print(-1)
else:
    print(ans)