# 区间和

import sys
sys.stdin = open('div7.in', 'r')
sys.stdout = open('div7.out', 'w')
n = int(input())

# (p[j] - p[i - 1]) % 7 == 0
# p[j] % 7 == p[i - 1] % 7
# 问题转换为找 %7 余数相等的最大gap
# 所以建立长度为7的两个数组，分别存储对应余数的最边缘index
left = [float('inf')]*n
right = [0]*n
cur = 0
for i in range(n):
    id = int(input())
    cur = (cur+id)%7
    left[cur] = min(i, left[cur])
    right[cur] = i

max_gap = 0
for i in range(7):
    max_gap = max(right[i]-left[i], max_gap)
print(max_gap)