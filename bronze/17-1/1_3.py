# 不适用defaultdict

import sys
sys.stdin = open("notlast.in", 'r')
sys.stdout = open("notlast.out", 'w')

names = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]
count = {name: 0 for name in names}

n = int(input())
for i in range(n):
    line = input().split()
    name, milk = line[0], int(line[1])
    count[name] += milk

milks = sorted(count.values(), reverse=True)
min_count = milks[-1]
while len(milks) > 0 and milks[-1] == min_count:
    milks.pop()

if len(milks) == 0 or (len(milks) >= 2 and milks[-1] == milks[-2]):
    print("Tie")
else:
    for cow in count:
        if count[cow] == milks[-1]:
            print(cow)
