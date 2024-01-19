# 2_1.py 的优化

n = int(input())
target = list(map(int, input().split()))
origin = list(map(int, input().split()))
diff = [target[i]-origin[i] for i in range(n)]

ans = 0
i = 0
last = 0
while i<n:
    if diff[i] * last > 0:  # 可以跟一部分
        ans += abs(diff[i]) - abs(last)
    else:
        ans += abs(diff[i])
    j = i

    # abs 是为了处理负数
    while j+1<n and diff[j+1]*diff[j] > 0 and abs(diff[j+1]) <= abs(diff[j]):
        j += 1
    last = diff[j]
    i = j+1

print(ans)

'''
5
1 2 -1 -2 3
0 0 0 0 0

'''


