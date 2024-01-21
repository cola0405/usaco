# 近似法

# 最优解的栏杆肯定可以贴近于某个牛 —— 贴近也就是odd+1 —— even
# 这里需要论证一个点，最优中心点一定是挨着某个牛的吗 —— 如果可以的话，枚举每头牛的坐标就解决问题了
# (1,1) (3,1) (5,3) (5,5) —— 这个测试用例的最优中心点并不贴近任何一头牛

# 但是并不代表着思路到这里就断了
# 思路应该转化为最优解的横、竖两条栏杆肯定是贴近于某头牛
# 横贴近某一头，竖贴近某一头 —— 当然，这两个贴近的可能是同一头牛

import sys
sys.stdin = open('balancing.in', 'r')
sys.stdout = open('balancing.out', 'w')

n, b = map(int, input().split())
X,Y = [],[]
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
    X.append(x)
    Y.append(y)

def count(x, y):
    count1, count2 = 0,0
    count3, count4 = 0,0
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
for x in X:     # 组合各个可能的横竖栏杆
    for y in Y:
        ans = min(ans, count(x+1, y+1))  # 遍历过程统一即可，+-关系不大
print(ans)
