# 动了前面的i-2 就贪不了了

round = int(input())

for r in range(round):
    n = int(input())
    levels = list(map(int, input().split()))
    if n == 1:
        print(0)
        continue
    diff = [-1]
    ans = 0
    for i in range(1, len(levels)):
        diff.append(levels[i] - levels[i-1])
    for i in range(len(diff))[1:]:
        if diff[i] > 0:
            if i+1 < len(levels) and levels[i+1] >= diff[i]:
                gap = diff[i]
                ans += gap
                levels[i+1] -= gap
                levels[i] -= gap
                diff[i] = 0
                if i+2 < len(levels):
                    diff[i+2] += gap
            else:
                print(-1)
                break
        if diff[i] < 0:
            if i-2 >= 0 and levels[i-2] >= abs(diff[i]):
                gap = abs(diff[i])
                ans += gap
                levels[i-2] -= gap
                levels[i-1] -= gap
                diff[i] = 0
            else:
                print(-1)
                break
    else:
        print(ans * 2)


