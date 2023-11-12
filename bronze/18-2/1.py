# 总共分三种情况
# ①不传送
# ②ax+by
# ③ay+bx

import sys
sys.stdin = open('teleport.in','r')
sys.stdout = open('teleport.out', 'w')

a,b,x,y = map(int, input().split())
d1 = abs(a-b)
d2 = abs(a-x) + abs(b-y)
d3 = abs(a-y) + abs(b-x)

print(min(d1,d2,d3))