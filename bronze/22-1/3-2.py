# 8p

# 定一个final line 然后计算可行性

round = int(input())
for r in range(round):
    n = int(input())
    levels = list(map(int, input().split()))
    if n == 1:
        print(0)
        continue
    min_value = min(levels)
    s = sum(levels)
    ans = s + 1
    for final in range(min_value+1)[::-1]:
        bags = 0
        pre_right = levels[0]
        for i in range(n-1):
            right = levels[i + 1]
            gap = pre_right - final
            if gap < 0 or right-gap < final:
                break
            pre_right = right-gap
            bags += gap
        else:
            if pre_right == final:
                ans = bags
                break

    if ans == s+1:
        print(-1)
    else:
        print(ans*2)


