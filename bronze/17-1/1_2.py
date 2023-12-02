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

cows = list(sorted(count, key=lambda item: count[item], reverse=True))
min_count = min(count.values())
while len(cows) > 0 and count[cows[-1]] == min_count:
    cows.pop()

if len(cows) == 0 or (len(cows) >= 2 and count[cows[-1]] == count[cows[-2]]):
    print("Tie")
else:
    print(cows[-1])
