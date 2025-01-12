t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    cur = 100
    left = 45
    while left <= n:
        right = cur//2 - 1
        cnt += min(n, right) - left + 1
        left += 4*cur
        cur *= 10
    print(cnt)
    