# 排列组合

import sys
sys.stdin = open('gymnastics.in', 'r')
sys.stdout = open('gymnastics.out', 'w')

k, n = map(int, input().split())

ranks = []
for i in range(k):
    rank = list(map(int,input().split()))
    ranks.append(rank)

def isConsistent(pair):
    a, b = pair[0], pair[1]
    for rank in ranks:
        b_appear = False
        for cow in rank:
            if cow == b:
                b_appear = True
            if cow == a and b_appear:
                return False
    return True


ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            continue
        pair = (i, j)
        if isConsistent(pair):
            ans += 1

print(ans)

