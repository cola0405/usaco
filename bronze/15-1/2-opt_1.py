# defaultdict 会新建key-value 效率比2-opt 慢一些

from collections import defaultdict
import sys
sys.stdin = open("cowroute.in", "r")
sys.stdout = open("cowroute.out", "w")

def build_inx():
    res = []
    for i in range(N):
        d = defaultdict(lambda: float('inf'))
        cities = route_cities[i]
        for i in range(len(cities)):
            d[cities[i]] = i
        res.append(d)
    return res

def two_route_check():
    if inx[first][A] == float('inf') or inx[second][B] == float('inf'):
        return False
    for city in inx[first]:
        if inx[first][city] > inx[first][A] and inx[second][city] < inx[second][B]:
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

inx = build_inx()     # optimize list.index()
min_cost = float("inf")

# one route
for i in range(N):
    if inx[i][A] < inx[i][B] < float('inf'):
        min_cost = min(min_cost, route_cost[i])

# permutation try two route
for first in range(N):
    for second in range(N):
        if first != second:
            if two_route_check():
                cost = route_cost[first] + route_cost[second]
                min_cost = min(cost, min_cost)

if min_cost == float("inf"):
    print(-1)
else:
    print(min_cost)

