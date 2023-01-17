# 2s -> 469ms
# 前面还是170ms 快不了多少

import sys
sys.stdin = open("cowroute.in", "r")
sys.stdout = open("cowroute.out", "w")

def build_index_table():
    table = []
    for i in range(N):
        d = dict()
        cities = route_cities[i]
        for i in range(len(cities)):
            d[cities[i]] = i
        table.append(d)
    return table


def one_route_check(i):
    if A not in table[i] or B not in table[i]:
        return False
    A_inx = table[i][A]
    B_inx = table[i][B]
    if A_inx < B_inx:
        return True
    else:
        return False

def two_route_check(i, j):
    if A not in table[i] or B not in table[j]:
        return False
    A_inx = table[i][A]

    for city in table[j]:
        if city == B:
            break
        if city in table[i] and table[i][city] > A_inx:
            return True
    return False

# main
A,B,N = map(int, input().split())
route_cities = []
route_cost = []
for i in range(N):
    cost, city_num = map(int, input().split())
    cities = list(map(int, input().split()))
    route_cities.append(cities)
    route_cost.append(cost)

table = build_index_table()
min_cost = float("inf")

# one route
for i in range(N):
    if one_route_check(i):
        cost = route_cost[i]
        min_cost = min(cost, min_cost)

# 排列
# two route
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if two_route_check(i, j):
            cost = route_cost[i] + route_cost[j]
            min_cost = min(cost, min_cost)

if min_cost == float("inf"):
    print(-1)
else:
    print(min_cost)

