# 50000 set 随便玩玩

import sys
sys.stdin = open('highcard.in', 'r')
sys.stdout = open('highcard.out', 'w')

n = int(input())
elsie = []
for i in range(n):
    elsie.append(int(input()))

elsie.sort()
e_set = set(elsie)
i = 0
bessie = []
for num in range(1, 2*n+1):
    if num not in e_set:
        bessie.append(num)

e_inx = 0
b_inx = 0

score = 0
while e_inx < n and b_inx < n:
    if elsie[e_inx] < bessie[b_inx]:
        score += 1
        e_inx += 1
    b_inx += 1

print(score)



