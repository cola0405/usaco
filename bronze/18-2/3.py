# O(n)
# from right to left
# the key point is the positive number in the log
# because the previous numbers must be in descending order

import sys
sys.stdin = open('taming.in', 'r')
sys.stdout = open('taming.out', 'w')

def solve():
    n = int(input())
    log = list(map(int, input().split()))
    if log[0] > 0:
        print(-1)
        return

    i = n-1
    while i >= 0:           # from right to left
        if log[i] > 0:      # meet with positive numbers
            r = log[i]
            while i >= 0 and r >= 0:        # update the previous numbers
                if log[i] != r and log[i] != -1:
                    print(-1)
                    return
                log[i] = r      # update the missing log
                r -= 1
                i -= 1
        else: i -= 1
    if log[0] == -1: log[0] = 0
    min_b = log.count(0)
    print(min_b, min_b + log.count(-1))     # in the end, the remaining -1 could become breakouts

solve()







'''
4
-1 -1 -1 -1

1 4

5
0 -1 -1 -1 2

2 3

5
0 -1 1 -1 2

-1

5
0 1 2 -1 0

2 3

'''
