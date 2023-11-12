import sys
sys.stdin = open("measurement.in", "r")
sys.stdout = open("measurement.out", "w")

n = int(input())
logs = [input().split() for _ in range(n)]
logs.sort(key=lambda item: int(item[0]))


display = ["Bessie","Elsie","Mildred"]
cur_top = 7
ans = 0
milk_output = {"Bessie":7, "Elsie":7, "Mildred":7}

for log in logs:
    name = log[1]
    num = int(log[2])

    # update output
    milk_output[name] += num

    # update display
    cur_top = max(milk_output.values())
    flag = 0

    for name in milk_output.keys():
        if milk_output[name] == cur_top and name not in display:
            display.append(name)
            flag = 1
        elif milk_output[name] != cur_top and name in display:
            display.remove(name)
            flag = 1
    if flag:
        ans += 1

print(ans)





