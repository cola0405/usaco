# 全排列

# 为什么area*2就行
# 因为边都是整数，唯一的小数就是在1/2来的
# 那么*2后就没小数问题了

# 别开方，精度不允许
# 最后要求输出int
# 2.0和2是不同的

from itertools import permutations
import sys
sys.stdin = open('triangles.in', 'r')
sys.stdout = open('triangles.out', 'w')

n = int(input())
points = [tuple(map(int, input().split())) for i in range(n)]

ans = 0
x,y = 0,1
for p1, p2, p3 in permutations(points, 3):
    if p1[x] == p2[x] and p3[y] == p2[y]:
        area = abs(p1[y] - p2[y]) * abs(p3[x] - p2[x])
        ans = max(area, ans)
print(ans)
