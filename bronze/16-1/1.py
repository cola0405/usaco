# g1 + s2g = g2 + g2p

import sys
sys.stdin = open('promote.in', 'r')
sys.stdout = open('promote.out', 'w')

b1, b2 = map(int, input().split())
s1, s2 = map(int, input().split())
g1, g2 = map(int, input().split())
p1, p2 = map(int, input().split())

g2p = p2 - p1
s2g = g2p + g2 - g1
b2s = s2g + s2 - s1

print(b2s)
print(s2g)
print(g2p)


