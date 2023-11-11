# 排序
# 怎么把统计面积的效率提高

# sort 不改变原有顺序


import math
import sys
sys.stdin = open("triangles.in", "r")
sys.stdout = open("triangles.out", "w")

X = 0
Y = 1

x_edge_sum = dict()
y_edge_sum = dict()

# init point and the amount of points
x_record = dict()
y_record = dict()


# 只有一个点的时候 怎么处理
def get_sum(index):
    i = 1
    while i < len(points):
        d = 0
        init_point = points[i-1]
        amount = 1
        while i < len(points) and points[i][index] == points[i-1][index]:
            edge = abs(points[i][(index+1)%2] - init_point[(index+1)%2])
            d += edge
            amount += 1
            i += 1
        if index == X:
            x_edge_sum[points[i-1][index]] = d
            x_record[points[i-1][index]] = (init_point, amount)
        else:
            y_edge_sum[points[i-1][index]] = d
            y_record[points[i-1][index]] = (init_point, amount)
        i += 1



n = int(input())
points = []
for i in range(n):
    x,y = map(int, input().split())
    points.append((x,y))

def by_y(item):
    return item[1]
points.sort(key=by_y)


def by_x(item):
    return item[0]
points.sort(key=by_x)
get_sum(X)


points.sort(key=by_y)
get_sum(Y)


ans = 0
for p in points:
    x, y = p

    # get x edge sum
    if x not in x_record:
        continue
    x_init = x_record[x]
    x_init_point = x_init[0]
    x_amount = x_init[1]

    # no edge is parallel to axis
    if x_amount < 2:
        continue

    cur_x_edge_sum = x_edge_sum[x] - (x_amount-2)*(y-x_init_point[Y])

    # get x edge sum
    if y not in y_record:
        continue
    y_init = y_record[y]
    y_init_point = y_init[0]
    y_amount = y_init[1]

    # no edge is parallel to axis
    if y_amount < 2:
        continue

    cur_y_edge_sum = y_edge_sum[y] - (y_amount - 2) * (x - y_init_point[Y])
    ans += cur_x_edge_sum * cur_y_edge_sum


ans = ans%(1e+9+7)
print(int(ans))


# 6
# 0 0
# 0 -1
# 0 1
# 1 0
# 1 2
# 1 1