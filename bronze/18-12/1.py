# 周期操作

import sys
sys.stdin = open('mixmilk.in', 'r')
sys.stdout = open('mixmilk.out', 'w')

buckets = [list(map(int, input().split())) for _ in range(3)]

for i in range(100):
    # pour buckets[i%3] to buckets[(i+1)%3]
    c1, m1 = buckets[i%3]
    c2, m2 = buckets[(i+1)%3]
    milk = c2 - m2

    # pour
    buckets[(i+1)%3][1] = min(c2, m2+m1)
    buckets[i%3][1] = max(0, m1-milk)

print(buckets[0][1])
print(buckets[1][1])
print(buckets[2][1])

