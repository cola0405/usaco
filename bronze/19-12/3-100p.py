# 枚举，然后把每个条件过一遍做筛除
# 序列也是可以做比较的
# 规则和字符串一样
# for 暴力20p还有问题

import sys
sys.stdin = open('lineup.in', 'r')
sys.stdout = open('lineup.out', 'w')

n = int(input())
pairs = []
for i in range(n):
    line = input().split()
    pairs.append((line[0], line[5]))

cows = ('Beatrice', 'Belinda', 'Bessie',
        'Betsy', 'Blue', 'Bella', 'Buttercup', 'Sue')

def p():
    import itertools
    orders = itertools.permutations(cows, len(cows))
    possible = []
    for order in orders:
        if len(order) > len(set(order)):
            continue
        for pair in pairs:
            inx1 = order.index(pair[0])
            inx2 = order.index(pair[1])
            if abs(inx1 - inx2) > 1:
                break
        else:
            possible.append(order)

    return min(possible)


order = p()
for i in order:
    print(i)