# 全排列

# 为什么area*2就行
# 因为边都是整数，唯一的小数就是在1/2来的
# 那么*2后就没小数问题了

# 别开方，精度不允许
# 最后要求输出int
# 2.0和2是不同的

# 什么题都可以手撸测试用例

import sys
sys.stdin = open('triangles.in', 'r')
sys.stdout = open('triangles.out', 'w')

n = int(input())
points = []
for i in range(n):
    point = list(map(int, input().split()))
    points.append(point)


ans = 0
for a in range(n):
    for b in range(n):
        # 确保a、b同一行（y相等）
        if a == b or points[a][1] != points[b][1]:
            continue
        for c in range(n):
            # 确保a、c同一列（x相等）
            if b == c or points[a][0] != points[c][0]:
                continue
            # 只取到符合规则的三个点
            # 且每次a作为直角
            # a、b在同一行
            # a、c在同一列
            x = abs(points[a][0] - points[b][0])
            y = abs(points[a][1] - points[c][1])
            ans = max(ans, x*y)

print(ans)

