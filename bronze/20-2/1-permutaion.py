import sys
import itertools
sys.stdin = open("triangles.in", "r")
sys.stdout = open("triangles.out", "w")

res = 0
N = int(input())
points = []
for _ in range(N):
    points.append(list(map(int, input().strip().split())))

def is_valid(coord):
    # restrict
    # c
    # a b
    if coord[0][1] == coord[1][1] and coord[0][0] == coord[2][0]:
        return 1
    else:
        return False

coords = list(itertools.permutations(points, 3))
for coord in coords:
    if is_valid(coord):
        del_x = abs(coord[0][0] - coord[1][0])
        del_y = abs(coord[0][1] - coord[2][1])
        res = max(res, del_x*del_y)

print(res)
