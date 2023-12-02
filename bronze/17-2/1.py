import sys
sys.stdin = open("crossroad.in", "r")
sys.stdout = open("crossroad.out", "w")

ans = 0
sides = dict()
n = int(input())
for i in range(n):
    cow, side = map(int, input().split())
    if cow not in sides:
        sides[cow] = side
    else:
        ans += side^sides[cow]
        sides[cow] = side

print(ans)