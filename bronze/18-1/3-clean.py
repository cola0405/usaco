# 注意等号的取舍

import sys
sys.stdin = open('outofplace.in', 'r')
sys.stdout = open('outofplace.out', 'w')

LEFT = 0
RIGHT = 1

n = int(input())
cows = []
for i in range(n):
    cows.append(int(input()))

i = 0
bessie = LEFT
while i+1 < n:
    if cows[i] <= cows[i+1]:
        i += 1
        continue
    # judge
    if i+2 < n and cows[i] > cows[i+2]:
        bessie = LEFT
        break
    if i-1 >= 0 and cows[i] > cows[i-1]:
        bessie = RIGHT
        break
    bessie = RIGHT
    break

bessie_index = i+bessie
ans = 0
s = set()
if bessie == RIGHT:
    # go left
    i = bessie_index-1
    while i >= 0 \
        and cows[bessie_index] < cows[i]:
            s.add(cows[i])
            i -= 1
else:
    # go right
    i = bessie_index+1
    while i < n \
            and cows[bessie_index] > cows[i]:
        s.add(cows[i])
        i += 1

print(len(s))