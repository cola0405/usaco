round = int(input())
ans = 0
for r in range(round):
    n = int(input())
    levels = list(map(int, input().split()))
    record = tuple(levels)
    i = 0
    while i < n-1:
        if levels[i] < 0:
            break
        if levels[i] > levels[i+1]:
            if i%2 == 0:
                break
            levels[i] = levels[i+1]
        elif levels[i] < levels[i+1]:
            if i+2 >= n:
                break
            diff = levels[i+1] - levels[i]
            levels[i+2] -= diff
            levels[i+1] = levels[i]
            if levels[i+2] < 0:
                break
        i += 1
    else:
        v = levels[n - 1]
        ans = 0
        for level in record:
            ans += level - v
        print(ans)
        continue
    print(-1)