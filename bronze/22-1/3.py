# 我都没动！


round = int(input())

for r in range(round):
    n = int(input())
    lst = list(map(int, input().split()))
    if len(lst) == 1:
        print(0)
        continue
    diff = [0]
    for i in range(1, len(lst)):
        diff.append(lst[i] - lst[i-1])

    tail = len(diff)-1
    ans = 0
    fail = 0
    while tail >= 0:
        if diff[tail] < 0 and tail-2  >= 0:
            if lst[tail-1] + diff[tail] >= 0 \
                    and lst[tail-2] + diff[tail] >= 0:
                ans += -2 * diff[tail]
                lst[tail-1] += diff[tail]
                lst[tail-2] += diff[tail]
                diff[tail] = 0
                tail -= 1
                continue
            else:
                fail = 1
                break
        if diff[tail] < 0 and tail-2  < 0:
            fail = 1
            break

        if diff[tail] > 0 and tail+1 < len(lst):
            if lst[tail+1] - diff[tail] >= 0\
                    and lst[tail] - diff[tail] >= 0:
                ans += 2 * diff[tail]
                lst[tail] -= lst[tail]
                lst[tail+1] -= lst[tail]
                diff[tail] = 0
                tail -= 1
                continue
            else:
                fail = 1
                break
        if diff[tail] > 0 and tail + 1 >= len(lst):
            fail = 1
            break
        tail -= 1

    if fail:
        print(-1)
    else:
        print(ans)