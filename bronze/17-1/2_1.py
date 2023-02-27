# 石头、剪刀、布
# (1, 2, 3)
# (1, 3, 2)
# ......
# (3, 2, 1)

ROCK = 0
SCISSOR = 1
PAPER = 2

import sys
from itertools import permutations
sys.stdin = open("hps.in", "r")
sys.stdout = open("hps.out", "w")

n = int(input())
games = []
for i in range(n):
    game = list(map(int, input().split()))
    games.append(game)

def play(gesture):
    win1 = 0

    for i in range(n):
        p1, p2 = games[i]
        if p1 == p2:
            continue
        elif (p1 == gesture[ROCK] and p2 == gesture[SCISSOR]) \
            or (p1 == gesture[SCISSOR] and p2 == gesture[PAPER]) \
            or (p1 == gesture[PAPER] and p2 == gesture[ROCK]):
            win1 += 1
    return win1

max_win = 0
for gesture in permutations(range(1,4)):
    win1 = play(gesture)
    max_win = max(win1, max_win)

print(max_win)



