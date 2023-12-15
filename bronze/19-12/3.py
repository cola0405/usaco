# 暴力枚举，检查所有限制就行
# 如果原序列是字典序，那么全排列也会按字典序

import itertools
import sys
sys.stdin = open('lineup.in', 'r')
sys.stdout = open('lineup.out', 'w')

def valid(s):
    for a, b in constraints:
        idx1 = s.index(a)
        idx2 = s.index(b)
        if abs(idx1 - idx2) > 1:
            return False
    return True

n = int(input())
constraints = []
for i in range(n):
    line = input().split()
    constraints.append((line[0], line[5]))

cows = ('Beatrice', 'Belinda', 'Bella', 'Bessie',
        'Betsy', 'Blue', 'Buttercup', 'Sue')

for order in itertools.permutations(cows, len(cows)):
    if valid(order):
        for cow in order:
            print(cow)
        break

