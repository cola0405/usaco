import sys
from itertools import permutations
sys.stdin = open("hps.in", "r")
sys.stdout = open("hps.out", "w")

n = int(input())
p1_win = 0
p2_win = 0

for i in range(n):
    p1, p2 = map(int, input().split())
    if p1 == p2:
        pass
    elif (p1 == 1 and p2 == 2) \
        or (p1 == 2 and p2 == 3) \
        or (p1 == 3 and p2 == 1):
        p1_win += 1
    else:
        p2_win += 1

# p2_win 包含了其他的情况 —— 如1赢3
# ps: 不存在1赢2又赢3的情况
# (1>2, 2>3, 3>1) 和(3>1, 3>2, 2>1) 就是所有的情况了
print(max(p1_win, p2_win))