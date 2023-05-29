# 全排列

# 为什么area*2就行
# 因为边都是整数，唯一的小数就是在1/2来的
# 那么*2后就没小数问题了

# 别开方，精度不允许
# 最后要求输出int
# 2.0和2是不同的

# 什么题都可以手撸测试用例

def main():
    from itertools import permutations
    import sys
    sys.stdin = open('triangles.in', 'r')
    sys.stdout = open('triangles.out', 'w')

    n = int(input())
    points = []
    for i in range(n):
        points.append(tuple(map(int, input().split())))

    X = 0
    Y = 1
    ans = 0
    for p1, p2, p3 in permutations(points, 3):
        if p1[X] == p2[X] and p3[Y] == p2[Y]:
            area = abs(p1[Y] - p2[Y]) * abs(p3[X] - p2[X])
            ans = max(area, ans)
    print(ans)

main()
