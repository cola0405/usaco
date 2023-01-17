import sys

sys.stdin = open("cowroute.in", "r")
sys.stdout = open("cowroute.out", "w")

A,B,N = map(int, input().split())

route_cities = []
route_cost = []
for i in range(N):
    cost, city_num = map(int, input().split())
    cities = list(map(int, input().split()))
    route_cities.append(cities)
    route_cost.append(cost)

def one_route_check():
    if A not in first or B not in first:
        return False
    A_inx = first.index(A)
    B_inx = first.index(B)
    if A_inx < B_inx:
        return True
    else:
        return False

def two_route_check():
    if A not in first or B not in second:
        return False
    A_inx = first.index(A)
    B_inx = second.index(B)
    mids = second[:B_inx]
    for city in mids:
        if city in first and first.index(city) > A_inx:
            return True
    return False

min_cost = float("inf")

# 排列
for i in range(N):
    first = route_cities[i]
    if one_route_check():
        cost = route_cost[i]
        min_cost = min(cost, min_cost)

    for j in range(N):
        if i == j:
            continue
        second = route_cities[j]
        if two_route_check():
            cost = route_cost[i] + route_cost[j]
            min_cost = min(cost, min_cost)

if min_cost == float("inf"):
    print(-1)
else:
    print(min_cost)

