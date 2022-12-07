# 近似法
# 单层for循环能取所有点
# 双重for循环能遍历所有可能的切割情况
# “当前x下划出所有y的切割线”


import sys
sys.stdin = open('balancing.in', 'r')
sys.stdout = open('balancing.out', 'w')

n, b = map(int, input().split())
X = []
Y = []
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    X.append(x)
    Y.append(y)


def count(x, y):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    for point in points:
        if point[0] < x and point[1] > y:
            count1 += 1
        elif point[0] > x and point[1] > y:
            count2 += 1
        elif point[0] < x and point[1] < y:
            count3 += 1
        else:
            count4 += 1
    return max(count1, count2, count3, count4)


ans = 100
for x in X:
    for y in Y:
        ans = min(ans, count(x+1, y+1))

print(ans)
