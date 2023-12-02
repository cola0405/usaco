# 不适用defaultdict
# 未ac
from collections import defaultdict
import sys
sys.stdin = open("notlast.in", 'r')
sys.stdout = open("notlast.out", 'w')

count = defaultdict(int)

n = int(input())
for i in range(n):
    line = input().split()
    name, milk = line[0], int(line[1])
    count[name] += milk

milks = sorted(set(count.values()), reverse=True)
milks.pop()

if len(milks) == 0 or list(count.values()).count(milks[-1]) > 1:
    print("Tie")
else:
    for cow in count:
        if count[cow] == milks[-1]:
            print(cow)

'''
1
Bessie 1
'''
