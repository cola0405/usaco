N, K = map(int, input().split())

days = list(map(int, input().split()))

ans = K+1
start = days[0]

for i in range(1, N):
    gap = days[i] - start
    if gap < K+1:
        ans += gap
    else:
        ans += K+1
    start = days[i]


print(ans)

# 5 5
# 1 2 8 9 10