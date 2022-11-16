# 抱怨是没有用的
# 只有根据测试用例去推导题目的意思

# ps: guess should be after the swap

import sys
sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")

n = int(input())
swap_shells = []
guess = []
for i in range(n):
    a, b, g = map(int, input().split())
    swap_shells.append((a, b))
    guess.append(g)

ans = 0
for pebble_loc in range(1,4):
    shells = [0, 1, 2, 3]
    score = 0
    for i in range(n):
        # swap
        a, b = swap_shells[i]
        shells[a], shells[b] = shells[b], shells[a]

        # update pebble location
        if pebble_loc == a:
            pebble_loc = b
        elif pebble_loc == b:
            pebble_loc = a

        # guess when after the swap
        if guess[i] == pebble_loc:
            score += 1

    ans = max(ans, score)

print(ans)






