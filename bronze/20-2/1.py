# 别开方，精度不允许
# 最后要求输出int

# tuple 来组合
# good search

# 2.0和2是不同的

# 什么题都可以手撸测试用例

import math
import sys

sys.stdin = open('triangles.in', 'r')
sys.stdout = open('triangles.out', 'w')

n = int(input())
points = []
for i in range(n):
    point = list(map(int, input().split()))
    points.append(point)



def area(p1,p2,p3):
    # right triange
    # good sim
    t = (p1,p2,p3)
    for i in range(3):
        a = t[i]
        b = t[(i+1)%3]
        c = t[(i+2)%3]
        if (a[0] == b[0] and a[1] == c[1])\
                or (a[0] == c[0] and a[1] == b[1]):
            break
    else:
        return 0

    p1_x, p1_y = p1
    p2_x, p2_y = p2
    p3_x, p3_y = p3
    p1_p2 = abs(p1_x - p2_x)**2 + abs(p1_y - p2_y)**2
    p2_p3 = abs(p2_x - p3_x)**2 + abs(p2_y - p3_y)**2
    p1_p3 = abs(p1_x - p3_x)**2 + abs(p1_y - p3_y)**2

    edges = [p1_p2, p2_p3, p1_p3]
    edges.sort()
    if edges[0] + edges[1] == edges[2]:
        return int(math.sqrt(edges[0]))*int(math.sqrt(edges[1]))
    else:
        return 0

ans = 0
for a in range(n-2):
    for b in range(a+1, n-1):
        for c in range(b+1, n):
            p1 = points[a]
            p2 = points[b]
            p3 = points[c]
            ans = max(ans, area(p1,p2,p3))

print(ans)

