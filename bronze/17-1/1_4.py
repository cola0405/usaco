# 不适用defaultdict

from collections import defaultdict
import sys
sys.stdin = open("notlast.in", 'r')
sys.stdout = open("notlast.out", 'w')

n = int(input())
count = defaultdict(int)
for i in range(n):
    line = input().split()
    name, milk = line[0], int(line[1])
    count[name] += milk

cows = sorted(count, key=lambda item: count[item], reverse=True)
min_count = min(count.values())
while len(cows) > 0 and count[cows[-1]] == min_count:
    cows.pop()

if len(cows) == 0 or (len(cows) >= 2 and count[cows[-1]] == count[cows[-2]]):
    print("Tie")
else:
    print(cows[-1])

'''
1
Bessie 1
'''
