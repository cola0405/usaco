# logic
# basic

import sys
sys.stdin = open("notlast.in", 'r')
sys.stdout = open("notlast.out", 'w')

log = {}
names = ['Bessie', 'Elsie', 'Daisy',
         'Gertie', 'Annabelle', 'Maggie', 'Henrietta']
for i in names:
    log[i] = 0

n = int(input())
for i in range(n):
    name, amount = input().split()
    log[name] += int(amount)

# find min2
milks = list(log.values())
min1 = min(milks)
min2 = float('inf')
for milk in milks:
    if min2 > milk > min1:
        min2 = milk

if min2 == float('inf') or milks.count(min2) > 1:
    print("Tie")
else:
    for i in log:
        if log[i] == min2:
            print(i)
            break






