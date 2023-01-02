import sys
sys.stdin = open("measurement.in", "r")
sys.stdout = open("measurement.out", "w")

n = int(input())
log = []
for i in range(n):
    log.append(input().split())

def by_day(item):
    return int(item[0])
log.sort(key=by_day)

def update(oup):
    cur_display = []
    for name in milk_output:
        if milk_output[name] == oup:
            cur_display.append(name)



display = ["B","E","M"]
cur_top = 7
ans = 0
milk_output = {"Bessie":7, "Elsie":7, "Mildred":7}
for i in range(n):
    name = log[1]
    op = log[2][0]
    num = int(log[2][1])

    # update log
    if op == '+':
        milk_output[name] += num
    else:
        milk_output[name] -= num

    # update display
    top = max(milk_output.values())
    if top > cur_top:
        ans += 1
        cur_top = top





