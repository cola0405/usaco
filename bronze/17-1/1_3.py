# 不适用defaultdict
import sys
sys.stdin = open("notlast.in", 'r')
sys.stdout = open("notlast.out", 'w')

names = ["Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"]
count = {name: 0 for name in names}

n = int(input())
min1, min2 = names[0], names[0]
for i in range(n):
    line = input().split()
    name, milk = line[0], int(line[1])
    count[name] += milk

    if count[name] < count[min1]:
        min1 = name

    if count[name] > count[min2]:
        min2 = name

cows = list(count)

for name in cows:
    if count[min1] < count[name] < count[min2]:
        min2 = name

if min1 == min2 or count.values():
    print("Tie")
else:
    print(min2)




