# 有些if条件是你试不出来的


n = int(input())
s = list(input())
ans = 0

# 以每个孤独的牛为研究对象，l和r分别记录了当前i点往l和r有throw photo的最大数量
left = [0]*n
right = [0]*n

# 构造left
c = 1
for i in range(1, n):
    # 相同则没办法作throw photo
    if s[i] == s[i-1]:
        left[i] = 0
        c += 1
    # 一旦有different的H，则之前有几个连续的G，就会有几个throw photo
    else:
        left[i] = c
        c = 1

# 构造right
c = 1
for i in range(n-2, 0, -1):
    if s[i] == s[i+1]:
        right[i] = 0
        c += 1
    else:
        right[i] = c
        c = 1

for i in range(1, n-1):
    # 以点i为轴心，两边组合计算次数
    if left[i] >= 1 and right[i] >= 1:
        ans += left[i]*right[i]

    # 以点i为边界，单边计算次数
    if left[i] > 1:
        ans += left[i]-1
    if right[i] > 1:
        ans += right[i] -1

print(ans)




