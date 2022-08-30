# 问题转化
# 差分数组


n = int(input())

dest = list(map(int, input().split(' ')))
src = list(map(int, input().split(' ')))

lst = [0]
for i in range(n):
    lst.append(dest[i] - src[i])
lst.append(0)

ans = 0
for i in range(1, n+2):
    ans += max(lst[i] - lst[i-1], 0)

print(ans)
