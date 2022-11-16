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


def find_sec():
    milks = list(log.values())
    milks.sort()

    # no second
    M = milks[0]
    sec = None
    for i in milks:
        if i != M:
            sec = i
            break
    else:
        print("Tie")
        return

    # not only one -- Tie
    if milks.count(sec) > 1:
        print("Tie")
        return

    # got the second
    for i in log.keys():
        if log[i] == sec:
            print(i)

find_sec()






