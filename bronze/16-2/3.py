# 不能简单对半分，即使左边比右边多两三个也不为过
# 因为之后还有另外一个方向的切分
# 所以“两边尽可能平衡”不能作为评判的标准

import sys
sys.stdin = open('balancing.in', 'r')
sys.stdout = open('balancing.out', 'w')

n, b = map(int, input().split())
X = []
Y = []
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x,y))
    X.append(x)
    Y.append(y)


def find_mid(C):
    mid_inx = n // 2
    if n % 2 == 0:
        right = mid_inx
        left = mid_inx - 1
    else:
        left = mid_inx
        right = mid_inx + 1
    while left >= 0 and right < n:
        if C[left] != C[mid_inx]:
            mid = C[mid_inx] - 1
            break
        elif C[right] != C[mid_inx]:
            mid = C[mid_inx] + 1
            break
        left -= 1
        right += 1
    else:
        if left == 0:
            mid = C[left]+1
        else:
            mid = C[right]-1
    return mid


if n != 1:
    X.sort()
    Y.sort()
    x = find_mid(X)
    y = find_mid(Y)
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
    print(max(count1, count2, count3, count4))

else:
    print(1)
